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
# nums=(input()).split(" ")
# target=int(input())
# a=0
# for i in range(len(nums)-1):
#     if nums[i]=="":
#         continue
#     for k in range(i+1,len(nums)):
#         if nums[k]=="":
#             continue
#         if target==int(nums[i])+int(nums[k]):
#             print(f"{i} {k}")
#             a=1
        
# if a==0:
#     print("NULL")

#   题目描述: 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
# 输入: 字符串s
# 输出: 无重复字符的最长字串长度（整数)



def sub(s:str)->str:
    count={char:s.count(char) for char in set(s)}
    in_s={}
    stack=[]
    for char in s:
        count[char]-=1 
        if in_s.get(char,False):
            continue
        while stack and stack[-1]> char and count[stack[-1]]>0:
            r_char=stack.pop()
            in_s[r_char]=False
        stack.append(char)
        in_s[char]=True
    return ".join(stack)
s=input()
print(sub(s))