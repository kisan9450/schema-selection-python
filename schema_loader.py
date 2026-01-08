import json
from django.core.files.storage import default_storage

SCHEMA_FILE = "schema.json"

class SchemaLoader:
    """Loads the database schema from a JSON file."""
    
    @staticmethod
    def load_schema():
        """Loads the schema JSON file."""
        if default_storage.exists(SCHEMA_FILE):
            with default_storage.open(SCHEMA_FILE, "r") as file:
                return json.load(file)
        return {"tables": []}
