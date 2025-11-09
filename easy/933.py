class RecentCounter:
    def __init__(self):
        self.history = []
        
    def ping(self, t: int) -> int:
        self.history.append(t)
        count = 0
        for value in self.history[::-1]:
            if value>=t-3000:
                count += 1
            else:
                break
        return count
