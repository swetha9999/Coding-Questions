""" You are given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.I want to answer with all the possible pairs of indices that add up to the target"""

def add_sum(nums,target):
    seen={}
    result=[]
    for i,num in enumerate(nums):
        comp=target-num
        if comp in seen:
            for j in seen[comp]:
                result.append((j, i))
        seen.setdefault(num, []).append(i)
    return result
nums=[2,7,11, 15,2,3,6]
target=9
print(add_sum(nums,target))