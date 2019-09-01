# A Simple Python Lib For Finding Central Tendencies of Sequences...
# Author : Atharva Kale



def asort(sequence):
	"""
	- sort the sequence in ascending order
	- params
		- sequence:list/tuple -> the sequence to be sorted
	- returns
		- insq:list -> the sequence sorted in ascending order
	"""
	n = len(sequence)
	insq = []
	for sq in sequence:
		insq.append(sq)

	for i in range(n):
		for j in range(0, n-i-1):
			if insq[j] > insq[j + 1]:
				insq[j], insq[j + 1] = insq[j + 1], insq[j]

	return insq


def dsort(sequence):
	"""
	- sort the sequence in ascending order
	- params
		- sequence:list/tuple > the sequence to be sorted
	- returns
		- insq:list > the sequence sorted in ascending order
	"""
	n = len(sequence)
	insq = []
	for sq in sequence:
		insq.append(sq)

	for x in range(n, 0, -1):
		for j in range(0, n-i-1):
			if insq[j] > insq[j + 1]:
				insq[j], insq[j + 1] = insq[j + 1], insq[j]

	return insq


def smax(sequence):
	"""
	- get maximum number from the `sequence`
	
	- params
		- sequence:list/tuple -> the sequence
	
	- returns
		- mx:int/float -> the maximum number
	"""
	mx = sequence[0]
	for n in sequence:
		if n > mx:
			mx = n

	return mx


def smin(sequence):
	"""
	- get minimum number from the `sequence`
	
	- params
		- sequence:list/tuple -> the sequence
	
	- returns
		- mn:int/float -> the minimum number
	"""
	mn = sequence[0]
	for n in sequence:
		if n < mn:
			mn = n

	return mn


def mean(sequence):
	"""
	- get the arithmetic mean of the given `sequence`
	
	- params
		- sequence:list/tuple -> the sequence to find mean
	
	- returns
		- mn:int/float -> the mean
	"""
	n = len(sequence)
	sm = 0
	for num in sequence:
		sm += num

	mn = sm / n

	return mn


def median(sequence):
	"""
	- get the median of the `sequence`
	
	- params
		- sequence:list/tuple -> the sequence to find the median of
	
	- returns
		- mdn:float -> the median
	"""
	d = asort(sequence)
	n = len(d)

	if n % 2 == 0:
		nx = n // 2
		mdn = (d[nx - 1] + d[nx]) / 2
		return mdn
	else:
		nx = n // 2
		mdn = d[nx]
		return mdn


def mode(sequence):
	"""
	- get the mode of the `sequence`
	
	- params
		- sequence:list/tuple -> the sequence to find the mean of
	
	- returns
		- mox:tuple -> the tuple of mode number(s)
	"""
	st = list(set(sequence))
	ln = len(st)
	dst = dict()
	for s in st:
		dst[s] = 0

	kx = dst.keys()
	vx = dst.values()

	for ky in kx:
		for sq in sequence:
			if sq == ky:
				dst[ky] += 1
	
	kx = list(kx)
	vx = list(vx)
	mox = tuple([k for k, v in dst.items() if v == smax(vx)])
	
	return mox


if __name__ == "__main__":
	pass

