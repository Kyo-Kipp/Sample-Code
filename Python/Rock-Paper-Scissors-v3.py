#Author: Kyo Kipp
#This program simulates multiple games of Rock, Paper, Scissors
#and keeps a running score of the wins, losses and ties.


import random  

def main():

    input('Welcome!\nI challenge you to a game of rock, paper, scissors.'\
          ' Best of 7!\nPress Enter to begin.')

    #Initialize a variable for playing again
    again = 'yes'

    #This will loop as long as the user wants to play again
    while again == 'yes':

        print('--------------------------------------------------------------')
        #Initialize accumulator variables for keeping score
        wins = 0
        losses = 0
        ties = 0
        
        #This will loop 7 times
        for count in range(1,8):

            #Display the round number
            print('\nRound #',count,sep='')

            #Generate the comuter's choice.
            comp_choice = get_comp_choice()

            #Get the user's choice
            user_choice = get_user_choice()

            #Figure out who won
            winner = find_winner(user_choice,comp_choice)

            #Display the choices
            print('\nYou chose ',user_choice,', and I chose ',comp_choice,'.',sep='')

            #Display what happens
            display_message(user_choice,comp_choice)

            #Display who won
            display_winner(winner)

            #Update the score
            if winner == 'win':
                wins += 1
            elif winner == 'loss':
                losses += 1
            else:
                ties += 1

        #Display the score
        print('------------------------------------------')
        print('\nHeres the score:\nWins:', \
               wins,'Losses:',losses,'Ties:',ties,'\n')
     
        #Display who won the whole round
        display_overall_winner(wins,losses)

        #Ask if the user wants to play again
        again = play_again()

        #If the user is done, say goodbye
        if again == 'no':
            print('\nThank you for playing! Goodbye!')

        
            

#This function randomly generates rock, paper or scissors.
def get_comp_choice():

    #Generate a random number from 1 to 3
    random_number = random.randint(1,3)

    #Choose a weapon based on the number and return it's name
    if random_number == 1:
        return 'rock'
    elif random_number == 2:
        return 'paper'
    else:
        return 'scissors'


#This function gathers the user's choice and validates the input.
def get_user_choice():

    #Input the user's choice
    choice = input('Please enter rock, paper, or scissors:')

    #If the input isn't rock, paper, or scissors, ask for the input again.
    options = ['rock','paper','scissors']
    while choice.lower() not in options:
        choice = input("I'm sorry, I didn't understand that."\
                       '\nPlease enter rock, paper, or scissors:')

    return choice.lower()
    
#This function will display what happens, there are only 3 possibilities.
def display_message(weapon1,weapon2):

    #Put the weapon choices into a list
    weapons = [weapon1,weapon2]

    #Find out what is in the list, disregarding order and display the result.
    if 'rock' in weapons and 'paper' in weapons:
        print('Paper covers rock.')
    elif 'paper' in weapons and 'scissors' in weapons:
        print('Scissors cuts paper.')
    elif 'scissors' in weapons and 'rock' in weapons:
        print('Rock breaks scissors.')
    #Display nothing if it's a tie.
    else:
        print(end='')


#This function will look at the choices and decide who won.
def find_winner(user_choice,comp_choice):

    #If the user choce rock, there are three possibilities
    if user_choice == 'rock':
        if comp_choice == 'paper':
            return 'loss'
        elif comp_choice == 'scissors':
            return 'win'
        else:
            return 'tie'

    #If the user chose paper, there are 3 possibilities
    elif user_choice == 'paper':
        if comp_choice == 'scissors':
            return 'loss'
        elif comp_choice == 'rock':
            return 'win'
        else:
            return 'tie'

    #If the user chose paper, there are three possibilities
    else:
        if comp_choice == 'rock':
            return 'loss'
        elif comp_choice == 'paper':
            return 'win'
        else:
            return 'tie'
        

#This funnction will display a message that says who won.
def display_winner(winner):
    if winner == 'win':
        print('You win!')
    elif winner == 'loss':
        print('You lose!')
    else:
        print("It's a tie!")


#This function figures out who won more games and displays the result
def display_overall_winner(wins,losses):

    if wins > losses:
        print('Looks like you won more than I did.'\
              ' Congratulations, you got lucky this time.')
    if wins < losses:
        print('Looks like I won more than you did.'\
              ' Better luck next time.')
    if wins == losses:
        print("Zonks! It seems we tied. You will play again, won't you?")
    

#This function asks the user if they want to play again and validates the input.
def play_again():
    
    #This is a list of several different ways the user can say yes
    yes_options = ['y','yes','yup','ya','sure','ok','okay','alright','fine','of course']
               
    #This is a list of several different ways the user can say no
    no_options = ['n','no','nope','no way','no thanks','never','negative','nein']

    #Get the input
    choice = input('Would you like to play again?')

    #If the choice is not one of the options in the lists, the input again.
    while choice.lower() not in yes_options and choice.lower() not in no_options:
        choice = input("I'm sorry, I didn't understand that.\n"\
                       'Would you like to play again?')

    #Return the user's chocie
    if choice.lower() in yes_options:
        return 'yes'
    if choice.lower() in no_options:
        return 'no'
    
   
main()
