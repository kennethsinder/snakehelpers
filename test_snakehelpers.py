# pylint: disable=E1101
import snakehelpers as h
import unittest


class SnakeHelpersTests(unittest.TestCase):
    def test_any_in_returns_false(self):
        self.assertFalse(h.any_in(
            ['test1', 'test2'],
            ['test22', 'test3'],
        ))

    def test_any_in_returns_true(self):
        self.assertTrue(h.any_in(
            ('test1', 'test2'),
            {'test3', 'test4', 'test2'},
        ))
    
    def test_first_not_in_returns_default(self):
        L = ['1', '2', '3', '4']
        criterion = lambda x: x == '5'
        default = 'five'
        required = False
        result = h.first(L, criterion, default, required)
        self.assertEqual(result, default)
    
    def test_first_true_predicate_returns_first(self):
        L = ('1', '2', '3', '4')
        criterion = True
        default = 'five'
        required = True
        result = h.first(L, criterion, default, required)
        self.assertEqual(result, L[0])
    
    def test_first_false_predicate_returns_default(self):
        L = ('1', '2', '3', '4')
        criterion = False
        default = 'five'
        required = False
        result = h.first(L, criterion, default, required)
        self.assertEqual(L, ('1', '2', '3', '4'))
        self.assertEqual(result, default)

    def test_filter_dict_mixed_keys_filters(self):
        mapping = {1: 0, 2: 1, 3: 2}
        keys = (3, 4)
        result = h.filter_dict(mapping, keys)
        self.assertDictEqual(result, {3: 2})

    def test_filter_dict_empty_keys_empty(self):
        mapping = {1: 0, 2: 1}
        keys = []
        result = h.filter_dict(mapping, keys)
        self.assertDictEqual(result, {})


if __name__ == '__main__':
    unittest.main()
