def most_frequent(list):
    '''
    Check what is the most frequent number in an array

    >>> most_frequent([3, 3, 3, 2, 2, 2, 4, 4])
    3
    '''
    counter = 0
    num = list[0]
    for i in list:
        curr_frequency = list.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


def cyclic_rotation(str, n):
    '''
    Calculate a cyclic rotation of a string; i.e. 
    move the last N elements from the end to the beginning

    >>> cyclic_rotation('abcde', 2)
    deabc
    '''
    return str[-n:] + str[:-n]

