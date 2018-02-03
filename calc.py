5


a = """My first program, try it:"""
c = "do you want to count more???"
print (a)
loop = 1
choice = 0
while loop == 1:
    x=int(input("type in first number: "))
    y=int(input("type in second number: "))
    z=input("Choose your operand, type +,-,* or / : ")
    if z == "+":
        print ("result is: ",(x+y))
    elif z == "*":
        print ("result is: ",(x*y))
    elif z == "-":
        print ("result is: ",(x - y))
    elif z == "/":
        print ("result is: ",(x / y))
    else:
        print ("wrong data!!!")
    print (c)
