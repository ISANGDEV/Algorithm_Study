n = int(input())

serial_info = {}
serials = []

for _ in range(n):
    serial = input()
    num_sum = 0
    for i in serial:
        try:
            num_sum += int(i)
        except:
            continue
    serial_info[serial] = (len(serial), int(num_sum))
    serials.append(serial)

serials.sort()
serials.sort(key=lambda x: serial_info[x][1])
serials.sort(key=lambda x: serial_info[x][0])

for serial in serials:
    print(serial)
