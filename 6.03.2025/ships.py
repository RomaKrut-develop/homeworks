class Base_Ship:
    def __init__(self, name, weight, speed, crew, type):
        self.name = name
        self.type = type
        self.weight = weight
        self.speed = speed
        self.crew = crew
        if self.crew < 189 and not self.crew > 189:
            self.type = "Frigate"
        elif self.crew < 600:
            self.type = "Destroyer"
        elif self.crew > 600:
            self.type = "Crusier"
    
    def show_info(self):
        print(f'{self.type} are: {self.name}. Weight: {self.weight}, Speed: {self.speed}, Crew: {self.crew} People')

class Frigate(Base_Ship):
    def __init__(self, name, weight, speed, crew, type):
        super().__init__(name, weight, speed, crew, type)
    def show_info(self):
        return super().show_info()
    
class Destroyer(Base_Ship):
    def __init__(self, name, weight, speed, crew, type):
        super().__init__(name, weight, speed, crew, type)
    def show_info(self):
        return super().show_info()
    
class Cruiser(Base_Ship):
    def __init__(self, name, weight, speed, crew, type):
        super().__init__(name, weight, speed, crew, type)
    def show_info(self):
        return super().show_info()
    
Brave_Ronald = Frigate("Brave Ronald", "Light", "High", 109, ())
Brave_Ronald.show_info()

Duke_Linkoln = Frigate("Duke Linkoln", "Medium", "Medium", 230, ())
Duke_Linkoln.show_info()

Tsar_Ivan = Frigate("Tsar Ivan", "Very Heavy", "Medium", 700, ())
Tsar_Ivan.show_info()