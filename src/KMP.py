'''
Author: 彭瑶
Date: 2019/11/11
Description: KMP字符串匹配算法
'''


def get_next_array(p):
    '''获取next数组'''
    next = [-1]
    for i in range(1, len(p)):
        pos = i - 1
        while pos != 0 and p[i - 1] != p[next[pos]]:
            pos = next[pos]
        next.append(next[pos] + 1)
    return next


def match(s, p):
    '''用字符串p来匹配s，返回所有匹配到的索引'''
    next = get_next_array(p)
    j, result = 0, []
    for i in range(len(s)):
        if s[i] == p[j]:
            j += 1
            if j == len(p):
                result.append(i - j + 1)
                j = 0
        else:
            while j != -1 and s[i] != p[j]:
                j = next[j]
            j += 1
    return result if result else None


def main():
    print(match('hello world world hello', 'hello'))


if __name__ == '__main__':
    main()