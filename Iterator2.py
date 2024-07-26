class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.index_stack = [0]
        self.current_list = list_of_lists

    def __iter__(self):
        return self

    def __next__(self):
        while self.index_stack:
            index = self.index_stack[-1]
            if index >= len(self.current_list):
                self.index_stack.pop()
                if self.index_stack:
                    current_level_index = self.index_stack[-1]
                    self.current_list = self.list_of_lists
                    for i in self.index_stack[:-1]:
                        self.current_list = self.current_list[i]
                    self.index_stack[-1] = current_level_index + 1
                continue

            item = self.current_list[index]
            if isinstance(item, list):
                self.index_stack.append(0)
                self.current_list = item
            else:
                self.index_stack[-1] += 1
                return item

        raise StopIteration


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
