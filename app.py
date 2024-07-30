from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    action = data.get('action')
    characters = data.get('characters')
    
    # Log received data
    logging.info(f"Action: {action}")
    logging.info(f"Characters detected: {characters}")
    
    # Respond with a success message
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
