import os
import json


# def load_db_config():
#     """TODO need to implement the basedir"""
#
#     json_file_path = "src/resources/db_config.json"
#
#     with open(json_file_path, 'r') as fr:
#         content = json.loads(fr.read())
#
#     return content




def load_db_config():
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'db_config.json')
    with open(json_file_path, 'r') as fr:
        content = json.load(fr)  # Use json.load() to parse JSON correctly
    return content
