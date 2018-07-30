print("1.添加学员姓名\n2.修改学员姓名\n3.查询学员姓名\n4.删除学员姓名\n0.退出程序")
a = int(input("请输入操作选项："))
c=[]
if a == 1:
    b = input("输入要添加的姓名:")
    c.append(b)
elif a == 2:
    if len(c):
        b = int(input("输入学员的序号:"))
        while b < 1 and b > len(c):
            b = int(input("序号输入错误，请重新输入你要修改的学员序号："))
        d = input("输入修改信息:")
        for i in range(len(c)):
            if i+1 == b:
                c[i] = d
        print("学员信息修改成功！")
    else:
        print("学员信息为空，无法修改！")
elif a == 3:
    if len(c):
        print("1-输入序号查询\n2-查询所有学员")
        b = int(input('请输入你要操作的序号：'))
        while b != 1 and b != 2:
            b=int(input('序号输入错误，请重新输入你要操作的序号：'))
        if b == 1:
            d = int(input("输入学员的序号:"))
            while d < 1 and d > len(c):
                d = int(input('输入错误，请重新输入要查询的学员序号：'))
            print("查询到的学员姓名是：%s"%c[d])
        if b == 2:
            for i in range(len(c)):
                print(i+1,c[i])        
    else:
        print("学员信息为空，无法修改！")
elif a == 4:
    if len(c):
        print("1.输入序号删除\n2.输入学员名称删除\n3.删除所有学员")
        b = int(input('请输入要操作的序号:'))
        while b != 1 and b != 2 and b != 3:
            b = int(input('没有该序号，请重新输入要操作的序号：'))
        if b == 1:
            d = int(input('请输入要删除的学员序号：'))
            while d < 1 and d > len(c):
                d = int(input('输入错误，请重新输入要删除的学员序号：'))
            c.pop(d-1)
            print('删除学员成功！')
        if b == 2:
            d = input('请输入要删除的学员名称')
            while d not in c:
                d = input('请重新输入要删除的学员姓名：')
            c.remove(d)
            print('学员信息删除成功！')
        if b == 3:
            for i in range(len(c)):
                del c[i]
            print('学员信息删除成功')
                
    else:
        print('学员信息为空，无法删除！')
elif a == 0:
    exit()    
    
                
                
            
        
