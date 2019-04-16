#This is a conversation bot, if you ever feel lonely and there's no one else to talk to, then this bot has your back

#This imports the necessary libraries for the program to run
import sys
import time

#The code trying to find out the user's name
name = input("What's your name?")
print("Hello " + name)

time.sleep(1)

#Asks the user how they feel
feeling = (input("How are you feeling? "))

#How the program responds to the user
if feeling.lower() == "good":
 print("Well that's good!")
 time.sleep(5)

#if the user responds with bad
if feeling.lower() == "bad":
 feeling_bad = input("What's wrong? ")
 if feeling_bad.lower() == "my dog died":
   print("John Wick anyone?")
   time.sleep(5)

 if feeling_bad.lower() == "my parents died":
   print("I feel an origin story coming on")
   time.sleep(5)

 if feeling_bad.lower() == "I got friendzoned":
   print("You'll get out of it someday")
   time.sleep(5)

#user responds with ok
if feeling.lower() == "ok":
  print("Well that's ok")
  time.sleep(5)

#if the response isn't recognised/written in yet
else: 
 print("Sorry, I haven't been programmed to deal with that yet.")
 time.sleep(5)

time.sleep(1)

#This happens once the program has finished
print("It was great talking to you, have a good one and see you next time!")
time.sleep(10)
sys.exit