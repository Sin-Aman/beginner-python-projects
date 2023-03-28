# DICTIONARY CHALLENGES

# Create a function named count_first_letter that takes a dictionary named names as a parameter. 
# names should be a dictionary where the key is a last name and the value is a list of first names.

def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

# test:
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

# -----------------------------------------------------------------------------------------------------------------------------

# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter.
# The function should return the number of unique values in the dictionary.
def unique_values(my_dictionary):
  list = []
  for value in my_dictionary.values():
    if value not in list:
      list.append(value)
  return len(list)
# test:
#print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
#print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# -----------------------------------------------------------------------------------------------------------------------------

# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. 
# The function should return a dictionary containing the frequency of each element in words.
def frequency_dictionary(words):
  dict = {}
  for word in words:
    if word not in dict:
      dict[word] = 0
    dict[word] += 1
  return dict
# test:
#print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# -----------------------------------------------------------------------------------------------------------------------------

# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
# The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

def word_length_dictionary(words):
  dict = {}
  for word in words:
    dict[word] = len(word)
  return dict
# test:
#print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
#print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}