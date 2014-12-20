__author__ = 'BELLAICHE Adrien'

from os import listdir
from ford_fulkerson import execute_algorithm


corresponding = {"\xeb": "e",
                 "\xe9": "e",
                 "\xe8": "e",
                 "\n": ""}


def clean_line(value):
    thing = list(value)
    for _ in range(len(thing)):
        if thing[_] in corresponding:
            thing[_] = corresponding[thing[_]]
    return ''.join(thing)


def get_name(value):
    return clean_line(value.split(",")[1] + " " + value.split(",")[0])


file_names = listdir("csv")
name_id = {}
k = 0
# Attribution des ID
name_id["Source"] = k
for name in file_names:
    k += 1
    name_id[clean_line(name.split(".")[0])] = k
idKnows = [[] for _ in name_id]
# Definition des connaissances
corresponding_file = open('correspondance.txt', 'w')
for name in file_names:
    self_name = clean_line(name.split(".")[0])
    selfID = name_id[self_name]
    with open("csv/" + name, 'r') as data:
        lines = data.readlines()
        for line in lines:
            if line != ',\n':
                if get_name(line) in name_id:
                    if get_name(line) != self_name:
                        idKnows[selfID].append(name_id[get_name(line)])
    corresponding_file.write(str(selfID) + " " + self_name + "\n")
corresponding_file.close()

for name in name_id:
    if name != "Source":
        idKnows[0].append(name_id[name])

with open("ex.graph", 'w') as out:
    out.write(str(2 * len(name_id)) + '\n')
    for name in name_id:
        selfID = name_id[clean_line(name.split(".")[0])]
        if name == "Source":
            for known in idKnows[name_id[name]]:
                out.write('0' + ' ' + str(known) + ' 1\n')
        else:
            for known in idKnows[name_id[name]]:
                out.write(str(selfID) + ' ' + str(known + len(name_id) - 1) + ' 1\n')
            out.write(str(selfID + len(name_id) - 1) + ' ' + str(2 * len(name_id) - 1) + ' 1\n')
execute_algorithm()