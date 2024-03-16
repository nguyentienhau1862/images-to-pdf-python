from math import sqrt

min_dif = 1
value = 0

for i in range(1394, 2378):
	temp = i*sqrt(2)
	dif = abs(round(temp) - temp)
	
	if dif < min_dif:
		min_dif = dif
		value = i

print(f"({value}, {round(value*sqrt(2))})", min_dif)
