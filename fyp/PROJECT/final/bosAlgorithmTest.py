import unittest
from bosAlgorithm import BattleOfTheSexes
import numpy as np
import nashpy as nash

class BattleOfTheSexesTest(unittest.TestCase):
    def setUp(self):
        self.test_p1 = np.array([[3,0], [0,7]])
        self.test_p2 = np.array([[7,0], [0,3]])
        self.test_game = nash.Game(self.test_p1, self.test_p2)
        self.test_bos = BattleOfTheSexes.create_game(self.test_p1, self.test_p2)

    def test_set_p1(self):
        with unittest.patch('builtins.input', side_effect=[3,0,0,7]):
            self.assertEqual(self.test_bos.set_p1(), self.test_p1)

    def test_set_p2(self):
        with unittest.patch('builtins.input', side_effect=[7,0,0,3]):
            self.assertEqual(self.test_bos.set_p2(), self.test_p2) 

    def test_create_game(self):
        self.assertEqual(self.test_bos.create_game(self.test_p1, self.test_p2), self.test_game)  
    
    def test_calc_p1_sigma(self):
        self.test_sigma_p1 = BattleOfTheSexes.calc_p1_sigma(self.test_p1)
        unittest.assertEqual(self.test_sigma_p1, [0.3, 0.7])

    def test_calc_p2_sigma(self):
        self.test_sigma_p2 = BattleOfTheSexes.calc_p2_sigma(self.test_p2)
        unittest.assertEqual(self.addCleanuptest_sigma_p2, [0.7, 0.3])  

    def test_calc_utils(self):
        self.test_util = self.test_game[self.test_sigma_p1, self.test_sigma_p2]
        unittest.assertEqual(self.test_util, [2.1, 2.1])

    def test_best_response_p1(self):
        self.test_best_resp_p1 = self.test_p2 * self.test_sigma_p2
        unittest.assertEqual(self.test_best_resp_p1, [[0., 2.1], [2.1, 0.]])
    
    def test_best_response_p2(self):
        self.test_best_resp_p2 = self.test_sigma_p1 * self.test_p1
        unittest.assertEqual(self.test_best_resp_p2, [[0.9, 0.], [0., 4.9]])


if __name__ == '__main__':
    unittest.main()