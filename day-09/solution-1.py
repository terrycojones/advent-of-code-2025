from lib import read_data

data = read_data()

max_area = 0

for i in range(len(data)):
    pi = data[i]
    for j in range(i, len(data)):
        pj = data[j]
        area = (abs(pi[0] - pj[0]) + 1) * (abs(pi[1] - pj[1]) + 1)
        if area > max_area:
            max_area = area
            

print(max_area)
