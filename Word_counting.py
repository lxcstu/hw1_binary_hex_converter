# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:14:36 2024

@author: 66
"""

def count_unique_words(file_path):
   
    word_count = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
       
        for line in file:
            
            line = line.strip().lower()
            words = line.split()
            for word in words:
                if word.isalpha():
                    
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    
    unique_word_count = len(word_count)
    

    print("總共有 %d 個不同的英文單詞" % unique_word_count)
    print("不同的英文單詞及其出現次數為:")
    for word, count in word_count.items():
        print("%s: %d" % (word, count))

count_unique_words('D:\Downloads\hw2_data.txt') 

