import csv
import random
listings = []
data = open('edinburgh_listings.csv', encoding='utf-8')
listing = csv.reader(data, delimiter=",")
for line in listing:
    listings.append(line)

num = len(listings)
def find_info_header(header, result_num=20):
    index = listings[0].index(header)
    results = []
    for i in range(result_num):
        results.append(listings[random.randint(1, num)][index])
    return results

listings[0].sort()
print(listings[0])

def find_null_values():
    null_dict = {}
    for header in listings[0]:
        index = listings[0].index(header)
        null_dict[header] = 0
        for row in listings[1:]:
            if row[index] == '':
                null_dict[header] += 1
    return null_dict


