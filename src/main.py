print('你好，世界')
list = [i for i in range(1, 10)]
print(list)
new_list = [('张三' + str(i)) for i in list if i < 5]
print(new_list)
