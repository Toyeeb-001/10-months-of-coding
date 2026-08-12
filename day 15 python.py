print("welcome to Olatoye Toyeeb game quiz")


playing = input("Do you want to play? (yes/No): ")
if playing.lower() == "yes":
    
    print("Okay! let's ride on")
    score = 0

    
    answer = input("What is the full meaning of ROM? ")
    if answer.lower() == "read only memory":
        print("correct!")
        score += 1
    else:
        print("incorrect!")
      
    
    answer = input(" what is the full meaning of GB and TB? ")
    if answer.lower() == "gigabyte and terabyte":
        print("Correct!")
        score += 1
    else:
        print("incorrect!")
      
    
    answer = input("what is the full meaning of OS and Mac OS? ")
    if answer.lower() == "operating system and macintosh operating system":
        print("correct!")
        score += 1
    else:
        print("incorrect!")
  
    
    raw_math = (score / 3) * 100
    clean_percentage = int(raw_math)

    print("you got " + str(score) + " questions correct!")
    print("you got " + str(clean_percentage) + "% correct!")

    
    if score == 3:
        print("Grade: A (distinction!)")
    elif score == 2:
        print("Grade: B (Excellent!)")
    elif score == 1:
        
        print("Grade: C (Credit!)")
    else:
        print("Grade: F (Better luck next time)")
else:
    print("Goodbye!")
#I am a beginner oo, please be nice

