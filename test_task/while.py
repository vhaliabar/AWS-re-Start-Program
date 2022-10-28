# entered_number = False
# list = []
# while entered_number != True:
#     number = input("Please enter a number:")
#     if int(number) != -1:
#         list.append(int(number))
#         print("Thank you!")
#         entered_number = False
#     else:
#         entered_number = True
#         print("You've entered -1. Script stopped! The everage number is:", sum(list)/len(list))


entered_number = False
list = []
while entered_number != True:
    number = input("Please enter a number:")
    try:
        if isinstance(number, int):
            if int(number) != -1:
                list.append(int(number))
                print("Thank you!")
                entered_number = False
            else:
                entered_number = True
                print("You've entered -1. Script stopped! The everage number is:", sum(list)/len(list))
    except: raise ValueError('Its not a number!')