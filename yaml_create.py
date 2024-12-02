import yaml

data = {
    "train" : '/box_data_4/train/',
        "val" : '/box_data_4/valid/',
        "test" : '/box_data_4/test/', 
        "names" : {0 : 'box'}}

with open('./box_data_4.yaml', 'w') as f :
    yaml.dump(data, f)

# check written file
with open('./box_data_4.yaml', 'r') as f :
    lines = yaml.safe_load(f)
    print(lines)
    