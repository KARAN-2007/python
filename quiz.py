print('Welcome to G.K. quiz')

playing=input("Do you want to play? ")

if playing.lower() != "yes":
    quit() 

print("Okay! let's play:)")
score=0
#print("Note:Write every answer in small letters!")

a1=input("1.) What is the full form of CPU? ")
if a1.lower() == "central processing unit"   :
    score+=1
    print("Correct!") 
else: print("Wrong answer:(")

a2=input("2.) Who is the Prime Minister of India? ")
if a2.lower() == "narendra modi"  :
    score+=1
    print("Correct!") 
else: print("Wrong answer:(")

a3=input("3.) Who is the president of U.S.A.? ")
if a3.lower() == "joe biden"  :
    score+=1
    print("Correct!") 
else: print("Wrong answer:(")

a4=input("4.) Full form of U.N.A. ")
if a4.lower() == "united nations association"  :
    score+=1
    print("Correct!") 
else: print("Wrong answer:(")

print("You got:"+ str(score)+ " question(s) correct")
print("You got:"+ str(score/4*100)+ " %")
