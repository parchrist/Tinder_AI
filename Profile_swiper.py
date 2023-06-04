import requests
import json
import time 
import random


# warning messages
warning_messages = [
    'BEFORE YOU START THE PROGRAM, PLEASE READ THE FOLLOWING WARNING MESSAGES:',
    'DO NOT LOG INTO TINDER ON YOU MOBILE DEVICE OR ANY KIND OF DEVICE.',
    'SET YOUR LOCATION TO THE CITY YOU WANT TO SWIPE IN AND DO NOT CHANGE IT ON ANY OTHER DEVICE',
    'WE ARE NOT RESPONSIBLE FOR ANY OF YOUR ACTIONS YOU TAKE WHILE USING THIS PROGRAM',
    'WE ARE NOT RESPONSIBLE FOR ANY ACTIONS TINDER TAKES AGAINST YOU WHILE USING THIS PROGRAM',
    'WE ARE NOT RESPONSIBLE FOR ANY ACTIONS OTHER USERS TAKE AGAINST YOU WHILE USING THIS PROGRAM',
    'WE STRONGLY ADVISE YOU TO USE THIS PROGRAM IN A SAFE AND RESPONSIBLE MANNER',
    'WE ALSO STRONGLY ADVISE YOU THAT YOU OPTIMIZE YOUR PROFILE TO GET THE BEST RESULTS'
]
print(warning_messages[])


# Accepting the warning messages

accept = input("DO YOU ACCEPT? (Y/N): ")
    if accept == "Y":
        print("Starting the program...")
    else: 
        print("The program has been terminated... goodbye")
        exit()
        
# Two Step Authentication protocol

phone_number = input("PLEASE ENTER YOUR PHONE NUMBER: ")

## Need to make a function that put the phone number into the TINDER login page 




Two_step = input("THE CODE HAS BEEN SENT TO YOUR PHONE NUMBER. PLEASE ENTER THE CODE: ")

## Need to make a function that puts the code into the TINDER login page




#Two Step Authentication protocol 

if Two_step == "200":
    print("You have successfully logged in! ")
    print("We are now booting up the AI bot. Please wait, this should only take a few seconds...")
    time.sleep(15)
    print("We are loading the surroding users in your area...")
    time.sleep(5)


# Starting the Script input y/n on the keyboard in terminal
Start_program = input("WOULD YOU LIKE TO START THE PROGRAM? (Y/N): ")
if Start_program == "Y":
    print("THE PROGRAM HAS STARTED... DON'T CLOSE THIS WINDOW OR ELSE YOU WONT GET ANY MATCHES...")
else: 
    print("THE PROGRAM HAS BEEN HAS ENDED...")
    exit()

# X-Auth-Token retrerival 

response.status_code ==200: 
    auth_token = response.headers['X-Auth-Token']
    

    
# Setting up the URL link and the response headers from the Tinder API

tinder_headers = {
 
}




# List of the pickup lines

list_of_pick_up lines = [   ### PUT YOUR OWN PICKUP LINES HERE ###
                         
                         ]



# SWIPE RIGHT FUNCTION 

def swipe_right(): 
    r = requests.get(url + '/like/' + _user['_id'], headers=headers)
    print("THE AI You has swiped right on " + _user['name'] + "!")
    print(r.status_code)
    return r.status_code
    
# SWIPE LEFT FUNCTION 

def swipe_left(): 
    r = requests.get(url + '/pass/' + _user['_id'], headers=headers)
    print("THE AI You has swiped  left on " + _user['name'] + "!")
    print(r.status_code)
    return r.status_code


# MATCH MADE FUNCTION
    if match = 1 
    print("THE AI You have matched with " + _user['name'] + "!")
    print()

        
# GET USER LIST OF USER FUNCTIONS 
list_of_users = []
user_photos= [] 
    for user in list of users: 
        user_photos.append(user['photos'])
        print("LIST OF USERS HAVE BEEN LOADED...")

        

# FROM LIST OF PHOTOS, MAKE AI PREDICTION FUNCTION
def ai_prediction():
    from ai import prediction 
    with user_photos as f:
        prediction = predict(f)
        return prediction
    if prediction == 1: 
        print("AI said " + prediction + " on " + _user['name'] + "resulting in a" "swipe right")
    if prediction == 0: 
        print("AI said " + prediction + " on " + _user['name'] + "resulting in a" "swipe left")


# Loop to load make and do the action of swiping right or left on the user and REPEAT
for user in list_of_users:
    make_ai_prediction()
    if prediction == 1:
        swipe_right()
    else:
        swipe_left()
        
    
