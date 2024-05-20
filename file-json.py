import json

# Data that will become json #
# Can be lists, dictionaries or tuples #
data = {
    'name': 'Jeanfsantos',
    'instagram': '@jeanfsantos',
    'language': 'python',
    'content': [
        {'content': 'codes'},
        {'content': 'curiosities'}
    ]
}

# Creates the json file in the path specified below #
with open(r'.\dados.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
