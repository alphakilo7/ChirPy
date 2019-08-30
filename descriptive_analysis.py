# Project 'Pyke' - (Spear)
# Project 'ChirPy' - (Cheerful and lively)
# Project 'Pyro' - (Fire)
# 

def sort(sequence):
	n = len(sequence)
	insq = []
	for sq in sequence:
		insq.append(sq)

	for i in range(n):
		for j in range(0, n-i-1):
			if insq[j] > insq[j + 1]:
				insq[j], insq[j + 1] = insq[j + 1], insq[j]

	return insq


def smax(sequence):
	mx = sequence[0]
	for n in sequence:
		if n > mx:
			mx = n

	return mx


def smin(sequence):
	mn = sequence[0]
	for n in sequence:
		if n < mn:
			mn = n

	return mn


def mean(sequence):
	n = len(sequence)
	sm = 0
	for num in sequence:
		sm += num

	mn = sm / n

	return mn


def median(sequence):
	d = sort(sequence)
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
	# print(mox)
	# print(kx)
	# print(vx)
	# print(sequence)
	# print(st)
	# print(dst)


if __name__ == "__main__":
	seq = [1, 4, 2, 6, 3, 2, 1, 4, 1, 1, 4, 4]
	sq = [1, 2, 3, 4, 5, 6]
	print(mode(seq))
