#!/bin/python3

if __name__ == '__main__':
    array = list(map(int, input().split()))

    min = array[0]
    max = array[0]
    sum = sum(array)
    minSum = 0
    maxSum = 0

    for i in range(1, len(array)):
        number = array[i]

        if number < min:
            min = number
        elif number > max:
            max = number

    minSum = sum - max
    maxSum = sum - min

    print('{} {}'.format(minSum, maxSum))
