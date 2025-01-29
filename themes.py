import csv 

DARA = "themes.csv"

themes = [
    ['HTML-CSS', "Studying"],
    ['XML', "Not studying"],
    ['JavaScript', "Studying"],
    ['Python', "Studying"],
    ['C++', "Studying"],
    ['Objective-C', "Not studying"],
    ['Pascal', "Not studying"],
    ['Holy C', "Studying with god's allow"],
    ['Jython', "Studying"],
    ['DaraScript', "Studying"],
    ['Scratch', "Not studying"],
    ['Ruby', 'Studying'],
    ['Hexagony', 'Not studying'],
    ['1C', 'Forgotted']
]

with open(DARA, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(themes)

with open(DARA, "a", newline="") as file:
    themes = ["Assembley", "Almost studying"]
    writer = csv.writer(file)
    writer.writerow(themes)