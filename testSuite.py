import unittest
from unittest.mock import patch
from player import Player
from game1 import PDG
from game2 import College, Student, CollegeAdmissionsGame

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Alice", 2, [-1, -3, 0, -2])
    #integration
    
    # def test_pdg_game(self):
    #     player1 = Player("Alice", 2, [-1, -3, 0, -2])
    #     player2 = Player("Bob", 2, [-1, 0, -3, -2])
    #     game1 = PDG(2) 
    #     game1.play_game(player1, player2)
    #     assert player1.payout == -1
    #     assert player2.payout == -1
        
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
        
    # def test_college_admissions_game(self):
    #     mit = College("MIT", 2, ["Alice", "Bob", "Charlie"])
    #     harvard = College("Harvard", 2, ["Bob", "Alice", "Charlie"])
    #     stanford = College("Stanford", 1, ["Bob", "Charlie", "Alice"])
    #     colleges = [mit, harvard, stanford]
        
    #     alice = Student("Alice", ["MIT", "Harvard", "Stanford"])
    #     bob = Student("Bob", ["MIT", "Harvard", "Stanford"])
    #     charlie = Student("Charlie", ["MIT", "Harvard", "Stanford"])
    #     students = [alice, bob, charlie]
        
    #     game = CollegeAdmissionsGame(colleges,students)
    #     game.deferred_acceptance()
        
    #     assert alice.assigned_college == harvard
    #     assert bob.assigned_college == mit
    #     assert charlie.assigned_college == stanford
    #     assert mit.is_full() == True
    #     assert harvard.is_full() == True
    #     assert stanford.is_full() == True

    # def test_pdg_and_college_admissions_game(self):
    #     player1 = Player("Alice", 2, [-1, -3, 0, -2])
    #     player2 = Player("Bob", 2, [-1, 0, -3, -2])
    #     game1 = PDG(2) 
    #     game1.play_game(player1, player2)

    #     mit = College("MIT", 2, ["Alice", "Bob", "Charlie"])
    #     harvard = College("Harvard", 2, ["Bob", "Alice", "Charlie"])
    #     stanford = College("Stanford", 1, ["Bob", "Charlie", "Alice"])
    #     colleges = [mit, harvard, stanford]


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

    # @patch('builtins.input', side_effect=['C', 'C', 'C', 'D'])
    #  def test_play_game(self, mock_input):
    #      self.pdg.play_game(self.player1, self.player2)
    #      self.assertEqual(self.player1.payout, -2)
    #      self.assertEqual(self.player2.payout, -1)

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