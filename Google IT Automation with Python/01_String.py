def double_word(word):
    doubl = word*2
    wordok = doubl + str(len(doubl))

    return wordok

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0