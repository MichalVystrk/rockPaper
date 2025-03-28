from django.shortcuts import render
import random

def home(request):
    result = None
    userChoice = None
    computerChoice = None
    if request.method == 'POST':
        userChoice = request.POST['weapon']
        computerChoice = random.choice(['rockPaperScissorsApp/images/gameSighns/Rock.png', 'rockPaperScissorsApp/images/gameSighns/Paper.png', 'rockPaperScissorsApp/images/gameSighns/Scissors.png'])
    result = determanWinner(userChoice, computerChoice)
    return render(request, 'rockPaperScissorsApp/home.html', {'userChoice': userChoice, 'computerChoice': computerChoice})

def determanWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return 'It\'s a tie!'
    if userChoice == 'rock' and computerChoice == 'scissors':
        return 'You win!'
    if userChoice == 'paper' and computerChoice == 'rock':
        return 'You win!'
    if userChoice == 'scissors' and computerChoice == 'paper':
        return 'You win!'
    return 'You lose!'