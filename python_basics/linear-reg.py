x = [1, 2, 3, 4, 5]
y = [30, 40, 50, 60, 70]

# print(x)
# print(y)

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

# print(mean_x)
# print(mean_y)

numerarator = 0
for i in range(len(x)):
  numerarator += (x[i]-mean_x)* (y[i]-mean_y)

# print(numerarator)  

denominator = 0

for i in range(len(x)):
  denominator += (x[i]-mean_x) * (x[i]-mean_x) 

# print(denominator)

# now slope will be m 

m = numerarator/denominator
print("m =", m)

# now lets find out b

b = mean_y - (m*mean_x)
print("b =",b)

# now lets do predictions 

new_x = [6,3,4,6,8,9,10]

for value in new_x:
  prediction = m*(value)+b
  print(prediction)