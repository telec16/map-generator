print "coucou"

with open("buildings.cfg", "r") as file:
  raw = file.read()
  blueprint = raw.split("\n\n")
  cfgRe = re.pattern("\\(\w):(\d*)")
  configs = cfgRe.search(blueprint[0])
  blueprint.unset(blueprint[0])

#retrieve config ('\\')
#split "\n\n"
#split at first \n\w:
#create objects with class 'Blueprint'

#select random bluid
#create new object from object 'Blueprint' with random values with class 'Build'
#put randomly on map (and check possibility)

#stop if maxtry or maxfill

