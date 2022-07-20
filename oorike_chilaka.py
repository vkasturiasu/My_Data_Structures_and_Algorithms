# # a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# # a = [[5,6]]
# # arr = []
# # for i in range(len(a)-1):
# #     if i>0:
# #         temp =[]
# #         for j in range(len(a[i])-1):
# #             if j>0:
# #                 temp.append(a[i][j])
# #         arr.append(temp)
# # print(arr)
# # a = [3,4,5]
# # ab = [5,6]
# # for i in a:
# #     ab.append(i)
# # print(ab)
# # def first():
# #     b = [1]
# #     def second(c):
# #         b.append(c)
# #         print(b)
# #
# #     print(b)
# #     second(3)
# # a= [[1,2,3,4,5],[6,8,9,10,11]]
# # print(len(a)).
# # for i in range(7,1,-1):
# #     print(i)
# def spiralTraverse(array):
#     # Write your code here.
#     ans = []
#     lenght = len(array)
#     def append(array, ans):
#         for i in array:
#             ans.append(i)
#         return ans
#
#     def getnext(a):
#         arr = []
#         for i in range(len(a) - 1):
#             if i > 0:
#                 temp = []
#                 for j in range(len(a[i]) - 1):
#                     if j > 0:
#                         temp.append(a[i][j])
#                 arr.append(temp)
#
#         return arr
#
#
#     def rot(array, ans):
#         if not array: return ans
#         if len(array)==1: return append(array[0], ans)
#         if array == [[]]: return ans
#         for i in range(len(array)):
#             if i == 0:
#                 append(array[i], ans)
#             elif i == len(array) - 1:
#                 j = len(array[i]) - 1
#                 while j >= 0:
#                     ans.append(array[i][j])
#                     j -= 1
#             else:
#                 ans.append(array[i][-1])
#
#         if len(ans)== lenght: return ans
#
#         for i in range(len(array) - 2, 0, -1):
#             ans.append(array[i][0])
#
#         return rot(getnext(array), ans)
#
#     return rot(array,ans)
#
# a= [
#     [1, 2, 3],
#     [12, 13, 4],
#     [11, 14, 5],
#     [10, 15, 6],
#     [9, 8, 7]
#   ]
#
#
# print(spiralTraverse(a))