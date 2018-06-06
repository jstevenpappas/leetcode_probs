

'''
Given an array of distinct integer values, count the # of pairs of
integers that have difference k.

For example, given the array {1, 7, 5, 9, 2, 12, 3} and the
difference k=2, there are four pairs with difference 2:
    (1,3), (3,5), (5, 7), (7, 9)
'''



arr_vals = {1,7,5,9,2,12,3}
k_diff = 2


def pairs_with_diff(arr, diff):
    pairs = list()
    arr_dict = dict((x, x ) for x in arr_vals)
    for x in arr_vals:
        key = x-diff
        if key in arr_dict:
            pairs.append((x, key))
    return pairs



    '''
    for key, val in arr_dict.items():
        print key, arr_dict.get(key)
    '''



def main():
    print pairs_with_diff(arr_vals, k_diff)
    print len(pairs_with_diff(arr_vals, k_diff))


if __name__ == "__main__":
    main()