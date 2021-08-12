# Collatz-Conjecture-code
# This Python code is written after I watch this video - https://www.youtube.com/watch?v=094y1Z2wpJg&amp;ab_channel=Veritasium

import matplotlib.pyplot as plt

y = int(input("Insert any number:")) 
y_data = []

while True:
  if y%2 == 1: # odd
    k =  3*y + 1
    y = k
    #print(k)
    y_data.append(y)
    if y == 1:
      break 
      

  elif y%2 == 0:  #even
    k =  y/2
    y = k
    #print(k)
    y_data.append(y)
    if y == 1:
      break
    

x_data = []
for i in range(len(y_data)):
  x_data.append(i)

print("")
print("y-data:", y_data)
print("")
print("x-data:", x_data)
print("")
plt.figure(figsize=(20,8))
plt.title("Collatz Conjecture Graph", size = 20)
plt.xlabel("x data", size = 20)
plt.ylabel("y data", size = 20)
plt.plot(x_data, y_data)
plt.plot(x_data, y_data, "x")
plt.show()
  


