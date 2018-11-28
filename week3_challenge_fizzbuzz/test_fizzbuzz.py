import unittest
from fizzbuzz import fizzbuzz

class Test_fizzbuzz(unittest.TestCase):
    
    def test_fizzbuzz_returns_fizz(self): 
        listA=[1,2]
        listb=[1,5]
        self.assertEqual(fizzbuzz(listA, listb),  'fizz')
       
       
    def test_fizzbuzz_returns_buzz(self):
        listA = [1,3]
        listB = [2,4]
        self.assertEqual(fizzbuzz(listA, listB), 'buzz')


    def test_fizzbuzz_returns_fizzbuzz(self):
        listA = [2,3,4]
        listB = [2,2,2]
        self.assertEqual(fizzbuzz(listA,listB), 'fizzbuzz')
