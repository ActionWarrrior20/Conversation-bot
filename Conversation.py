#This is a conversation bot, if you ever feel lonely and there's no one else to talk to, then this bot has your back

#This imports the necessary libraries for the program to run
import sys
import time

#The code trying to find out the user's name
n = input("What's your name?")
print("Hello " + n)

time.sleep(1)

#Asks the user how they feel
f = (input("How are you feeling? "))

#How the program responds to the user
if f.lower() == "good":
 print("Well that's good!")
 time.sleep(5)

#if the user responds with bad
if f.lower() == "bad":
 fA = input("What's wrong? ")
 if fA.lower() == "my dog died":
   print("John Wick anyone?")
   time.sleep(5)

 if fA.lower() == "my parents died":
   print("I feel an origin story coming on")
   time.sleep(5)

 if fA.lower() == "I got friendzoned":
   print("You'll get out of it someday")
   time.sleep(5)

#user responds with ok
if f.lower() == "ok":
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