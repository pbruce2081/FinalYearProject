import unittest
from polymatrixGame import PolymatrixGame

class PolymatrixGameTest(unittest.TestCase):
    def setUp(self):
        self.test_payoffs1 = [
            [[1,2], [0,0]],
            [[0,0], [2,1]]
        ]
        self.test_payoffs2 = [
            [[1,2,3], [0,0,1]],
            [[0,1,0], [2,1,2]]
        ]
        self.test_strategies1 = [[0,0], [1,1]]
        self.test_strategies2 = [[0,0,0], [1,0,1]]

    def test_calculate_payoffs(self):
        test_payoffs3 = PolymatrixGame.calculate_payoffs(self.test_strategies1)
        test_payoffs4 = PolymatrixGame.calculate_payoffs(self.test_strategies2)
        self.assertEqual(test_payoffs3, [[0,0], [0,0]])
        self.assertEqual(test_payoffs4, [[0,0,0], [1,0,1]])

    def test_best_response(self):
        test_game1 = PolymatrixGame(self.test_payoffs1)
        test_game2 = PolymatrixGame(self.test_payoffs2)
        self.assertEqual(test_game1.get_best_response(), (0,1))
        self.assertEqual(test_game2.get_best_response(), (0,1))
    
    def test_nash_equilibria(self):
        test_game1 = PolymatrixGame(self.test_payoffs1)
        test_game2 = PolymatrixGame(self.test_payoffs2)
        self.assertEqual(test_game1.get_nash_equilibria(), [(1,0)])
        self.assertEqual(test_game2.get_nash_equilibria(), [(0,2), (1,2), (2,2)])

    def test_draw_graph(self):
        test_game1 = PolymatrixGame(self.test_payoffs1)
        test_game2 = PolymatrixGame(self.test_payoffs2)
        test_game1.draw_graph()
        test_game2.draw_graph()

if __name__ == "__main__":
    unittest.main()