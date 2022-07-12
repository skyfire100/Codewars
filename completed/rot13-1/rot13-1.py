def rot13(message):
    answer = ""
    for letter in message:
        if letter.isalpha():
            num = ord(letter)
            num += 13
            if letter.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letter.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            answer += chr(num)
        else:
            answer += letter
    return answer