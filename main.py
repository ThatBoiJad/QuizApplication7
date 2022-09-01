import random

Red = "\033[0;31m"
Green = "\033[0;32m"
Blue = "\033[0;34m"

loop = True  

score = 0

play = input (Red + "Hi would you like to the start the quiz?: " + Blue)
if play == 'Yes' or play == 'yes':
  print("Ok starting the quiz!")

question1 = input (Red + "what is the most popular coding language?: " + Blue)
if question1 == 'javascript' or question1 == 'Javascript':
  score += 1

question2 = input (Red + "what code was used to make this quiz?: " + Blue)
if question2 == 'Python' or question2 == 'python':
  score += 1

question3 = input (Red + "who invented coding: " + Blue)
if question3 == 'ada lovelace' or question3 == 'Ada Lovelace':
  score += 1

question4 = input (Red + "where is the eiffel tower: " + Blue)
if question4 == 'paris' or question4 == 'Paris':
  score += 1

question5 = input (Red + "who is the president of maldives: " + Blue)
if question5 == 'Ibrahim Mohamed Solih' or question5 == 'ibrahim mohamed solih':
  score += 1

question6 = input (Red + "when did france attack england: " + Blue)
if question6 == 'april 30 1230' or question6 == 'April 30 1230':
  score += 1

question7 = input (Red + "what is the number 1 most sold game: " + Blue)
if question7 == 'Minecraft' or question7 == 'Minecraft':
  score += 1

question8 = input (Red + "what anime has sold the most manga: " + Blue)
if question8 == 'One Piece' or question8 == 'one piece':
  score += 1

question9 = input (Red + "what is the most popular subject in school: " + Blue)
if question9 == 'Maths' or question9 == 'maths':
  score += 1

question10 = input (Red + "How many questions are in this quiz?: " + Blue)
if question10 == '10' or question10 == '10':
  score += 1 

if score <= 5:
  print("Better luck next time, your score is " + str(score) + "/10")

else:
  print("CONGRATULATIONS!, you got " + str(score) + "/10")