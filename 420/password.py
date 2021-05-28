def strongPasswordChecker(password: str) -> int:
    problems = {
        "too_short": 0,
        "too_long": 0,
        "no_upper": 0,
        "no_lower": 0,
        "no_digit": 0,
        "repeating": [],
    }
    if len(password) < 6:
        problems["too_short"] = 6 - len(password)

    elif len(password) > 20:
        problems["too_long"] = len(password) - 20

    if not any([c.isupper() for c in password]):
        problems["no_upper"] = 1

    if not any([c.islower() for c in password]):
        problems["no_lower"] = 1

    if not any([c.isdigit() for c in password]):
        problems["no_digit"] = 1

    i = 0
    while i < len(password) - 2:
        if password[i] == password[i + 1] and password[i] == password[i + 2]:
            problems["repeating"].append(i)
            i += 3
        else:
            i += 1

    p = problems
    print(p)
    S = p["too_short"]
    L = p["too_long"]
    missing = p["no_upper"] + p["no_lower"] + p["no_digit"]
    R = len(p["repeating"])

    if p["too_short"]:
        return max(S, missing)

    elif p["too_long"]:
        diff = R - missing if R - missing >= 0 else missing - R
        return diff + L

    else:
        return max(R, missing)


print(strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))
print(strongPasswordChecker("aaaaAAAAAA000000123456"))

