# Import the modules
import sys
import random

again = "y"

while again == "y":
    question = raw_input("Ask Re-choose a question")
    
    answers = random.randint(1,12)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "For sure"
    
    elif answers == 2:
        print "Exactly"
    
    elif answers == 3:
        print "You may rely on it"
    
    elif answers == 4:
        print "Possibly"
    
    elif answers == 5:
        print "Concentrate and ask again"
    
    elif answers == 6:
        print "Probably Not"
    
    elif answers == 7:
        print "My reply is no"
    
    elif answers == 8:
        print "My sources say no"
        
    elif answers == 9:
        print "My sources say yes"
        
    elif answers == 10:
        print "You probably will"
        
    elif answers == 11:
        print "My sources say it will"
        
    elif answers == 12:
        print "My sources say they could"
        
    again = ""
    while(again == ""):
        ans = raw_input("Ask another question? (y/n):")
        if ans == "y" || ans == "Y":
            again = "y"
        else if ans == "n" || ans == "N":
            again = "n"
        else:
            again = ""
