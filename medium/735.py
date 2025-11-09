class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        results = []
        for i in asteroids:
            if i >= 0 or len(results) == 0:
                results.append(i)
            else:
                while True:
                    if len(results) == 0:
                        results.append(i)
                        break
                    num = results.pop()
                    if num < 0:
                        results.append(num)
                        results.append(i)
                        break
                    else:
                        if abs(i) < abs(num):
                            results.append(num)
                            break
                        elif abs(i) == abs(num):
                            break
        return results
