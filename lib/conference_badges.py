def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    l = []
    for name in names:
        l.append(badge_maker(name))
    return l

def assign_rooms(names):
    l = []
    c = 1
    for name in names:
        l.append(f"Hello, {name}! You'll be assigned to room {c}!")
        c+=1
    return l

def printer(names):
    for name in batch_badge_creator(names):
        print(name)
    for assigns in assign_rooms(names):
        print(assigns)

    return None
