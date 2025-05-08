import threading
import time
import random

stock = {
    'GeForce RTX 4090': 36,
    'Intel Pentium IV': 5,
    'Intel Core I7 13620h': 12,
}

stock_lock = threading.Lock()

def add_item(stock, item_name, quantity):
    with stock_lock:
        if item_name in stock:
            stock[item_name] += quantity
        else:
            stock[item_name] = quantity
        print(f'Added {quantity} amount of goods {item_name}. Now: {stock[item_name]}')

def remove_item(stock, item_name, quantity):
    with stock_lock:
        if item_name in stock and stock[item_name] >= quantity:
            stock[item_name] -= quantity
            print(f'Deleted {quantity} amount of goods {item_name}. Now: {stock[item_name]}')
        else:
            print(f'Cannot delete {quantity} amount of {item_name}')

def thread_operation(stock):
    for _ in range(random.randint(20, 50)):
        operation = random.choice(['add', 'remove'])
        item_name = random.choice(list(stock.keys()))
        quantity = random.randint(1, 10)

        if operation == 'add':
            add_item(stock, item_name, quantity)
        else:
            remove_item(stock, item_name, quantity)
        time.sleep(random.uniform(0.1, 0.6))

threads = []

for _ in range(random.randint(5, 10)):
    thread = threading.Thread(target=thread_operation, args=(stock, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('\nIn total: ')
for item, quantity in stock.items():
    print(f'{item}:{quantity}')