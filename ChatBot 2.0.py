import random
import time
import tkinter
from tkinter import *

mainroot=tkinter.Tk()
mainroot.title("ChatBot")
#mainroot.geometry('450x550')
r=0
def StartChatBot():
#######################################################################################################
    mainroot.destroy()
    root=tkinter.Tk()
    root.title("ChatBot")
    root.geometry('450x550')
    #root.configure(background='yellow')
                
    label=tkinter.Label(root,text="Enter your msg : ",font="Times 15")
    label.grid(row=0,column=0)
    user=tkinter.Entry(root,width=30)
    user.grid(row=0,column=1)

    class database:       #AGENT FUNCTION
        def __init__(self,row,column,data):
            self.row=row
            self.column=column
            self.data=data
        
        def fetch(self):
            if(self.data==1):
                col=["madhya_pradesh","uttar_pradesh","punjab","bihar","chhattisgarh","goa","gujarat","haryana","himachal pradesh"]
                ro=["temperature","capital","cm","places","population"]
                rowIndex=ro.index(self.row)
                columnIndex=col.index(self.column)
                return (rowIndex,columnIndex)
            elif(self.data==2):
                col1=["year","actor","actress","budget","collection","ratings","verdict"]
                ro1=["bahubali","kgf","dabangg","chappak","good_newz","padmavat","simba"]
                rowIndex=ro1.index(self.column)
                columnIndex=col1.index(self.row)
                return (rowIndex,columnIndex)     
    db=[
        [["20 degree celcius"],["17 degree celcius"],["11 degree celcius"],["21 degree celcius"],["15 degree celcius"],
        ["27 degree celcius"],["28 degree celcius"],["10 degree celcius"],["14 degree celcius"]],
        [["bhopal"],["lucknow"],["chandigarh"],["city1"],["city2"],["city3"],["city4"],["city5"],["city6"]],
        [["person1"],["person2"],["person3"],["person4"],["person5"],["person6"],["person7"],["person8"],["person9"]],
        [["bhopal,indore,shipuri"],["lucknow,varanasi,jhansi"],["amritsar"],["place4"],["place5"],["beach"],["ahemdabad"],["place7"],["dehradun"]],
        [["2billion"],["2.3billion"],["1.6billion"],["1.9billion"],["0.8billion"],["0.1billion"],["1.4billion"],["1.2billion"],["1.8billion"]]   
        ]   
    db1=[[["2016"],["prabas"],["anushka shetty"],["180cr"],["700cr"],["4.1"],["blockbuster"]],
        [["2018"],["yash"],["shidhi shetty"],["120cr"],["500cr"],["4.5"],["blockbuster"]],
        [["2019"],["salman khan"],["sunakshi sinha"],["90cr"],["170cr"],["2.1"],["hit"]],
        [["2020"],["none"],["deepika padukon"],["65cr"],["80cr"],["3.6"],["average"]],
        [["2019"],["akshay kumar"],["kareena kapoor"],["68cr"],["160cr"],["3.2"],["hit"]],
        [["2017"],["ranvir singh"],["deepika padukon"],["150cr"],["250cr"],["4.3"],["hit"]],
        [["2019"],["ranvir singh"],["sara ali khan"],["60cr"],["65cr"],["1.6"],["below average"]]
        ]
      
    r=0
    class chat:
        def __init__(self,userInput):
            self.sentence=userInput
        def startfunc(self):
            global r
            r+=1
            label=tkinter.Label(root,text=self.sentence,fg="red",font="Times 10")
            label.grid(row=r,column=0)

        def greetUser(self):
            global r
            greet_Response=["hello","hi","hey", "superb bro","namaste"]
            label=tkinter.Label(root,text=(random.choice(greet_Response)),fg="green",font="Times 10")
            label.grid(row=r+1,column=2)

        def endUserChat(self):
            global r
            greet_exit_response=["bye","nice to meet you", "see you later","thanks for talking","have a good day"]
            label=tkinter.Label(root,text=(random.choice(greet_exit_response)),fg="green",font="Times 10")
            label.grid(row=r+1,column=2)
            def kill():
                root.destroy()
            button=tkinter.Button(root,text="Exit",command=kill,width=15)
            button.grid(row=r+2,column=0)
            r+=1

        def findAnswer(self):
            global r
            self.sentence=self.sentence.split()
            unneccessary=["is","in","what","how","why","tell","me","the","?","of","who","when","was","which"]
            arr=[0,0]
            for i in self.sentence:     #percepts
                if(i not in unneccessary):
                    if(i=="capital" or i=="temperature" or i=="cm" or i=="places" or i=="population" or
                        i=="year" or i=="actor" or i=="actress" or i=="budget" or i=="collection" or i=="ratings" or i=="verdict"):
                        arr[0]=(i)
                    else:
                        arr[1]=i

            if(arr[0]=="capital" or arr[0]=="temperature" or arr[0]=="cm" or arr[0]=="places" or arr[0]=="population"):
                obj=database(arr[0],arr[1],1)
                row,column=obj.fetch()
                label=tkinter.Label(root,text=(db[row][column]),fg="green",font="Times 10")

            elif(arr[0]=="year" or arr[0]=="actor" or arr[0]=="actress" or arr[0]=="budget" or arr[0]=="collection" or
                     arr[0]=="ratings" or arr[0]=="verdict"):
                    obj=database(arr[0],arr[1],2)
                    row,column=obj.fetch()
                    label=tkinter.Label(root,text=(db1[row][column]),fg="green",font="Times 10")
            label.grid(row=r+1,column=2)
           
        def randomAnswer(self):          #RANDOM AGENT
            global r
            random_Response=["i did'nt get", "sorry!"] 
            label=tkinter.Label(root,text=(random.choice(random_Response)),fg="green",font="Times 10")
            label.grid(row=r+1,column=2)
            

    def chatbutton():                         #ENVIRONMENT AND OBJECT
        global r
        statement=user.get()
        statement=statement.lower()
        obj2=chat(statement)
        #obj2.conversation()
        obj2.startfunc()
        greet_Keywords=["hello","hey","hi","what's up","hi there"]
        greet_exit_query=["bye","thanks","thanks alot"]
        if(statement in greet_Keywords):
            obj2.greetUser()
        elif(statement in greet_exit_query):
            obj2.endUserChat()
        elif(("capital" in statement) or ("temperature" in statement) or ("places" in statement) or
                 ("population" in statement) or ("year" in statement) or ("actor" in statement) or
                 ("actress" in statement) or ("budget" in statement) or ("collection" in statement)  or
                 ("ratings" in statement) or ("verdict" in statement)):
            obj2.findAnswer()
        else:
            obj2.randomAnswer()
        r+=1

    button = tkinter.Button(root, text='Send', width=15,command=chatbutton)

    button.grid(row=0,column=2)
    root.mainloop()

########################################################################################################
button = tkinter.Button(mainroot, text='START',font="Times ",width=45,height=5,command=StartChatBot,bg="pink")
button.grid(row=0,column=0)
mainroot.mainloop()

