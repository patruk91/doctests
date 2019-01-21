def cyclic_rotation(string, number):
    """
    Calculate a cyclic rotation of a string; i.e. move the last N elements
    from the end to the beginning.
    >>> cyclic_rotation("abcde", 2)
    'deabc'
    >>> cyclic_rotation("abcde", 3)
    'cdeab'
    >>> cyclic_rotation("hello", -1)
    'ohell'
    >>> cyclic_rotation("hello", -3)
    'llohe'
    >>> cyclic_rotation("", 1)
    ''
    """
    if number >= 0:
        new_string = string[-number:] + string[:-number]
        return new_string
    else:
        new_string = string[number:] + string[:number]
        return new_string
