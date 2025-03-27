from django.shortcuts import render
import random

def home(request):
    result = None
    if request.method == 'POST':
        user_choice = request.POST['weapon']
        computer_choice = random.choice(['rockPaperScissorsApp/images/gameSighns/Rock.png', 'rockPaperScissorsApp/images/gameSighns/Paper.png', 'rockPaperScissorsApp/images/gameSighns/Scissors.png'])
    return render(request, 'rockPaperScissorsApp/home.html', {'userChoice': user_choice, 'computerChoice': computer_choice})
    