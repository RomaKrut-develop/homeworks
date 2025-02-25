class Device:
    def __init__(self, name, need_electricy, need_liquid, need_human_power):
        self.name = name
        self.need_electricy = need_electricy
        self.need_liquid = need_liquid
        self.need_human_power = need_human_power
    
    def show_info(self):
        print(f'for {self.name} need: ')

class CoffeMachine(Device):
    def __init__(self, name, need_electricy, need_liquid, need_human_power):
        super().__init__(name, need_electricy, need_liquid, need_human_power)
    def show_info(self):
        print(f"for {self.name} need: electricy: {self.need_electricy}, human power: {self.need_human_power}, water: {self.need_liquid}")

class Blender(Device):
    def __init__(self, name, need_electricy, need_liquid, need_human_power):
        super().__init__(name, need_electricy, need_liquid, need_human_power)
    def show_info(self):
        print(f"for {self.name} need: electricy: {self.need_electricy}, human power: {self.need_human_power}, water: {self.need_liquid}")

class MeatGrinder(Device):
    def __init__(self, name, need_electricy, need_liquid, need_human_power):
        super().__init__(name, need_electricy, need_liquid, need_human_power)
    def show_info(self):
        print(f"for {self.name} need: electricy: {self.need_electricy}, human power: {self.need_human_power}, water: {self.need_liquid}")

Coffe_Machine = CoffeMachine("Coffe Man 3000", "Yes", "Yes", "No")
Coffe_Machine.show_info()

Blender_cool = Blender("Mixagony", "Yes", "No", "No")
Blender_cool.show_info()

Meat_Grinder = MeatGrinder('Meatballer', "No", "No", "Yes")
Meat_Grinder.show_info()