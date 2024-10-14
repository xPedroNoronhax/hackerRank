def duplicate_encode(word):
    word = word.lower()
    letters = {}
    splitted = list(word)
    for i in splitted:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    answear = ''
    for i in splitted:
        if letters[i] > 1:
            answear += ')'
        else:
            answear += '('
    return answear




duplicate_encode('(( @')