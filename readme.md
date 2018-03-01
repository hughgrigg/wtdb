# WTDB (What's the Difference Between?)

WTDB is a word-play game where you guess
[spoonerism](https://en.wikipedia.org/wiki/Spoonerism) pairs based on a clue
beginning with "what's the difference between?"

For example,

"What's the difference between an old locomotive and stress on a group?"
-> "steam train" / "team strain"

This is a hacky Python script to produce potential spoonerism pairs based on a
list of words.

## Usage

Pipe the list of words to `python3 wtdb.py`, e.g. if you're on Ubuntu you can
try:

```bash
cat /usr/share/dict/british-english | python3 wtdb.py
```

However that produces quite a lot of garbage due to weird words, short words,
words with spaces or apostrophes, proper nouns etc.

A shorter word list might be better, e.g. from
https://github.com/first20hours/google-10000-english

You could also limit to longer words to get more interesting results, e.g.

```bash
cat google-10000-english.txt | awk '{ if (length($0) > 4) print }' | python3 wtdb.py
```

## Testing

```bash
python3 -m unittest wtdb_test.py
```
