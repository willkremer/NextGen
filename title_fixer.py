def fix_title(title):
    title = title.capitalize()
    title = title.lower()
    words = title.split()
    for i in range(len(words)):
        if words[i] not in('a', 'the', 'an', 'in', 'of'):
            words[i] = words[i].capitalize()
    words = ' '.join(words)
    return words
print(fix_title('wind In The willows'))