class Player:
    def __init__(self, name, n, matrix_values):
        self.name = name
        self.n = n
        self.matrix = [[matrix_values[i * n + j] for j in range(n)] for i in range(n)]
        self.payout = 0
    
    def play(self, row, col):
        self.payout += self.matrix[row][col]
    
    def resetPayout(self):
        self. payout = 0
        
    def __str__(self):
        return f"Player {self.name}: Payout {self.payout}"