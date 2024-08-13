root_word='оКРуг'
other_words='окраина','труд','весна', 'крУг','окрошка','суБокруг', 'листва', 'округЛость'

def single_root_words(root_word,*other_words):
    same_words=[]
    for k in range (len(other_words)):
        if any (i in str(other_words[k]).lower() for i in  [root_word])  > 0:
            same_words.append(other_words[k])
        elif any (i in root_word for i in [str(other_words[k]).lower()])>0:
            same_words.append (other_words[k])
    print( same_words)
single_root_words(root_word.lower(),*other_words)

