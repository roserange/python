print("Welcome to Simple calculator in Python")

while True:
    expression = input("Enter expression: ")
    try:
        print(eval(expression))
    except:
        print("Please enter correct expression")
        continue
    choice = input("Enter 'E' to exit program else any key to continue: ")
    if choice=='E':
        print("Exiting...")
        break
    continue
