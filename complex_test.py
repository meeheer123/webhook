import sqlite3
import requests
import json
from datetime import datetime

class DataProcessor:
    def __init__(self, db_name="test.db"):
        self.db_name = db_name
        self.connection = None
        self.api_url = "https://api.nonexistent-service.com/data"
        
    def connect_to_db(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            # Intentionally wrong SQL syntax
            create_table_query = """
                CREATE TABLE IF NOT EXISTS data_table
                id INTEGER PRIMARY KEY,
                name TEXT,
                timestamp DATETIME
                -- Missing commas between columns
            """
            self.connection.execute(create_table_query)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise
        
    def fetch_api_data(self):
        try:
            # This will fail as the API doesn't exist
            response = requests.get(self.api_url, timeout=5)
            return response.json()
        except requests.RequestException as e:
            print(f"API error: {e}")
            raise

    def process_data(self, data):
        # Trying to access non-existent dictionary keys
        processed_data = {
            'id': data['id'],
            'name': data['user']['profile']['name'],
            'timestamp': datetime.now()
        }
        return processed_data

    def save_to_file(self, data):
        # Trying to write to a file in a non-existent directory
        with open('/nonexistent/directory/output.txt', 'w') as f:
            json.dump(data, f)

def main():
    processor = DataProcessor()
    
    # This will create a chain of errors
    try:
        # Step 1: Database connection and table creation
        processor.connect_to_db()
        
        # Step 2: API call
        api_data = processor.fetch_api_data()
        
        # Step 3: Data processing
        processed_data = processor.process_data(api_data)
        
        # Step 4: File saving
        processor.save_to_file(processed_data)
        
        print("Process completed successfully!")
        
    except Exception as e:
        print(f"Process failed with error: {str(e)}")
        raise  # Re-raise the exception to make the script fail

if __name__ == "__main__":
    main()