# Define Tower of Hanoi function
def tower_of_hanoi(n, source, auxiliary, destination):
    # n = Number of disks
    # source = Starting rod
    # auxiliary = Helper rod
    # destination = Final rod

    if n == 1:
        # Base condition: If only one disk is left

        print("Move Disk 1 from", source, "to", destination)
        # Move the smallest disk directly to destination

        return
        # Stop the current recursive function call

    tower_of_hanoi(n-1, source, destination, auxiliary)
    # Move n-1 disks from source to auxiliary
    # Using destination as helper rod

    print("Move disk", n, "from", source, "to", destination)
    # Move the largest remaining disk to destination

    tower_of_hanoi(n-1, auxiliary, source, destination)
    # Move n-1 disks from auxiliary to destination
    # Using source as helper rod


# Take input from user
n = int(input("Enter the number of disks: "))
# Accept number of disks and convert input into integer

print("\nSteps: ")
# Display heading for the steps

tower_of_hanoi(n, 'A', 'B', 'C')
# Call function:
# A = Source rod
# B = Auxiliary rod
# C = Destination rod

print("\nMinimum number of moves: ", 2 ** n - 1)
# Display minimum moves required.
# Formula = 2^n - 1
