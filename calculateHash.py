#!/usr/bin/env python3

# Reference: https://pypi.org/project/filehash/

import filehash

test_file = "/home/kajol/LawFact/Windows-Forensics/test.txt"

# Calculating MD5 of test file
md5hash = filehash.FileHash('md5')
calc_hash = md5hash.hash_file(test_file)
print("MD5:", calc_hash)

# Calculating SHA256 of test file
sha256 = filehash.FileHash('sha256')
calc256_hash = sha256.hash_file(test_file)
print("SHA256:", calc256_hash)

