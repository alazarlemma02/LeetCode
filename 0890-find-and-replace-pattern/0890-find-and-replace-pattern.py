class Solution(object):
    def matchpattern(self, word, pattern):
        if len(word) != len(pattern):
            return False

        p_map = {}
        w_map = {}

        for p_char, w_char in zip(pattern, word):
            if p_char not in p_map:
                p_map[p_char] = w_char
            if w_char not in w_map:
                w_map[w_char] = p_char

            if p_map[p_char] != w_char or w_map[w_char] != p_char:
                return False
        return True
    def findAndReplacePattern(self, words, pattern):
        result = []
        for word in words:
            if self.matchpattern(word, pattern):
                result.append(word)
        return result
        