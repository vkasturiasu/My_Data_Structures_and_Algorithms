a =[
    [1, 2, 3],
    [12, 13, 4],
    [11, 14, 5],
    [10, 15, 6],
    [9, 8, 7]
   ]
print(a)
# def spiralTraverse(array):
#     ans =[]
#
#     def append(a,ans):
#         for i in a:
#             ans.append(i)
#         return ans
#
#     def getnext(a):
#
#         arr = []
#         for i in range(len(a) - 1):
#             if i > 0:
#                 temp = []
#                 for j in range(len(a[i]) - 1):
#                     if j > 0:
#                         temp.append(a[i][j])
#                 arr.append(temp)
#         return arr
#     def rows(array,ans):
#         if not array: return ans
#         if len(array)==1: return append(array,ans)
#         for i,j in enumerate(array):
#             if i==0:
#                 append(j,ans)
#             if i==len(array) - 1:
#                 j= j[::-1]
#                 append(j,ans)
#             elif len(j)>1:
#                 ans.append(j[-1])
#                 ans.append(j[0])
#             else: ans.append(j[0])
#         return rows(getnext(array),ans)
#
#     return rows(array,ans)
#
# print(spiralTraverse(a))
#
#
#
#
#
