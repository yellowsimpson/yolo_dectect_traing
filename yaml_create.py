import yaml

data = {
    "train" : '/home/shim/truck.v2-truck-detect.yolov8/train/',
        "val" : '/home/shim/truck.v2-truck-detect.yolov8/val/',
        "test" : '/home/shim/truck.v2-truck-detect.yolov8/test/', 
        "names" : {0 : 'truck'}}

with open('./truck_detect.yaml', 'w') as f :
    yaml.dump(data, f)

# check written file
with open('./box_data.yaml', 'r') as f :
    lines = yaml.safe_load(f)
    print(lines)
    