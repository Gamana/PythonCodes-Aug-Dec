# In Python, multithreading allows different parts of your code to 
# run together at the same time. Instead of waiting for one function to 
# finish before starting another, you can run them simultaneously, 
# which makes your program faster and more efficient.

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Pause for 1 second

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)  # Pause for 1 second

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All tasks are complete!")