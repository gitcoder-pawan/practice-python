# # n=[1,2,3,4]
# # f=n*3
# # print(f)
# # n=9
# # init_list = list(range)
# # final_list = [] +init_list
# # print(final_list)
# # print(final_list)
# # test_string = "xxx" + " " * n + "xxx"
# # split_list = test_string.split(" ")
# # print(split_list)
# # print(len(split_list))
# sum=0
# list1=list(range(123))
# list2=list(range(77))
# list3=list1+list2
# # print(list3)
# for i in list3:
#     if i%3 != 0:
#         sum=sum+i
#
# print(sum)
# def leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# def days_in_month(month):
#     if month == 1 or month == 3 or month == 5 or month == 7 \
#     or month == 8 or month == 10 or month == 12:
#         return month == 31
#     elif month == 2:
#         if leap_year(year):
#             return 29
#         else:
#             return 28
#     else:
#         return 30
def leap(n):
    if n<1100:
        return "enter valid date"
    elif (n%400==0) or  (n%4==0 and n%100!=0 ):
        return "leap yrr"
    return "not a leap yr"
print(leap(int(input("enter yr: "))))