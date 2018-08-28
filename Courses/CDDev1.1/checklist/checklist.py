checklist = []
def create(item):
    checklist.append(item)
def read(index):
    return checklist[index]
def update(index,item):
    checklist[index] = item
def destroy(index):
    checklist.pop(index)
def list_all_items():
    indx = 0
    for i in checklist:
        print(str(indx) + ", " + i)
        indx += 1
def mark_completed(index):
    brief = checklist[index]
    checklist[index] = u'\u2713' + brief
def select(code):
    if code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
    elif code == "R":
        item_index = user_input("Index number: ")
        read(item_index)
    elif code == "L":
        list_all_items()
    elif code == "E":
        running = False
    else:
        print("Unknown Option")
def user_input(prompt):
    user_input = input(prompt)
    return user_input
running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, L to display list, and E to exit: ")
    running = select(selection)
def test():
    create("Puse")
    print(read(0))
    create("Cobalt")
    print(read(1))
    create("Fusia")
    mark_completed(0)
    list_all_items()
    select("R")
    select("C")
    select("L")
    user_value = user_input("Please Enter a value: ")
    print(user_value)
    destroy(0)
#test()
