import unittest
import ex101


class Ex101TestCase(unittest.TestCase):
    def setUp(self):
        self.exercise = ex101
        self.env = self.exercise.Environment() 

    def test_initial_state(self):
        print('test initial state')
        self.assertEqual(self.env.reset(), 1)  # add assertion here

    def test_transition(self):
        print('test transition function')
        self.env.reset()
        self.assertEqual(self.env.step(0), (2, 1))
        self.assertEqual(self.env.step(1), (3, 1))


if __name__ == '__main__':
    unittest.main()
