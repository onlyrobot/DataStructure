'''
Author: 彭瑶
Date: 2019/11/11
Description: 树状数组
'''


def lowbit(x):
    return x & (-x)


def sum(array, beg, end):
    total = 0
    while end > 0:
        total += array[end - 1]
        end -= lowbit(end)
    while beg > 0:
        total -= array[beg - 1]
        beg -= lowbit(beg)
    return total


def change(array, pos, delta):
    pos += 1
    while pos <= len(array):
        array[pos - 1] += delta
        pos += lowbit(pos)


def init(array):
    for i in range(1, len(array) + 1):
        total = lowbit(i) - 1
        count = 1
        while count <= total:
            array[i - 1] += array[i - 1 - count]
            count += lowbit(i - count)


def main():
    array = [i for i in range(16)]
    init(array)
    change(array, 5, 8)
    print(array)
    print(sum(array, 0, 7))


if __name__ == '__main__':
    main()