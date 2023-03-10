
# A function to Write pigletLatin(s), which accepts an argument that is a string s. s will be a single word consisting of lowercase letters.
#Then, pigletLatin should return the translation of s to "piglet latin," which has these rules:
#If the argument has no letters at all (the empty string), your function should return the empty string
#If the argument begins with a vowel, the piglet latin result simply appends the string 'way' at the end. 'y' will be considered a consonant, and not a vowel, for this problem.
#Example: pigletLatin('one') returns 'oneway'
#If the argument begins with a consonant, the piglet latin result is identical to the argument, except that the argument's initial consonant is at the end of the word instead of the beginning and it's followed by the string 'ay'.
#Example: pigletLatin('be') returns 'ebay'
def pigletLatin(s):
  if s=='':
    return ''
  elif s[0] in 'aeiou':
    return s + 'way'
  else:
    return s[1:] + s[0] + 'ay'


print( "pigletLatin('one')   should be 'oneway' :",  pigletLatin('one'))
assert pigletLatin('be') == "ebay"


# The full challenge is to create a function called pigLatin(s) that handles the rules above and handles more than one initial consonant correctly in the translation to pig Latin.
# That is, pigLatin moves all of the initial consonants to the end of the word before adding 'ay'. (You will want to write and use a helper function to do this—see the hint below.)
# Also, pigLatin should handle an initial 'y' either as a consonant OR as a vowel, depending on whether the y is followed by a vowel or consonant, respectively:
# If an initial 'y' is followed by a vowel ('yes', 'yodel'), then the 'y' is considered a consonant.
# If an initial 'y' is followed by a consonant ('yttrium', element #39), then the 'y' is considered a vowel.
# That is, 'yes' has an initial y acting as a consonant. The word 'yttrium', however, (element #39) has an initial y acting as a vowel. (Admittedly, there aren't many 'y'-as-vowel instances: ylem, ytterbium, element #70, and Yggdrasil, a mythic tree.)

def pigLatin(s):
  vowels = "aeiouy"
  if not s:
      return ""
  elif s[0].lower() in vowels:
        return s + "way"
  else:
    for i in range(len(s)):
        if s[i].lower() in vowels:
            if s[i-1].lower() == "y":
                return s[i:] + s[:i-1] + "ay"
            else:
                return s[i:] + s[:i] + "ay"