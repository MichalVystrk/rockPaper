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
    return render(request, 'rockPaperScissorsApp/home.html', {'userChoice': userChoice, 'computerChoice': computerChoice, 'result': result})

def determanWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return 'It\'s a tie!'
    if userChoice == 'rockPaperScissorsApp/images/gameSighns/Rock.png':
        if computerChoice == 'rockPaperScissorsApp/images/gameSighns/Scissors.png':
            return 'You win!'
        elif computerChoice == 'rockPaperScissorsApp/images/gameSighns/Paper.png':
            return 'You lose!'
    elif userChoice == 'rockPaperScissorsApp/images/gameSighns/Paper.png':
        if computerChoice == 'rockPaperScissorsApp/images/gameSighns/Rock.png':
            return 'You win!'
        elif computerChoice == 'rockPaperScissorsApp/images/gameSighns/Scissors.png':
            return 'You lose!'
    elif userChoice == 'rockPaperScissorsApp/images/gameSighns/Scissors.png':
        if computerChoice == 'rockPaperScissorsApp/images/gameSighns/Paper.png':
            return 'You win!'
        elif computerChoice == 'rockPaperScissorsApp/images/gameSighns/Rock.png':
            return 'You lose!'
    return 'Invalid choice!'