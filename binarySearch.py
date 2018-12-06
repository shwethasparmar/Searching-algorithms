import math
def binarySearch(a, key, low, high):
	if(low == high):
		if key == a[low]:
			print "Key %s is present in list " %(key)

		else:
			print "Key %s not present in list " %(key)
			
	if (low < high):
		midIndex = int(math.ceil(float((low+high)/2)))
		if key < a[midIndex]:
			binarySearch(a, key, low, midIndex-1)
		elif key > a[midIndex]: 
			binarySearch(a, key, midIndex+1, high)
		elif key == a[midIndex]:
			print "Key %s is present in list " %(key)
			


a = [10, 1, 2,4, 6, 3, 16, 20]
a.sort()
print a
key = 20
binarySearch(a, key, 0, len(a)-1)