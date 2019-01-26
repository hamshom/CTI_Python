"""
Chapter 01 - Problem 01 - Is Unique - CTCI 6th Edition page 90
Problem Statement:
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
Example:
"aalex" -> False
Solution:
Assume that the input string will contain only ASCII characters. Traverse the
string one character at a time and use a hash table to record which characters
have been observed. If a character is observed more than once, return False.
If no character is observed more than once, return True. Because we assumed that
the string would contain only ASCII characters, we can implement the hash table as
a 128-wide bit vector that uses a character's ASCII value as its hash code.
Time complexity: O(N) where N is the length of the of the linearly traversed string.
Space complexity: O(1) because bit vector size does not scale with input string length.
Follow-up discussion (unimplemented):
If we cannot use additional structures, we can do O(N^2) character comparisons
to check for uniqueness. If we are allowed to modify the original string, we
could sort it in place in N*log(N) time and test consecutive characters for equality.
"""


def unique(s1):

    dc = dict()
    for character in s1:
        if character in dc:
            dc[character] += 1
        else:
            dc[character]  = 1
        if dc[character] > 1:
            return False
        else:
            pass

    return True



if __name__ == '__main__':

    print('Example of having duplicate characters: abcdeghhsas')
    print(unique('abcdeghhsas'))

    print('Example of having no duplicate characters: abcdefg')
    print(unique('abcdefg'))