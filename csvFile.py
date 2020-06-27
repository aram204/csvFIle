import csv
import sys


if sys.argv[1] == 'start':
    with open('test.csv','w') as f:
        writer = csv.writer(f)
        for i in range(1,1001):
            writer.writerow([i,i**2,i**3,i**4,i**5])


if sys.argv[1] == 'run':
    with open('test.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for coupleNum in row:
                if int(coupleNum)%2==0:
                    print(coupleNum,end=" , ")





