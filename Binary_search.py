def BinarySearch(nums,target):
    n=len(nums)
    if n==0:
        return -1
    elif n==1:
        if nums[0]==target:
            return 0
        else:
            return -1
    left=0
    right=n-1
    while(left<=right):
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        else:
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
    return -1

nums=[]
print("请输入一串有序的数，之间用空格分隔，回车结束输入:")
line=input()
for port in line.split():
    try:
        num=int(port)
        nums.append(num)
    except ValueError:
        print(f"无效输入'{port}',已跳过")
if (nums!=sorted(nums)):
    print("错误！输入的数据无序")
    exit()
print("请输入要在数组中查询的target值:")
target=int(input())
answer=BinarySearch(nums,target)
if answer!=-1:
    print("target在数组nums中对应的下标为:",answer)
else:
    print("nums数组中不存在要找的target值")
