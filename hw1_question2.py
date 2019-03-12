def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    for num in range(100000,999999):
        if is_palindrome(str(num)[2:]):
            if is_palindrome(str(num+1)[1:]):
                if is_palindrome(str(num+2)[1:5]):
                    if is_palindrome(str(num+3)):
                        return num


def is_palindrome(s):
    rev = s[::-1]
    return s == rev


if __name__ == '__main__':
    # Question 2
    return_value = check_palindrome()
    print(f"Question 2 solution: {return_value}")
