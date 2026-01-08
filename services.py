import json
import spacy
import openai
from sentence_transformers import SentenceTransformer, util
from .schema_loader import SchemaLoader

# Load NLP models
nlp = spacy.load("en_core_web_sm")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


class QueryProcessor:
    """Processes natural language queries to extract keywords and select relevant tables."""
    
    @staticmethod
    def extract_keywords(nl_query):
        """Extracts nouns, proper nouns, and verbs from the query."""
        doc = nlp(nl_query)
        return [token.text for token in doc if token.pos_ in ["NOUN", "PROPN", "VERB"]]

    @staticmethod
    def select_relevant_tables(nl_query):
        """Finds the most relevant tables based on semantic similarity."""
        schema = SchemaLoader.load_schema()
        keywords = QueryProcessor.extract_keywords(nl_query)
        query_embedding = embedding_model.encode(" ".join(keywords), convert_to_tensor=True)

        table_scores = []
        for table in schema["tables"]:
            table_name = table["name"]
            columns = " ".join(table["columns"])
            table_embedding = embedding_model.encode(f"{table_name} {columns}", convert_to_tensor=True)
            score = util.pytorch_cos_sim(query_embedding, table_embedding).item()
            table_scores.append((table, score))

        table_scores.sort(key=lambda x: x[1], reverse=True)
        return [table[0] for table in table_scores if table[1] > 0.3]  # Threshold

    
class SQLGenerator:
    """Generates SQL queries using OpenAI."""
    
    @staticmethod
    def generate_sql(nl_query, selected_tables):
        """Converts a natural language query into SQL using GPT-4-turbo."""
        
        prompt = (
            f"Convert the following natural language query into SQL using the given tables:\n"
            f"Query: {nl_query}\n\n"
            f"Tables:\n{json.dumps(selected_tables, indent=2)}"
        )

        try:
            openai_api_key = os.getenv("OPENAI_API_KEY")
            client = openai.OpenAI(api_key=openai_api_key)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  
                messages=[
                    {"role": "system", "content": "You are an expert SQL generator."},
                    {"role": "user", "content": prompt}
                ]
            )

            return response.choices[0].message.content.strip()

        except openai.OpenAIError as e:
            print(f"❌ OpenAI API Error: {e}")
            return None  # Return None on failure

