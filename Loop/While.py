import os
import time

attemps = 3
correct_password = "12345678"

while True:
    print(f"You have {attemps} times to enter your password.")
    password = input("Enter your password:")
    
    if password == correct_password:
        print("Welcome to your account.")
        break
    else:
        os.system("cls")
        attemps -= 1
    
    if attemps == 0:
        duration = 10
        while duration >= 0:
            os.system("cls")
            print(f"Wait for: {duration}s for the retry to access your account again.")
            duration -= 1
            time.sleep(1)
        attemps = 3