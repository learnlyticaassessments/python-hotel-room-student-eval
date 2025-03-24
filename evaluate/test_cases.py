def test_room_str(student):
    r = student.Room("Alice")
    return str(r) == "Room booked for Alice"

def test_luxury_str(student):
    lr = student.LuxuryRoom("Bob", 5)
    return str(lr) == "Luxury Room booked for Bob with 5 minibar items"

def test_del(student):
    try:
        r = student.Room("Charlie")
        del r
        return True
    except:
        return False

def test_subclass_check(student):
    return issubclass(student.LuxuryRoom, student.Room)

test_suite = {
    "TC1": (test_room_str, 2.5),
    "TC2": (test_luxury_str, 2.5),
    "TC3": (test_del, 2.5),
    "HTC1": (test_subclass_check, 2.5)
}
