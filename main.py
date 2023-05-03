import game1 as g1
import game2 as g2
import player as pa

if __name__ == "__main__":
    player1 = pa.Player("Alice", 2, [-1, -3, 0, -2])
    player2 = pa.Player("Bob", 2, [-1, 0, -3, -2])
    game1 = g1.PDG(2) 
    game1.play_game(player1, player2)
    
    mit = g2.College("MIT", 2, ["Alice", "Bob", "Charlie"])
    harvard = g2.College("Harvard", 2, ["Bob", "Alice", "Charlie"])
    stanford = g2.College("Stanford", 1, ["Bob", "Charlie", "Alice"])
    colleges = [mit, harvard, stanford]
    
    alice = g2.Student("Alice", ["MIT", "Harvard", "Stanford"])
    bob = g2.Student("Bob", ["MIT", "Harvard", "Stanford"])
    charlie = g2.Student("Charlie", ["MIT", "Harvard", "Stanford"])
    students = [alice, bob, charlie]
    game = g2.CollegeAdmissionsGame(colleges,students)
    game.run()

        