def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = f"Hello, my name is {name}."
        badges.append(badge)
    return badges

def assign_rooms(names):
    rooms = range(1, 9)
    room_assignments = []
    for i, name in enumerate(names):
        room = rooms[i % len(rooms)]
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {room}!")
    
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)
