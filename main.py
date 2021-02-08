import pyttsx3
engine = pyttsx3.init('sapi5')

engine.say("Welcome to the calculator")
engine.runAndWait()
print ("Welcome to the calculator")
def calculator():
    engine.say("Enter the first number")
    engine.runAndWait()
    x = float (input("Enter the first number:- "))
    engine.say("Enter the second number")
    engine.runAndWait()
    y = float (input ("Enter the second number:- "))

    a = str (x)
    b = str (y)

    add = str (x + y)
    sub1 = str (x- y)
    sub2 = str (y - x)
    mul = str (x * y)
    div1 = str (x/ y)
    div2 = str (y/ x)

    engine.say("Press 1 for Addition, 2 for Subtraction, 3 for Multiplication, & 4 for Division")
    engine.runAndWait()
    s = str (input ("Press 1 for Addition, 2 for Subtraction, 3 for Multiplication, & 4 for Division:- "))

    if s == '1':
        engine.say ("The sum of " + a + " and " + b + " is " + add)
        print ("The sum of " + a + " and " + b + " is " + add)
    elif s == '2':
        if a >= b:
            engine.say ("The difference between " + a + " and " + b + " is " + sub1)
            print ("The difference between " + a + " and " + b + " is " + sub1)
        else:
            engine.say ("The difference between " + b + " and " + a + " is " + sub2)
            print ("The difference between " + b + " and " + a + " is " + sub2)
    elif s == '3':
        engine.say ("The product of " + a + " and " + b + " is " + mul)
        print ("The product of " + a + " and " + b + " is " + mul)
    elif s == '4':
        if a >= b:
            engine.say ("The remainder while dividing " + a + " from " + b + " is " + div1)
            print ("The remainder while dividing " + a + " from " + b + " is " + div1)
        else:
            engine.say ("The remainder while dividing " + b + " from " + a + " is " + div2)
            print ("The remainder while dividing " + b + " from " + a + " is " + div2)
    else:
        engine.say("Invalid Input")
        print ("Invalid Input")
        print ()
        calculator()
    engine.runAndWait()
    print ()

calculator()

while True:
    engine.say("Do you want to reuse the application?")
    engine.runAndWait()
    print ("Do you want to reuse the application?")

    engine.say("Press 1 for Yes and 2 for no")
    engine.runAndWait()
    g = str (input ("Press 1 for Yes and 2 for no:- "))

    if g == '1':
        print ()
        calculator()
    elif g == '2':
        engine.say("Thank you for using the application!")
        engine.runAndWait()
        print("Thank you for using the application!")
        break
    else:
        engine.say ("Invalid Input")
        
        print ("Invalid Input")
        print ()
