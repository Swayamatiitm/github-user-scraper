from flask import Flask, request, jsonify, render_template
import logging

app = Flask(__name__)

# Configure logging to a file
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.before_request
def log_request_info():
    logging.info("Data Received in App Successfully")

@app.route('/request-permission', methods=['POST'])
def request_permission():
    data = request.json
    app_name = data.get('app_name')
    permission_type = data.get('permission_type')
    logging.info(f"Received permission request for {permission_type} from {app_name}")

    # Generate response based on permission type
    if permission_type == 'call_logs':
        response = {
            'ai_check': 'allowed',
            'data': [
                'Call from 123-456-7890 to 987-654-3210 at 10:00 AM',
                'Call from 234-567-8901 to 876-543-2109 at 11:00 AM'
            ]
        }
        logging.info("Call logs permission granted with dummy data provided.")
    
    elif permission_type == 'messages':
        response = {
            'ai_check': 'allowed',
            'data': [
                'Message from 123-456-7890: "Hello!"',
                'Message from 234-567-8901: "Hi there!"'
            ]
        }
        logging.info("Messages permission granted with dummy data provided.")
    
    elif permission_type == 'file_access':
        response = {
            'ai_check': 'denied',
            'message': 'File access not granted'
        }
        logging.info("File access permission denied. User will be notified.")
    
    else:
        response = {'ai_check': 'denied', 'message': 'Invalid permission type'}
        logging.error("Invalid permission type requested.")

    return jsonify(response)

@app.route('/file-access', methods=['POST'])
def file_access():
    logging.info("File access request received.")
    return jsonify({'message': 'File access granted'})

@app.route('/logs')
def show_logs():
    try:
        with open('app.log', 'r') as file:
            logs = file.readlines()
        return render_template('logs.html', logs=logs)
    except FileNotFoundError:
        return "Log file not found", 404

if __name__ == '__main__':
    app.run(debug=True)
