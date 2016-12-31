def ransom_note(magazine, ransom):
    
    m = len(magazine)
    n = len(ransom)
    
    if m < n:
        return False

    magazine_words = {}
    for word in magazine:
        magazine_words[word] = magazine_words.get(word, 0) + 1

    for word in ransom:
        if word not in magazine_words or magazine_words[word] < 1:
            return False
        else:
            magazine_words[word] -= 1
            
    return True
    
        



magazine = raw_input('Enter magazine: ').strip().split(' ')
ransom = raw_input('Enter ransom: ').strip().split(' ')
answer = ransom_note(magazine, ransom)


if(answer):
    print "Yes"
else:
    print "No"
