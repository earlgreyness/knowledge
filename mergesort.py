import unittest
import random


def merge_sort(arr):
    """It's recursive."""
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    return _merge(
        merge_sort(arr[:half]),
        merge_sort(arr[half:]),
    )


def _merge(a, b):
    iters = (iter(a), iter(b))
    vals = [next(it, None) for it in iters]

    while True:
        if vals == [None, None]:
            break
        if None in vals:
            crit = vals[1] is None
        else:
            crit = vals[0] < vals[1]
        index = 0 if crit else 1
        yield vals[index]
        vals[index] = next(iters[index], None)


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        random_list = self._get_random_list()
        self.assertEqual(list(merge_sort(random_list)), sorted(random_list))

    def test_merge(self):
        list_a = sorted(self._get_random_list())
        list_b = sorted(self._get_random_list())
        self.assertEqual(list(_merge(list_a, list_b)), sorted(list_a + list_b))

    @staticmethod
    def _get_random_list():
        length = random.randint(100, 1000)
        return [random.randint(-100, 100) for _ in range(length)]


if __name__ == '__main__':
    unittest.main()
