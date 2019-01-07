


class MinMaxIdx(object):

    def __init__(self):
        pass

    def max_idx(self, arr):
        max_idx = 0
        for i in range(1, len(arr)):
            print i
            if arr[i] > arr[max_idx]:
                max_idx = i
        return max_idx


def main():

    arr = [1, 10, 4, 5, 2, 99]
    min_max_idx = MinMaxIdx()

    print min_max_idx.max_idx(arr)



if __name__ == "__main__":
    main()