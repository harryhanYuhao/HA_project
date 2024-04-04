import json
import os

file_names = [
    "./page_rank_info.ipynb",
    "./power_iteration.ipynb",
    "./markov_matrix.ipynb",
    "./sum_up.ipynb"
]

build_destination = "./build/project.ipynb"


def write_components_to_file(file_name, components):
    # create directory
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))

    f = open(file_name, "w")
    f.write(json.dumps(components))
    f.close()


final_json = {}
cells = []


f = open(file_names[2], "r")
j = json.load(f)
f.close()


for i in file_names:
    f = open(i, "r")
    j = json.load(f)
    f.close()
    cells += j["cells"]


final_json["cells"] = cells
for i in j:
    if i == "cells":
        continue
    final_json[i] = j[i]

write_components_to_file(build_destination, final_json)
