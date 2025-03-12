def ResolutionProp(KB):
    List=[]
    l=len(KB)
    if l==0:
        return List
    for clause in KB:
        lisA=[]
        for element in clause:
            lisA.append(element)
        List.append(lisA)
    answer=[]
    for line in List:
        str1='('
        length_line=len(line)
        for element in line:
            str1+=element
            str1+=','
        if length_line!=1:
            str1=str1[:-1]
        str1+=')'
        answer.append(str1)
    if l==1:
        return answer
    dict={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    status=[0]*1000
    for i in range(0,len(List)):
        if status[i]==1:
            continue
        flag=0
        for col1 in range(0,len(List[i])):
            elementA=List[i][col1]
            if elementA[0]=='~':
                not_elementA=elementA[1:]
            else:
                not_elementA='~'+elementA
            for j in range(0,len(List)):
                if status[j]==1 or j==i:
                    continue
                for col2 in range(0,len(List[j])):
                    elementB=List[j][col2]
                    if elementB==not_elementA:
                        flag+=1
                        new_List=[]
                        for i_element in List[i]:
                            if i_element != elementA:
                                new_List.append(i_element)
                        for j_element in List[j]:
                            if j_element != elementB:
                                new_List.append(j_element)
                        str2='R['+str(i+1)
                        if len(List[i]) > 1:
                            str2+=dict[col1+1]
                        str2+=','
                        str2+=str(j+1)
                        if len(List[j]) > 1:
                            str2+=dict[col2+1]
                        str2+='] = ('
                        for new_List_element in new_List:
                            str2+=new_List_element
                            str2+=','
                        if len(new_List) > 1:
                            str2=str2[0:]
                        str2+=')'
                        answer.append(str2)
                        if len(new_List) != 0:
                            List.append(new_List)
                        else:
                            Printing_process(answer)
                            return 
                        status[i]=1
                        status[j]=1
                        break
                if flag==1:
                    break
            if flag==1:
                break
    Printing_process(answer)
    return

def Printing_process(answer):
    for k in range(0,len(answer)):
        print(k+1,answer[k])
    return


KB = set()
count=1
while True:
    while True:
        input_str = input(f"请输入第{count}个子句的元素(元素之间用逗号分隔,以回车结束输入):\n")
        elements=[port.strip() for port in input_str.split(',') if port.strip() != '']

        if not elements:
            print("错误:子句不能为空,请重新输入!")
            continue

        # 去除子句中重复的元素:
        seen = set()
        unique_elements=[]
        for e in elements:
            if e not in seen:
                seen.add(e)
                unique_elements.append(e)

        # 转变为不可变元组:
        clause=tuple(unique_elements)

        # 检查输入的子句是否已经在子句集中存在:
        if clause in KB:
            print("警告:该子句已存在,自动忽略重复输入!")
            continue
        
        KB.add(clause)
        count+=1
        break

    while True:
        choice = input("是否继续添加子句?(y/n):").strip().lower()
        if choice in ['y','n']:
            break
        else:
            print("无效输入,请输入y或n")

    if choice == 'n':
        break
# test_KB={("FirstGrade",),("~FirstGrade","Child"),("~Child",)}
ResolutionProp(KB)


    # while r<=len(List):
    #     for col1 in range(0,len(List[r-1])):
    #         elementA=List[r-1][col1]
    #         flag=0
    #         if elementA[0]=="~":
    #             tmp=elementA[1:]
    #         else:
    #             tmp="~"
    #             tmp+=elementA
    #         for col2 in range(0,len(List[r])):
    #             elementB=List[r][col2]
    #             if elementB==tmp:
    #                 flag+=1
    #                 strr='R['+str(r)
    #                 if len(List[r-1])!=1:
    #                     strr+=dict[col1+1]
    #                 strr+=','
    #                 strr+=str(r+1)
    #                 if len(List[r])!=1:
    #                     strr+=dict[col2+1]
    #                 strr+='] = '
    #                 ListC=[]
    #                 clause='('
    #                 count=0
    #                 for c1 in range(0,len(List[r-1])):
    #                     if c1!=col1:
    #                         tmpp=List[r-1][c1]+','
    #                         clause+=tmpp
    #                         count+=1
    #                         ListC.append(List[r-1][c1])
    #                 for c2 in range(0,len(List[r])):
    #                     if c2!=col2:
    #                         tmpp=List[r][c2]+','
    #                         clause+=tmpp
    #                         count+=1
    #                         ListC.append(List[r][c2])
    #                 if count>1:
    #                     clause=clause[:-1]
    #                 clause+=')'
    #                 strr+=clause
    #                 answer.append(strr)
    #                 if len(ListC)!=0:
    #                     List.append(ListC)
    #                 break
    #         if flag!=0:
    #             break
    #     r+=2
    # return answer                    
