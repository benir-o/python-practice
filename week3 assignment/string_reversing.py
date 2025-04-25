
word=input("Enter word: ")

def word_reversal(word_detail):
    word_character_list=list(word_detail)
    j=-1
    for _ in word_character_list:
        print(word_character_list[j],end="")
        j-=1

word_reversal(word)
#Finished


