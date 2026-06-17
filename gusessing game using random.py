import random
no=random.randint(1,100)
guess=int(input("Enter a number between 1 and 100:"))
attempts=0
def rytguess(g):
    if(no==g):
        print("Epdi macha you got it ryt da")
        print("NO of attempts:",attempts)
while(guess!=no):
    if(guess<no):
        print("Try greater buddy")
        attempts+=1
    elif(guess>no):
        print("Try something small da")
        attempts+=1
    guess=int(input("enter again lets see:"))
attempts+=1 #here see whats happening in attempts ryt case we have to increment still where we took a chance to find it ryt??        
rytguess(guess)