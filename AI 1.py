def display_rooms(roomA, roomB, location):
    print("\n-------------------")
    print("Current Environment")
    print("\n-------------------")
    print("Room A:", roomA)
    print("Room B:", roomB)
    print("Vacuum Location :", location)
    print("---------------------")

roomA = input("Enter Room A Status (Clean/Dirty): ").capitalize()
roomB = input("Emter Room B Status (Clean/Dirty): ").capitalize()
location = input("Enter Vacuum Location (A/B): ").upper()
count = 0

display_rooms(roomA, roomB, location)

print("\nActions Performed")

while roomA == "Dirty" or roomB == "Dirty":

    if location == "A":
        if location == "Dirty":
            print("Room A is dirty -> Clean")
            count += 1
            roomA = "Clean"
        else:
            print("Room A is clean -> Move Right")
            count += 1
            location = "B"

    elif location == "B":
        if roomB == "Dirty":
            print("Room B is Dirty -> Clean")
            count += 1
            roomB = "Clean"
        else:
            print("Room B is Clean -> Move Left")
            count += 1
            location = "A"

display_rooms(roomA, roomB, location)

print("Both Rooms are Clean.")
print("Action: NO OP (Stop)")
print("Total Actions Performed:", count)

