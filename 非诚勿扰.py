a=input("输入男生年龄、身高、体重、收入:")
b=input("输入女生年龄、身高、体重、收入:")
c,d = a.split(),b.split()
for i in range(4):
    c[i]=int(c[i])
    d[i]=int(d[i])
if d[0]>20 and d[0]<28 and d[1]>160 and d[1]<175 and d[2]>40 and d[2]<60 and d[3]>2000 and d[3]<5000:
    if c[0]>20 and c[0]<28 and c[1]>165 and c[1]<180 and c[2]>50 and c[2]<70 and c[3]>4000:
        print("配对成功")
else:
    print("配对不成功")
    
        
