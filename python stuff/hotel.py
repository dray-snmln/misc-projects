class Hotel():
    def __init__(self, room_capacity):
        self.room_capacity = room_capacity
        self.guests = []
    
    def add_guest(self, name):
        if not self.available_rooms():
            print("No more rooms available")
            return False
        self.guests.append(name)
        return True

    def available_rooms(self):
        return self.room_capacity - len(self.guests)


print("Set the capacity of the hotel and add guests")
inp = int(input("hotel capacity: "))
hotel = Hotel(inp)

for _ in range(inp):
    x = input("Enter name of guest: ")
    success = hotel.add_guest(x)
    if success:
        print(f"   Added {x} successfully!")
    else:
        print("Error")


print("Hotel capacity has been reached.\n")

for i in range(inp):
    print(f"Room no.{i+1}: {hotel.guests[i-1]}")

# test