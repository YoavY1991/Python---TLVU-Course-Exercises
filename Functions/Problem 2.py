def sentence_to_words(s):
    # s contains eng letters, numbers, spaces and punctuation marks "!?., %#$"
    split_l = s.split()
    marks = '!?., %#$'
    for i, w in enumerate(split_l):
        split_l[i] = w.lower()

    for i, w in enumerate(split_l):
        for m in marks:
            if m is w[0]:
                split_l[i] = w[1:]
                break
        for m in marks:
            if m is w[-1]:
                split_l[i] = w[:-1]

    return split_l


print(sentence_to_words("Mr. Stark... I don't feel so good"))
print(sentence_to_words("THE CAKE IS A LIE. THE CAKE IS A LIE."))
print(sentence_to_words("It's simple, we kill the batman!"))