#writher gu peng
#edit date 20160309

from fractions import Fraction#����
from random import randint#�����


layer_amount=3  #׼�����֣�ִ�в�����������������㵽�Ĳ���
layer_accual=0

operator=["k"]*(layer_amount+3)#������ļ�¼
operat_number=["?"]*(layer_amount+3)#�������ļ�¼��
brackets=[0]*(layer_amount+1)#���ŵĴ��ڱ�־
operator[0]="?"
operator[2]="?"
expressions="4"
opreation_radom2=[0]*(layer_amount+1)
def layer(layer_accual2,operat_number2,brackets2,layer_amount2):#�ݹ����
    
    if(layer_accual2>0):#�Ե�һ�㿪ʼ���㣬���γ�3�����ϵ����֣�������ʱΪ�趨��3��
        #ѡ�����ֱ��
        #print"layer_accual2",layer_accual2
        opreation_radom=randint(0,layer_accual2)#��һ���1����ȡ���룬�����滻
        opreation_radom2[layer_accual2]=opreation_radom
        find_operat_number=operat_number[opreation_radom]
        #����������ѡ��һ���������滻��Ϊһ���򵥵������Ԫ����
        #print "opreation_num",opreation_num
        #��ѡ�е����ִӵڶ��㿪ʼ����һ���򵥵Ķ�Ԫ����ʽ�滻ѡ�е����֣�����������
        #����ʱ�������ֱ���ж��Ƿ�������ţ����ݴ��������ڵ���Χ�Ƿ���*\����
        #�ж��Ƿ����������
        if((operator[opreation_radom]=="/")or(operator[opreation_radom]=="*")or(operator[opreation_radom+1]=="/")or(operator[opreation_radom+1]=="*")):#�ж�ѡ��������Χ�ķ���
            brackets[layer_accual2]=1
            #print"(",

    opreation_num=randint(1,4)  #�������������
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

    #���


    #������ʽ
    if(layer_accual2==1):
        tempperate1=str(operat_number[0])
        tempperate2=str(operat_number[1])
        expressions=operat_number[0]+operator[1]+operat_number[1]
        #print"��һ����ʽ",expressions
      
    if(layer_accual2>1):
        #���ҵ��滻���֣�Ȼ��������ʽ2����2�滻���ʽ1
        global expressions
        kk=str(operat_number[opreation_radom])
        expressions2=operat_number[opreation_radom]+operator[opreation_radom]+operat_number[opreation_radom-1]
        #print "expressions2",expressions2
        expressions=expressions.replace(find_operat_number,expressions2)
        #print "���ʽ",expressions


    if(layer_accual2==0):
        operator[1]=operator_one
    else:
        mov_amount=layer_accual2+2-opreation_radom
        opreation_radom=opreation_radom+1
        for i in range(0,mov_amount):
            operator[layer_accual2+2-i]=operator[layer_accual2+2-i-1]
        operator[opreation_radom]=operator_one

            
    zhen_zheng=randint(1,2)  #��������������������
    if(zhen_zheng==1):          #������һ������ 
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
    zhen_zheng=randint(1,2)  #��������������������
    if(zhen_zheng==1):          #�����ڶ������� 
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

    if(layer_accual2==0):#��0�㣬���ʼ���������ִ�������
        operat_number[0]=first_num
        operat_number[1]=second_num


    #�ӵ�һ�㿪ʼ������������
    if(layer_accual2>0):
        mov_amount=layer_accual2+2-opreation_radom
        for i in range(0,mov_amount):
            operat_number[mov_amount-i]=operat_number[mov_amount-i-1]
        operat_number[opreation_radom]=first_num
        operat_number[opreation_radom+1]=second_num


        
    #�����
    layer_accual2=layer_accual2+1
    if(layer_accual2<layer_amount2+1):
        layer(layer_accual2,operat_number2,brackets2,layer_amount2)
    layer_accual2=layer_accual2-1
    #�ݹ����������������ʽ

    

layer(layer_accual,operat_number,brackets,layer_amount)
#print opreation_radom2
print "���ʽ",expressions
#print'ok'
