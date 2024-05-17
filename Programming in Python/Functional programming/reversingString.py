def reverseString(s: str) -> str:
    return s[::-1]


def reverseStringRecursive(s: str) -> str:
    if len(s) == 0:
        return s
    return reverseStringRecursive(s[1:]) + s[0]


print("*********")
print(reverseString("abcdef"))

print("*********")
print(reverseStringRecursive("abcdef"))
