import sys
import os
import json
import yaml
import xmltodict
from jsonschema import validate, ValidationError

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    input_ext = os.path.splitext(input_path)[1]
    output_ext = os.path.splitext(output_path)[1]
    
    return input_path, output_path, input_ext, output_ext

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        sys.exit(1)
    except ValidationError as e:
        print(f"JSON Validation Error: {e}")
        sys.exit(1)

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Invalid YAML format: {e}")
        sys.exit(1)

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def read_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = xmltodict.parse(file.read())
        return data
    except Exception as e:
        print(f"Invalid XML format: {e}")
        sys.exit(1)

def write_xml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            xml_str = xmltodict.unparse(data, pretty=True)
            file.write(xml_str)
    except Exception as e:
        print(f"Error writing XML: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_path, output_path, input_ext, output_ext = parse_arguments()
    
    if input_ext == '.json':
        data = read_json(input_path)
        print("JSON Data:", data)
    elif input_ext == '.yml' or input_ext == '.yaml':
        data = read_yaml(input_path)
        print("YAML Data:", data)
    elif input_ext == '.xml':
        data = read_xml(input_path)
        print("XML Data:", data)
    else:
        print(f"Unsupported input format: {input_ext}")
        sys.exit(1)
    
    if output_ext == '.json':
        write_json(data, output_path)
        print(f"Data saved to {output_path}")
    elif output_ext == '.yml' or output_ext == '.yaml':
        write_yaml(data, output_path)
        print(f"Data saved to {output_path}")
    elif output_ext == '.xml':
        write_xml(data, output_path)
        print(f"Data saved to {output_path}")
    else:
        print(f"Unsupported output format: {output_ext}")
        sys.exit(1)