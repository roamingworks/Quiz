questions=["1) what is the colour of apple",
           "2) what is the colour of grapes",
            "3) what is the colour of mango "]

options=[["1) red","2) yellow","3) purple"],        
         ["1) yellow","2)blue","3)purple"],
         ["1) green","2)yellow","3)blue"]]
 
answer=[1,3,2]

question_index=0

for question in questions:
    print(question,"\n","\n".join(options[question_index]))
    
    
    user=int(input("enter the option you selected: "))
    
    if user == answer[question_index]:
        
        print("your answer is right wohoooo!!!")
        print("\n===========")
    else:
        print("your answer is wrong poor!!!")
        
        print("\n===========")
        
    question_index += 1