class Shoe:
    def __init__(self, male, female, type, color, price, size, made_by):
        self.male = male
        self.female = female
        self.type = type
        self.color = color
        self.price = price
        self.size = size
        self.made_by = made_by

class ShoeModel:
    def __init__(self, shoe_data_base):
        self.shoe_data_base = shoe_data_base

    def get_shoe_by_gender(self, male, female):
        data = self.shoe_data_base.get(male, female)
        if data:
            return Shoe(data['gender'])
        return False

class UserView:
    def display_user(self, shoe):
        if shoe:
            print(f"Shoe: {shoe.female}")
        else:
            print("404")

    def display_message(self, message):
        print(message)