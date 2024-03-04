class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        currScore = 0
        maxScore = 0

        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                currScore += 1
                left += 1
                maxScore = max(maxScore, currScore)
            else:
                if not currScore:
                    break
                power += tokens[right]
                currScore -= 1
                right -= 1

        return maxScore