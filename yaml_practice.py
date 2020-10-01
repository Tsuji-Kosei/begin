import yaml
with open('test.yaml') as file:
    yml = yaml.load(file)
    print(yml)