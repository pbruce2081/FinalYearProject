import unittest
from prisonersDilemma import PrisonersDilemma
import numpy as np
import nashpy as nash

class PrisonersDilemmaTest(unittest.TestCase):
    def setUp(self):
        self.test_p1 = np.array([[-1,-10], [0,-9]])
        self.test_p2 = self.test_p1.T
        self.test_game = nash.Game(self.test_p1, self.test_p2)
        self.test_pd = PrisonersDilemma.create_game(self.test_p1, self.test_p2)

    def test_set_p1(self):
        with unittest.patch('builtins.input', side_effect=[-1,-10,0,-9]):
            self.assertEqual(self.test_pd.set_p1(), self.test_p1)

    def test_set_p2(self):
        with unittest.patch('builtins.input', side_effect=[-9,0,-10,-1]):
            self.assertEqual(self.test_pd.set_p2(), self.test_p2) 

    def test_create_game(self):
        self.assertEqual(self.test_pd.create_game(self.test_p1, self.test_p2), self.test_game)  

    def test_calc_p1_sigma(self):
        self.test_sigma_p1 = PrisonersDilemma.calc_p1_sigma(self.test_p1)
        unittest.assertEqual(self.test_sigma_p1, [-0, 1]) # calculate sigma

    def test_calc_p2_sigma(self):
        self.test_sigma_p2 = PrisonersDilemma.calc_p2_sigma(self.test_p2)
        unittest.assertEqual(self.test_sigma_p2, [-0, 1]) # calculate sigma

    def test_calc_utils(self):
        self.test_util = self.test_pd[self.test_sigma_p1, self.test_sigma_p2]
        unittest.assertEqual(self.test_util, [-9, -9])

    def test_best_response_p1(self):
        self.test_best_resp_p1 = self.test_p2 * self.test_sigma_p2
        unittest.assertEqual(self.test_best_resp_p1, [[0, 0], [0, -9]])

    def test_best_response_p2(self):
        self.test_best_resp_p2 = self.test_sigma_p1 * self.test_p1
        unittest.assertEqual(self.test_best_resp_p2, [[0, -10], [-0, -9]])

    def test_check_best_response_true(self):
        self.test_is_best = self.test_pd.is_best_response(self.test_sigma_p1, self.test_sigma_p2)
        unittest.assertEqual(self.test_is_best, True)

    def test_check_best_response_false(self):
        self.test_is_best = self.test_pd.is_best_response(self.test_sigma_p1, self.test_sigma_p2)
        unittest.assertEqual(self.test_is_best, False)

if __name__ == '__main__':
    unittest.main()