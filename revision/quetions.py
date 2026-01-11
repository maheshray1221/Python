from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText

import pyttsx3


# print("twinkle twinkle Poem")
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.''')


# # table of 5 using repl
# print(5*1)
# print(5*2)
# print(5*3)
# print(5*4)
# print(5*5)
# print(5*6)
# print(5*7)
# print(5*8)
# print(5*9)
# print(5*10)




# def demo(screen):
#     effects = [
#         Cycle(
#             screen,
#             FigletText("Mahesh Ray", font='big'),
#             screen.height // 2 - 8),
#         Cycle(
#             screen,
#             FigletText("ROCKS!", font='big'),
#             screen.height // 2 + 3),
#         Stars(screen, (screen.width + screen.height) // 2)
#     ]
#     screen.play([Scene(effects, 500)])

# Screen.wrapper(demo)

#using pyttsx3

# engine = pyttsx3.init()
# engine.say('chal re noooooooooooob')
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# import os

# Change this to the directory you want to list,
# or leave it as '.' for the current directory
# directory_path = "/Autodesk"

# try:
#     # Get list of files and directories
#     contents = os.listdir(directory_path)

#     print(f"Contents of directory '{directory_path}':")
#     for name in contents:
#         print(name)

# except FileNotFoundError:
#     print(f"Error: The path '{directory_path}' was not found.")
# except NotADirectoryError:
#     print(f"Error: The path '{directory_path}' is not a directory.")
# except PermissionError:
#     print(f"Error: Permission denied to access '{directory_path}'.")

#  -------->>  chepter 2 <<-----------------

#  add two numbers

# a = 5
# b = 8
# print(a+b)


#  find remainder when devied by z

# z = int(input("give me interger value"))

# print(20%z)

# print(type(z))

# check a is greater or not

# a = 34 
# b = 80

# print(a>b)


#  average of two numbers

# a = int(input("give me interger value"))
# b = int(input("give me interger value"))

# print ((a+b)/2)

# squar of n
# n = int(input("give me interger value"))

# print(n*n)


# Sting function

#1.
# name = input("enter name")
# print(name.title())

#2.assign name and date in paragraph
# name = "Mahesh Ray"

# date = "24 jan"

# letter = f'''
# Dear {name},
# you are selected!
# {date}'''

# print(letter)

#3. check double space in string

# name1 = "mahesh  "

# ans =  "  "  in name1
# print(ans)


#4. replace duble space in name to convert single space 
# name1 = "mahesh  ray"
# ans = name1.replace("mahesh  ray","mahesh ray") 

# print(ans)

#5. formate the following things

# thought = " hey mahesh \n, You are assowm ,\n thank you!"

# print(thought)


# ------------>>  Tuple and list  <<------------

#1. store seven fruits nane by user in list

# fruits = []

# fruits.append(input("give 1st fruit name"))
# fruits.append(input("give 2nd fruit name"))
# fruits.append(input("give 3rd fruit name"))
# fruits.append(input("give 4th fruit name"))
# fruits.append(input("give 5th fruit name"))
# fruits.append(input("give 6th fruit name"))
# fruits.append(input("give 7th fruit name"))
# print(fruits)


#2. disply 6 student marks in a sorted order

marks = []

marks.append(int(input("give 1st student marks")))
marks.append(int(input("give 2nd student marks")))
marks.append(int(input("give 3rd student marks")))
marks.append(int(input("give 4th student marks")))
marks.append(int(input("give 5th student marks")))
marks.append(int(input("give 6th student marks")))
marks.append(int(input("give 7th student marks")))

print(marks)
print("sorted order")
marks.sort()
print(marks)
#3.
#4.
#5.