from time import time


def solution(s: str, wordDict: list[str]) -> bool:
    wordset = set(wordDict)

    cache = {}

    def recursive(s: str) -> bool:
        if s in wordset:
            return True

        if s in cache:
            return cache[s]

        candidates = []
        for i in range(len(s) - 1, 0, -1):
            if s[:i] in wordset:
                if s[i:] not in cache:
                    cache[s[i:]] = recursive(s[i:])
                candidates.append(cache[s[i:]])

            if True in candidates:
                return True
        return False

    return recursive(s)


# start = time()

# solution(
#     "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#     ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
# )

# elapsed = time() - start
# print(elapsed)
