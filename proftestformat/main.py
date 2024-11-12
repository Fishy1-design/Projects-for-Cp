#ProficiencyTest: What are these numbers?

number = int(input("what is your number?:"))

print("thousandths:")
matted = "{:,}".format(number)
print(matted)

print("This is it with 4 decimal places:")
formatted = "{:.4f}".format(number)
print(formatted)

print("Precent:")
format = "{:%}".format(number)
print(format)

print("dollar ammount:")
form = "{:.2f}".format(number)
print("$",form)