print("Wellcome to my computer quiz!")

playing = input("Do you want to play?")

if playing !="yes":
    quit()

print("Okay! let's play") 
score = 0
answer = input("What does cpu stands for?")
if answer == "Central processing unit":
    print("Your are correct!")
    score += 1
    
else:
    print("Incorrect, either answer is wrong or punctuation wrong")
    print("answer is Central processing unit")


answer = input("What is the scientific name for a giraffe?")
if answer == "Giraffa camelopardalis":
    print("Your are correct!")
    score += 1
    
else:
    print("Incorrect, either answer is wrong or punctuation wrong") 
    print("answer is Giraffa camelopardalis ")

answer = input(" What is the chemical symbol for iron?")
if answer == "Fe":
    print("Your are correct!")
    score += 1
    
else:
    print("Incorrect, either answer is wrong or punctuation wrong")
    print("answer is Fe")  


answer = input(" What is the chemical symbol for gold?")
if answer == "Au":
    print("Your are correct!")
    score += 1
    
else:
    print("Incorrect, either answer is wrong or punctuation wrong")
    print("answer is Au")  

answer = input("What is the process by which plants convert sunlight into energy?")
if answer == "Photosynthesis":
    print("Your are correct!")
    score += 1
    print("You got " + str(score) + " questions correct!")
    print(" yaaah hooo! Congratulations !You won the game." )
    
else:
    print("Incorrect, either answer is wrong or punctuation wrongAu")
    print("answer is Photosynthesis")  
    print("You got " + str(score) + " questions correct!")
    print("You lose the game.Better luck in next time!" )

    



   
       



    