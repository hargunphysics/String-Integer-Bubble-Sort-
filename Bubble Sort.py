# The Checking algorithm

def check(nalist, reverse = False):
	no = False
	yes = False
	issorted = False
	c = -1
	alp = [' ','0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	#Empty or single value lists
	if len(nalist) == 0 or len(nalist) == 1:
				issorted = True
				return issorted

		#Normal checking
	
	if reverse == False:
		#Integers
		if type(nalist[0]) == int:
			for i in nalist:
				c +=1
				if nalist[c] < nalist[c-1] and c != 0:
					no = True
				if c == len(nalist) - 1:
					c = -1
				if nalist[c] >= nalist[c-1] and c != 0:
					yes = True
			if yes and (no==False):
				issorted = True
			return issorted
		#Strings
		if type(nalist[0]) == str:
			for i in nalist:
				c +=1
				cur = nalist[c]
				prev = nalist[c-1]
				r = 0
				q = r
				notdone = True
				while notdone and c!= 0:
					if prev == cur:
						yes = True
						notdone = False
					try:
						if alp.index(cur[r]) < alp.index(prev[q]):
							no = True
							notdone = False
						if alp.index(cur[r]) > alp.index(prev[q]):
							yes = True
							notdone = False
						if cur[r] == prev[q] and notdone:
							same = True
							while same:
								r += 1
								q = r
								if r == len(cur) or q == len(prev):
									if len(cur) < len(prev):
										no = True
										notdone = False
										same = False
										break
									if len(cur) >= len(prev):
										yes = True
										notdone = False
										same = False
										break
								if alp.index(cur[r]) > alp.index(prev[q]):
									same = False
									yes = True
									notdone = False
								if alp.index(cur[r]) < alp.index(prev[q]):
									same = False
									no = True
									notdone = False
						if notdone:
							if len(cur) < len(prev):
								no = True
								notdone = False
							if len(cur) >= len(prev):
								yes = True
								notdone = False
					except IndexError:
						if len(prev) == 0 or len(cur) == 0:
							if len(prev) <= len(cur):
								yes = True
								notdone = False
							else:
								no = True
								notdone = False
				if c == len(nalist) - 1:
						c = -1
			if yes and (no==False):
				issorted = True
			return issorted

		#Reversed checking

	if reverse:
		#Integers,Reversed
		if type(nalist[0]) == int:
			for i in nalist:
				c +=1
				if nalist[c] > nalist[c-1] and c != 0:
					no = True
				if c == len(nalist) - 1:
					c = -1
				if nalist[c] <= nalist[c-1] and c != 0:
					yes = True
			if yes and (no==False):
				issorted = True
			return issorted
		#Strings,Reversed
		if type(nalist[0]) == str:
			for i in nalist:
				c +=1
				cur = nalist[c]
				prev = nalist[c-1]
				r = 0
				q = r
				notdone = True
				while notdone and c!= 0:
					if prev == cur:
						yes = True
						notdone = False
					try:
						if alp.index(cur[r]) > alp.index(prev[q]) and c != 0:
							no = True
							notdone = False
						if alp.index(cur[r]) < alp.index(prev[q]) and c != 0:
							yes = True
							notdone = False
						if cur[r] == prev[q] and notdone:
							same = True
							while same:
								r += 1
								q = r
								if r == len(cur) or q == len(prev):
									if len(cur) > len(prev):
										no = True
										notdone = False
										same = False
										break
									if len(cur) <= len(prev):
										yes = True
										notdone = False
										same = False
										break
									
								if alp.index(cur[r]) < alp.index(prev[q]):
									same = False
									yes = True
									notdone = False
								if alp.index(cur[r]) > alp.index(prev[q]):
									same = False
									no = True
									notdone = False
						if notdone:
							if len(cur) > len(prev) and c != 0:
								no = True
								notdone = False
							if len(cur) <= len(prev) and c != 0:
								yes = True
								notdone = False
					except IndexError:
						if len(prev) == 0 or len(cur) == 0:
							if len(prev) >= len(cur):
								yes = True
								notdone = False
							else:
								no = True
								notdone = False
				if c == len(nalist) - 1:
						c = -1
			if yes and (no==False):
				issorted = True
			return issorted
			

# The Sorting Algorithm (Bubble Sort)


def sort(nalist,reverse = False):
	l = len(nalist)
	notsort = True
	
	if l == 0:
		return nalist
		
		#Normal sorting
		
	if reverse == False:
		#For integers
		if type(nalist[0]) == int:
				c = -1
				while notsort:
					for i in nalist:
						c += 1
						if i < nalist[c-1] and c-1 != -1:
							num = nalist[c-1]
							nalist[c-1] = nalist[c]
							nalist[c] = num
						if c == l-1 :
							c = -1
						if check(nalist):
							notsort = False
		#For strings
		if type(nalist[0]) == str:
				c = -1
				r = 0
				q = r
				while notsort:
					for i in nalist:
						c += 1
						cur = nalist[c]
						prev = nalist[c-1]
						temp = [prev,cur]
						if check(temp) == False and c-1 != -1:
							word = nalist[c-1]
							nalist[c-1] = nalist[c]
							nalist[c] = word
						if c == l-1 :
							c = -1
						if check(nalist) == True:
								notsort = False
		return nalist
		
		#Reversed sorting
		
	elif reverse :
		#For integers, reversed
		if type(nalist[0]) == int:
				c = -1
				while notsort:
					for i in nalist:
						c += 1
						if i > nalist[c-1] and c-1 != -1:
							num = nalist[c-1]
							nalist[c-1] = nalist[c]
							nalist[c] = num
						if c == l-1 :
							c = -1
						if check(nalist, reverse = True):
							notsort = False
				return nalist
		#For strings, reversed
		if type(nalist[0]) == str:
				c = -1
				while notsort:
					for i in nalist:
						c += 1
						cur = nalist[c]
						prev = nalist[c-1]
						temp = [prev,cur]
						if c-1 != -1:
							if check(temp,reverse = True) == False:
								word = nalist[c-1]
								nalist[c-1] = nalist[c]
								nalist[c] = word
							if c == l-1 :
								c = -1
						if check(nalist,reverse = True):
							notsort = False
		return nalist

# Sample lists to prove the workings of the function.

tests = [
    ["banana", "apple", "cherry", "apricot"],
    ["apple", "Banana", "APPLE", "banana"],
    ["0",'0',"1", "2", "100"],
    [" apple", "apple", "apple ", "", "  "],
    ["a", "aaa", "aa", "aaaa"],
    ["testing", "test", "tester", "testers"],
    ["a", "b", "a"],
    ["apple", "banana", "apple"],
    ["same", "same", "same"],
    [42, -5, 0, 100, -20, 5]
]

# This part tests if the results for using sort() on each list are the same as using the inbuilt sorted() function:

test_results = [sort(t.copy()) == sorted(t) for t in tests]
print(test_results)

# Output should be [True, True, True, True, True, True, True, True, True, True]
