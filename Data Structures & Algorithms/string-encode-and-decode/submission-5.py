class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += f"{s}~"
        encoded_string = string[::-1]

        return encoded_string

    def decode(self, s: str) -> List[str]:
        ds = s[::-1]
        decoded_strs = ds.split("~")
        decoded_strs.pop()
        return decoded_strs
        