Python 3.8.6rc1 (tags/v3.8.6rc1:08bd63d, Sep  7 2020, 23:10:23) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Python is a popular programming language. It was created by Guido van Rossum, and released in 1991"
>>> #index search
>>> text[2]
't'
>>> text[0:7] #[index:position]
'Python '
>>> text[-1] #searching from last
'1'
>>> text[0:15:2] #[index:position:step(skip)]
'Pto sapp'
>>> len(text) #length of string
98
>>> text[0:] #read till last
'Python is a popular programming language. It was created by Guido van Rossum, and released in 1991'
>>> text[0:-1]
'Python is a popular programming language. It was created by Guido van Rossum, and released in 199'
>>> text[10:1:-1] #reverse order
'a si noht'
>>> text[14::-1]
'pop a si nohtyP'
>>> text[-1:-10] #wrong method
''
>>> text[-1:-10:-1] #reverse
'1991 ni d'
>>> text.lower() #converts to lower text
'python is a popular programming language. it was created by guido van rossum, and released in 1991'
>>> text.upper()
'PYTHON IS A POPULAR PROGRAMMING LANGUAGE. IT WAS CREATED BY GUIDO VAN ROSSUM, AND RELEASED IN 1991'
>>> text.capitalize() #first word capital
'Python is a popular programming language. it was created by guido van rossum, and released in 1991'
>>> text.title() #first letter of each word capital
'Python Is A Popular Programming Language. It Was Created By Guido Van Rossum, And Released In 1991'
>>> text.split() #list of strings in sentence
['Python', 'is', 'a', 'popular', 'programming', 'language.', 'It', 'was', 'created', 'by', 'Guido', 'van', 'Rossum,', 'and', 'released', 'in', '1991']
>>> text.count('t') #count of alphabet t in text
3
>>> text.find('s') #first time alphabet s appears on which index
8
>>> text.find('p',5) #search will start from 5th index
12
>>> text.endswith('y') #checks whether text ends with letter y
False
>>> text.split()[0] #1st word in text
'Python'
>>> text.split()[0].endswith('n') #checks whether 1st word ends with letter n or not
True
>>> text.startswith('pop') #checks whether text starts with particular string
False
>>> text.isalpha() #checks whether text contains only alphabets(not even spaces) or not
False
>>> dir(str) #string directory
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.replace('python','c') #replaces a part of string with another
'Python is a popular programming language. It was created by Guido van Rossum, and released in 1991'
>>> text.replace('Python','C')
'C is a popular programming language. It was created by Guido van Rossum, and released in 1991'
>>> text.splitlines() #list of lines
['Python is a popular programming language. It was created by Guido van Rossum, and released in 1991']
>>> text.swapcase() #upper case to lower case and vice versa
'pYTHON IS A POPULAR PROGRAMMING LANGUAGE. iT WAS CREATED BY gUIDO VAN rOSSUM, AND RELEASED IN 1991'
>>> text.strip() #removes spaces
'Python is a popular programming language. It was created by Guido van Rossum, and released in 1991'
>>> text.strip('popular') #removes mentioned string from text
'Python is a popular programming language. It was created by Guido van Rossum, and released in 1991'
>>> text.strip('lan')
'Python is a popular programming language. It was created by Guido van Rossum, and released in 1991'
>>> text.strip('Py')
'thon is a popular programming language. It was created by Guido van Rossum, and released in 1991'
>>> #strip removes only from starting
>>> s = ('good','morning')
>>> d = '-'.join(s)
>>> d
'good-morning'
>>> 