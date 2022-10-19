def common_words_filter(my_string_1, my_string_2):
   
   my_word_count = {}

   for word in my_string_1.split():
      my_word_count[word] = my_word_count.get(word, 0) + 1

   for word in my_string_2.split():
      my_word_count[word] = my_word_count.get(word, 0) + 1

   return [word for word in my_word_count if my_word_count[word] == 1]

my_string_1 = "Python is fun"
print("The first string is :")
print(my_string_1)

my_string_2 = "Python is fun to learn"
print("The second string is :")
print(my_string_2)

print("The result is :")
print(common_words_filter(my_string_1, my_string_2))
