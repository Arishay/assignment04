import random

def play():
    user = input('What\'s your choice ? \nr for Rock, p for Paper, s for Scissor : \n')
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a Tie.'
    

    #r>s p>r s>p

    if is_win(user, computer):
        return 'You Won'
    
    return 'You lose'

def is_win(player, opponent):
        if(player == 'r' and opponent == 's') or ( player == 's' and opponent == 'p' ) \
            or (player == 's' and opponent == 'p'):
           return True
        
print(play())        

