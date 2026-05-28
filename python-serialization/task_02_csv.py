import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.
    
    :param csv_filename: The name of the CSV file to read.
    :return: True if successful, False if the file falls not found or other exceptions occur.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
            
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
            
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
