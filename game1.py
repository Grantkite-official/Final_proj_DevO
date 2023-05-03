class PDG: #prisoner's dilemma game
    def __init__(self, playernum):
        self.pn = playernum
        
    def play_game(self, player1, player2):
        print("Playing game 1: Prisoner's Dilemma\n")
        for i in range(player1.n):
            for j in range(player1.n):
                p1_choice = input(f"{player1.name}, choose (C)ooperate or (D)efect for cell ({i},{j}): ")
                p2_choice = input(f"{player2.name}, choose (C)ooperate or (D)efect for cell ({i},{j}): ")
                
                if p1_choice.lower() == "c" and p2_choice.lower() == "c":
                    player1.play(i, j)
                    player2.play(i, j)
                elif p1_choice.lower() == "c" and p2_choice.lower() == "d":
                    player2.play(i, j)
                elif p1_choice.lower() == "d" and p2_choice.lower() == "c":
                    player1.play(i, j)
                elif p1_choice.lower() == "d" and p2_choice.lower() == "d":
                    player1.play(i, j)
                    player2.play(i, j)
        print(player1)
        print(player2)
        player1.resetPayout()
        player2.resetPayout()