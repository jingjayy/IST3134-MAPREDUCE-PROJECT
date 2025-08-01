#!/usr/bin/env python3
import sys

current_word = None
total = 0

for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)

    if word == current_word:
        total += count
    else:
        if current_word:
            print(f"{current_word}\t{total}")
        current_word = word
        total = count

if current_word:
    print(f"{current_word}\t{total}")
