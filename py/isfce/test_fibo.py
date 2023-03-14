import unittest
import Fibo

class TestMyMath(unittest.TestCase):
    
    def test_estPair(self):
        self.assertEqual(0, Fibo.fibo(0))
        self.assertEqual(1, Fibo.fibo(1))
        self.assertEqual(1, Fibo.fibo(2))
        self.assertEqual(8, Fibo.fibo(6))
        self.assertRaises(AssertionError, Fibo.fibo, -1)
       

if __name__ == "__main__":
    unittest.main()