from random import Random
print('Rock, Paper, Scissors')
Abbr = ['R', 'P', 'S']
Win = 0
Lose = 0
Tie = 0
while True:
    computer = Random().choice(Abbr)
    print(f'Win = {Win} Lose = {Lose} Tie = {Tie}')
    user = input('Select Rock(R), Paper(P), Scissors(S), Quit(Q):')
    if user == 'P':
        if computer == user:
            Tie = Tie + 1
            print('Computer choice = Paper')
            print('it\'s a Tie')
        elif computer == 'R':
            print('Computer choice = Rock')
            print('You Win Paper covers Rock')
            Win = Win + 1
        elif computer == 'S':
            print('Computer choice = Scissors')
            print('You Lose Scissors cuts Paper')
            Lose = Lose + 1

    elif user == 'R':
        if computer == user:
            Tie = Tie + 1
            print('Computer choice = Rock')
            print('it\'s a Tie')
        elif computer == 'P':
            print('Computer choice = Paper')
            print('You Lose Paper covers Rock')
            Lose = Lose + 1
        elif computer == 'S':
            print('Computer choice = Scissors')
            print('You Win Rock break scissors')
            Win = Win + 1

    elif user == 'S':
        if computer == user:
            Tie = Tie + 1
            print('Computer choice = Scissors')
            print('it\'s a Tie')
        elif computer == 'P':
            print('Computer choice = Paper')
            print('You Win scissors cuts paper')
            Win = Win + 1
        elif computer == 'R':
            print('Computer choice = Rock')
            print('You Lose Rock breaks scissors')
            Lose = Lose + 1

    elif user == 'Q':
        print('Restart Game')
        break

    else:
        print('Invalid input')
        continue




