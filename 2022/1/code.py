result = {}

cpt = 0
result[cpt] = 0
try:
    with open("2022/1/value.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                cpt += 1
                result[cpt] = 0

            else:
                result[cpt] =  result[cpt] + int(line)
except Exception as e:
    print(e)

sorted_res = sorted(result.items(), key=lambda k: k[1], reverse=True)

print("max eat :  " + str(max(result.items(), key=lambda k: k[1])[1]))

tot = 0 
for x in list(sorted_res)[0:3]:
    tot += x[1]

print("sum eat :  " + str(tot))

print("end")