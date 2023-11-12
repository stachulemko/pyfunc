from re import T


test_data = ["())(", "()", "", "("]
test_output = [False, True, True, True]


def nawiasowanie(wejscie):
    licznik = 0
    for i in wejscie:
        if i == "(":
            licznik += 1
        elif i == ")":
            licznik -= 1
        else:
            return False
        if licznik < 0:
            return False
    if licznik == 0:
        return True
    else:
        return False


for input, out in zip(test_data, test_output):

    assert nawiasowanie(input) == out
