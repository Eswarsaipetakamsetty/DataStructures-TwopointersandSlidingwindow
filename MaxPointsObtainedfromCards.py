class Solution:
    def maxScore(self, cardPoints, k):
        lsum = 0
        rsum = 0
        maxsum = 0
        n = len(cardPoints)
        for i in range(k):
            lsum += cardPoints[i]
        maxsum = lsum
        
        right = n-1
        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[right]
            right -= 1
            maxsum = max(maxsum, (lsum + rsum))
        return maxsum


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    index = 1
    for _ in range(t):
        cardPoints = list(map(int, data[index].split()))
        k = int(data[index + 1])
        solution = Solution()
        print(solution.maxScore(cardPoints, k))
        print("~")
        index += 2

