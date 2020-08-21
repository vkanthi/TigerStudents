from os import system
from sys import argv


# script,first_name, last_name, msg = argv
# print("My script name is", script)
# print("My first name is", first_name)
# print("My last name is", last_name)
# print("My message is", msg)

def clear():
    system('cls')


script , prompt_name , your_name = argv
prompt = f'{prompt_name}> '
print(f"Hell {your_name}, I am Mala running the script {script}")
print("I would like to ask you few questions")
print(f"Do you like me {your_name}?")
likes = input(prompt)

print("Where do you live?")
live = input(prompt)

print("What is your passion?")
passion = input(prompt)

clear()
print ('*' * 100)
print(f""" Awesome! {your_name}. I am really happy that you said {likes} 
when i asked you whether you liked me.I know lot of people in my college 
likes me but your like is something special to me. I didn't know you live in {live}.
That is really a nice place right? I want to live there too. I am really
glad that you like to {passion}""")
print ('*' * 100)
