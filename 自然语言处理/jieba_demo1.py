import jieba

text = '我爱北京天安门，天安门前太阳升'
words_list = " ".join(list(jieba.cut(text, cut_all=True)))  # 全模式
print(words_list)

words_list2 = " ".join(list(jieba.cut(text, cut_all=False)))  # 精确模式
print(words_list2)

