from flask import Flask, request, jsonify
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_error():
    app.logger.info("Received POST request")
    try:
        data = request.json
        app.logger.debug(f"Received data: {data}")  # Log received data
        
        # Write to a file for persistence
        with open('error_logs.txt', 'a') as f:
            f.write(f"\n\nNew Error Report:\n")
            f.write(f"Repository: {data.get('repository')}\n")
            f.write(f"Error: {data.get('error_logs')}\n")
            f.write("-" * 50)
        
        return jsonify({"status": "success", "message": "Error logged"}), 200
    
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")  # Log any exceptions
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
