#!/usr/bin/env python
# coding: utf-8

# In[60]:


import numpy
import string
import sys
import re
import os


# # 第0步

# In[131]:


def get_letter(path, letter=[]):
    with open(path, 'r', encoding='gb18030', errors='ignore') as f:
        lines = f.readlines()
    f.close()
    letter_dic = {}
    count_en = 0
    for line in lines:
        for s in line:
            if s in string.ascii_letters:
                if s not in letter_dic:
                    letter_dic[s] = 0
                letter_dic[s] += 1
                count_en += 1
    letter = sorted(letter_dic.items(), key=lambda e:e[1], reverse=True)
    return letter


# In[135]:


def zero_one(path):
    letter = get_letter(path)
    for x in letter:
        print(x[0]+':'+str(x[1]/count_en))


# In[136]:


# test
zero_one("C:/Users/柠檬/Desktop/test/one.txt")


# In[137]:


if sys.argv[0] == '-c' and len(sys.argv) == 2:
    zero_one(sys.argv)


# # 第一步

# In[54]:


word_dic = {}
for line in lines:
    s = re.split(r'\W+',line)
    s = [word.lower() for word in s if len(word) > 0]
    for x in s:
        if x not in word_dic:
            word_dic[x] = 0
        word_dic[x] += 1


# In[55]:


word_dic


# In[57]:


word = sorted(word_dic.items(), key=lambda e:e[1], reverse=True)
word


# ## 功能1

# In[110]:


def get_word(path): #return one list
    with open(path, 'r', encoding='gb18030', errors='ignore') as f:
        lines = f.readlines()
    f.close()
    
    word_dic = {}
    for line in lines:
        s = re.split(r'\W+',line)
        s = [word.lower() for word in s if len(word) > 0]
        for x in s:
            if x not in word_dic:
                word_dic[x] = 0
            word_dic[x] += 1
    word = sorted(word_dic.items(), key=lambda e:e[1], reverse=True)
    return word

def one_one(path):
    word = get_word(path)
    for x in word:
        print(x[0],end=' ')
    print('\n')


# In[112]:


# test
one_one("C:/Users/柠檬/Desktop/test/one.txt")


# In[113]:


# 调用
if sys.argv[0] == '-f':
    one_one(sys.argv[1]) 


# ## 功能2

# In[114]:


def get_file(root_path,_files=[]):
    files = os.listdir(root_path)
    for file in files:  
        if not os.path.isdir(root_path + '/' + file):   # not a dir
            _files.append(root_path + '/' + file)
    return _files

def get_all_file(root_path,all_files=[]):
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):   # not a dir
            all_files.append(root_path + '/' + file)
        else:  # is a dir
            get_all_file((root_path+'/'+file),all_files)
    return all_files

def one_two_one(root_path):
    paths = get_file(root_path)
    for path in paths:
        print(path)
        one_one(path)  

def one_two_two(root_path):
    paths = get_all_file(root_path)
    for path in paths:
        print(path)
        one_one(path)  


# In[115]:


# test
one_two_one("C:/Users/柠檬/Desktop/test")


# In[116]:


# test
one_two_two("C:/Users/柠檬/Desktop/test")


# In[117]:


# 调用
if sys.argv[0] == '-d':
    if len(sys.argv) >= 2 and sys.argv[1] == '-s':
        root_path = sys.argv[2] 
        one_two(sys.argv[2])
    elif len(sys.argv) == 2:
        root_path = sys.argv[1] 
        one_two(sys.argv[1])  


# ## 功能3

# In[126]:


def one_three(path, n=None):
    word = get_word(path)
    if n == None:        
        for x in word:
            print(x[0]+':'+str(x[1]))
    else:
        for i in range(n):
            print(word[i][0]+':'+str(word[i][1]))


# In[127]:


# test
one_three("C:/Users/柠檬/Desktop/test/one.txt")


# In[128]:


# test
one_three("C:/Users/柠檬/Desktop/test/one.txt",10)


# In[129]:


# 调用
if sys.argv[0] == '-n':
    path = sys.argv[1] 
    if len(sys.argv) == 2:
        one_three(sys.argv[1])
    elif len(sys.argv) == 3:
        one_three(sys.argv[1], sys.argv[2])


# # 第二步

# In[ ]:



