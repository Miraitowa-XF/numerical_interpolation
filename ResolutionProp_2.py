def is_variable(term):
    if '(' in term:
        return False
    elif len(term)>1 and term[0]!=term[1]:
        return False
    elif len(term)==1:
        if term=='x' or term=='y' or term=='z' or term=='u' or term=='v' or term=='w':
            return True
        else:
            return False
    else:
        return True

def occurs_check(v,t):
    if v in t:
        if '(' in t:
            return True
        else:
            return False
    else:
        return False

def apply_substitution(formula,v,t):
    result=''
    i=0
    while i<= len(formula)-len(v):
        if formula[i:i+len(v)] == v and (formula[i-1]=='(' or formula[i-1]==','):
            result+=t
            i+=len(v)
        else:
            result+=formula[i]
            i+=1
    result+=formula[i:]
    return result

def count_bracket(formula,bracket):
    k=0
    for t in range(0,len(formula)):
        if formula[t]==bracket:
            k+=1
    return k

def can_be_replaced(mgu,variable_replace):
    element1=mgu[0]
    element2=mgu[1]
    for key1 in variable_replace:
        element1=apply_substitution(element1,key1,variable_replace[key1])
        element2=apply_substitution(element2,key1,variable_replace[key1])
    if element1==element2:
        return True
    else:
        return False

def MGU(KB):
    formulaA=KB[0]
    formulaB=KB[1]
    answer=dict()
    while formulaA!=formulaB:
        Count=0
        while formulaA[Count]==formulaB[Count]:
            Count+=1
        i=Count
        d1=''
        while i < len(formulaA)-1 and formulaA[i]!=',':
            if formulaA[i]==')':
                left_count=count_bracket(d1,'(')
                right_count=count_bracket(d1,')')
                if right_count >= left_count:
                    i+=1
                    continue
            d1+=formulaA[i]
            i+=1
        j=Count
        d2=''
        while j < len(formulaB)-1 and formulaB[j]!=',':
            if formulaB[j]==')':
                left_count=count_bracket(d2,'(')
                right_count=count_bracket(d2,')')
                if right_count >= left_count:
                    j+=1
                    continue
            d2+=formulaB[j]
            j+=1
        v=''
        t=''
        if is_variable(d1) and is_variable(d2)==False:
            v+=d1
            t+=d2
        elif is_variable(d2) and is_variable(d1)==False:
            v+=d2
            t+=d1
        else:
            return answer
        # 检查变量符号是否出现在项中:
        if occurs_check(v,t):
            # print('该集合是不可合一的')
            return answer
        
        answer[v]=t
        formulaA=apply_substitution(formulaA,v,t)
        formulaB=apply_substitution(formulaB,v,t)

    return answer


def get_name(element):
    tag=0
    while(element[tag]!='('):
        tag+=1
    return tag

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
    status=[]
    flag=0
    while flag==0:
        length=len(List)
        for i in range(0,length):                        # i表示列表的行
            for col1 in range(0,len(List[i])):              # col1 表示列表第i行的第col1列
                elementA=List[i][col1]
                if elementA[0]=='~':
                    right_name=get_name(elementA)
                    not_elementA=elementA[1:]
                    flag_not_elementA=elementA[1:right_name]
                else:
                    right_name=get_name(elementA)
                    not_elementA='~'+elementA
                    flag_not_elementA='~'+elementA[0:right_name]
                for j in range(0,len(List)):   # j表示第j行
                    for col2 in range(0,len(List[j])):         # col2表示第j行的第col2列
                        unite=str(i)+str(col1)+str(j)+str(col2)
                        if unite in status:
                            continue
                        elementB=List[j][col2]
                        right_name=get_name(elementB)
                        flag_elementB=elementB[0:right_name]
                        if flag_elementB==flag_not_elementA:
                            mgu=[]
                            mgu.append(not_elementA)
                            mgu.append(elementB)
                            variable_replace=MGU(mgu)
                            if can_be_replaced(mgu,variable_replace)==False:
                                continue
                            if len(variable_replace)==0:
                                if not_elementA!=elementB:
                                    continue
                            str_replace=''
                            for key in variable_replace:
                                str_replace+= key+'='+variable_replace[key]
                                str_replace+=','
                            if(len(variable_replace)>=1):
                                str_replace=str_replace[:-1]
                            new_List=[]
                            for i_element in List[i]:
                                if i_element != elementA:
                                    if len(variable_replace)>0:
                                        for key in variable_replace:
                                            new_element=apply_substitution(i_element,key,variable_replace[key])
                                            if new_element in new_List:
                                                continue
                                            else:
                                                new_List.append(new_element)
                                    else:
                                        new_List.append(i_element)
                            for j_element in List[j]:
                                if j_element != elementB:
                                    if len(variable_replace)>0:
                                        for key in variable_replace:
                                            new_element=apply_substitution(j_element,key,variable_replace[key])
                                            if new_element in new_List:
                                                continue
                                            else:
                                                new_List.append(new_element)
                                    else:
                                        new_List.append(j_element)

                            str2='R['+str(i+1)
                            if len(List[i]) > 1:
                                str2+=dict[col1+1]
                            str2+=','
                            str2+=str(j+1)
                            if len(List[j]) > 1:
                                str2+=dict[col2+1]
                            str2+=']'
                            if len(variable_replace)!=0:
                                str2+='{'
                                str2+=str_replace
                                str2+='}'
                            str2+=' = ('
                            for new_List_element in new_List:
                                str2+=new_List_element
                                str2+=','
                            if len(new_List) > 1:
                                str2=str2[:-1]
                            str2+=')'
                            if len(new_List)==0:
                                str2=str2[:-2]
                                str2+='[]'
                            answer.append(str2)
                            if len(new_List) != 0:
                                List.append(new_List)
                            else:
                                flag+=1
                                Printing_process(answer)
                                return 
                            
                            united=str(i)+str(col1)+str(j)+str(col2)
                            status.append(united)
                            break
    Printing_process(answer)
    return

def Printing_process(answer):
    for k in range(0,len(answer)):
        print(k+1,answer[k])
    return


test_KB1=(("A(tony)",),("A(mike)",),("A(john)",),("L(tony,rain)",),("L(tony,snow)",),("~A(x)","S(x)","C(x)"),("~C(y)","~L(y,rain)"),("L(z,snow)","~S(z)"),("~L(tony,u)","~L(mike,u)"),("L(tony,v)","L(mike,v)"),("~A(w)","~C(w)","S(w)"))
test_KB2=(("On(tony,mike)",),("On(mike,john)",),("Green(tony)",),("~Green(john)",),("~On(xx,yy)","~Green(xx)","Green(yy)"))
ResolutionProp(test_KB1)