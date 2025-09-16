class Solution:

    def encode(self, strs: list[str]) -> str:
        return "|".join(strs)

    def decode(self, s: str) -> list[str]:
        return s.split("|")
