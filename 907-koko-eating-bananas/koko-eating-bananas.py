class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            # Calculate total hours needed at speed = mid
            hours = 0
            for pile in piles:
                # Ceiling division: ceil(pile / mid)
                hours += (pile + mid - 1) // mid

            if hours <= h:
                # mid is fast enough, try a smaller speed
                right = mid
            else:
                # mid is too slow, need a faster speed
                left = mid + 1

        return left