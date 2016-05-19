import sys
import random

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def make_drink(drink_choices):
    drink = ["strong", "salty", "bitter", "sweet", "fruity"]
    selections = set(drink_choices).intersection(drink)
    return selections

def qutting_time():
    print "Would ye like to exit the Pirate Bar me hearty! Type 6!"
    choice = raw_input("Enter your choice [1-6]: ")
    if choice == 6:
        loop = False
    else:
        enter_bar()
    print 67 * "-"
    return loop
    
def ingredient_type():
    ingredient_type = []
    

## Your menu design here
def enter_bar():
    
    print("RRRRRR, what kind of drink would ye be havin?")
    
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. strong"
    print "2. salty"
    print "3. bitter"
    print "4. sweet"
    print "5. fruity"
    print "6. exit"
    print 67 * "-"
    
    drink_choices = []
    print 30 * "-" , "MENU" , 30 * "-"
    choice_text = "Enter your choice: "
    
    print "Do ye like yer drinks strong? Type 1!"
    choice1 = raw_input(choice_text)
    if choice1 == "1":
        drink_choices.append("strong")
    
    print "Do ye like it with a salty tang? Type 2!"
    choice2 = raw_input(choice_text)
    if choice2 == "2":
        drink_choices.append("salty")
    
    print "Are ye a lubber who likes it bitter? Type 3!"
    choice3 = raw_input(choice_text)
    if choice3 == "3":
        drink_choices.append("bitter")
    
    print "Would ye like a bit of sweetness with yer poison? Type 4!"
    choice4 = raw_input(choice_text)
    if choice4 == "4":
        drink_choices.append("sweet")
    
    print "Are ye one for a fruity finish? Type 5!"
    choice5 = raw_input(choice_text)
    if choice5 == "5":
        drink_choices.append("fruity")
        
    return drink_choices
   
    ## While loop which will keep going until loop = False
    
def main():
    while True:
        drink_choices = enter_bar()
        selections = make_drink(drink_choices)
        for item in selections:
            print item
        
        qutting_time()

if __name__ == '__main__':
    main()