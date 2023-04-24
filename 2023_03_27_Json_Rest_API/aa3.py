import json

class House:
    def __init__(self):
        self.name = "House"
        self.rooms = []


h = House()

print(type(json.dumps(h.__dict__)))
