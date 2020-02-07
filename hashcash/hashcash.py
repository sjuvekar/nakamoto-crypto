import random
import string
from hashlib import sha256

def binary_leading_0s(hex_str: str):
    binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
    return len(binary_representation) - len(binary_representation.lstrip('0'))

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
    '''
    Method to verify that a given token is in right format, .e.
    1) It is in the form 'version:date:email:nonce'
    2) version is '1'
    3) date is a 6 letter string
    4) nonce is a 16 letter hex string
    '''
    try:
        (version, extracted_date, extracted_email, nonce) = token.split(':')
    except:
        # token is not formatted correctly
        return False

    if version != '1':
        return False

    if len(extracted_date) != 6 or len(date) != 6 or date != extracted_date:
        # Date format is wrong
        return False

    if extracted_email != email:
        return False

    if len(nonce) != 16:
        # Nonce is not 16 digit hex number
        return False

    # Token format is correct. Check whether the sha256 of the token has the
    # required number of leading zeros
    return (binary_leading_0s(sha256(token.encode()).hexdigest()) == difficulty)


def mint(date: str, email: str, difficulty: int) -> str:
  '''
  Method to mint a hashcash token at a given level of difficulty. The token is
  of the form 'version:date:email:nonce', where
  1) version is '1'
  2) nonce is a 16 letter hex string
  3) The number of leading zeros in sha256 hash of the token is equal to
     difficulty
  '''
  version = '1'
  letters = string.ascii_lowercase + string.digits
  while True:
    nonce = ''.join(random.choice(letters) for i in range(16))
    token = ':'.join([version, date, email, nonce])
    if binary_leading_0s(sha256(token.encode()).hexdigest()) == difficulty:
      return token

if __name__ == '__main__':
    print ('Demo of is_valid(): ')
    valid_token = '1:081031:satoshin@gmx.com:b4c26b1694691666'
    print ('  Token = {}'.format(valid_token))
    print ('  Sha256(Token) = {}'.format(sha256(valid_token.encode()).
                                         hexdigest()))
    if is_valid(valid_token, '081031', 'satoshin@gmx.com', 20):
        print ('  The token is valid at difficulty 20')
    else:
        print ('  The token is not valid at difficulty 20')
    print ('  -----------------------------------')
    invalid_token = '1:081031:satoshin@gmx.com:835b8121ee4da3f8'
    print ('  Token = {}'.format(invalid_token))
    print ('  Sha256(Token) = {}'.format(sha256(invalid_token.encode()).
                                         hexdigest()))
    if is_valid(invalid_token, '081031', 'satoshin@gmx.com', 20):
        print ('  The token is valid at difficulty 20')
    else:
        print ('  The token is not valid at difficulty 20')

    print ('Demo of mint(): ')
    print ('  mint(081031, satoshin@gmx.com, 20) = {}'.
           format(mint('081031', 'satoshin@gmx.com', 20)))
