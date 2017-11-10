# https://stackoverflow.com/questions/931092/reverse-a-string-in-python
str1='shakti'
strrev=str1[::-1]
print(strrev)
print(''.join(reversed(str1)))

def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1                       
        new_strings.append(a_string[index])
    return ''.join(new_strings)
print(reverse_a_string_more_slowly('cat'))
