#start python with this parametres: c:\Python39\python c:\Python\Zed_A._Shaw\
#exercise13.py first 2nd 3rd
from sys import argv

script, user_name = argv
promt = "> "

print(f"Hello, {user_name}, I'm a script {script}.")
print("I want to ask you some questions")
print(f"Do you like me, {user_name}?")
likes = input(promt)

print(f"Where do you live, {user_name}?")
lives = input(promt)

print(f"""
Well, you answered {likes} to the question, if you like me.
You live in {lives}. I don't know where it is.
""")