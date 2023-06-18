import unittest
swap_file = __import__('swap')
Solution = swap_file.Solution
class TestSwap(unittest.TestCase):    
    def test_single_char(self):
        sol = Solution('a','a')
        self.assertEqual(sol.solve(),'Yes')

    def test_unique_char_same_seq_positive(self):
        sol = Solution('asdfe','asdfe')
        self.assertEqual(sol.solve(),'Yes')
    
    def test_unique_char_diff_seq_positive(self):
        sol = Solution('efasd','asdfe')
        self.assertEqual(sol.solve(),'Yes')

    def test_unique_char_diff_seq_negative(self):
        sol = Solution('edfas','asdfe')
        self.assertEqual(sol.solve(),'No')
    
    def test_mismatch_char(self):
        sol=Solution("adffsd","zcxcvv")
        self.assertEqual(sol.solve(),'No')

    def test_single_mismatch_char(self):
        sol=Solution("adffsd","adffse")
        self.assertEqual(sol.solve(),'No')

    def test_repeated_char_same_seq_positive(self):
        sol = Solution("aaaaa","aaaaa")
        self.assertEqual(sol.solve(),'Yes')
    
    def test_duplicated_char_same_seq_positive(self):
        sol = Solution("abaced","acebed")
        self.assertEqual(sol.solve(),'No')


if __name__ == '__main__':
    unittest.main()
