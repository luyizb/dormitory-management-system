'''
学生信息包括 
学号（唯一）  姓名  性别  年龄  寝室（一间寝室最多安排4人）
寝室编号 男生（100 101 102） 女生（200 201 202）

功能包括：
1. 可以录入学生信息
2. 录入过程中可以为其分配寝室（可选自动分配或手动分配，手动分配的话如果选择的寝室人员已满，提示重新分配）
3. 可以打印各寝室人员列表（做到表格打印是加分项）
4. 可以用学号索引打印特定学生信息，可以打印所有学生信息（做到表格打印是加分项）
5. 可以为学生调整寝室（一人调整到其他寝室，两人交换寝室等，自由发挥）         #学号是唯一的，我们可以根据学号，改变想要调换寝室的学生
6. 可以将所有信息存入文件（json格式）
7. 程序启动时，将文件中的学生信息自动导入系统
'''
#我们先用一个列表存储学生的信息，然后将字典写入文件中永久保存。

from prettytable import PrettyTable  #表格
from operator import itemgetter      #排序
dormitory_list = [] #[{},{},{},...,{}]--每个学生的信息存在一个字典中，所有学生信息存在一个大的字典中


#寝室管理系统操作界面显示
def interface():
    print('-'*30)
    print('学生寝室管理系统 v1.0')
    print('1.添加学生信息')
    print('2.打印寝室人员列表')
    print('3.查找学生')
    print('4.寝室调换')
    print('5.信息更改')
    print('0.退出')
    print('-'*30)


#寝室人数判断是否>4人
def people_judge():
    room_num = input("请手动分配寝室(男-1XX,女-2XX)：")
    while True:
                                                                #=2时自动（random）,男生寝室范围是100-199；女生寝室范围是200-299，每次我们根据输入的性别来确定寝室范围，进行随机分配
        i=0                                                     #判断一下性别，如果是男生，不小心输入201,就报错
        for num in dormitory_list:
            if num['寝室号'] == room_num :                      #print("123")
                i+=1
        if i > 3:
            print("人数已满，请重新选择寝室")
            room_num = input("请重新手动分配寝室：")          
        else:
            break       #这个break是跳出while
    return room_num



def judge_student_id():                                        #检查整个字符串是否为中文 Args:  string (str): 需要检查的字符串, 包含空格也是False     Return bool
    while True:
        t = -1                                                 #还要判断是否输入的学号已经存在？？？（还没写）
        student_id = input("请输入学生学号：")
        for num in student_id:
            if student_id.isdigit():
                if int(student_id) < 0 or int(student_id) > 999:
                    print("输入错误，请重新输入学号")
                    break
                else:
                    t = 1
            else:
                print("输入错误，请重新输入学号")
                break
        if t == 1:                                                         #这个break 是为了跳出while            
             break
                
    return student_id
        

 
def judge_name():                                             #检查整个字符串是否为中文 Args:  string (str): 需要检查的字符串, 包含空格也是False     Return bool
    while True:
        flag = -1
        string = input("请输入学生姓名：")
        for chart in string:
            if chart < u'\u4e00' or chart > u'\u9fff':
                print("输入错误，请重新输入姓名")
                break                                         #这个break 是为了只显示一次上面的句子
            else:
                flag = 1
                break                                         #这个break 是为了跳出for
        if flag == 1:
            break                                             #这个break 是为了跳出while
    return string


def judge_sex():
    while True:
        sex = input("请输入学生性别：")
        if sex == '男' or sex == '女':
            break
        else: 
            print("输入错误，请重新输入性别")
    return sex


def judge_age():
    while True:
        age = input("请输入学生年龄：")
        if age.isdigit():
            if int(age) > 0 and int(age) < 40:
                break
            else:
               print("输入错误，请重新输入年龄")
        else:
            print("输入错误，请重新输入年龄")
    return age
        
       

#录入学生信息
def add_student():
    while True:
        judge = input("确定/退出录入学生信息（Y/N）:")
        if judge == "Y":
            add_dict = {}                                     #当我们在输入学生信息时，输错了，提醒‘输入错误，请重新输入’？？？？？？？（基本完成）
            add_dict['学号'] = judge_student_id() 
            add_dict['姓名'] = judge_name()
            add_dict['性别'] = judge_sex()
            add_dict['年龄'] = judge_age()
            add_dict['寝室号'] = people_judge()
            dormitory_list.append(add_dict)
            
        else:
            break
        
    


    

#显示指定寝室人员名单
def print_list():
    while True:
        judge = input("确定/退出显示指定寝室人员名单（Y/N）:")
        if judge == "Y":
            global  dormitory_list                          #使用全局变量加global
            dormitory_list = sorted(dormitory_list,key=itemgetter('学号'))    #对同一寝室的人按照学号排序再输出
            a = 1
            num = input("请输入需要人员名单的寝室号：")                       #num 是字符
            #dormitory_list.sort()                                            #这个只能对列表排序
            x = PrettyTable(['学号','姓名','性别','年龄','寝室号'])
            for temp in dormitory_list:
                if temp['寝室号'] == num:
                    x.add_row([temp['学号'],temp['姓名'],temp['性别'],temp['年龄'],temp['寝室号']])
                    #print(x)
                    #print(" 学号    姓名    性别    年龄    寝室号 ")
                   #print("  %s      %s      %s      %s      %s"
                    #      %(temp['学号'],temp['姓名'],temp['性别'],temp['年龄'],temp['寝室号']))
                    a += 1
            print(x)                                        #我们只要一个抬头，其余信息全部在这个下面显示，我们在for外显示抬头，然后一直使用.add_row，先全部加在下面，然后我们最后再for 外面打印
        else:
             break
            


#查找指定学号学生信息
def find_student():
    while True:
        judge = input("确定/退出查找指定学号学生信息（Y/N）:")
        if judge == "Y":
            flag = 0
            student_id = input("请输入想要查找学生的学号（00X）：")        
            for temp in dormitory_list:
                if temp['学号'] == student_id :
                    x = PrettyTable(['学号','姓名','性别','年龄','寝室号'])
                    x.add_row([temp['学号'],temp['姓名'],temp['性别'],temp['年龄'],temp['寝室号']])
                    flag = 1 
                    break
            print(x)
            if flag ==0:
                print("查无此人，请重新输入")
                #break
            break
        else:
            break
            

'''
def find_student():
    while True:
        student_id = input("请输入想要查找学生的学号（00X）：")

        #由于文件里面存储的顺序不是从学号001开始，如果保留else的break,那么我们输入001时，与遍历的开始对比，不相等，
        #直接执行else，紧接着两个break,退出 #现在我们去除else的break，当我们查找001时，由于与遍历文件的开始对比（002），不相等，，所以会多打印一个
        #查无此人，请重新输入   现在我们更改程序，我们设置一个标志位flag

        for temp in dormitory_list:                                        
            if temp['学号'] == student_id :                               
                x = PrettyTable(['学号','姓名','性别','年龄','寝室号'])    
                x.add_row([temp['学号'],temp['姓名'],temp['性别'],temp['年龄'],temp['寝室号']])
                print(x)
                break
           else:
                print("查无此人，请重新输入")
                #break
        break
'''
        

#学生寝室变更--1.单人更换寝室；2.两人互换寝室
def exchange_room():
    while True:
        judge = input("确定/退出学生寝室变更（Y/N）:")
        if judge == 'Y': 
            
            temp = int(input("1-一人调整到其他寝室，2-两人交换寝室："))
            if temp ==1:
                a = 0
                num = input("输入想要换寝室人的学号：")
                for i in dormitory_list:
                    if i['学号'] == num :
                        print("%s的当前寝室为：%s"%(i['姓名'],i['寝室号']))
                        dormitory_list[a]['寝室号'] = people_judge()                     #一个人更换寝室要判断新寝室是否满人  
                        print(dormitory_list[a])
                    a += 1
            elif temp == 2:                                                              #两个人对换寝室--先将第一个人的寝室号存入中间变量，将第二个人的寝室号给第一个人，将中间变量的值给第二个人
                t = 0                                                                    #两人交换寝室，我们要判断性别是否一致
                b = 0
                student_id1 = input("输入第一个想要换寝室人的学号：")
                student_id2 = input("输入第二个想要换寝室人的学号：")
                for i in dormitory_list:
                    if i['学号'] == student_id1 :     
                        mid1 = dormitory_list[t]['寝室号']
                        #print(type(mid1))
                        #print(mid1)
                        #print(dormitory_list[t])
                        break
                    t += 1
                print(t)
            
                for j in dormitory_list:
                    if j['学号'] == student_id2 :                                       #我们还要判别互换的寝室两人性别是否相同
                        sex_same(t,b)        
                        #print(dormitory_list[t])
                        dormitory_list[t]['寝室号'] = dormitory_list[b]['寝室号']                              
                        #print(dormitory_list[b])
                        #print(mid1)
                        dormitory_list[b]['寝室号'] = mid1
                    else:
                        print("男女之间不能互换寝室")
                    break
                    #print(dormitory_list[a]['寝室号'])
                b += 1
        else:
            break
                
#学生信息更改
def change_information():
    while True:
        judge = input("确定/退出学生信息更改（Y/N）:")
        if judge == 'Y': 
            num = input("输入想要更改信息的学生学号：")
            for temp in dormitory_list:
                if temp['学号'] == num:
                    which = input("1.修改学号，2.修改姓名，3.修改性别，4.修改年龄：")
                    if which == '1':
                        temp['学号'] = input("输入更改的学号：")
                    elif which == '2':
                        temp['姓名'] = input("输入更改的姓名：")
                    elif which == '3':
                        temp['性别'] = input("输入更改的性别：")
                    elif which == '4':
                        temp['年龄'] = input("输入更改的年龄：")
                    else:
                        break
        else:
            break

    

#将学生信息存入文件中 
def file_save():  #保存所有x学生的信息
 f=open('E:/domitory.txt','w')
 f.write(str(dormitory_list))                                                           #str--转换成字符串
 f.close()
 

#从文件中提取学生信息
def file_recover():#从文件中提取信息
  global  dormitory_list
  f=open('E:/domitory.txt')
  content1=f.read()
  dormitory_list=eval(content1)                                                         #eval---转换成列表
  f.close ()


#主函数
while True:
    file_recover()                                                                      #如果我们选错了业务，怎么退回来重新选择？？？？？？
    interface()
    data = int(input("请输入选择业务："))   
    if data ==1:
        add_student()
        file_save()
    elif data == 2:                     
        print_list()        
    elif data == 3:
        find_student()
    elif data == 4:
        exchange_room()
        file_save()                                                                     #换了寝室之后必须存入文件，不然寝室信息不会改变
    elif data == 5:
        change_information()
        file_save()
    elif data == 0:
        exit_signal = input("确定要退出吗？(Y/N)：")
        if exit_signal == 'Y':
            break
        else:
            print("输入有误，请重新输入")
    else:                                       
        print("输入错误，请重新输入！")
    
