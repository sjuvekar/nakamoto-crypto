# Simple program to demonstrate Merkle Trees and proof of inclusion using Merkle
# Trees. The first part of the program
#   1) breaks a sentence in its constituent words
#   2) computes the hash of every word (we are using sha256 hash)
#   3) pads the resulting list to make power-of-2 size-simplistic
#   4) iteratively computes a binary Merkle Tree
#
# The second part of the program demonstrates an inclusion proof by iteratively
# computing the hashes using data and siblings and comparing the hashes with
# the root of the Merkle Tree.
import math
from enum import Enum
from hashlib import sha256


def perfect_pow(l: int) -> bool:
    """
    A boolean function to test whether an integer is a complete power of 2
    """
    return 2 ** int(round(math.log(l, 2))) == l


def hash(word: str) -> str:
    """
    Util function to compute sha256 hash of a string. Encodes the string as
    binary using string.encode() method before computing the hash.
    """
    return sha256(word.encode()).hexdigest()


def merkleize(sentence: str) -> str:
    """
    Main function to compute the Merkle Tree (as a string) from a given
    sentence.
    """
    # First separate the sentence into words
    words = sentence.strip().split()

    # Base layer: append the hashes of individual elements
    old_hashes = list()
    new_hashes = list()
    for word in words:
        old_hashes.append(hash(word))
    # Pad the hashes with '\x00' to complete power-of-2 size
    while not perfect_pow(len(old_hashes)):
        old_hashes.append('\x00')

    # Main loop to iteratively compute hashes and update new_hashes
    while len(old_hashes) > 1:
        for i in range(0, len(old_hashes), 2):
            new_hashes.append(hash(old_hashes[i] + old_hashes[i + 1]))
        old_hashes = new_hashes
        new_hashes = list()
    return old_hashes[0]


class Side(Enum):
    LEFT = 0
    RIGHT = 1


def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
    """
    Main method to validate that a given data (str) is present in a Merkle Tree
    represented by root. The method accepts a sibling path as proot (e.g.
    [(sibling1, Side.LEFT), (sibling2, Side.RIGHT), ...])
    """
    data_hash = hash(data)
    for p in proof:
        sibling_hash = p[0]
        sibling_enum = p[1]
        if sibling_enum == Side.LEFT:
            data_hash = hash(sibling_hash + data_hash)
        else:
            data_hash = hash(data_hash + sibling_hash)
    return data_hash == root


if __name__ == '__main__':
    # Demo of merkelize()
    sentence = 'I love chicken!'
    print("Original sentence: '{}''".format(sentence))
    root = merkleize(sentence)
    print("Merkle Tree: {}".format(root))

    # demo of validate_proof
    # hash of "I love"
    data = "chicken!"
    left_hash = merkleize("I love")
    validation = validate_proof(root, data, [('\x00', Side.RIGHT), (left_hash, Side.LEFT)])
    if validation:
        print("String '{}' is present in '{}'".format(data, sentence))
    else:
        print("String '{}' is not present in '{}'".format(data, sentence))
