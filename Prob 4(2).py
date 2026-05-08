# def is_anagram(s1, s2): 
#     s1 = s1.lower() 
#     s2 = s2.lower() 
#     return letter_counts(s1) == letter_counts(s2)

# def letter_counts(s): 
#     counts = {}
#     for letter in s: 
#         if letter.isalpha(): 
#             counts[letter] = s.count(letter) 
#     return counts

# ## This is another way of doing it
# def is_anagram_v2(s1, s2): 
#     s1 = [s.lower() for s in s1 if s.isalpha()] 
#     s2 = [s.lower() for s in s2 if s.isalpha()] 
#     return sorted(s1) == sorted(s2)

def is_anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    first = list(text1)
    second = list(text2)
    first_alpha = []
    second_alpha = []
    for char in first:
        if char.isalpha():
            first_alpha.append(char)
    for char in second:
        if char.isalpha():
            second_alpha.append(char)
    
    first_alpha.sort()
    print(first_alpha) ## Sorts the letters in order
    second_alpha.sort()
    print(second_alpha)
    return first_alpha == second_alpha        

if __name__ == "__main__":
    print(is_anagram("the", "het"))
