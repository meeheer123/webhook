class DataManipulator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.text_data = "Hello World"
        
    def list_operations(self):
        # Index error - trying to access index beyond list length
        print("Accessing index 10:", self.numbers[10])
        
        # Out of range error in list slicing
        print("Invalid slicing:", self.numbers[10:20:2])
    
    def type_conversion_errors(self):
        # Type conversion errors
        text_numbers = ["1", "2", "three", "4", "5"]
        
        # This will fail when trying to convert "three" to int
        numbers = [int(x) for x in text_numbers]
        print("Converted numbers:", numbers)
    
    def string_operations(self):
        # String index error
        try:
            print(self.text_data[20])  # String index out of range
        except IndexError as e:
            print(f"String index error: {e}")
            raise
            
        # String formatting error
        template = "Name: {}, Age: {}, City: {}"
        data = ("John", 25)  # Missing one argument
        print(template.format(*data))
    
    def arithmetic_errors(self):
        # Zero division error
        numbers = [10, 5, 0, 2, 1]
        results = []
        
        for n in numbers:
            # Will fail when n = 0
            result = 100 / n
            results.append(result)
            
        print("Division results:", results)
    
    def recursive_error(self, n=5):
        # Recursion error - will exceed maximum recursion depth
        print(f"Recursive call with n = {n}")
        return self.recursive_error(n + 1)

def process_student_data():
    # Dictionary key errors and type errors
    students = [
        {"name": "Alice", "grades": [85, 90, 92]},
        {"name": "Bob", "grades": [78, 85]},
        {"name": "Charlie", "grades": None},
        {"name": "David"}  # Missing grades key
    ]
    
    for student in students:
        # Will fail for Charlie (None grades) and David (missing grades)
        average = sum(student['grades']) / len(student['grades'])
        print(f"{student['name']}'s average: {average}")

def main():
    manipulator = DataManipulator()
    
    print("Starting error-prone operations...")
    
    # Running different error scenarios
    try:
        print("\n1. List Operations:")
        manipulator.list_operations()
    except Exception as e:
        print(f"List operation failed: {e}")
        
    try:
        print("\n2. Type Conversion:")
        manipulator.type_conversion_errors()
    except Exception as e:
        print(f"Type conversion failed: {e}")
    
    try:
        print("\n3. String Operations:")
        manipulator.string_operations()
    except Exception as e:
        print(f"String operation failed: {e}")
    
    try:
        print("\n4. Arithmetic Operations:")
        manipulator.arithmetic_errors()
    except Exception as e:
        print(f"Arithmetic operation failed: {e}")
    
    try:
        print("\n5. Processing Student Data:")
        process_student_data()
    except Exception as e:
        print(f"Student data processing failed: {e}")
    
    print("\n6. Recursive Error:")
    manipulator.recursive_error()

if __name__ == "__main__":
    main()