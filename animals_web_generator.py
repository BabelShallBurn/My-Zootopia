import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html(file_path):
  """ Loads a HTML file """
  with open(file_path, "r") as handle:
      html_content = handle.read()
      return html_content


animals_data = load_data('animals_data.json')

html_data = load_html('animals_template.html')

animals_data_string = ""

for animal in animals_data:
    animals_data_string += f"Name: {animal['name']}\n"
    animals_data_string += f"Diet: {animal['characteristics']['diet']}\n"
    locations = "Locations: "
    for location in animal['locations']:
        locations += f"{location}, "
    animals_data_string += locations + "\n"
    if "type" in animal['taxonomy']:
        animals_data_string += f"{animal['taxonomy']['type']}\n"

html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_data_string)

with open("animals_data.html", "w") as handle:
    handle.write(html_data)
