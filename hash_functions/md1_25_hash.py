# This is a simple demonstration of hash collision with a simplistic hash
# function.
#
# MD1.25 is just MD5 truncated to the first 4 bytes (the first 8 digits in hex).
# Thus, MD1.25 only has a digest size of 32 bits.
#

import random
import string
from hashlib import md5


def md125(s: str) -> str:
    return md5(s.encode()).hexdigest()[:8]


def generate_md125_collisions() -> (str, str):
    '''
    Slower version of md125 collision generator. It randomly generates a string,
    with prefix 'nakamoto', generates its md125 hash, inserts in a dict till a
    match is found.
    '''

    prefix = 'nakamoto'
    letters = string.ascii_lowercase + string.digits

    matches = dict()

    while True:
        str_len = random.randint(32, 64)
        random_str = prefix + ''.join(random.choice(letters) for i in
                range(str_len))
        random_hash = md125(random_str)
        if random_hash in matches.keys():
            return (random_str, matches[random_hash])
        matches[random_hash] = random_str


if __name__ == '__main__':
    print ('Randomly generated collision strings: ')
    print (generate_md125_collisions())
