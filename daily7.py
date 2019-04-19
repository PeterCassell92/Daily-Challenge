"""Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed."""

import unittest

class TestOutput(unittest.TestCase):
	@unittest.skip("practicing skip")
	def testskip():
		print("Nothing to see here")

	def testnumpossibles(message1):
		self.assertEqual(numpossibles(message1), 3, "unittest says it should be 3")


def numpossibles(message):

	
	#this function creates a list of tuples that represents the how many digits can be legally decoded from each the index position of each character in the string.
	def getpossiblejumps(message):
		possiblejumps = []
		alphabetindex = range(1,27)
		alphabetindex = [str(i) for i in alphabetindex]

		a =0
		while a < len(message):
			singlejump = False
			doublejump = False
			if message[a] != '0':
				singlejump = True

			if a+1 <len(message):
				twodigits = str(message[a] + message [a+1])
				if twodigits in alphabetindex:
					doublejump = True
			possiblejumps.append((singlejump,doublejump))
			a += 1
		print(possiblejumps)
		return possiblejumps

	possiblejumps = getpossiblejumps(message)

	def jump(messagelength, index , numcompletedpaths):
		k = index
		x = numcompletedpaths
		if possiblejumps[k][0] == True:
			if k+1 == messagelength: #jump path is complete
				x +=1
			else:
				x = jump(messagelength, k +1 , x)
		if possiblejumps[k][1] == True and k < messagelength-1:
			if k+2 == messagelength: #jump path is complete
				x +=1
			else:
				x= jump(messagelength, k+2, x)
		return x
	
	x= jump(len(message), 0, 0)
	return x

if __name__ == '__main__':
	message1 = "111"
	message2 = "2232"
	message3 = "21312"
	message4 = "2010213262110"
	message5 = "1111111"
	message6 = "11111111"
	#assert numpossibles(message1) == 3, "should be 3"
	#unittest.main()
	print(numpossibles(message1))
	print(numpossibles(message2))
	print(numpossibles(message3))
	print(numpossibles(message4))
	print(numpossibles(message5))
	print(numpossibles(message6))