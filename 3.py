class FlatIterator:

    def __init__(self, list_of_list):
        self.iterator = self.flatten_iterator(list_of_list)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    def flatten_iterator(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                yield from self.flatten_iterator(item)
            else:
                yield item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
