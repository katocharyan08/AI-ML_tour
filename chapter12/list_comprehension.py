l = [1,2,3,4,5,6,7]

# squareList = []
#
# for item in l:
#     squareList.append(item*item)
#
# print(squareList)

squareList = [i*i for i in l]
print(squareList)

l2 = [item for item in l if item > 5]
print(l2)