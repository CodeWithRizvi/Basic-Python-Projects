first= int(input("Enter first number: "))
operator=input("Enter operator(+ , - , * , /  , % ): ")
second= int(input("Enter second number: "))

#Perform any operator
if operator=="+":
    print(f"{first} + {second}","=",first+second)
elif operator=="-":
    print(f"{first} - {second}","=",first-second)
elif operator=="*":
    print(f"{first} * {second}","=",first*second)
elif operator=="/":
    print(f"{first} / {second}","=",first/second)
elif operator=="%":
    print(f"{first} % {second}","=",first%second)
elif operator=="//":
    print(f"{first} // {second}","=",first//second)
else:
    # If the operator is not recognized, print an error message
    print("Please try again later")