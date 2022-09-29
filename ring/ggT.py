
def ggT(a, b):
	if a == 0:
		return b
	if b == 0:
		return a
	if a < 0:
		a = -a
	if b < 0:
		b = -b
		
	while a != 0:
		if b > a:
			a, b = b, a
		a = a % b
	return b


def gcd(a, b):
	return ggT(a, b)


def bezout(a, b):
	u, v, s, t = 1, 0, 0, 1
	while b != 0:
		q = a // b
		a, b = b, a - q * b
		u, s = s, u - q * s
		v, t = t, v - q * t
	return a, u, v  # ggT(a, b) = a * u + b * v
