
def HelloWorld(myString):
    print(myString)

    myName = input("What is your name ? ")
    myVar = input("Enter a number ")
    # print(myName)

    if myName == "Avinash" or myVar == 1:
        print("Dude... your are the MAN..!")
    elif myName == "Raju" or myVar == 2:
        print(myName + " you are great")

    else:
        print("bhak sale...")

HelloWorld("Hello Function World")
HelloWorld("Hello 123 World")

