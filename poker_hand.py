def poker_hand(numbers):
    """
    Write a poker_hand function that will score a poker hand. The function
    will take an array 5 numbers and return a string based on what is inside.
    >>> poker_hand([1, 1, 1, 1, 1])
    'five'
    >>> poker_hand([2, 2, 2, 2, 3])
    'four'
    >>> poker_hand([1, 1, 1, 2, 3])
    'three'
    >>> poker_hand([2, 2, 3, 3, 4])
    'twopairs'
    >>> poker_hand([1, 2, 2, 3, 4])
    'pair'
    >>> poker_hand([1, 1, 2, 2, 2])
    'fullhouse'
    >>> poker_hand([1, 2, 3, 4, 6])
    'nothing'
    """
    poker_values = [numbers.count(number) for number in set(numbers)]

    if 5 in poker_values:
        return 'five'
    elif 4 in poker_values:
        return 'four'
    elif 3 in poker_values and len(poker_values) == 3:
        return 'three'
    elif len(poker_values) == 5:
        return 'nothing'
    elif len(poker_values) == 4:
        return 'pair'
    elif len(poker_values) == 3:
        return 'twopairs'
    elif len(poker_values) == 2:
        return 'fullhouse'
