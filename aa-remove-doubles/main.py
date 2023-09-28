import random


def shift_buf_tail_left_to_index(buf, buf_len, cut_index):
    for ii in range(cut_index + 1, buf_len):
        buf[ii - 1] = buf[ii]


def main():
    # получаем массив красивых круглых случайных чисел ))
    buf = [random.randint(1, 9) * 10 for _ in range(20)]
    print(buf)

    # удаляем дубликатыы
    i_look_at, cur_length = 0, len(buf)
    while i_look_at < cur_length:
        for ii in range(i_look_at + 1, cur_length):
            if buf[i_look_at] == buf[ii]:
                shift_buf_tail_left_to_index(buf, cur_length, i_look_at)
                cur_length -= 1
                break
        else:
            i_look_at += 1

    # используем
    print(buf[:cur_length])


main()
