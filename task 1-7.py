import sys
import json
import yaml
import xml.etree.ElementTree as ET

def xml_to_json(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_dict = {}
    for elem in root:
        data_dict[elem.tag] = elem.text
    return json.dumps(data_dict, indent=4)

def json_to_xml(json_path):
    with open(json_path) as json_file:
        data_dict = json.load(json_file)
        root = ET.Element("root")
        for key, value in data_dict.items():
            elem = ET.SubElement(root, key)
            elem.text = str(value)
        return ET.tostring(root, encoding="unicode")

def json_to_yaml(json_path):
    with open(json_path) as json_file:
        data_dict = json.load(json_file)
        return yaml.dump(data_dict, default_flow_style=False)

def yaml_to_json(yaml_path):
    with open(yaml_path) as yaml_file:
        data_dict = yaml.safe_load(yaml_file)
        return json.dumps(data_dict, indent=4)

def xml_to_yaml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data_dict = {}
    for elem in root:
        data_dict[elem.tag] = elem.text
    return yaml.dump(data_dict, default_flow_style=False)

def yaml_to_xml(yaml_path):
    with open(yaml_path) as yaml_file:
        data_dict = yaml.safe_load(yaml_file)
        root = ET.Element("root")
        for key, value in data_dict.items():
            elem = ET.SubElement(root, key)
            elem.text = str(value)
        return ET.tostring(root, encoding="unicode")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: program.py inputFile outputFile")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_ext = input_file.split(".")[-1].lower()
    output_ext = output_file.split(".")[-1].lower()

    if input_ext == "xml" and output_ext == "json":
        result_data = xml_to_json(input_file)
    elif input_ext == "json" and output_ext == "xml":
        result_data = json_to_xml(input_file)
    elif input_ext == "json" and output_ext == "yaml":
        result_data = json_to_yaml(input_file)
    elif input_ext == "yaml" and output_ext == "json":
        result_data = yaml_to_json(input_file)
    elif input_ext == "xml" and output_ext == "yaml":
        result_data = xml_to_yaml(input_file)
    elif input_ext == "yaml" and output_ext == "xml":
        result_data = yaml_to_xml(input_file)
    else:
        print("Unsupported file extensions.")
        sys.exit(1)

    with open(output_file, "w") as output:
        output.write(result_data)

    print(f"Conversion from {input_ext} to {output_ext} completed successfully.")
