import os
import json
   
class Movies:
    def __init__(self, file):
        self.filename = file
        try:
            if os.path.exists(file):
                with open(self.filename, 'r', encoding="UTF-8") as File:
                    self.file = json.load(File)
                    print(File.read())
            else:
                self.file = []
        except json.JSONDecodeError:
            self.file = []
    
    def search_movie(self, nameMovie):
        for movie in self.file:
            if movie['name'] == nameMovie:
                return movie
            
    def add_movie(self, nameMovie, yearMovie):
        self.file.append({"name":nameMovie, "year":yearMovie})

    def del_movie(self, nameMovie):
        for movie in self.file:
            if movie['name'] == nameMovie:
                self.file.remove(movie)

    def save_file(self):
        with open(self.filename, 'w', encoding='UTF-8') as file:
            json.dump(self.file, file, indent=4, ensure_ascii=False)

FILE = "movie_list.json"
myMovie_List = Movies(FILE)
myMovie_List.del_movie('Devs')
myMovie_List.add_movie('Nerds', "2012")
myMovie_List.save_file()