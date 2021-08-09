import json
 
username = input("What is your name:")
filename = 'username.json'
with open(filename, 'w+') as f:
        json.dump(username, f)
        useraddress = input("What is your address:")
        user_phone = input("What is your phone number:")
        print(f" Data saved to the file.")
