import unittest

import hashcash

from hashlib import sha256

def sha2(s: str) -> str:
    return sha256(s.encode()).hexdigest()

class TestHashcash(unittest.TestCase):

    def test_binary_leading_0s(self):
        self.assertEqual(2, hashcash.binary_leading_0s(
            sha2('1:081031:satoshin@gmx.com835b8121ee4da3f8')))
        self.assertEqual(20, hashcash.binary_leading_0s(
            sha2('1:081031:satoshin@gmx.com:b4c26b1694691666')))


    def test_is_valid_example(self):
        valid_token = '1:081031:satoshin@gmx.com:b4c26b1694691666'
        self.assertTrue(hashcash.is_valid(
            valid_token, '081031', 'satoshin@gmx.com', 20))
        invalid_token = '1:081031:satoshin@gmx.com:835b8121ee4da3f8'
        self.assertFalse(hashcash.is_valid(
            invalid_token, '081031', 'satoshin@gmx.com', 20))


    def test_mint_1(self):
        email = 'test@gmail.com'
        date = '200209'
        difficulty = 1
        self.assertTrue(hashcash.is_valid(
            hashcash.mint(date, email, difficulty), date, email, difficulty))


    def test_mint_5(self):
        email = 'test@aol.com'
        date = '200208'
        difficulty = 5
        self.assertTrue(hashcash.is_valid(
            hashcash.mint(date, email, difficulty), date, email, difficulty))

    def test_mint_20(self):
        email = 'test@eecs.berkeley.edu'
        date = '100601'
        difficulty = 20
        self.assertTrue(hashcash.is_valid(
            hashcash.mint(date, email, difficulty), date, email, difficulty))


if __name__ == '__main__':
    unittest.main()
