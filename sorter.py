import math
import threading
import time
import datetime

sortedlist = list()
nums = dict()

def sleeper(duration):
	while(Sorter.start == 0):
		time.sleep(0.05)
	time.sleep(duration)
	sortedlist.append(nums[duration])
	print(duration)

def insertionsort(array):
	for i in range(1, len(array)):
		key = array[i]
		j = i - 1

		#if the key is smaller than current j
		while j>= 0 and key < array[j]:
			#swap
			array[j+1] = array[j]
			j = j - 1

		#leave key 
		array[j+1] = key
	return array


class Sorter():
	start = 0

	def sortlinear(self, array):
		#apply log to length of array
		for i in range(len(array)):
			scaled = array[i] * 0.0135
			nums[scaled] = array[i]

		for i in nums:
			t = threading.Thread(target=sleeper, args=(i,))
			t.start()


		Sorter.start = 1

	def sortlog(self, array):
		#apply log to length of array
		for i in range(len(array)):
			scaled = math.log10(array[i])
			nums[scaled] = array[i]

		for i in nums:
			t = threading.Thread(target=sleeper, args=(i,))
			t.start()


		Sorter.start = 1


if __name__ == '__main__':
	sorter = Sorter()
	array = list()
	for i in range(256):
		if(i != 0):
			array.append(i)		
	print('sorting ...' + str(datetime.datetime.now()))
	sorter.sortlinear(array)	
	while(threading.activeCount() > 1):
		time.sleep(0.05)
	print(sortedlist)
	print('done sleepsort: ' + str(datetime.datetime.now()) )


	print(insertionsort(sortedlist))
	print('done insertionsort: ' + str(datetime.datetime.now()))

