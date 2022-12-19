"""
Problem 8
https://leetcode.com/problems/string-to-integer-atoi/
"""


def myAtoi(s: str) -> int:
    digits = {str(digit): digit for digit in range(10)}
    sign = 0
    digit_detected = False
    number = 0
    for i in range(len(s)):
        if not digit_detected:
            if s[i] == " ":
                continue
            elif s[i] in ["-", "+"]:
                if sign != 0:  # because you can't have a number with both signs
                    return 0
                sign = 1 if s[i] == "+" else -1
                digit_detected = True
                continue
            elif s[i] in digits:
                digit_detected = True
            else:
                return 0

        if s[i] in digits:
            number = number * 10 + digits[s[i]]
        else:
            break

    if sign == 0:
        sign = 1

    number *= sign
    lower_bound = -(2**31)
    upper_bound = 2**31 - 1

    if number < lower_bound:
        return lower_bound
    elif upper_bound < number:
        return upper_bound

    return number


for num in [
    "3246",
    "-44",
    "       0000000623",
    "    0000-4256",
    "     -9",
    "     -0043fasdfb    ",
    "5.1415",
    "- 3.141547456",
    "00000-42a1234",
]:
    print(f"${num}$, ${myAtoi(num)}$")
