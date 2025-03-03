def ReverseKeyValue(dict1):
    dict2={}
    for key, value in dict1.items():
        dict2[value]=key
    return dict2

dict1={}
while(1):
    line=input("请输入学生的姓名和学号,之间用空格分隔,输入exit退出:")
    flag=0
    list=[]
    for port in line.split():
        if port=="exit":
            flag=1
            break
        else:
            list.append(port)
    if(flag):
        break
    else:
        dict1[list[0]]=list[1]

print(dict1)
print(ReverseKeyValue(dict1))    