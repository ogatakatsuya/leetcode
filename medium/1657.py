from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 片方にしかないアルファベットがある場合、絶対にattainできない
        set1 = set(word1)
        set2 = set(word2)

        if len(set1 | set2) != len(set1):
            return False

        # 数字の個数の分布が一致すればoperation1とoperation2を繰り返したら必ずattainできる
        _, v1 = zip(*Counter(word1).most_common())
        _, v2 = zip(*Counter(word2).most_common())

        if len(v1) != len(v2):
            return False

        for i in range(len(v1)):
            if v1[i] != v2[i]:
                return False

        return True
