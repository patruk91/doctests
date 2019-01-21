def most_frequent(numbers):
    """
    Check what is the most frequent number in array. If there are multiple
    such numbers, return the largest one.
    >>> most_frequent([3, 3, 3, 2, 2, 2, 4, 4])
    3
    >>> most_frequent([3, 3, 3, 5, 5, 5, 4, 4])
    5
    >>> most_frequent([3, 3, 3, 5, 5, 5, 4, 4, 4, 4, 4])
    4
    """

    max_number_occurrence = max([numbers.count(number) for number in set(numbers)])
    numbers_list = [number for number in set(numbers) if numbers.count(number) == max_number_occurrence]
    numbers_list.sort(reverse=True)
    return numbers_list[0]
