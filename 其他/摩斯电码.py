def morse_code(string_input):
    # 大写字符串
    in_str = string_input.upper()

    # 判断字符串是否合规
    for i in in_str:
        if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.-/':
            return 'Error'

    # 构造密码表
    d1 = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }

    # 构造反密码表
    d2 = {}
    for x in d1:
        d2[d1[x]] = x

    # 判断是否解码
    if '.' in in_str:
        out_str = ''
        ls = in_str.split('/')
        for i in ls:
            out_str += d2[i]
        return out_str
    else:
        out_str = []
        for i in in_str:
            out_str.append(d1[i])
        return '/'.join(out_str)


if __name__ == '__main__':
    while 1:
        string = input('输入:')
        if not string:
            break
        print('输出:' + morse_code(string))
