def isPalindrome(s):
	s1 = s.replace(' ', '')
	s1 = s1.lower()
	s2 = s1[::-1];
	return True if s1 == s2 else False
s = input("string is:")
if (isPalindrome(s)):
	print ("true.")
else:
	print ("false.")
