import json
import yaml 


# converts json to yaml
def j2y_converter(path):
    with open(path) as f:
        to_yaml = json.load(f)
    with open('/Users/sean/labs/PyJsonYaml/converted j2y.yaml', 'w') as j:
        yaml.dump(to_yaml, j)


# pickle.dump(read_all_json_files(path), f)

# converts yaml to json
def y2j_converter(path):
    with open(path) as f:
        to_json = yaml.load(f)
    with open('/Users/sean/labs/PyJsonYaml/converted y2j.json', 'w') as j:
        json.dump(to_json, j)

#j2y_converter('/Users/sean/labs/PyJsonYaml/donuts.json')

y2j_converter('/Users/sean/labs/PyJsonYaml/xmas.yaml')


