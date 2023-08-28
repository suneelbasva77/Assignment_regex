#!/usr/bin/env python
# coding: utf-8

# # WORK SHEET ON REGULAR EXPRESSIONS
Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.

Sample Text- 'Python Exercises, PHP exercises.'

Expected Output: Python:Exercises::PHP:exercises:

# In[1]:


import re
text='Python Exercises, PHP exercises.'
pattern=re.sub(r'\W',':',text)


# In[2]:


pattern

Question 2-  Write a Python program to find all words starting with 'a' or 'e' in a given string.
# In[3]:


string='Data science is the study of data to extract meaningful insights for business.'
pattern=re.findall('[ae]\w+',string)


# In[4]:


pattern

Question 3- Create a function in python to find all words that are at least 4 characters long in a string. 

The use of the re.compile() method is mandatory.
# In[5]:


sample_string='Data science is the study of data to extract meaningful insights for business.'
string_pattern= r"\w{4,}"
regex_pattern=re.compile(string_pattern)
result=regex_pattern.findall(sample_string)
result

Question 4- Create a function in python to find all three, four, and five character words in a string. 

The use of the re.compile() method is mandatory.
# In[7]:


sample_string='Data science is the study of data to extract meaningful insights for business.'
string_pattern= r"\w{3,5}"
regex_pattern=re.compile(string_pattern)
result=regex_pattern.findall(sample_string)
result

Question 5- Create a function in Python to remove the parenthesis in a list of strings.

The use of the re.compile() method is mandatory.

Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

Expected Output:
example.com
hr@fliprobo.com
github.com
Hello Data Science World
Data Scientist

# In[4]:


import re
sample_text= ["example(.com)", "hr@fliprobo(.com)", "github(.com)", "Hello (Data Science World)", "Data (Scientist)"]
string_pattern=r"[()]"
r_p=re.compile(string_pattern)
for i in sample_text: 
    result= r_p.sub('',i)
    print(result)


Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.

Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]

Note- Store given sample text in the text file and then to remove the parenthesis area from the text.

# In[19]:


with open("sample.txt") as file:
    for text in file:
        result=re.sub(r" ?\([^)]+\)", "",text)
        print(result)
        

Question 7- Write a regular expression in Python to split a string into uppercase letters.

Sample text: “ImportanceOfRegularExpressionsInPython”

Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

# In[7]:


import re
text= "ImportanceOfRegularExpressionsInPython"
result=re.findall('[A-Z][^A-Z]*', text)
result

Question 8- Create a function in python to insert spaces between words starting with numbers.

Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"

Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

# In[9]:


import re
def space_before_numbers(str1):
  return re.sub(r"(\w)([0-9])", r"\1 \2", str1)
print(space_before_numbers("RegularExpression1IsAn2ImportantTopic3InPython"))

Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.

Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"

Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

# In[2]:


import re
def space_before_capital_letters(string):
  return re.sub(r"(\w)([A-Z]|[0-9])", r"\1 \2", string)
print(space_before_capital_letters("RegularExpression1IsAn2ImportantTopic3InPython"))

Question 10- Write a python program to extract email address from the text stored in the text file using Regular Expression.

Sample Text- Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. 
Please contact us at hr@fliprobo.com for further information. 

Expected Output: 
['xyz@domain.com', 'xyz.abc@sdomain.domain.com']
['hr@fliprobo.com']
# In[5]:


import re
with open("for_email.txt") as file:
    for text in file:
        result=re.findall(r"\S+@\S+",text)
        print(result)

Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# In[53]:


import re
sub='Data Science Is The Study Of Data9 To9 Extract8 Meaningful6 Insights_ For_9 Business4.'
pattern=re.match("^[A-Za-z0-9_-]*$",sub)
sub

Question 12- Write a Python program where a string will start with a specific number. 
# In[18]:


import re
def match_num(string):
    text = re.compile(r"^9")
    if text.match(string):
        return True
    else:
        return False
print(match_num('98858'))
print(match_num('7775'))

Question 13- Write a Python program to remove leading zeros from an IP address
# In[5]:


import re
ip=input('ip_adress:')
pattern=re.sub(r'[0]+','',ip)
pattern

Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
Expected Output- August 15th 1947
Note- Store given sample text in the text file and then extract the date string asked format.


# In[57]:


with open("date.txt") as date:
    for sub in date:
        pattern=re.findall(r"[A-Za-z]+\s\w+\s\d{4}", sub)
        print(pattern) 

Question 15- Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'
Question 17- Write a Python program to find the substrings within a string.
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'.

# In[16]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print("%s" % match)

Question 18- Write a Python program to find the occurrence and position of the substrings within a string.
# In[18]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('"%s" at %d:%d' % (text[s:e], s, e))


Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[21]:


import re
def date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
date = "2023-08-20"
print("Actual date Format:YYYY-MM-DD: ",date)
print("Converted date Format:DD-MM-YYYY: ",date_format(date))

Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. 
The use of the re.compile() method is mandatory.
Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']

# In[48]:


Sample_Text=["01.12, 0132.123, 2.31875, 145.8, 3.01, 27.25, 0.25"]
result = re.search(r"^[0-9]+(\.[0-9]{1,2})?$",Sample_Text)
print(result)
    

Question 21- Write a Python program to separate and print the numbers and their position of a given string.
# In[ ]:


import re
text=input('enter the text :')

for i in re.finditer('\d+',text):
    print(i.group())
    print('Index position:', i.start())

Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
Expected Output: 950

# In[5]:


text='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
pattern=re.findall('\d+',text)
print(max(pattern))

Question 23- Create a function in python to insert spaces between words starting with capital letters.
Sample Text: “RegularExpressionIsAnImportantTopicInPython"
Expected Output: Regular Expression Is An Important Topic In Python

# In[6]:


def space_before_numbers(str1):
    return re.sub(r'(\w)([A-Z])',r'\1 \2',str1)

print(space_before_numbers('Regular Expression Is An Important Topic In Python'))

Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[8]:


text = ' Sachin scored 100 centuries'
pattern= '[A-Z]+[a-z]+'
regex=re.findall(pattern,text)
print(regex)

Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
Sample Text: "Hello hello world world"
Expected Output: Hello hello world

# In[10]:


text= "Hello hello world world"
pattern= r'\b(\w+)(?:\W+\1\b)+'
r=re.sub(pattern,r'\1',text)
print(r)


# In[ ]:


Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.


# In[11]:


import re
regex_exp = '[A-Za-z0-9]$'

def check_str(my_string):
    
    if re.findall(regex_exp,my_string):
        print("The string ends with alphanumeric character")
        
    else:
        print("The string doesnot end with alphanumeric character")
        
my_string_1='Datascience23'
print("the string is:")
print(my_string_1)
check_str(my_string_1)
my_string_2='Datascience@'
print("\nthe string is:")
print(my_string_2)
check_str(my_string_2)

Question 27-Write a python program using RegEx to extract the hashtags.
Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

# In[12]:


text="""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetizati
on as the same has rendered 
USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
pattern=re.findall(r"#\w+", text)
print(pattern)

Question 28- Write a python program using RegEx to remove <U+..> like symbols
Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

# In[14]:


with open("dateformat.txt") as file:
    for text in file:
        result=re.findall('\d{2}[/-]\d{2}[/-]\d{4}',text)
        print(result)


# Question 29- Write a python program to extract dates from the text stored in the text file.
# 
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# 
#     Note- Store this sample text in the file and then extract dates.
# 

# In[13]:


import re
text= "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
pattern='\d{2}[\-]\d{2}[\-]\d{4}'
dates= re.findall(pattern,text)
print(dates)

Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
The use of the re.compile() method is mandatory.
Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

# In[16]:


regex_exp = re.compile(r'\W*\b\w{2,4}\b')
def remove_words(str1):
  return re.sub(regex_exp,"", str1)

print(remove_words("The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."))

