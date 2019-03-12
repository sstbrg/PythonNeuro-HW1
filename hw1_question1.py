from itertools import groupby


def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    cnt = 0
    num_of_consec_chars = 2
    num_of_groups = 3

    if word == '':
        return False
    else:
        content = [[k, len(list(g))] for k, g in groupby(word)]
        for element in content:
            if element[1] % num_of_consec_chars == 0:
                cnt += element[1]
                if cnt == num_of_consec_chars * num_of_groups:
                    return True
            else:
                cnt = 0

    return False


if __name__ == '__main__':
    # Question 1
    return_value = trifeca('aaAAaa')
    print(f"Question 1 solution: {return_value}")

