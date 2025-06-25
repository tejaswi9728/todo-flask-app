"""
new = []
def view_tasks():
    for index,task in enumerate(new, start =1):
        print(index, task)
view_tasks()
def add_tasks():
    while True:
        your_tasks = input("Add your tasks:" )

        if your_tasks == "exit":
            break
        new.append(your_tasks)
    print("Task added succesfully")
    print("your tasks are:" )
    for index,new_one in enumerate(new, start =1):
        print(index, new_one)
add_tasks()
def tasks_done():
    done_tasks = input("enter your task numbers as (comma-seperated):")
    numbers = done_tasks.split(",")
    for num in numbers:
        if num.strip().isdigit():
            index = int(num.strip())
            if 1 <= index  <= len(new):
                print(f"task  {new[index -1]} as done")
            else:
                print("invlid num")
        else:
            print("out of range")

tasks_done()
"""

