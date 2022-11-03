class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        l = [chr(i + ord('a')) for i in range(26)]
        queue = deque([])
        queue.append([beginWord,0])
        while queue:
            a, b = queue.popleft()
            if a == endWord:
                return b + 1
            for j in range(len(a)):
                for i in l:
                    if (a[:j] + i + a[j+1:]) in s and (a[:j] + i + a[j+1:]) != beginWord:
                        s.remove(a[:j] + i + a[j+1:])
                        queue.append([a[:j] + i + a[j+1:], b+1])
        return 0