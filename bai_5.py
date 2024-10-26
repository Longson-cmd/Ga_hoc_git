import numpy as np  
import matplotlib.pyplot as plt #thư viện vẽ biểu đồ
from functions import *
#import toàn bộ file data.txt
raw = np.loadtxt('data.txt', delimiter = ',')
#Tách lấy X
X = np.copy(raw)
X[:,1] = X[:,0]
#thêm bias 1
X[:,0] = 1
#Tách lấy y
y = raw[:,1]

#Train data
[Theta, J_hist] = GradientDescent(X,y)#mặc định alpha = 0.02 iter = 5000
#Predict
predict = predict(X,Theta) * 10000#chuyển về đơn vị người
#Plot kết quả
plt.figure(1)
plt.plot(X[:,1],y,'rx')
plt.plot(X[:,1],predict/10000,'-b') #đơn vị gốc: nghìn người
plt.figure(2)
plt.plot(J_hist[:,0],J_hist[:,1],'-r')
plt.show() #chỉ gọi 1 lần trong chương trình để hiển thị các biểu đồ cùng lúc