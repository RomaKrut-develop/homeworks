from abc import ABC, abstractmethod
from colorama import Fore, Style
from dataclasses import dataclass

class Device(ABC):
    @abstractmethod
    def get_device_info(self):
        pass

    @abstractmethod
    def use_device(self):
        pass

@dataclass
class MobileDevice(Device):
    def __init__(self):
        brand: str
        mode: str
        ram: int
        os: str
        
    def get_device_info(self):
        return Fore.LIGHTRED_EX + f"Smartphone: {self.brand}"  + Style.RESET_ALL
    
    def use_device(self):
        return  Fore.LIGHTRED_EX + f"Using the {self.brand} smartphone, model {self.mode} with {self.ram} RAM. OS: {self.os}"  + Style.RESET_ALL
    
@dataclass
class ComputerDevice(Device):
    def __init__(self):
        brand: str
        mode: str
        ram: int
        os: str
        
    def get_device_info(self):
        return Fore.LIGHTBLUE_EX + f"PC: {self.brand}"  + Style.RESET_ALL
    
    def use_device(self):
        return  Fore.LIGHTBLUE_EX + f"Using the {self.brand} PC, model {self.mode} with {self.ram} and {self.os} OS" + Style.RESET_ALL
    
class DeviceFactory(ABC):
    @abstractmethod
    def create_mobile_device(self) :
        pass

    @abstractmethod
    def create_computer_device(self):
        pass

class WindowsFactory(DeviceFactory):
    def create_mobile_device(self):
        return MobileDevice("Nokia", "Lumia 940", 2, "Windows Phone")
    
    def create_computer_device(self):
        return ComputerDevice("Desktop", "Default", 6, "Windows 8.1")
    
class AppleFactory(DeviceFactory):
    def create_mobile_device(self):
        return MobileDevice("Iphone", "16", 8, "MacOS")
    
    def create_computer_device(self):
        return ComputerDevice("Mac", "Apple", 16, "MacOS")

def demonstrate_device_usage(factory: DeviceFactory):
    mobile_device = factory.create_mobile_device()
    computer_device = factory.create_computer_device()

    print(mobile_device.get_device_info())
    print(mobile_device.use_device())

    print(computer_device.get_device_info())
    print(computer_device.use_device)

print("Apple Devices")
apple_factory = AppleFactory()
demonstrate_device_usage(apple_factory)
print()
print("Microsoft Devices")
windows_factory = WindowsFactory()
demonstrate_device_usage(windows_factory)