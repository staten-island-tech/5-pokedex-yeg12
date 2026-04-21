import json
pokedex = open ("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
def pokemon():
    for s in data:
        print(s["name"]["english"])
pokemon()


# import json
# pokedex = open ("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)

# def pokemon():
#     user = input("what pokemon u want   ")
#     lang = input("Waht language u want  ")
#     for v in data :
#         if v["name"]["english"] == user:
#             print(v["name"][lang])
# pokemon()
        

# import json
# pokedex = open ("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)

# def pokemon():
#     type = input("hwat type of pokemon  ")
#     for a in data:
#         if type in a["type"]:
#             print(a["name"]["english"])
# pokemon()







# import json
# pokedex = open ("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)

# def pokemon():
#     search = input("input keywords for ur pokemon   ")
#     for k in data:
#         if search in k["name"]["english"]:
#             print(k["name"]["english"])
# pokemon()
