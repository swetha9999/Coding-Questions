""" You are given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.This return the first occuring sum"""
def two_sum(nums, target):
    seen={}
    for i,num in enumerate(nums):
        comp=target - num
        if comp in seen:
            return [seen[comp],i]
        seen[num]=i
nums = [2,7,11, 15,2,3,6]
target = 9
print(two_sum(nums, target))