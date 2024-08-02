print("Welcome to my Computer Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Let's Play!")
score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct out of 4")
print("You got " + str((score/4)*100) + "%.")
