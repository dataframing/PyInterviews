"""
    Here's the assignment:
        Find the total number of prime pairs (x, y) such that:
            1. x and y are both consecutive (i.e. there are no primes that are
               greater than x or less than y)
            2. x and y are both less than 500,000,000
            3. y - x = 36
        Note: you're looking for distinct prime *pairs*. So if we have three
              consecutive primes x, y, z where z - y = 36 and y - x = 36, we
              count this as two pairs of primes.

        I made this code a bit more flexible so that it (1) allows for a
        prime difference other than 36 and so that we can (2) increase or
        decrease our limit as we'd like.
"""

__author__ = "Danny Vilela"

def main():
    run()


def run(difference=36, limit=500000000):
    """ Driver for entire assignment. Includes formatted output and some kind thanks """

    # list_of_primes will hold, well, our list of primes post-sieve
    print("Populating list of primes...")
    list_of_primes = primes_query(limit)

    # dictionary_of_primes will hold {a:b} value pairs such that a,b are prime,
    # less than 'limit', and a - b = difference
    print("Filtering for consecutive, differ-by-{} primes...".format(difference))
    dictionary_of_primes = difference_evaluation(list_of_primes)

    # boom
    print_dictionary(dictionary_of_primes)

    print("\n***************************************************************")
    print("Given: \n \t(1) A difference between consecutive primes of exactly {} \n \t(2) Consecutive prime pairs under {:,} only\n".format(difference, limit))
    print("We arrive at {:,} pairs of distinct primes".format(len(dictionary_of_primes)))
    print("***************************************************************\n")
    print("Above is our entire dictionary of prime pairs. \n \nThanks! \n- Danny")


def primes_query(limit):
    """
        Utilizes Sieve of Eratosthenes primality algorithm test approach in order to reduce time complexity of
        generating list of prime numbers whose value is less than parameter :limit

        :return list object as comprehension, representing each prime number
                below :limit
    """
    # [False, False, True, True, ..., True]
    is_prime_bool_list = ([False] * 2) + ([True] * (limit - 1))

    for i in range(int(limit ** 0.5) + 1):
        if is_prime_bool_list[i]:
            # Eratosthenes sieve-ing locations in the array that are multiples of i
            for j in range(i * i, limit + 1, i):
                is_prime_bool_list[j] = False

    return [index for index, is_prime_bool_list in enumerate(is_prime_bool_list) if is_prime_bool_list]


def difference_evaluation(list_of_primes, difference=36):
    """
        Cycles through :list_of_primes and populates dictionary_of_primes, which
        will serve to track our consecutive primes whose difference is 36
    """
    dictionary_of_primes = {}
    previous_prime = 0

    # Evaluates difference between (i+1)th and (i)th elements within list_of_primes,
    # inserting those whose difference is 36 into our dictionary_of_primes
    for i in list_of_primes:
        if i - previous_prime == difference:
            dictionary_of_primes[i] = previous_prime
        previous_prime = i

    return dictionary_of_primes


def print_dictionary(dictionary_of_primes):
    """ Prints formatted output of dictionary_of_primes """
    for key, value in dictionary_of_primes.items():
        print("[Prime: {:>12,}; Previous Prime: {:>12,}; Difference: {}]".format(key, value, key - value))
        

if __name__ == "__main__":
    main()