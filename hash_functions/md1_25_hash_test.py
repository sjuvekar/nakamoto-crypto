import unittest

import md1_25_hash

class TestMD125HashCollision(unittest.TestCase):

    def test_md125(self):
        self.assertEqual(md1_25_hash.md125('hi'), '49f68a5c')
        self.assertEqual(md1_25_hash.md125('nakamotobl7q6vrfgpahzhsk5sdqg6u7b6empfefmnuoj2'),
                         md1_25_hash.md125('nakamotoph5n2kcjwf2wiova6ycotev011xibnr0i870ilupz5jng9pr5hmfaar'))

    def test_md125_collision(self):
        (str1, str2) = md1_25_hash.generate_md125_collisions()
        self.assertEqual(md1_25_hash.md125(str1), md1_25_hash.md125(str2))


if __name__ == '__main__':
    unittest.main()
