from flask import Flask, jsonify
import os
import yaml

app = Flask(__name__)

def load_config():
    
    config_file_path = os.getenv('PY_CONFIG_FILE_PATH', 'config.yaml')
    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

@app.route('/hello')
def hello():
    
    config = load_config()
    # Get values from config.yaml
    message = config.get('message', 'Hello World!')
    environment = config.get('environment', 'no_env')
    secretEnvName = config.get('varSecretVaultName')
    secret_variable = os.environ.get(secretEnvName, 'no_secret')

    return jsonify({
        'message': message,
        'environment': environment,
        'secret_variable': secret_variable
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
