from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_error():
    print("Received POST request")  # Console logging
    try:
        data = request.json
        print(f"Received data: {data}")  # Console logging
        
        # Write to a file for persistence
        with open('error_logs.txt', 'a') as f:
            f.write(f"\n\nNew Error Report:\n")
            f.write(f"Repository: {data.get('repository')}\n")
            f.write(f"Error: {data.get('error_logs')}\n")
            f.write("-" * 50)
        
        return jsonify({"status": "success", "message": "Error logged"}), 200
    
    except Exception as e:
        print(f"Error processing request: {str(e)}")  # Console logging
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)