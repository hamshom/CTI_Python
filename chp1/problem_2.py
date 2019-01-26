'''
Chapter 01 - Problem 02 - Check Permutation - CTCI 6th Edition page 90
Problem Statement:
Given two strings, write a method to decide if one is a permutation of the
other.
Example:
("alex", "lexa") -> True

'''


def permutation_check(s1, s2):

    s1_dc = dict()

    for character in s1:
        if character in s1_dc:
            s1_dc[character] += 1
        else:
            s1_dc[character]  = 1

    for character in s2:
        if character in s1_dc:
            s1_dc[character] -= 1
            if s1_dc[character] < 0:
                return False
        else:
            return False

    if sum(s1_dc.values()) == 0:
        return True
    else:
        return False

print(permutation_check('aleaa', 'elxaa'))
