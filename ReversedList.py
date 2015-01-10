def reverse_list (list):
	"""
	:param: list
	:return: list
	Return a list, whose elements are in reversed order
	e.g. reverse_list([30,40,50]) returns [50,40,30]
	"""
	reversed=[]
	#Copy the first element of the given list into empty reversed list: reversed list is now [30]
	reversed.append(list[0])
	#Insert second element 40 into reversed list at index 0, so the list now is [40,30] etc.
	for i in list[1:]:
		reversed.insert(0,i)
	return reversed
