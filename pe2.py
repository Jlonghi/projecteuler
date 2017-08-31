sum = 0
prev = 1
current = 1
next = 2
while True:
    if(current > 4000000):
        break
    if current % 2 == 0:
        sum += current
    prev = current
    current = next
    next = current + prev
print(("final sum: %d") %(sum))