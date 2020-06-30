import matplotlib.pyplot as plt
x1=[1,2,3]
y1=[1,2,3]

x2=[5,6,7]
y2=[7,6,5]

plt.plot(x1,y1,label="Line1")
plt.plot(x2,y2,label="Line2")

plt.legend()

plt.show()
