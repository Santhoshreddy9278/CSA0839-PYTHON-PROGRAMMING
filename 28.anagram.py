from collections import defaultdict
# initializing list
test_list = ["eat","tea","tan","ate","hat","bat"]

# printing original list
print("The original list : " + str(test_list))

# using defaultdict() + sorted() + values()
# Grouping Anagrams
temp = defaultdict(list)
for ele in test_list:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())

# print result
print("The grouped Anagrams : " + str(res))
