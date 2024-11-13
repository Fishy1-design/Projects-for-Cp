#Elisheva Kibbie, ProficiencyTest: Secret Cypher

# A cool thing to encode a string using a Caesar Cipher B-)
def shift_message(message, shift):
    shifted_message = ""
    for char in message:
        # Check if character is a letter
        if char.isalpha():
            # Shift lettered Messages 
            # My Dad told me about ASCII characters, he had to explane it to me VERY slowly lol 😭✌️
            shift_base = 65 if char.isupper() else 97
            shifted_letter = chr(((ord(char) - shift_base + shift) % 26) + shift_base)
            shifted_message += shifted_letter
        else:
            # Numbers remain the same
            shifted_message += char
    return shifted_message

# This block decodes the message ( •̀ ω •́ )✧
def decode_message(shifted_message, shift):
    return shift_message(shifted_message, -shift)

# Example 
if __name__ == "__main__":
    # This asks for an input
    #my dad told me to put comments through out my code, apparently it makes it eaiser to read ╰（‵□′）╯
    user_message = input("Enter a message to encode: ")
    shift_value = int(input("Enter a shift value: "))

    # This encodes the message
    secret_code = shift_message(user_message, shift_value)
    print(f"Encoded Message: {secret_code}")

    # This decodes the message
    decoded_message = decode_message(secret_code, shift_value)
    print(f"Decoded Message: {decoded_message}")
