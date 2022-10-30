from typing import List


class Substrings:
    def __init__(self, a: str, b: str) -> None:
        self.a = a
        self.b = b
        self.__longest_substring_result = None
        self.__all_longest_substring_result = None
        self.__all_substring_result = None

    def longest_substring(self) -> str:
        if self.__longest_substring_result is not None:
            return self.__longest_substring_result

        self.__longest_substring_result = self.all_longest_substring()[-1]
        return self.__longest_substring_result

    def all_longest_substring(self) -> List[str]:
        if self.__all_longest_substring_result is not None:
            return self.__all_longest_substring_result

        all_substrings = self.all_substring()
        longest = len(all_substrings[-1])
        self.__all_longest_substring_result = [i for i in all_substrings if len(i) == longest]
        return self.__all_longest_substring_result

    def all_substring(self) -> List[str]:
        if self.__all_substring_result is not None:
            return self.__all_substring_result

        score_matrix = [[0 for i in range(len(self.a)+1)] for j in range(len(self.b)+1)]
        for i in range(1, len(self.b)+1):
            for j in range(1, len(self.a)+1):
                score_matrix[i][j] = 0 if self.b[i-1] != self.a[j-1] else score_matrix[i-1][j-1] + 1

        words = set()
        for i in range(len(self.b), -1, -1):
            for j in range(len(self.a), -1, -1):
                m, n = i, j
                current_word = ""
                while score_matrix[m][n] > 0:
                    current_word = self.b[m-1] + current_word
                    score_matrix[m][n] = 0
                    m, n = m - 1, n - 1
                    words.add(current_word)
                if current_word != "":
                    words.add(current_word)
        self.__all_substring_result = sorted(list(words), key=len)
        return self.__all_substring_result
