word_list = ['apple','watch','apolo','star','abocado']

# words = [i for i in word_list if i[0] =='a']
# print(words)

for word in word_list:
    if word[0] != 'a':
        word_list.remove(word)



print(word_list)