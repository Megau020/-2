#writher gu peng
#edit date 20160309

from fractions import Fraction#分数
from random import randint#随机数


layer_amount=3  #准备部分，执行参数，运算层数，运算到的层数
layer_accual=0

operator=["k"]*(layer_amount+3)#运算符的记录
operat_number=["?"]*(layer_amount+3)#运算数的记录器
brackets=[0]*(layer_amount+1)#括号的存在标志
operator[0]="?"
operator[2]="?"
expressions="4"
opreation_radom2=[0]*(layer_amount+1)
def layer(layer_accual2,operat_number2,brackets2,layer_amount2):#递归程序
    
    if(layer_accual2>0):#对第一层开始计算，将形成3个以上的数字，层数暂时为设定的3。
        #选择数字标号
        #print"layer_accual2",layer_accual2
        opreation_radom=randint(0,layer_accual2)#第一层加1，抽取号码，进行替换
        opreation_radom2[layer_accual2]=opreation_radom
        find_operat_number=operat_number[opreation_radom]
        #即两个数中选择一个数进行替换成为一个简单的四则二元运算
        #print "opreation_num",opreation_num
        #将选中的数字从第二层开始，用一个简单的二元运算式替换选中的数字，并插入数组
        #插入时依据数字编号判断是否加入括号，依据此数字所在的周围是否有*\符号
        #判断是否有添加括号
        if((operator[opreation_radom]=="/")or(operator[opreation_radom]=="*")or(operator[opreation_radom+1]=="/")or(operator[opreation_radom+1]=="*")):#判断选中数字周围的符号
            brackets[layer_accual2]=1
            #print"(",

    opreation_num=randint(1,4)  #将运算符入数组
    operator_one="?"
    if(opreation_num==1):
        operator_one="+"
    if(opreation_num==2):
        operator_one="-"
    if(opreation_num==3):
        operator_one="*"
    if(opreation_num==4):
        operator_one="/"
    #operator_one

    #输出


    #整理算式
    if(layer_accual2==1):
        tempperate1=str(operat_number[0])
        tempperate2=str(operat_number[1])
        expressions=operat_number[0]+operator[1]+operat_number[1]
        #print"第一产生式",expressions
      
    if(layer_accual2>1):
        #先找到替换数字，然后产生表达式2，用2替换表达式1
        global expressions
        kk=str(operat_number[opreation_radom])
        expressions2=operat_number[opreation_radom]+operator[opreation_radom]+operat_number[opreation_radom-1]
        #print "expressions2",expressions2
        expressions=expressions.replace(find_operat_number,expressions2)
        #print "表达式",expressions


    if(layer_accual2==0):
        operator[1]=operator_one
    else:
        mov_amount=layer_accual2+2-opreation_radom
        opreation_radom=opreation_radom+1
        for i in range(0,mov_amount):
            operator[layer_accual2+2-i]=operator[layer_accual2+2-i-1]
        operator[opreation_radom]=operator_one

            
    zhen_zheng=randint(1,2)  #是真分数或者整数，随机
    if(zhen_zheng==1):          #产生第一个数字 
        first_num=randint(0,10)
        first_num=str(first_num)
    else:
        first_num1=2
        first_num2=1
        while (first_num1>=first_num2):
            first_num1=randint(1,10)
            first_num2=randint(1,10)
        first_num=Fraction(first_num1,first_num2)
        if(first_num!=0):
            first_num="("+str(first_num)+")"        
        first_num=str(first_num)
    zhen_zheng=randint(1,2)  #是真分数或者整数，随机
    if(zhen_zheng==1):          #产生第二个数字 
        second_num=randint(0,10)
        second_num=str(second_num)
    else:
        second_num1=2
        second_num2=1
        while (second_num1>=second_num2):
            second_num1=randint(1,10)
            second_num2=randint(1,10)
        second_num=Fraction(second_num1,second_num2)
        if(second_num!=0):
            second_num="("+str(second_num)+")"  

    if(layer_accual2==0):#第0层，将最开始的两个数字存入数组
        operat_number[0]=first_num
        operat_number[1]=second_num


    #从第一层开始存入两个数字
    if(layer_accual2>0):
        mov_amount=layer_accual2+2-opreation_radom
        for i in range(0,mov_amount):
            operat_number[mov_amount-i]=operat_number[mov_amount-i-1]
        operat_number[opreation_radom]=first_num
        operat_number[opreation_radom+1]=second_num


        
    #输出段
    layer_accual2=layer_accual2+1
    if(layer_accual2<layer_amount2+1):
        layer(layer_accual2,operat_number2,brackets2,layer_amount2)
    layer_accual2=layer_accual2-1
    #递归结束，往回整理算式

    

layer(layer_accual,operat_number,brackets,layer_amount)
#print opreation_radom2
print "表达式",expressions
#print'ok'
