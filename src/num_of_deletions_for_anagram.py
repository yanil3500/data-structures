def num_of_deletions_for_anagrams(str1, str2):
    """Return the number of deletions needed to create an anagram from two strings."""
    chars_in_common = []
    # count1 = 0
    # count2 = 0
    # list_str1 = list(str1)
    # list_str2 = list(str2)
    #
    # for ch1 in list_str1:
    #     count1 += list_str2.count(ch1)
    #     count2 += list_str1.count(ch1)

    for ch1 in str1:
        for ch2 in str2:
            if ch1 == ch2 and ch1 not in chars_in_common:
                chars_in_common.append(ch1)

    return (len(str1) - len(chars_in_common)) + (len(str2) - len(chars_in_common))


print(num_of_deletions_for_anagrams('abcdef', 'qkje'))
print(num_of_deletions_for_anagrams('racecar', 'racerac'))