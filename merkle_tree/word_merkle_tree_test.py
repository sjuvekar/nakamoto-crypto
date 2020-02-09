import unittest

import word_merkle_tree

class TestWordMerkleTreen(unittest.TestCase):

    def test_perfect_pow(self):
        for i in range(1, 17):
            if i == 1 or i == 2 or i == 4 or i ==8 or i == 16:
                self.assertTrue(word_merkle_tree.perfect_pow(i))
            else:
                self.assertFalse(word_merkle_tree.perfect_pow(i))


    def test_hash(self):
        self.assertEqual('bb5f9549fc282efd3b5658cf241fa9027f9c54d807c400bd6c67479d0ceae0af',
                         word_merkle_tree.hash('I love chicken!'))
        self.assertEqual('a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c',
                         word_merkle_tree.hash('I'))
        self.assertEqual('0344d28d3508a660c276b6b0bdb7d019c6f2f67a5eb1f6c6cc5b17f29f96330d',
                         word_merkle_tree.hash('I love'))
        self.assertEqual('d122d720aeeec33cf6b4cb4713c263d144720bead07c3b61e6310dbaf8b21145',
                         word_merkle_tree.hash('chicken!'))


    def test_merkelize_chicken(self):
        self.assertEqual('ac5544f3322e06322c6740a7c428c5cf9f2f33b88a023a3aad6d7199c31cbe29',
                         word_merkle_tree.merkleize('I love chicken!'))



    def test_merkelize_nakamoto(self):
        self.assertEqual('363b815b22916026e2619132ac4f469be92047451271f3f6b0f1ead63e0a3f77',
                     word_merkle_tree.merkleize('nakamoto is the father of crypto'))


    def test_validate_chicken(self):
        '''
                     H()
                /             \
          H() (left_sibling)    H()
        /      \          /        \
        H()    H()       H()     '\x00' (right_sibling)
        |      |          |
        I     love     chicken
        '''
        root = word_merkle_tree.merkleize('I love chicken!')
        left_sibling = word_merkle_tree.merkleize('I love')
        right_sibling = '\x00'
        self.assertTrue(word_merkle_tree.validate_proof(
            root, 'chicken!',
            [(right_sibling, word_merkle_tree.Side.RIGHT),
             (left_sibling, word_merkle_tree.Side.LEFT)]))


    def test_validate_nakamoto(self):
        '''
                                    root->H()
                              /                 \
                            /                     \
                     H()                                r3->H()
                /            \                     /               \
             H()            r2->H()              H()                H()
         /          \        /      \          /      \          /        \
        H()      r1->H()    H()      H()      H()      H()     '\x00'    '\x00'
        |            |      |        |        |        |
        nakamoto     is    the     father     of     crypto
        '''
        root = word_merkle_tree.merkleize('nakamoto is the father of crypto')
        r1 = word_merkle_tree.hash('is')
        r2 = word_merkle_tree.hash(
            word_merkle_tree.hash('the')+
            word_merkle_tree.hash('father')
        )
        r3 = word_merkle_tree.hash(
            word_merkle_tree.hash(
                word_merkle_tree.hash('of')+word_merkle_tree.hash('crypto')
            ) + word_merkle_tree.hash('\x00'+'\x00')
        )
        self.assertTrue(word_merkle_tree.validate_proof(
            root, 'nakamoto',
            [(r1, word_merkle_tree.Side.RIGHT),
             (r2, word_merkle_tree.Side.RIGHT),
             (r3, word_merkle_tree.Side.RIGHT)]))


if __name__ == '__main__':
    unittest.main()
