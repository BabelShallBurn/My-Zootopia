import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as fileobj:
        return json.load(fileobj)


def load_html(file_path):
    """ Loads a HTML file """
    with open(file_path, "r", encoding="utf-8") as fileobj:
        html_content = fileobj.read()
        return html_content


def serialize_animal(animal):
    """ Serializes an animal """
    animal_obj = ''
    animal_obj += '<li class="cards__item">\n'
    animal_obj += f'  <div class="card__title">{animal["name"]}</div>\n'
    animal_obj += '  <p class="card__text">\n'
    animal_obj += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
    locations = "    <strong>Locations:</strong> "
    if len(animal['locations']) > 1:
        for i, location in enumerate(animal['locations']):
            if i == len(animal['locations']) - 1:
                locations += f"{location}"
            else:
                locations += f"{location}, "
    else:
        locations += animal['locations'][0]
    animal_obj += locations + "<br/>\n"
    if "type" in animal['characteristics']:
        animal_obj += f'    <strong> Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
    if "distinctive_feature" in animal['characteristics']:
        animal_obj += f'    <strong>Distinctive Feature:</strong> {animal["characteristics"]["distinctive_feature"]}<br/>\n'
    if "temperament" in animal['characteristics']:
        animal_obj += f'    <strong>Temperament:</strong> {animal["characteristics"]["temperament"]}<br/>\n'
    if "lifespan" in animal['characteristics']:
        animal_obj += f'    <strong>Lifespan:</strong> {animal["characteristics"]["lifespan"]}<br/>\n'
    animal_obj += "  </p>\n"
    animal_obj += '</li>\n'
    return animal_obj

animals_data = load_data('animals_data.json')

html_data = load_html('animals_template.html')

animals_data_string = ""

for animal_item in animals_data:
    animals_data_string += serialize_animal(animal_item)



html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_data_string)

with open("animals_data.html", "w", encoding="utf-8") as handle:
    handle.write(html_data)
