import codecs
import string
first_half = string.ascii_lowercase[:13]
second_half = string.ascii_lowercase[:12:-1]
def encrypter(strng):
    need_to_flip = codecs.encode(strng, 'rot_13')
    answer = ''
    for x in need_to_flip:
        if x in first_half:
            answer += second_half[first_half.index(x)]
        elif x in second_half:
            answer += first_half[second_half.index(x)]
        else:
            answer += x
    return answer