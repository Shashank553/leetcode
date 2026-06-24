class Solution(object):
    def reverseWords(self, s):
        '''How it works
s.split() → splits the string into words and automatically removes extra spaces.
[::-1] → reverses the list of words.
" ".join(...) → joins the words back together with a single space.
        '''
        return " ".join(s.split()[::-1])