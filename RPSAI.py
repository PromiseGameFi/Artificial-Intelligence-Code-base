import random

class RPSAI:
    def __init__(self):
        self.strategy = None
        self.last_move = None
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.history = []

    def play(self, opponent_last_move):
        # update history
        self.history.append(opponent_last_move)

        # determine opponent's most common move
        opp_move_count = [self.history.count('R'), self.history.count('P'), self.history.count('S')]
        opp_most_common_move = ['R', 'P', 'S'][opp_move_count.index(max(opp_move_count))]

        # choose strategy based on opponent's most common move
        if opp_most_common_move == 'R':
            self.strategy = 'P'
        elif opp_most_common_move == 'P':
            self.strategy = 'S'
        else:
            self.strategy = 'R'

        # play the move based on the chosen strategy
        if self.strategy == 'R':
            self.last_move = 'P'
        elif self.strategy == 'P':
            self.last_move = 'S'
        else:
            self.last_move = 'R'

        return self.last_move

    def update_score(self, result):
        if result == 'win':
            self.wins += 1
        elif result == 'loss':
            self.losses += 1
        else:
            self.ties += 1

    def reset(self):
        self.strategy = None
        self.last_move = None
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.history = []

# create the four bots to play against
random_bot = lambda x: random.choice(['R', 'P', 'S'])
cycle_bot = lambda x: ['R', 'P', 'S'][x % 3]
mirror_bot = lambda x: x[-1] if x else random.choice(['R', 'P', 'S'])
smart_bot = RPSAI()

# play 1000 games against each bot
for i, bot in enumerate([random_bot, cycle_bot, mirror_bot, smart_bot.play]):
    player1 = RPSAI()
    player2 = bot
    wins = 0
    for j in range(1000):
        p1_move = player1.play(player2.last_move if callable(player2) else player2)
        p2_move = player2(p1_move)
        if p1_move == p2_move:
            player1.update_score('tie')
            if not callable(player2):
                player2.update_score('tie')
        elif (p1_move, p2_move) in [('R', 'S'), ('S', 'P'), ('P', 'R')]:
            player1.update_score('win')
            if not callable(player2):
                player2.update_score('loss')
                wins += 1
        else:
            player1.update_score('loss')
            if not callable(player2):
                player2.update_score('win')
    win_rate = wins / 1000.0
    print(f'Bot {i+1} win rate: {win_rate*100:.2f}%')
    assert win_rate >= 0.6
