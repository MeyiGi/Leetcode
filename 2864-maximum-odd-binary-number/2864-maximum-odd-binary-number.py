class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")

        one = ('1' * (ones - 1))
        zero = ('0' * (len(s) - ones))

        return one + zero + "1"