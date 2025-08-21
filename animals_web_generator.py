import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
for animal in animals_data:
    print(f"Name: {animal['name']}")
    print(f"Diet: {animal['characteristics']['diet']}")
    print("Locations: ", end="")
    [print(location + ", ", end="") for location in animal['locations']]
    if "type" in animal['taxonomy']:
        print(animal['taxonomy']['type'])
    print()
    print('\n')
