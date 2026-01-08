import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import QueryProcessor, SQLGenerator

@csrf_exempt
def nl_to_sql_api(request):
    """API to convert a natural language query to SQL."""
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            nl_query = data.get("query", "")

            if not nl_query:
                return JsonResponse({"error": "Query is required"}, status=400)

            print("test--------------------->")
            relevant_tables = QueryProcessor.select_relevant_tables(nl_query)
            sql_query = SQLGenerator.generate_sql(nl_query, relevant_tables)

            return JsonResponse({
                "natural_query": nl_query,
                "relevant_tables": relevant_tables,
                "sql_query": sql_query
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Send a POST request with a query."})
