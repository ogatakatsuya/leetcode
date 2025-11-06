class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max_candy_num = max(candies)
        for kid in candies:
            result.append(max_candy_num <= kid+extraCandies)
        return result
  
    