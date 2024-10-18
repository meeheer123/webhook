import requests
import json
import os
from time import sleep

class CustomAPIError(Exception):
    pass

class APITester:
    def __init__(self):
        self.api_endpoints = [
            "https://jsonplaceholder.typicode.com/posts/1",  # Valid API
            "https://api.nonexistent.com/data",             # Invalid API
            "https://api.github.com/rate_limit"             # GitHub API
        ]
        self.data_file = "processed_data.json"

    def test_api_calls(self):
        results = []
        for endpoint in self.api_endpoints:
            try:
                print(f"Calling API: {endpoint}")
                response = requests.get(endpoint, timeout=3)
                response.raise_for_status()
                results.append(response.json())
            except requests.exceptions.Timeout:
                print(f"Timeout error for {endpoint}")
                raise CustomAPIError(f"API Timeout: {endpoint}")
            except requests.exceptions.RequestException as e:
                print(f"API error: {str(e)}")
                raise CustomAPIError(f"API Failed: {str(e)}")

        return results

    def process_large_data(self):
        # Generate a list that's too large for memory
        print("Generating large dataset...")
        large_data = list(range(10**8))  # Will cause memory error
        return sum(large_data)

    def file_operations(self):
        try:
            # Try to read a non-existent file
            with open('nonexistent.txt', 'r') as f:
                data = f.read()
        except FileNotFoundError as e:
            print(f"File error: {str(e)}")
            raise

    def infinite_loop(self):
        counter = 0
        while True:
            print(f"Loop iteration: {counter}")
            counter += 1
            sleep(0.1)
            if counter > 100:  # This will take 10 seconds
                raise TimeoutError("Process took too long!")

def main():
    tester = APITester()
    errors = []

    # Test 1: API Calls
    print("\nRunning API Tests...")
    try:
        results = tester.test_api_calls()
    except CustomAPIError as e:
        errors.append(f"API Error: {str(e)}")
        print(f"API test failed: {str(e)}")

    # Test 2: Memory Error
    print("\nTesting Memory Limits...")
    try:
        result = tester.process_large_data()
    except MemoryError as e:
        errors.append(f"Memory Error: Process requires too much memory")
        print("Memory test failed: Process requires too much memory")

    # Test 3: File Operations
    print("\nTesting File Operations...")
    try:
        tester.file_operations()
    except FileNotFoundError as e:
        errors.append(f"File Error: {str(e)}")
        print(f"File test failed: {str(e)}")

    # Test 4: Timeout Test
    print("\nTesting Timeout...")
    try:
        tester.infinite_loop()
    except TimeoutError as e:
        errors.append(f"Timeout Error: {str(e)}")
        print(f"Timeout test failed: {str(e)}")

    # Final Error Report
    if errors:
        print("\nError Summary:")
        for i, error in enumerate(errors, 1):
            print(f"Error {i}: {error}")
        raise Exception("\n".join(errors))

if __name__ == "__main__":
    main()