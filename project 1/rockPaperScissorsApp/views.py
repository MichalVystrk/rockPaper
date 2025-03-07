from django.shortcuts import render
import random

def home(request):
    result = None
    if 'weapon' in request.GET:
        user_choice = request.GET['weapon']
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = determine_winner(user_choice, computer_choice)
    return render(request, 'rockPaperScissorsApp/home.html', {'result': result})

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"Both chose {user_choice}. It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return f"You chose {user_choice} and the computer chose {computer_choice}. You win!"
    else:
        return f"You chose {user_choice} and the computer chose {computer_choice}. You lose!"