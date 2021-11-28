favorite_places={
   "Piti" : ["bridge", "shop"],
   "Adam" : ["a park", "town"],
   "Dana" : ["underground", "river"]
    }
for p, i in favorite_places.items():
    print(p.title() + " favorite places is : ")
    for place in i:
        print(place.title())
