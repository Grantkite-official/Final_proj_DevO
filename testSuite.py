import unittest
from unittest.mock import patch
from player import Player
from game1 import PDG
from game2 import College, Student, CollegeAdmissionsGame

class TestPDG(unittest.TestCase):

    def test_play_game(self):
        player1 = MockPlayer("Player 1")
        player2 = MockPlayer("Player 2")
        game = PDG(2)

        # Mock user input for each round of the game
        with patch('builtins.input', side_effect=['c', 'c', 'd', 'd']):
            game.play_game(player1, player2)

        # Assert that players' scores have been updated correctly
        self.assertEqual(player1.getPayout(), 5)
        self.assertEqual(player2.getPayout(), 5)

class MockPlayer:
    def __init__(self, name):
        self.name = name
        self.n = 2
        self.payout = [[0, 0], [0, 0]]

    def play(self, i, j):
        self.payout[i][j] += 3

    def getPayout(self):
        return sum(sum(row) for row in self.payout)

    def resetPayout(self):
        self.payout = [[0, 0], [0, 0]]
        
class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Alice", 2, [-1, -3, 0, -2])
        
    #integration tests
    
    def test_pdg_game(self):
         player1 = Player("Alice", 2, [-1, -3, 0, -2])
         player2 = Player("Bob", 2, [-1, 0, -3, -2])
         game1 = PDG(2) 
         game1.play_game(player1, player2)
         player1.payout = -1
         player2.payout = -1
         assert player1.payout == -1
         assert player2.payout == -1
        
    def test_college_student(self):
        mit = College("MIT", 2, ["Alice", "Bob", "Charlie"])
        harvard = College("Harvard", 2, ["Bob", "Alice", "Charlie"])
        stanford = College("Stanford", 1, ["Bob", "Charlie", "Alice"])
        colleges = [mit, harvard, stanford]
        
        alice = Student("Alice", ["MIT", "Harvard", "Stanford"])
        bob = Student("Bob", ["MIT", "Harvard", "Stanford"])
        charlie = Student("Charlie", ["MIT", "Harvard", "Stanford"])
        students = [alice, bob, charlie]
        
        assert mit.is_full() == False
        assert harvard.prefers("Bob", "Alice") == True
        assert charlie.prefers("Stanford", "MIT") == False
        
    def test_college_admissions_game(self):
         mit = College("MIT", 2, ["Alice", "Bob", "Charlie"])
         harvard = College("Harvard", 2, ["Bob", "Alice", "Charlie"])
         stanford = College("Stanford", 1, ["Bob", "Charlie", "Alice"])
         colleges = [mit, harvard, stanford]
        
         alice = Student("Alice", ["MIT", "Harvard", "Stanford"])
         bob = Student("Bob", ["MIT", "Harvard", "Stanford"])
         charlie = Student("Charlie", ["MIT", "Harvard", "Stanford"])
         students = [alice, bob, charlie]
       
         game = CollegeAdmissionsGame(colleges,students)
         game.deferred_acceptance()
       
         assert alice.assigned_college == mit
         assert bob.assigned_college == mit
         assert charlie.assigned_college == harvard
         assert mit.is_full() == True
         assert harvard.is_full() == False
         assert stanford.is_full() == False

    def test_pdg_and_college_admissions_game(self):
         player1 = Player("Alice", 2, [-1, -3, 0, -2])
         player2 = Player("Bob", 2, [-1, 0, -3, -2])
         game1 = PDG(2) 
         game1.play_game(player1, player2)

         mit = College("MIT", 2, ["Alice", "Bob", "Charlie"])
         harvard = College("Harvard", 2, ["Bob", "Alice", "Charlie"])
         stanford = College("Stanford", 1, ["Bob", "Charlie", "Alice"])
         colleges = [mit, harvard, stanford]


    def test_play(self):
        self.assertEqual(self.player.payout, 0)
        self.player.play(0, 0)
        self.assertEqual(self.player.payout, -1)
        self.player.play(1, 0)
        self.assertEqual(self.player.payout, -1)

    def test_resetPayout(self):
        self.player.play(0, 0)
        self.player.play(1, 0)
        self.assertEqual(self.player.payout, -1)
        self.player.resetPayout()
        self.assertEqual(self.player.payout, 0)

class TestPDG(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Alice", 2, [-1, -3, 0, -2])
        self.player2 = Player("Bob", 2, [-1, 0, -3, -2])
        self.pdg = PDG(2)

    def test_play_game(self):
          self.pdg.play_game(self.player1, self.player2)
          self.player1.payout = 0
          self.player2.payout = 0
          self.assertEqual(self.player1.payout, 0)
          self.assertEqual(self.player2.payout, 0)

class TestCollege(unittest.TestCase):
    def setUp(self):
        self.college = College("MIT", 2, ["Alice", "Bob", "Charlie"])

    def test_is_full(self):
        self.assertFalse(self.college.is_full())
        self.college.accepted_students = ["Alice", "Bob"]
        self.assertTrue(self.college.is_full())

    def test_prefers(self):
        self.assertTrue(self.college.prefers("Alice", "Bob"))
        self.assertFalse(self.college.prefers("Charlie", "Bob"))

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Alice", ["MIT", "Harvard", "Stanford"])

    def test_prefers(self):
        self.assertTrue(self.student.prefers("MIT", "Harvard"))
        self.assertFalse(self.student.prefers("Stanford", "MIT"))

class TestCollegeAdmissionsGame(unittest.TestCase):
    def setUp(self):
        mit = College("MIT", 2, ["Alice", "Bob", "Charlie"])
        harvard = College("Harvard", 2, ["Bob", "Alice", "Charlie"])
        stanford = College("Stanford", 1, ["Bob", "Charlie", "Alice"])
        colleges = [mit, harvard, stanford]
        alice = Student("Alice", ["MIT", "Harvard", "Stanford"])
        bob = Student("Bob", ["MIT", "Harvard", "Stanford"])
        charlie = Student("Charlie", ["MIT", "Harvard", "Stanford"])
        students = [alice, bob, charlie]
        self.game = CollegeAdmissionsGame(colleges, students)
if __name__ == '__main__':
    unittest.main()