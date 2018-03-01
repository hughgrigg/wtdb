import wtdb
import unittest


class TestWtdbFunctions(unittest.TestCase):

    def test_n_swaps_zero(self):
        self.assertEqual(
            frozenset(),
            wtdb.n_swaps('foo', 'bar', 0),
        )

    def test_n_swaps_single(self):
        self.assertSequenceEqual(
            {
                frozenset({'bar', 'foo'}), frozenset({'boo', 'far'}),
                frozenset({'oo', 'fbar'}), frozenset({'bfoo', 'ar'}),
            },
            wtdb.n_swaps('foo', 'bar', 1),
        )

    def test_n_swaps_one_double(self):
        self.assertSequenceEqual(
            {
                frozenset({'strain', 'team'}), frozenset({'train', 'steam'}),
                frozenset({'srain', 'tteam'}), frozenset({'trsteam', 'ain'}),
                frozenset({'stain', 'tream'}), frozenset({'tsteam', 'rain'}),
                frozenset({'sttrain', 'eam'}), frozenset({'sain', 'trteam'}),
            },
            wtdb.n_swaps('steam', 'train', 2),
        )

    def test_order_pair(self):
        self.assertSequenceEqual(
            ('national', 'rail'),
            wtdb.order_pair(('rail', 'national'))
        )

    def test_order_pair_same_length(self):
        self.assertSequenceEqual(
            ('steam', 'train'),
            wtdb.order_pair(('train', 'steam'))
        )


class TestWordSet(unittest.TestCase):

    def test_find_swaps_none(self):
        word_set = wtdb.WordSet()
        word_set.add('foo')
        word_set.add('bar')
        self.assertListEqual([], list(word_set.find_swaps('hello')))

    def test_find_swaps_single_letter(self):
        word_set = wtdb.WordSet()
        word_set.add('national')
        word_set.add('rail')
        word_set.add('rational')
        self.assertListEqual(
            [
                (('national', 'rail'), ('rational', 'nail')),
            ],
            sorted(word_set.find_swaps('nail')),
        )

    def test_find_swaps_double_letter(self):
        word_set = wtdb.WordSet()
        word_set.add('steam')
        word_set.add('train')
        word_set.add('team')
        self.assertListEqual(
            [
                (('steam', 'train'), ('strain', 'team')),
            ],
            sorted(word_set.find_swaps('strain')),
        )

    def test_validate_ok(self):
        word_set = wtdb.WordSet()
        word_set.add('foo')
        word_set.add('bar')
        self.assertTrue(word_set.validate('foo', 'bar'))

    def test_validate_bad(self):
        word_set = wtdb.WordSet()
        word_set.add('foo')
        word_set.add('bar')
        self.assertFalse(word_set.validate('foo', 'bar', 'foobar'))


if __name__ == '__main__':
    import doctest
    doctest.testmod(wtdb)
    unittest.main()
