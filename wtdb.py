import itertools


def n_swaps(word_a: str, word_b: str, n: int) -> frozenset:
    """
    Return words with all combinations of swapping up to their first n letters.
    """
    if n <= 0:
        return frozenset()
    swaps = set()
    # Swap cartesian product of n letters in each word.
    # E.g. [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for swap_counts in itertools.product(range(n + 1), range(n + 1)):
        swap_a = swap_counts[0]
        swap_b = swap_counts[1]
        swaps.add(
            frozenset((
                word_a[:swap_a] + word_b[swap_b:],
                word_b[:swap_b] + word_a[swap_a:],
            ))
        )
        swaps.add(
            frozenset((
                word_b[:swap_a] + word_a[swap_b:],
                word_a[:swap_b] + word_b[swap_a:],
            ))
        )
    return frozenset(swaps)


def order_pair(words: tuple) -> tuple:
    """
    Ensure consistency ordering of pairs.
    """
    # Sort alphabetically first to ensure consistency when pair is same length.
    return tuple(sorted(sorted(words), key=len, reverse=True))


def render_pair(words: tuple) -> str:
    return '{} {} / {} {}'.format(
        words[0][0], words[0][1], words[1][0], words[1][1]
    )


class WordSet:

    words = set()

    def add(self, word: str):
        self.words.add(word)

    def find_swaps(self, word: str, n: int = 2):
        for partner in self.words:
            if partner == word:
                continue
            if partner[:1] == word[:1]:
                continue
            for swap in n_swaps(word, partner, n):
                if self.validate(*swap):
                    yield (order_pair(swap), order_pair((word, partner)))

    def validate(self, *potentials) -> bool:
        for potential in potentials:
            if potential not in self.words:
                return False
        return True


if __name__ == '__main__':
    word_set = WordSet()
    import sys
    for line in sys.stdin:
        word = line.strip().lower()
        if len(word) < 3:
            continue
        for pair in word_set.find_swaps(word):
            print(render_pair(pair))
        word_set.add(word)
