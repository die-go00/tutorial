demo_list = [1, "Awesome", 90.32, True, [1,2,3,4,5]]

colors = ["red", "blue", "white"]

numbers_list = list((1,2,3,4))

print(type(numbers_list))

r = list(range(1,1000))

print(r)

print(len(demo_list))

print(colors[-2])

print (numbers_list)

print ("white" in colors)

colors[1] = "black"

#print(dir(colors))

colors.append("violet")

colors.extend(['orange', "pink"])

colors.extend(["yellow", "grey"])

colors.insert(1, 'green')

#colors.pop()

#colors.remove()

#colors.clear()

#colors.sort()

colors.sort(reverse=True)

print(colors.count("green"))

print(colors)