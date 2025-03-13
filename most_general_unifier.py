def is_variable(term):
    if '(' in term:
        return False
    elif len(term)>1 and term[0]!=term[1]:
        return False
    elif len(term)==1:
        if term=='x' or term=='y' or term=='z' or term=='u':
            return True
        else:
            return False
    else:
        return True

def occurs_check(v,t):
    if v in t:
        return True
    else:
        return False

def apply_substitution(formula,v,t):
    result=''
    i=0
    while i<= len(formula)-len(v):
        if formula[i:i+len(v)] == v:
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
        if is_variable(d1):
            v+=d1
            t+=d2
        else:
            v+=d2
            t+=d1
        # 检查变量符号是否出现在项中:
        if occurs_check(v,t):
            print('该集合是不可合一的')
            return ''
        
        answer[v]=t
        formulaA=apply_substitution(formulaA,v,t)
        formulaB=apply_substitution(formulaB,v,t)

    return answer

test_KB1=('P(xx,a)','P(b,yy)')
test_KB2=('P(a,xx,f(g(yy)))','P(zz,f(zz),f(uu))')
test_KB3=('P(x,x)','P(y,f(y))')
print(MGU(test_KB1))
print(MGU(test_KB2))
print(MGU(test_KB3))
