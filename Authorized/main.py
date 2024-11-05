#ProficiencyTest: Authorized

admin = ["D0g", "ca1", "f1sh-101", "<python>"]

users = ["smile", "tree", "dead fish", "skeleton"]

authorized=input("whats your account name?:")

if authorized in users:

    print("welcome to the system user!")
elif  authorized in admin:
    print("welcome to the sytem admin!")

else:
    print("Sorry go back and check your account name, you may be banned from the system.")    
