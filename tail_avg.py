class TailAvg(object):

    def __init__(self, num_to_avg):
        self.num_to_avg = num_to_avg
        self.bids = [0] * self.num_to_avg
        self.sum = 0

    def tail_avg(self, curr_bid):
        if len(self.bids) == self.num_to_avg:

            # pops first ele off list while subtracting it from total
            self.sum -= self.bids.pop(0)

        self.sum += curr_bid
        self.bids.append(curr_bid)

        return self.sum / self.num_to_avg


def main():
    tailAvg = TailAvg(3)
    print tailAvg.tail_avg(2)
    print tailAvg.tail_avg(2)
    print tailAvg.tail_avg(2)
    print tailAvg.tail_avg(20)
    print('')
    print(tailAvg.bids)

    print tailAvg.tail_avg(20)
    print('')
    print(tailAvg.bids)


if __name__ == "__main__":
    main()
