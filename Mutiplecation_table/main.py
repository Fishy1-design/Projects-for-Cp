# ProficiencyTest: Multiplication Table

def print_multiples_of(number):
    # Printing the multiples of the given number from 0 to 12
    print(f"Multiples of {number}:")
    for i in range(13):
        print(f"{number} x {i} = {number * i}")
    print()  # Blank line for readability

def print_full_multiplication_table():
    # Printing a full multiplication table (1-12)
    print("Multiplication Table (1 to 12):\n")
    
    # Print the header row with numbers 1 to 12
    print("     ", end="")
    for i in range(1, 13):
        print(f"{i:4}", end="")
    print("\n" + " " * 5 + "-" * 48)  # Line to separate header

    # Print each row of the multiplication table
    for i in range(1, 13):
        # Print the row label (the number being multiplied)
        print(f"{i:2} |", end="")
        for j in range(1, 13):
            print(f"{i * j:4}", end="")
        print()  # New line after each row

# Main execution
if __name__ == "__main__":
    # Ask the user for a number and print its multiples from 0 to 12
    number = int(input("Enter a number to see its multiples from 0 to 12: "))
    print_multiples_of(number)

    # Bonus: Print the full multiplication table
    print_full_multiplication_table()
