from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

class RegularOrder(Order):
    def process_order(self):
        return "Regular is analyzing by standart method"
    
class SpecialOrder(Order):
    def process_order(self):
        return "Special is analyzing faster than standart method"
    
class InterOrder(Order):
    def process_order(self):
        return "International analyzing by border's condition and country's realtionship"
    
class OrderFactory(ABC):
    @abstractmethod
    def create_order(self):
        pass

class RegularOrderFactory(OrderFactory):
    def create_order(self):
        return RegularOrder()
    
class SpecialOrderFactory(OrderFactory):
    def create_order(self):
        return SpecialOrder()
    
class InterOrderFactory(OrderFactory):
    def create_order(self):
        return InterOrder()
    
def work_order(factory: OrderFactory):
    order = factory.create_order()
    print(order.procces_order())

regular_order_factory = RegularOrderFactory()
special_order_factory = SpecialOrderFactory()
international_order_factory = InterOrderFactory()

work_order(regular_order_factory)
work_order(special_order_factory)
work_order(international_order_factory)