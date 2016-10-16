# python sequences: hold a collection, or sequence, of items; e.g. list, tuple, set
# set: unordered collection of items
# dictionary: holds key:value pairs; unordered collection
# tuple: cannot add or delete items
    # line = "a apples"
    # command = line[:1] // a
        # square brackets indicate splice
    # item = line[2:] // apples
    # order = command, item // creates a tuple. Implicit (); could also be written
        # order = (command, item)
        #'order' returns (a, apples) // 'command' returns a // 'item' returns apples
    # c, i = order
        # unpacking a tuple
        # 'c' returns a
        # i returns apples

def get_order():
    print("[command] [item] [command is 'a' to add; 'd' to delete'; 'q' to quit] ")
    line = input()
    
    command = line[:1]
    item = line[2:]

    return command, item

def process_order(order, cart):
    command, item = order

    if command == "a":
        # TODO: When cart = [] and cart.append(item), items get appended twice. WHY?
        cart.add(item)
    elif command == "d" and item in cart:
        cart.remove(item)
    elif command == "q":
        return False

    return True

def go_shopping():
    cart = set()

    while True:
        order = get_order()
        process_order(order, cart)
        if not process_order(order, cart):
            break

    print(cart)
    print("Finished")
    
go_shopping()
