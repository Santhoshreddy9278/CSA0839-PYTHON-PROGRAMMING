# Python3 implementation of the above approach

# function to check palindrome
def checkPalindrome(str):

	# Run loop from 0 to len/2
	for i in range(0, len(str)//2):
		if str[i] != str[len(str)-i-1]:
			return False
		
	# If the above loop doesn't
	#return then it is palindrome
	return True


# Driver code
st = "112233445566778899000000998877665544332211"
if(checkPalindrome(st) == True):
	print("it is a palindrome")
else:
	print("It is not a palindrome")
