# nakamoto-crypto
This is the repository containing Python code samples/exercises/tests from https://nakamoto.com/introduction-to-cryptocurrency/

## Topics

* **Hash functions:** An artificial MD1.25 Hash function for demonstrating collision
  * Run Hash collision generator: `cd hash_functions && python3 md1_25_hash.py`
  * Run tests: `cd hash_functions && python3 md1_25_hash_test.py`

* **Merkel Trees:** A demonstration of constructing Merkel Trees and proof of inclusion using them.
  * Run Merkle Tree generator: `cd merkle_tree && python3 word_merkle_tree.py`
  * Run tests: `cd merkle_tree && python3 word_merkle_tree_test.py`

* **Hashcash:** A demonstration of minting and validating Hashcash token.
  * Run token minter/validator: `cd hashcash && python3 hashcash.py`
  * Run tests: `cd hashcash && python3 hashcash_test.py`
