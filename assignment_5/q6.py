def median(numbers):
    # sort list
    numbers = sorted(numbers)
    # select element "in the middle"
    middle_idx = len(numbers) // 2
    print(middle_idx)
    # case distinction
    if len(numbers) % 2:
        return int(numbers[middle_idx])
    else:
        l = numbers[middle_idx-1]
        r = numbers[middle_idx]
        return int((l+r)//2)
    
print(median([10.90, 11.90, 8.90, 12.90, 5.90]))

# ================ Answer for test suite ================
class MedianTests(TestCase):
    def test1(self):
        actual = median([10.90, 11.90, 8.90, 12.90, 5.90])
        expected = 10.90
        self.assertEqual(expected, actual)

    def test2(self):
        actual = median([1.0, 3.0, 1.0, 2.0])
        expected = 1.5
        self.assertEqual(expected, actual)

    def test4(self):
        actual = median([])
        expected = None
        self.assertEqual(expected, actual)