import json

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)
    

def save_config(config_path, config_data):
    with open(config_path, 'w'):
        json.dump(config_data, config_path)