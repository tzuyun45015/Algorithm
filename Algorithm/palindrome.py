    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        return newStr == newStr[::-1]
