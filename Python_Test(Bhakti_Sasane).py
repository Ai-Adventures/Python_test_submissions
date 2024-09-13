#!/usr/bin/env python
# coding: utf-8

# ## Python Test
# 
# ### Instructions:
# 
# You are given with Python coding problems. These problems will give you the chance to test your implementations of the questions. Each code runs your implementations for a number of testcases. You use the test codes to make sure that:
# 
#     • Your function does not crash, that is, there is no Python errors when trying to run the
#     function.
# 
#     • Compare the results of the testcases to your results. Expected results are given at the
#     end of each code.
# 
# 
# In each problem, replace pass command with your implementation of each required function.

# ### Question 1 - Arithmetic
# 
# In this question, your task is to implement a function `do_arithmetic(x,y,op)` which takes three input arguments: a number x,
# a number y, and a string op representing an operation. The function has to perform the
# operation on the two numbers and return the result.
# 
# - Example 1: if you call the function with the parameter `do_arithmetic(10,4,’add’)` the function should return the value 14.0.
# 
# - Example 2: `do_arithmetic(2,3,’*’)` should return 6.0.
# 
# **Detailed instructions:**
# -  You can assume that x and y are always provided and always valid numbers (e.g. integers or floats).
# 
# - `op` is a string representing the operation to perform. You have to implement four operations with ’add’, ’+’, ’subtract’, ’-’, ’multiply’, ’*’, and ’divide’, ’/’.
# 
# - If `op` is not specified by the user it should default to ’add’.
# 
# - If `op` is specified by the user but it is not one of the four operations (with eight keywords), print ’Unknown operation’ and return None.
# 
# - Division by zero should be avoided. To this end, return None whenever division by zero would occur, and print ’Division by 0!’
# 
# - The returned result should always be of type float.
# 
# Test code: The following test cases will be tested:
# 
# `do_arithmetic(24, -7, 'add')`
# - Expected result:- 17.0
# 
# `do_arithmetic(6, 6, 'multiply')`
# - Expected result:- 36.0
# 
# `do_arithmetic(4, 0, '/')`
# - Expected result: "Division by Zero!"
# 
# `do_arithmetic(3, 9, '-')`
# - Expected result: -6.0
# 
# `do_arithmetic(10, -43, 'subtract')`
# - Expected result: 53.0
# 
# `do_arithmetic(3, 9)`
# - Expected result: 12.0

# In[48]:


def do_arithmetic(x,y,op):
      if op=='add' or op=='+':
        print('Expected result : ',x+y)
        pass
      elif op=='subtract' or op=='-':
        print('Expected result : ',x-y)
        pass
      elif op=='divied' or op=='/':
        print('Expected result : ',x/y)
        pass
      elif op=='multiply' or op=='*':
        print('Expected result : ',x*y)
        pass
x=int(input('enter x value:'))
y=int(input('enter y value:'))
op=input('enter oprations:')
do_arithmetic(x,y,op)


# ### Question 2 - Sum of digits
# 
# Write a function `sum_of_digits(s)` that takes as input a string s that contains some numbers. The function calculates the sum of all the digits in the string, ignoring any symbols that
# are not digits.
# 
# • Example: `sum_of_digits("123")` should return 6 since 1+2+3 = 6
# 
# • Example 2: `sum_of_digits("10a20")` should return 3 because 1+0+2+0 = 3.
# Detailed instructions:
# 
# - if s includes both digits and nondigits
#  
#   – Calculate the sum of digits and return the result whilst ignoring any
#   
#   non-digit symbols in the string.
#   
#   – print e.g. for `sum_of_digits("10a20")`
#   
#   ’The sum of digits operation performs 1+0+2+0’
# 
#   – Save the extracted non-digits in a variable of interest as a list and print "The extracted non-digits are: [’a’]"
# 
# - If s is not provided or an empty string return 0 and print
#   
#   ’Empty string entered!’.
# 
# - If s is provided, but it contains no digits return 0 and print
#   
#   ’The sum of digits operation could not detect a digit!’
#   
#   ’The returned input letters are: [ALL NONDIGITS HERE]’
# 
# - The returned number should be an integer.
# 
#   - Example 1: When you run `sum_of_digits("a1w3")` , the function should print
#     
#     The sum of digits operation performs 1+3
#     
#     The extracted non-digits are: [’a’, ’w’]
#     
#     4
# 
#   - Example 2: When you run `sum_of_digits("united")`, the function should print
#     
#     The sum of digits operation could not detect a digit!
# 
#     The returned input letters are: [’u’, ’n’, ’i’, ’t’, ’e’, ’d’]
#     
#     0
# 
# Test code: The following test cases will be tested:
# 
# `sum_of_digits("123")`
# 
# - Expected result: 
#   
#   The sum of digit operation performs 1 + 2 + 3
#   
#   The extracted non-digits are []
#   
#   6
# 
# `sum_of_digits("we10a20b")`
# 
# - Expected result: 
# 
#   The sum of digit operation performs 1 + 0 + 2 + 0
# 
#   The extracted non-digits are ['w', 'e', 'a', 'b']
# 
#   3
# 
# `sum_of_digits("united")`
# - Expected result: 
# 
#   The sum of digits operation could not detect a digit!
#   
#   The extracted non-digits are ['u', 'n', 'i', 't', 'e', 'd']
#   
#   0
# 
# `sum_of_digits("")`
# 
# - Expected result:
# 
#   The sum of digits operation could not detect a digit!
#   
#   The extracted non-digits are []
#   
#   0

# In[60]:


'8'.isdigit()


# In[ ]:





# In[1]:


def sum_of_digits(s):
        l1=[]
        j=0
        for i in s:
            if i  in 'qwertyuioplkjhgfdsazxcvbnm' :
                 l1.append(i)
            else:
                j=j+int(i)
                pass
        return(j,l1)
s=input("Enter the string:")
sum_of_digits(s)


# In[ ]:





# ### Question 3 - Pluralize
# 
# Please download following file named `pronoun.txt` before you solve this questions the link is given below:
# 
# [Required file link](https://cdn.discordapp.com/attachments/953213295710584862/974555326865100830/pronoun.txt)
# 
# Write a function `pluralize(word)` that determines the plural of an English word.
# Input: Your function takes one argument as input, word, a string representing the word to be
# pluralised. We assume this word will only be one single token, i.e., no spaces. Your function will also have to load the text file `proper nouns.txt`.
# 
# Output: The function should return a dictionary of the form:
#   - {’plural’: word_in_plural, ’status’: x}
# 
# 
# where word_in_plural is the pluralized version of the input argument word and x is a
# string which can have one of the following values: ’empty_string’, ’proper_noun’, ’
# already_in_plural’, ’success’.
# 
# 
# Below is the logic (in order) that the function should execute.
# 
# 1) Determine if the word is an empty string, already in plural, or a proper noun.
# 
#     • If the word is an empty string, then your function returns a dictionary with the following values:
#     
#       – word_in_plural = ’’ and x = ’empty_string’
#     
#       – Explanation: The input word is an empty string and it cannot be pluralized.
#     
#     • If the word is already in plural, then your function returns a dictionary with the following values:
#     
#       – word_in_plural = word and x = ’already_in_plural’.
#     
#       – Explanation: The input word remains untouched (e.g., input: houses, output: houses).
#     
#     • If the word is a proper noun, then your function returns a dictionary with the following values:
#     
#       – word_in_plural = word and x = ’proper_noun’.
#     
#       – Explanation: The input word is a proper noun, and therefore cannot be pluralized (e.g., input: Adam, output: Adam).
# 
#     • How to determine plural form: We will assume a word is in plural if it ends with ’s’.
# 
#     • How to determine if a word is a proper noun: We will assume a word is a proper noun if it exists in the file proper nouns.txt. Note that your function should convert any capitalised input to lower case first because the proper nouns in the list are all lower case. The values in your output dictionary, however, will retain the original capitalisation
# 
# 2) If the word is not plural and is not a proper noun, then:
#   Apply the following English plural rules.
#     
#     • If the word ends with a vowel:
#         – add -s.
#     
#     • Otherwise:
#         
#         – If it ends with ’y’ and is preceded by a consonant, erase the last letter and add
#         
#           -ies.
#         
#         – If it ends with ’f’, erase the last letter and add -ves.
#         
#         – If it ends with ’sh’/’ch’/’z’, add -es.
#         
#         – If none of the above applies, just add -s.
# 
#     • After these rules are applied, your output dictionary should be:
#         – {’plural’: word_in_plural, ’status’: ’success’}
# 
# 
# Test code: The following test cases will be tested:
# 
# `pluralize("failure")`
# - Expected result: `{'plural':'failures', 'status':'success'}`
# 
# `pluralize("food")`
# - Expected result: `{'plural':'foods', 'status':'success'}`
# 
# `pluralize("Zulma")`
# - Expected result: `{'plural':'zulma', 'status':'proper_noun'}`
# 
# `pluralize("injury")`
# - Expected result: `{'plural':'injuries', 'status':'success'}`
# 
# `pluralize("elf")`
# - Expected result: `{'plural':'elves', 'status':'success'}`
# 
# `pluralize("buzz")`
# - Expected result: `{'plural':'buzzes', 'status':'success'}`
# 
# `pluralize("computers")`
# - Expected result: `{'plural':'computers', 'status':'already_in_plural'}`
# 
# `pluralize("PCs")`
# - Expected result: `{'plural':'PCs', 'status':'already_in_plural'}`
# 
# `pluralize("")`
# - Expected result: `{'plural':'', 'status':'empty_string'}`
# 
# `pluralize("highway")`
# - Expected result: `{'plural':'highways', 'status':'success'}`
# 
# `pluralize("presentation")`
# - Expected result: `{'plural':'presentations', 'status':'success'}`
# 
# `pluralize("pouch")`
# - Expected result: `{'plural':'pouches', 'status':'success'}`
# 
# `pluralize("COVID-19")`
# - Expected result: `{'plural':'COVID-19s', 'status':'success'}`
# 
# `pluralize("adam")`
# - Expected result: `{'plural':'adam', 'status':'proper_noun'}`
# 

# In[89]:


import os
os.getcwd()
f=open('pronoun.txt', 'r')
def pluralize(word):
    if word == "":
        return {'plural': '', 'status': 'empty_string'}
    
    original_word = word  
    word_lower = word.lower() 
    
    if word_lower.endswith('s'):
        return {'plural': original_word, 'status': 'already_in_plural'}
    

    if word_lower in f:
        return {'plural': original_word, 'status': 'proper_noun'}
    
    vowels = "aeiou"
    
    if word_lower[-1] in vowels:
        plural_word = original_word + 's'
    
    elif word_lower[-1] == 'y' and word_lower[-2] not in vowels:
        plural_word = original_word[:-1] + 'ies'
    
    elif word_lower.endswith('f'):
        plural_word = original_word[:-1] + 'ves'
    

    elif word_lower.endswith(('sh', 'ch', 'z')):
        plural_word = original_word + 'es'
    

    else:
        plural_word = original_word + 's'
    
    return {'plural': plural_word, 'status': 'success'}


word=input('entar word:')
pluralize(word)


# ### Question 4 - Function renamer
# 
# 
# You are working on a large-scale software project involving thousands of different Python files. The files have been written by different programmers and the naming of functions is somewhat inconsistent. You receive a new directive stating that the function names all have to be in camel case. In camel case, function names consisting of multiple words have a capital letter in each word and most underscores are removed. For instance, `def MyArithmeticCalculator()` is in camel case but `def my_arithmetic_calculator()` is not in camel case.
# 
# You want to write a Python program that automatically processes Python code and renames the function names instead of doing it by hand. The instruction states that:
# 
#   1.) All functions names need to be changed to camel case. E.g. a function
#   `calculate_speed_of_vehicle()` needs to be renamed to `CalculateSpeedOfVehicle()`.
# 
#   2.) If the function has one or more leading ’_’ (underscores) they need to be preserved.
# 
#   All other underscores need to be removed. E.g. a function `__calc_size()` is renamed to `__CalcSize()`.
# 
#   3.) If the function is already in camel case, you do not need to change it but it still needs to appear in the dictionary d specified below.
# 
#   4.) You can assume that there will be no name clashes. That is, a given function name which is not in camel case will not already appear in camel case elsewhere. E.g.if there is a function `print_all_strings()` then there is no function `PrintAllStrings()` elsewhere in the code.
# 
# 5.) Tip: You can use regular expressions to find the function names.
# 
# 
# To implement this, write a function `function_renamer(code)` that takes as input a string code that represents the Python code. It is typically a multi-line Python string. Your function needs to return the tuple `(d, newcode)`:
# 
#   • `d` is a nested dictionary where each key corresponds to the original function name. The value is a nested dictionary that has the following items:
# 
#     – hash: hash code of the original function name (tip: use Python’s hash function)
# 
#     – camelcase: camel case version of original function name
# 
#     – allcaps: all caps version of original function name
# 
#   • newcode is a string containing the code wherein all function names have been renamed by their camel case versions. Note that you need to change the function name and also all other locations where the function name is used (e.g. function calls). You should not change anything else in the code (e.g. the contents of any strings). To clarify this, a few examples are given below:
#     - Example 1: Assume your input code is the multi-line string
#     
#         def add_two_numbers(a, b):
#           return a + b
#           print(add_two_numbers(10, 20))
#  
#     
#     
#       After processing it with your function, the code should be changed to
# 
#         def AddTwoNumbers(a, b):
#           return a + b
#         print(AddTwoNumbers(10, 20))
# 
#         The nested dictionary is given by
#         d = {’add_two_numbers’:
#         {’hash’:-9214996652071026704,
#         ’camelcase’:’AddTwoNumbers’,
#         ’allcaps’:’ADD_TWO_NUMBERS’} }
# 
# 
#     - Example 2: Assume your input code is the multi-line string
#           def _major_split(*args):
#             return (args[:2], args[2:])
#           
#           
#           def CheckTruth(t = True):
#             print(’t is’, t)
#             return _major_split([t]*10)
#           
#           x, y = _major_split((10, 20, 30, 40, 50))
# 
# 
# 
#       CheckTruth(len(x) == 10)
# 
#       After processing it with your function, the code should be changed to
#           def _MajorSplit(*args):
#             return (args[:2], args[2:])
#           
#           def CheckTruth(t = True):
#             print(’t is’, t)
#             return _MajorSplit([t]*10)
#           x, y = _MajorSplit((10, 20, 30, 40, 50))
#           
#           CheckTruth(len(x) == 10)
#           
#           The nested dictionary is given by
#           
#           d = {’CheckTruth’:
#           {’hash’:-6410081306665365595,
#           ’camelcase’:’CheckTruth’,
#           ’allcaps’:’CHECKTRUTH’,
#           ’_major_split’:
#           {’hash’:484498917506710667,
#           ’camelcase’:’_MajorSplit’,
#           ’allcaps’:’_MAJOR_SPLIT’}}
# 
# 
# 
# Test code: The examples given above are the only test cases to be handled for this question.

# In[59]:


import re

def function_renamer(code):
    pattern = re.compile(r'def\s+([a-zA-Z_]\w*)\s*\(')

    fun=pattern.findall(code)
    g=str(fun).title()
    f=str(g).replace('_','')
    r=code.replace('add_two_numbers',str(f))
    print(r)
   
    #def camel_case(fun):
       
        
    #camel_case(fun) 
    pass


code = '''
def add_two_numbers(a, b):
      return a + b
      print(add_two_numbers(10, 20))'''
function_renamer(code)


# In[ ]:





# In[ ]:


code = '''
def add_two_numbers(a, b):
      return a + b
      print(add_two_numbers(10, 20))'''

c2 = '''
def _major_split(*args):
        return (args[:2], args[2:])
      
      
      def CheckTruth(t = True):
        print(’t is’, t)
        return _major_split([t]*10)
      
      x, y = _major_split((10, 20, 30, 40, 50))
'''


# ## Submit your solution
# 
# Once you are finish with the test, please make sure that you have renamed your solutions in the format given ahead ex. **python_test(pranav_uikey)** and submit it using this [following link](https://github.com/Ai-Adventures/Python_test_submissions)

# ## All The Best!!
