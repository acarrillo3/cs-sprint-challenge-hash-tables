def has_negatives(a):
    """
    YOUR CODE HERE
    """
    numbers_seen = dict()
    numbers_with_negatives = []

    for number in a:

        # add all numbers to the dictionary
        numbers_seen[number] = 1

        # if the current number's additive inverse in the dictionary, add the positive version to the resulting array
        # exclude zero
        if number != 0 and -number in numbers_seen:
            numbers_with_negatives.append(abs(number))

    return numbers_with_negatives


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
