#-*-coding:utf-8-*-

dict1={'小明':'广州','小红':'深圳','小王':'北京'} 
x=input('输入数字1进行好友添加，输入数字2删除好友，输入数字3进行好友信息修改,输入数字4进行好友信息查询')
if  x=1:
    dict_1=input('请输入姓名：')
    dict_2=input('请输入电话：')
    dict_3=input('请输入地址：')
    dict2=dict_1,dict_2,dict_3
    dict1.update(dict2)
elif x=2:
    del_name=input('请输入要删除好友的姓名：')
    del dict1[del_name]
elif x=3:
    alter_name=input('请输入要修改好友的姓名：')
    alter_name1=input('输入更改姓名：')
    alter_address1=input('请输入更改地址：')
    dict[alter_name]='alter_name1','alter_address1'
elif x=4:
    ask_name=input('请输入要查询好友的姓名：')
    dict1.get('ask_name')
