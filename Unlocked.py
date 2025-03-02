                   #Sample code
#correct password
password="Ali"
your_input=input("Enter password : ")

while password != your_input:
    # Loop while the entered password is not correct
    your_input = input("Enter password : ")
else:
    print("Unlocked !")
    

                     #Advance pattern
password = "Ali"
max_attempts = 3    
attempts = 0

while attempts < max_attempts:
    your_input = input("Enter password: ")
    
    if your_input == password:
        print("Unlocked!")
        break
    else:
        # Increment the number of attempts made
        attempts += 1
        
        # Calculate the remaining number of attempts
        remaining_attempts = max_attempts - attempts
        
        # Provide feedback to the user
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Too many incorrect attempts. Access denied.")




