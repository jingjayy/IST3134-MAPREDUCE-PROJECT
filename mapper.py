#!/usr/bin/env python3
import sys
import re

# Load valid words
with open("words.txt") as f:
    english_words = set(word.strip() for word in f)

for line in sys.stdin:
    # Remove XML tags
    line = re.sub(r'<[^>]+>', ' ', line)
    words = re.findall(r'\b[a-z]{2,}\b', line.lower())
    for word in words:
        if word in english_words:
            print(f"{word}\t1")

