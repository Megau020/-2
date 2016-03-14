#writher gu peng
#edit date 20160312

from fractions import Fraction#分数
from random import randint#随机数

def layer(layer_accual2,operat_number2,brackets2,layer_amount2):#递归程序


    if(layer_accual2>0):#对第一层开始计算，将形成3个以上的数字，层数暂时为设定的3。
         #选择数字标号
        #print"layer_accual2",layer_accual2
        opreation_radom=randint(0,layer_accual2-1)#第一层加1，抽取号码，进行替换
        find_operat_number=operat_number[opreation_radom]
        #即两个数中选择一个数进行替换成为一个简单的四则二元运算
        #print "operater_num",operater_num
        #将选中的数字从第二层开始，用一个简单的二元运算式替换选中的数字，并插入数组
        #插入时依据数字编号判断是否加入括号，依据此数字所在的周围是否有*\符号
        #判断是否有添加括号
        if((operator[opreation_radom]=="/")or(operator[opreation_radom]=="*")or(operator[opreation_radom+1]=="/")or(operator[opreation_radom+1]=="*")):#判断选中数字周围的符号
            brackets[layer_accual2]=1
        if(multiplication_and_division==2):
            brackets[layer_accual2]=0


    operater_num=randint(1,multiplication_and_division)  #将运算符入数组
    operator_one="?"
    if(operater_num==1):
        operator_one="+"
    if(operater_num==2):
        operator_one="-"
    if(operater_num==3):
        operator_one="*"
    if(operater_num==4):
        operator_one="/"
        
    if(layer_accual2==0):
        operator[1]=operator_one
    else:
        
        mov_amount=layer_accual2+2-opreation_radom
        for i in range(0,mov_amount):
            operator[layer_accual2+2-i]=operator[layer_accual2+2-i-1]
            #print"i",i 
        operator[opreation_radom+1]=operator_one
        
    zhen_zheng=randint(1,2)  #是真分数或者整数，随机
    if(fraction_exist==0):
        zhen_zheng=1
    if(zhen_zheng==1):          #产生第一个数字 
        first_num=randint(0,number_range)
        first_num=str(first_num)
    else:
        first_num1=2
        first_num2=1
        while (first_num1>=first_num2):
            first_num1=randint(1,number_range)
            first_num2=randint(1,number_range)
        first_num=Fraction(first_num1,first_num2)
        if(first_num!=0):
            first_num="("+str(first_num)+")"        
        first_num=str(first_num)
    zhen_zheng=randint(1,2)  #是真分数或者整数，随机
    if(fraction_exist==0):
        zhen_zheng=1
    if(zhen_zheng==1):          #产生第二个数字 
        second_num=randint(0,10)
        second_num=str(second_num)
    else:
        second_num1=2
        second_num2=1
        while (second_num1>=second_num2):
            second_num1=randint(1,number_range)
            second_num2=randint(1,number_range)
        second_num=Fraction(second_num1,second_num2)
        if(second_num!=0):
            second_num="("+str(second_num)+")"  

    if(layer_accual2==0):#第0层，将最开始的两个数字存入数组
        operat_number[0]=first_num
        operat_number[1]=second_num
        if(negative_exit==0):#(如果不存在负数)
            if(second_num>first_num and operator_one==2):
                while(second_num>=first_num):
                    second_num=randint(1,number_range)
                    
        if(remainder==0):#(如果不存在余数)
           if(operator_one==4):
                while(second_num%first_num!=0):
                    print"remainder"
                    second_num=randint(1,number_range)




    #从第一层开始存入两个数字
    if(layer_accual2>0):
        mov_amount=layer_accual2+2-opreation_radom
        for i in range(0,mov_amount):
            operat_number[layer_accual2+1-i]=operat_number[layer_accual2+1-i-1]
        operat_number[opreation_radom]=first_num
        operat_number[opreation_radom+1]=second_num


    #整理算式
    if(layer_accual2==1):
        tempperate1=str(operat_number[0])
        tempperate2=str(operat_number[1])
        expressions=operat_number[0]+operator[1]+operat_number[1]
      
    if(layer_accual2>1):
        #先找到替换数字，然后产生表达式2，用2替换表达式1
        global expressions
        kk=str(operat_number[opreation_radom])
        expressions2=first_num+operator_one+second_num
        #创建一个查找机制，寻找不同的数字将其替换？
        #while(same_amount>0):
            
        expressions=expressions.replace(find_operat_number,expressions2)
        
    layer_accual2=layer_accual2+1
    if(layer_accual2<layer_amount2+1):
        layer(layer_accual2,operat_number2,brackets2,layer_amount2)


##############程序开始
expressions_amount=5#算式数量
layer_amount=2  #层数，即数的个数
number_range=10#整数数值的大小范围
fraction_exist=1#是否有分数
multiplication_and_division=2#是否有乘除，有则为4
negative_exit=0#负数是否存在，1存在
remainder=0#余数是否存在，1存在
pritenr=1#打印机模式
quit_num=1
#print "expressions_amount",expressions_amount
for counter1 in range(0,expressions_amount):
    #准备部分，执行参数，运算层数，运算到的层数
    layer_accual=0
    operator=['k']*(layer_amount+3)#记录运算符的记录
    operat_number=["?"]*(layer_amount+2)#记录运算数的记录器
    brackets=[0]*(layer_amount+1)#记录括号的存在标志
    operator[0]="?"
    operator[2]="?"
    layer(layer_accual,operat_number,brackets,layer_amount)
    #expressions_mul[counter1]=expressions#查重功能

while(quit_num==1):

    
    print"打印方式，1为屏幕显示，2为导出为txt文件"
    temp=input()
    while(temp!=1 and temp!=2):
        print"请重新输入"
        temp=input()
    pritenr=temp

    print"参数个数"
    layer_amount=input()-1
    
    print"是否有括号，支持十个参数参与计算,1为无括号，2为有括号"
    temp=input()
    while(temp!=1 and temp!=2):
        print"请重新输入"
        temp=input()
    multiplication_and_division=2*temp
        
    print"数值范围"
    number_range=input()
    
    print"加减有无负数,1为有负数，0为无负数"
    temp=input()
    while(temp!=0 and temp!=1):
        print"请重新输入"
        temp=input()
    negative_exit=temp


    print"加减有无分数,1为有分数，0为无分数"
    temp=input()
    while(temp!=0 and temp!=1):
        print"请重新输入"
        temp=input()
    fraction_exist=temp
        
    print"除法有无余数，1为有余数，0为无余数"
    temp=input()
    while(temp!=1 and temp!=0):
        print"请重新输入"
        temp=input()
    remainder=temp

    print"总数"
    expressions_amount=input()
    #expressions_mul="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"*expressions_amount
    #print expressions_mul
    print"start"
    for counter1 in range(0,expressions_amount):
        #准备部分，执行参数，运算层数，运算到的层数
        layer_accual=0
        operator=['k']*(layer_amount+3)#记录运算符的记录
        operat_number=["?"]*(layer_amount+2)#记录运算数的记录器
        brackets=[0]*(layer_amount+1)#记录括号的存在标志
        operator[0]="?"
        operator[2]="?"
        layer(layer_accual,operat_number,brackets,layer_amount)
        #expressions_mul[counter1]=expressions#查重功能
        if(pritenr==1):
            print expressions
        else:
            f = file('output.txt', 'a')
            f.write(expressions+"\n")
            #f.write(expressions)

    print"退出？0为退出，1为继续"
    temp=input()
    while(temp!=0 and temp!=1):
        print"请重新输入"
        temp=input()
    quit_num=temp
    
