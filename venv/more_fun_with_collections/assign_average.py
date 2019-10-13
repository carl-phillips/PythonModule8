"""Carl Phillips, the program demonstrates selection using a dictionary"""
def switch_average(key):
    """
    :param key: key to match with value in dictionary
    :return: returns dictionary value unless it does not match
    """
    my_dict = dict({'A': 5, 'B': 10, 'C': 15, 'D': 20, 'E': 25})
    if(key == None):
        raise KeyError
    if key in my_dict.keys():
        return my_dict[key]
    else:
        raise KeyError


if __name__ == '__main__':
    try:
        switch_average()
    except KeyError:
        print("No key in dictionary")
