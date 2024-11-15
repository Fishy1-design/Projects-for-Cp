# ProficiencyTest: Multiplication Table

def print_multiples_of(number):
    # This displaies the Multaples the number you pick (oﾟvﾟ)ノ 
    print(f"Multiples of {number}:")
    for i in range(13):
        print(f"{number} x {i} = {number * i}")
    print()  # Blank line to make it eaiser to read 🙀

def print_full_multiplication_table():
    # This prints a full multiplication table (1-12)
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

# The body or the main part of the program: ✌️
if __name__ == "__main__":
    # Ask the user for a number and print its multiples from 0 to 12
    number = int(input("Enter a number to see its multiples from 0 to 12: "))
    print_multiples_of(number)

    # The Bonus: Print the full multiplication table BECAUSE IM COOL! щ(ʘ╻ʘ)щ
    print_full_multiplication_table()
