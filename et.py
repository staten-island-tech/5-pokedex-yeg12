# import json
# pokedex = open ("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)
# def pokemon():
#     for s in data:
#         print(s["name"]["english"])
# pokemon()


import json
pokedex = open ("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
def pokemon():
    user = input("what pkemone u wnat")
    lang = input("what language u wnat")
pokemon()