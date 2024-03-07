#!/usr/bin/env python
# coding: utf-8

# In[4]:


def decimal_to_binary(十進制):
    if 十進制 == 0:
        return "0"
    
    二進制 = ""
    while 十進制 > 0:
        remainder = 十進制 % 2
        二進制 = str(remainder) + 二進制
        十進制 //= 2
    
    return 二進制

# 输入一个十进制数
十進制_num = int(input("請輸入一個十進制數："))
二進制_num = decimal_to_binary(十進制_num)
print("十進制數", 十進制_num, "轉換為二進制數為:", 二進制_num)


# In[ ]:


def decimal_to_hexadecimal(十進制):
    hex_chars = "0123456789ABCDEF"
    十六進制 = ""
    if 十進制 == 0:
        return "0"
    while 十進制 > 0:
        remainder = 十進制 % 16
        十六進制 = hex_chars[remainder] + 十六進制
        十進制 = 十進制 // 16
    return 十六進制

# 輸入一個十進制數
十進制_num = int(input("請輸入一個十進制數："))
十六進制_num = decimal_to_hexadecimal(十進制_num)
print("十進制數", 十進制_num, "十進制數轉換為十六進制數為:", 十六進制_num)


# In[ ]:




