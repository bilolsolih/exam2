def last_word_length(s):
    if ' ' in s:
        last_word = s.rsplit(' ', 1)[1]
        return len(last_word)
    else:
        return len(s)


def integer_array(a):
    if 1 > len(a) > 100:
        raise ValueError('Length error')
    for i in range(0, len(a) + 1):
        a[i] = int(a[i])

    for i in range(1, len(a) + 1):
        if a[-i] > 9 or a[-i] < 0:
            raise ValueError('Digit cannot be bigger than 9 or smaller than 0')

    a[-1] = a[-1] + 1
    carried_value = 0
    for i in range(1, len(a) + 1):
        if a[-i] + carried_value == 10:
            a[-i] = 0
            carried_value = 1
        else:
            a[-i] = a[-i] + carried_value
            carried_value = 0
    return a


print(last_word_length(input('Enter a string, and the length of the last word will be returned: ')))
