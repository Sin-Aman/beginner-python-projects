#STRING CHALLENGES

# Write a function called unique_english_letters that takes the string word as a parameter. 
# The function should return the total number of unique letters in the string.
# Uppercase and lowercase letters should be counted as different letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  unique_letters = 0
  for letter in letters:
    if letter in word:
      unique_letters +=1
  return unique_letters


# test:
print(unique_english_letters("mississippi"))
#should print 4
print(unique_english_letters("Apple"))
# should print 4

#  ------------------------------------------------------------------------------------------------------------------------------------------------

# Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. 
# However, this time, make sure your function works when x is multiple characters long.

def count_multi_char_x(word, x):
  split = word.split(x)
  return(len(split)-1)
# test:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end.
# This function should return the substring between the first occurrence of start and end in word. 
# If start or end are not in word, the function should return word.


def substring_between_letters(word,start, end):
  st = word.find(start)
  en = word.find(end)
  if st>-1 and en>-1:
    return (word[st+1:en])
  return word
# test:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"