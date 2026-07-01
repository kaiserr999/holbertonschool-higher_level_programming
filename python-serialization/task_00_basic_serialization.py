import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    
    :param data: A Python Dictionary with data
    :param filename: The filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file.
    
    :param filename: The filename of the input JSON file
    :return: A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
