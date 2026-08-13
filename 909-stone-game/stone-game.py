class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        
        """
        n = len(piles)

        # best_lead[i][j] = lead of the player to move on piles[i..j].
        # Only cells where i <= j are ever used; the rest stay 0 and are ignored.
        best_lead = [[0] * n for _ in range(n)]

        # Length-1 ranges: take the only pile.
        for i in range(n):
            best_lead[i][i] = piles[i]

        # Grow the range length. Every cell we compute depends on cells one
        # shorter, which are already filled in by the time we reach them.
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                take_left = piles[i] - best_lead[i + 1][j]
                take_right = piles[j] - best_lead[i][j - 1]
                best_lead[i][j] = max(take_left, take_right)

        return best_lead[0][n - 1] > 0

        """