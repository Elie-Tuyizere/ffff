import random
print("-"*50)
print("|","     Game"  ,"Raund:1                               |")
print("-"*50)

score=0
for n in range(2):
 for i in range (3):
    num1=random.randint(1,50)
    num2=random.randint(1,50)
    result=num1+num2
    print(num1,"+",num2,"=")
    resul=int(input("enter answer"))
    if result==resul:
      score=score+1
      print("score",score,"/3 marks")
    else:
        print("score is false",score,"/3mark")
    if score==3:
        print("winner contiue next Raund:2")  
        print("raund:2")
        score=3
for i in range (3):
    num1=random.randint(1,50)
    num2=random.randint(1,50)
    result=num1+num2
    print(num1,"*",num2,"=")
    resul=int(input("enter answer"))
    if result==resul:
      score+=1
      print("score",score,"/6 marks")
    else:
        print("srore is false",score,"/6mark")