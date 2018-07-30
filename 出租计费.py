while(1):
    a=int(input())
    if a>0 and a<=2:
        print(8)
    elif a>2 and a<=12:
        print(8+1.2*(a-2))
    elif a>12:
        print(8+1.2*10+1.5*(a-12))
    else:
        print("请输入正确的公里数进行计算，程序结束")
    
