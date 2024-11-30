# a = {1:1,2:2,3:3}
# b = a
# del b[3]
# print(a)

# def a():
#     def b():
#         print('b',end=' ')
#     print('a',end=' ')
#     b()
# def b():
#     print('B',end=' ')   
 
# a()
# b()
# a=[1,2,3]
# b=a
# b.remove(3)
# print(a)


# 给定一个整数数组 nums 和一个整数目标值 target，
# 请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 如果找到请以按从小到大顺序返回答案。
# 如果不存在请返回NULL
nums=(input()).split(" ")
target=int(input())
a=0
for i in range(len(nums)):
    for k in range(i+1,len(nums)):
        if target==int(nums[i])+int(nums[k]):
            print(f"{i} {k}")
            a=a+1
if a==0:
    print("NULL")

        
        
