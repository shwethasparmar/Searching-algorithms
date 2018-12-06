def linearSearch(a, key):
	for i in range(len(a)):
		if a[i] == key:
			return True

	return False

a = [10, 9, 8, 1, 2, 5, 6, 9]
key = 9999
if(linearSearch(a, key)):
	print "Key %s exists in the list " %(key)
else:
	print "Key %s does not exist in the list " %(key)
