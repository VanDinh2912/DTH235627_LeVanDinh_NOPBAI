import re


def NegativeNumberInStrings(s: str):
    numbers = re.findall(r"-\d+", s)
    return [int(num) for num in numbers]


s = input("Nhập vào một chuỗi:")
print(NegativeNumberInStrings(s))
