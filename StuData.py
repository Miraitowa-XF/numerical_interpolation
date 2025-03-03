class StuData():
    def __init__(self,filename):
        self.data=[]
        with open(filename) as file_object:
            for line in file_object.readlines():
                one=[]
                for port in line.split():
                    one.append(port)
                self.data.append(one)
    
    def AddData(self,name,stu_num,gender,age):
        one=[]
        one.append(name)
        one.append(stu_num)
        one.append(gender)
        one.append(age)
        self.data.append(one)

    def SortData(self,feature):
        pattern={'name':0,'stu_num':1,'gender':2,'age':3}
        try:
            t=pattern[feature]
        except ValueError:
            print("输入的属性特征错误")
        self.data.sort(key=lambda x:x[t])
        print("按照{feature}排序后的结果为:",self.data)

    def ExportFile(self,filename):
        txt_filename=f"{filename}.txt"
        with open(txt_filename,'w') as file_object:
            for one in self.data:
                line=' '.join(one)
                file_object.write(line+'\n')

try:
    name_list = StuData("F:\VsCode\Python\student_data.txt")
except FileNotFoundError:
    print("文件未找到！")

name_list.AddData('Bob','003','M','20')

feature=input("请输入排序所要按照的属性:")
name_list.SortData(feature)

name_list.ExportFile("new_stu_data")