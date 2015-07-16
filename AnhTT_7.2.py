import random


class Player:
    def __init__(self):
        self.score = 0

    def roll(self):
        turn_total = 0
        while True:
            turn = random.randint(1, 6)
            if turn != 1:
                turn_total += turn
                if self.score + turn_total >= 100:
                    self.score += turn_total
                    return self.score
                if hold(turn_total):
                    self.score += turn_total
                    break
            else:
                break


def hold(score):
    magic_number = 10
    return random.choice([True, False]) if score >= magic_number else False


def play_game(player1, player2, turn_of_player1=True):
    while player1.score < 100 and player2.score < 100:
        if turn_of_player1:
            player1.roll()
            turn_of_player1 = False
        else:
            player2.roll()
            turn_of_player1 = True
    return player1.score if player1.score >= 100 else player2.score


if __name__ == '__main__':
    total_win_p1 = 0
    for i in xrange(100):
        p1 = Player()
        p2 = Player()
        play_game(p1, p2)
        if p1.score >= 100:
            total_win_p1 += 1
            print 'Round {0}|\tP1: {1}\t|\tP2: {2}\t| P1 won!'.format(i+1,
                                                       p1.score,
                                                       p2.score)
        elif p2.score >= 100:
            print 'Round {0}|\tP1: {1}\t|\tP2: {2}\t| P2 won!'.format(i+1,
                                                       p1.score,
                                                       p2.score)
    print "P1's winning rate: {0}%".format(total_win_p1)
    print "P2's winning rate: {0}%".format(100-total_win_p1)

# output
#
# Round 1|	P1: 89	|	P2: 101	| P2 won!
# Round 2|	P1: 81	|	P2: 102	| P2 won!
# Round 3|	P1: 35	|	P2: 101	| P2 won!
# Round 4|	P1: 102	|	P2: 85	| P1 won!
# Round 5|	P1: 51	|	P2: 102	| P2 won!
# Round 6|	P1: 94	|	P2: 101	| P2 won!
# Round 7|	P1: 33	|	P2: 100	| P2 won!
# Round 8|	P1: 78	|	P2: 102	| P2 won!
# Round 9|	P1: 100	|	P2: 83	| P1 won!
# Round 10|	P1: 100	|	P2: 66	| P1 won!
# Round 11|	P1: 59	|	P2: 101	| P2 won!
# Round 12|	P1: 100	|	P2: 76	| P1 won!
# Round 13|	P1: 103	|	P2: 27	| P1 won!
# Round 14|	P1: 100	|	P2: 80	| P1 won!
# Round 15|	P1: 104	|	P2: 52	| P1 won!
# Round 16|	P1: 81	|	P2: 100	| P2 won!
# Round 17|	P1: 102	|	P2: 82	| P1 won!
# Round 18|	P1: 84	|	P2: 103	| P2 won!
# Round 19|	P1: 102	|	P2: 79	| P1 won!
# Round 20|	P1: 56	|	P2: 101	| P2 won!
# Round 21|	P1: 100	|	P2: 69	| P1 won!
# Round 22|	P1: 104	|	P2: 79	| P1 won!
# Round 23|	P1: 100	|	P2: 50	| P1 won!
# Round 24|	P1: 73	|	P2: 101	| P2 won!
# Round 25|	P1: 101	|	P2: 79	| P1 won!
# Round 26|	P1: 102	|	P2: 66	| P1 won!
# Round 27|	P1: 84	|	P2: 100	| P2 won!
# Round 28|	P1: 99	|	P2: 101	| P2 won!
# Round 29|	P1: 91	|	P2: 102	| P2 won!
# Round 30|	P1: 48	|	P2: 101	| P2 won!
# Round 31|	P1: 88	|	P2: 101	| P2 won!
# Round 32|	P1: 102	|	P2: 86	| P1 won!
# Round 33|	P1: 103	|	P2: 36	| P1 won!
# Round 34|	P1: 100	|	P2: 94	| P1 won!
# Round 35|	P1: 74	|	P2: 103	| P2 won!
# Round 36|	P1: 75	|	P2: 100	| P2 won!
# Round 37|	P1: 103	|	P2: 51	| P1 won!
# Round 38|	P1: 102	|	P2: 68	| P1 won!
# Round 39|	P1: 73	|	P2: 101	| P2 won!
# Round 40|	P1: 103	|	P2: 45	| P1 won!
# Round 41|	P1: 28	|	P2: 103	| P2 won!
# Round 42|	P1: 61	|	P2: 101	| P2 won!
# Round 43|	P1: 101	|	P2: 85	| P1 won!
# Round 44|	P1: 78	|	P2: 103	| P2 won!
# Round 45|	P1: 72	|	P2: 105	| P2 won!
# Round 46|	P1: 94	|	P2: 101	| P2 won!
# Round 47|	P1: 100	|	P2: 89	| P1 won!
# Round 48|	P1: 74	|	P2: 100	| P2 won!
# Round 49|	P1: 102	|	P2: 84	| P1 won!
# Round 50|	P1: 100	|	P2: 33	| P1 won!
# Round 51|	P1: 101	|	P2: 93	| P1 won!
# Round 52|	P1: 100	|	P2: 61	| P1 won!
# Round 53|	P1: 100	|	P2: 81	| P1 won!
# Round 54|	P1: 105	|	P2: 66	| P1 won!
# Round 55|	P1: 100	|	P2: 39	| P1 won!
# Round 56|	P1: 102	|	P2: 25	| P1 won!
# Round 57|	P1: 101	|	P2: 73	| P1 won!
# Round 58|	P1: 100	|	P2: 79	| P1 won!
# Round 59|	P1: 35	|	P2: 100	| P2 won!
# Round 60|	P1: 101	|	P2: 46	| P1 won!
# Round 61|	P1: 102	|	P2: 64	| P1 won!
# Round 62|	P1: 104	|	P2: 62	| P1 won!
# Round 63|	P1: 100	|	P2: 55	| P1 won!
# Round 64|	P1: 84	|	P2: 100	| P2 won!
# Round 65|	P1: 101	|	P2: 31	| P1 won!
# Round 66|	P1: 87	|	P2: 102	| P2 won!
# Round 67|	P1: 101	|	P2: 98	| P1 won!
# Round 68|	P1: 105	|	P2: 52	| P1 won!
# Round 69|	P1: 30	|	P2: 102	| P2 won!
# Round 70|	P1: 100	|	P2: 86	| P1 won!
# Round 71|	P1: 100	|	P2: 45	| P1 won!
# Round 72|	P1: 100	|	P2: 95	| P1 won!
# Round 73|	P1: 87	|	P2: 101	| P2 won!
# Round 74|	P1: 100	|	P2: 83	| P1 won!
# Round 75|	P1: 100	|	P2: 81	| P1 won!
# Round 76|	P1: 90	|	P2: 100	| P2 won!
# Round 77|	P1: 100	|	P2: 62	| P1 won!
# Round 78|	P1: 86	|	P2: 100	| P2 won!
# Round 79|	P1: 101	|	P2: 51	| P1 won!
# Round 80|	P1: 85	|	P2: 103	| P2 won!
# Round 81|	P1: 104	|	P2: 80	| P1 won!
# Round 82|	P1: 101	|	P2: 74	| P1 won!
# Round 83|	P1: 44	|	P2: 101	| P2 won!
# Round 84|	P1: 103	|	P2: 89	| P1 won!
# Round 85|	P1: 102	|	P2: 63	| P1 won!
# Round 86|	P1: 103	|	P2: 76	| P1 won!
# Round 87|	P1: 81	|	P2: 102	| P2 won!
# Round 88|	P1: 100	|	P2: 66	| P1 won!
# Round 89|	P1: 36	|	P2: 102	| P2 won!
# Round 90|	P1: 100	|	P2: 69	| P1 won!
# Round 91|	P1: 100	|	P2: 81	| P1 won!
# Round 92|	P1: 102	|	P2: 88	| P1 won!
# Round 93|	P1: 100	|	P2: 55	| P1 won!
# Round 94|	P1: 102	|	P2: 56	| P1 won!
# Round 95|	P1: 101	|	P2: 80	| P1 won!
# Round 96|	P1: 101	|	P2: 59	| P1 won!
# Round 97|	P1: 66	|	P2: 101	| P2 won!
# Round 98|	P1: 100	|	P2: 53	| P1 won!
# Round 99|	P1: 45	|	P2: 102	| P2 won!
# Round 100|	P1: 102	|	P2: 42	| P1 won!
# P1's winning rate: 61%
# P2's winning rate: 39%

