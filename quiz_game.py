print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Sorry, that is incorrect!")


answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Sorry, that is incorrect!")


answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Sorry, that is incorrect!")


answer = input("What does SSD stand for? ")

if answer.lower() == "solid state drive":
    print("Correct!")
    score+=1
else:
    print("Sorry, that is incorrect!")


print("You have finished the quiz. Your score is " + str(score) + "/4")

percentage = (score/4) * 100

print("You got " + str(percentage) + "% correct.")
if percentage == 100:
    print("Wow, a perfect score! Congratulations.")
