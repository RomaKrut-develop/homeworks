# Ghost rider
import heapq
from colorama import Style, Fore, Back

class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.counter = 0 # Счётчик для обеспечения порядка добавления при одинаковых приоритетах
    
    def enqueqe(self, item, priority):
        heapq.heappush(self.__queue, (priority, self.counter, item))
        self.counter += 1

    def is_empty(self):
        return len(self.__queue) == 0

    def dequeu(self):
        if not self.is_empty():
            return heapq.heappop(self.__queue)[2]
        else:
            raise IndexError(Fore.LIGHTRED_EX + "Cannot delete elements from queue. Queue is empty" + Style.RESET_ALL)
        
pq = PriorityQueue()

pq.enqueqe(Fore.LIGHTRED_EX + "task1" + Style.RESET_ALL, 3)
pq.enqueqe(Fore.LIGHTGREEN_EX + "task2" + Style.RESET_ALL, 2)
pq.enqueqe(Fore.LIGHTBLUE_EX + "task3" + Style.RESET_ALL, 1)

print(pq.dequeu())
print(pq.dequeu())
print(pq.dequeu())