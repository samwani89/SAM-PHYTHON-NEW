counter = 0  

def increment_counter():
    counter = 0 
    counter += 1
    print(f"Counter inside the function: {counter}")

increment_counter()  
increment_counter()  
increment_counter()  

print(f"Counter outside the function: {counter}")  