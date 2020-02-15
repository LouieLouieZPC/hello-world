#-*-coding:utf-8-*-

dict1={'小明':'广州','小红':'深圳','小王':'北京'} 
x=int(input('输入数字1进行好友添加，输入数字2删除好友，输入数字3进行好友信息修改,输入数字4进行好友信息查询：'))
while True:
    if  x==1:
        dict_1=input('请输入添加的姓名：')
        dict_2=input('请输入添加的地址：')
        dict1[dict_1]=dict_2
        print(dict1)
        break
    elif x==2:
        del_name=input('请输入要删除好友的姓名：')
        del dict1[del_name]
        print(dict1)
        break
    elif x==3:
        alter_name=input('请输入要修改好友的姓名：')
        alter_address=input('请输入更改后的地址：')
        dict1[alter_name]=alter_address
        print(dict1)
        break
    elif x==4:
        ask_name=input('请输入要查询好友的姓名：')
        get_dates=dict1.get(ask_name)
        print(get_dates)
        break