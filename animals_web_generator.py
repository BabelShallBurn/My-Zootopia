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
    animals_data_string += '<li class="cards__item">\n'
    animals_data_string += f'  <div class="card__title">{animal['name']}</div>\n'
    animals_data_string += '  <p class="card__text">\n'
    animals_data_string += f'    <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n'
    locations = "    <strong>Locations:</strong> "
    if len(animal['locations']) > 1:
        for i, location in enumerate(animal['locations']):
            if i == len(animal['locations']) - 1:
                locations += f"{location}"
            else:
                locations += f"{location}, "
    else:
        locations += animal['locations'][0]
    animals_data_string += locations + "<br/>\n"
    if "type" in animal['characteristics']:
        animals_data_string += f'    <strong> Type:</strong> {animal['characteristics']['type']}<br/>\n'
    animals_data_string += "  </p>\n"
    animals_data_string += '</li>\n'


html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_data_string)

with open("animals_data.html", "w") as handle:
    handle.write(html_data)
