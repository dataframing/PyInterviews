"""
    Here's the assignment:
        You're asked to generate all phone numbers of length `n`.
        A phone number where n = 3 is of the form: `321` or `234` or `999`
        There is no special formatting required (i.e. no dashes, parentheses)

    Constraints:
        A phone number cannot begin with a `0`

    Examples:
        If n = 5: `10000`, `99999`, `98765`
        If n = 2: `10`, `90`, `43`
"""

__author__ = 'Danny Vilela'


def rec_permutations(n=10, phone_string=""):
    """
    In our recursive solution, we treat our problem as an implicit tree of
    depth n and utilize a depth-first-search in order to print out each
    possible permutation.

    :param n: the length of our phone number string
    :param phone_string: the phone number being strung together
    :return: will print out each permutation
    """
    if n == 0:
        print(phone_string)
    else:
        for level in range(n):
            if phone_string == "" and level == 0:
                pass
            else:
                phone_string += str(level)
                rec_permutations(n-1, phone_string)


def iter_permutations(n=10):
    """
    In our iterative solution, we utilize a for-loop and some not-so-clever
    math in order to generate all possible permutations. We note that,
    for any n length string, we will have [(10 ** n) - (10 ** (n-1))] - 1 possible
    permutations. i.e.:

    If n = 3, we note that our valid permutations will range from
    100 -- (10 ** (n - 1)) -- to 999 -- (10 ** n) - 1. Ergo,
    we have [(10 ** 3) - (10 ** (2))] - 1 = 899 valid permutations.

    :param n: the length of our phone number string
    :param phone_string: the phone number being strung together
    :return: will print out each permutation
    """

    start = 10 ** (n-1)
    end = (10 ** n)
    for phone_string in range(start, end):
        print(phone_string)


def main(n_limit=6):
    for i in range(n_limit):
        print("Recursive phone numbers of length {}\n".format(i))
        rec_permutations(i)
        print("Iterative phone numbers of length {}\n".format(i))
        iter_permutations(i)

if __name__ == "__main__":
    main()