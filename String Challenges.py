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
#print(unique_english_letters("mississippi"))
#should print 4
#print(unique_english_letters("Apple"))
# should print 4

#  ------------------------------------------------------------------------------------------------------------------------------------------------

# Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. 
# However, this time, make sure your function works when x is multiple characters long.

def count_multi_char_x(word, x):
  split = word.split(x)
  return(len(split)-1)
# test:
#print(count_multi_char_x("mississippi", "iss"))
# should print 2
#print(count_multi_char_x("apple", "pp"))
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

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Write a function called check_for_name that takes two strings as parameters named sentence and name. 
# The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. 
# The function should return False otherwise.

def check_for_name(sentence,name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False
# test:
#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Create a function named every_other_letter that takes a string named word as a parameter. 
# The function should return a string containing every other letter in word.

def every_other_letter(word):
  return word[::2]

# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 

# -------------------------------------------------------------------------------------------------------------------------------------------------

# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. 
# Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. 
# Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
  return word2[:1]+word1[1:] + " " +word1[:1]+word2[1:]
# Uncomment these function calls to test your function:
#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a

# -------------------------------------------------------------------------------------------------------------------------------------------------

#Create a function named add_exclamation that has one parameter named word. 
#This function should add exclamation points to the end of word until word is 20 characters long. 
#If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  while len(word) < 20:
     word += "!"
  return word
  
# Uncomment these function calls to test your function:
#print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
#print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
