import re
from pprint import pprint

from Blueprint import Blueprint


def get_configs(cfgs, name):
    for c in cfgs:
        if c[0] == name:
            return int(c[1])


# Read file
with open("buildings.cfg", "r") as file:
    raw = file.read()
raw_bp = raw.split("\n\n")

# Retrieve config
configs = re.findall(r'\\(\w)=(\d*)', raw_bp.pop(0))
maxtry = get_configs(configs, "t")
maxfill = get_configs(configs, "f")

# Split pattern and values
patterns = [re.split(r'\n(\w):', b) for b in raw_bp]
blueprints = [Blueprint(pattern) for pattern in patterns]

# Generate map
tries = 0
filling = 0
stop = False
while not stop:
    placed = False

    

    tries = 0 if placed else tries+1
    stop = (tries >= maxtry) or (filling >= maxfill)

# select random bluid
# create new object from object 'Blueprint' with random values with class 'Build'
# put randomly on map (and check possibility)
