# d={}
# d[1]="pawan"
# d["age"]=20
# # print(d)
# for i in d:
     # print(d[i])
# a={
# n=int(input("enter no of keys: "))
# def cubefinder(n):
#     return {i:i**100 for i in range(1,n+1)}
# print(cubefinder(n))
#
# n= input("enter your string: ")
# def word_counter(string):
#     return {i:string.count(i) for i in string}
# print(word_counter(n))


# n=int(input("enter no of keys: "))
# user_info={}
# for i in range(n):
#     keys=input(f"key{i+1} = ")
#     values=input(f"give comma if u have multiple value{i+1} = ").split(",")
#     if len(values)==1:
#         # a="check"
#         # b=5
#         if type(values[0])==type("str"):
#             values=values[0]
#         elif values[0].isdigit():
#             values=int(values[0])
#     user_info.update({keys:values})
# print(user_info)
# for k,v in user_info.items():
#     print(f"{k} : {v}")

# n=int(input("enter no of elements: "))
# lst=[input(f"enter {i+1} element: ") for i in range(n)]
# print("reverse of list is ",[i[::-1] for i in lst])
# dict1={
#     "hn":"pawan","age":20,"roll":10,
#     "hn":"rawan","age":30,"roll":50,
#     "hn":"sawan","age":40,"roll":20,
#     }
# sorted_dict=sorted(dict1,key=dict1['age'])
# print(sorted_dict)

#unpacking zipped function
# l1=[1,4,5,7,9]
# l2=[2,1,7,8,1]
# l3=zip(l1,l2)
# print([max(pair) for pair in l3])
# average=lambda *args:[round(sum(i)/len(i),3) for i in zip(*args)]
# print(average([1,2,3],[2,3,4],[4,5,6]))
# list=[]
# for i in range(3):
# list=[[int(input(f"{i}")) for i in range(3)] for i in range(3)]
# print(list)
# print(average(*list)
n = int(input())
arr = map(int, input().split())
print(arr)