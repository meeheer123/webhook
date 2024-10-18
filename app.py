from flask import Flask, request, jsonify
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='deployment_errors.log'
)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_error():
    try:
        data = request.json
        
        # Extract data
        repository = data.get('repository')
        workflow = data.get('workflow')
        status = data.get('status')
        error_logs = data.get('error_logs')
        commit_sha = data.get('commit_sha')
        commit_message = data.get('commit_message')
        
        # Log the error
        logging.error(f"""
        Deployment Failed:
        Repository: {repository}
        Workflow: {workflow}
        Status: {status}
        Commit SHA: {commit_sha}
        Commit Message: {commit_message}
        Error Logs: {error_logs}
        """)
        
        return jsonify({
            "status": "received",
            "message": "Error logged successfully"
        }), 200
        
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Failed to process error: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)