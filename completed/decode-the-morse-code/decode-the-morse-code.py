def decodeMorse(morse_code):
    answer = ""
    morse_code = morse_code.strip()
    words = morse_code.split('   ')
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            answer += MORSE_CODE[letter]
        answer += " "
    return answer.strip()