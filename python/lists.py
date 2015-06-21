# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """

    items = list(filter(lambda x: len(x) >= 2 and x[0] == x[-1], words))
    return len(items)


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """

    sorted_words = sorted(words)
    first_half = [i for i in sorted_words if i[0] == 'x']
    second_half = [i for i in sorted_words if i[0] != 'x']

    return first_half + second_half


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    return sorted(tuples, key=lambda tup: tup[1])


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    if len(nums) == 0:
        return nums

    previous = nums[0]
    newList = [previous]

    for i in range(1, len(nums)):
        currentNum = nums[i]
        if currentNum != previous:
            previous = currentNum
            newList.append(currentNum)

    return newList





def remove_adjacent_ls(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent_ls([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent_ls([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent_ls([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent_ls([])
    []
    >>> remove_adjacent_ls([3, 2, 3, 3, 3,4,4,5])
    [3, 2, 3, 4, 5]
    """
    last_elem_idx=len(nums)-1
    new_list = [nums[i] for i in range(0,len(nums)) if i==last_elem_idx or nums[i+1] != nums[i] ]

    return new_list





def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    mList = []
    aIdx = 0
    bIdx = 0

    if (len(list1) == 0 or len(list2) == 0):
        return list1 + list2

    while aIdx < len(list1) and bIdx < len(list2):
        if list1[aIdx] < list2[bIdx]:
            mList.append(list1[aIdx])
            aIdx = aIdx + 1
        else:
            mList.append(list2[bIdx])
            bIdx = bIdx + 1

    while aIdx < len(list1):
        mList.append(list1[aIdx])
        aIdx = aIdx + 1

    while bIdx < len(list2):
        mList.append(list2[bIdx])
        bIdx = bIdx + 1

    return mList
