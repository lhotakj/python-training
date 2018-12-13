
lines = [line.rstrip('\n') for line in open('cities.txt')]
data = []
for line in lines:
    s = line.split(",")
    data.append({"code": s[0].strip(), "city": s[1].strip()})

ordered_by_code = sorted(data, key=lambda k: k['code'])
print(ordered_by_code)

per_code = []
for item in data:
    if item['code'] not in per_code:
        per_code.append(item['code'])

for country in per_code:
    # print(country + ": ")
    towns = []
    for item in data:
        if item['code'] == country:
            towns += item['city']






