demo_list = [1 , "hola" , 1.13 , True , [1, 2, 3]]
colors = ["rojo" , "verde" , "azul"]

numbers_list = ([1, 2, 3])
print(numbers_list)

r = list(range(1, 1001))
print(r)

print(len(colors))
print(colors[2])

print("amarillo" in colors) 

print(colors)
colors[1] = "amarrillo"
print(colors)

print(dir(colors))

colors.extend(["amarillo" , "celeste"])
colors.extend(["negro" , "blanco"])

colors.insert(1 , "negro")
colors.insert(len(colors), "negro")

print(colors)
colors.remove("rojo")

colors.pop() #quita elementos 

colors.sort(reverse=True)


print(colors.count("azul"))
 
