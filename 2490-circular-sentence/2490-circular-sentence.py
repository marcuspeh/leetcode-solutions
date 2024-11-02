class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        prev = sentence[-1]
        sentence = " " + sentence
        for i in range(len(sentence)):
            if sentence[i] != " ":
                prev = sentence[i]
                continue
            if sentence[i + 1] != prev:
                return False
        return True