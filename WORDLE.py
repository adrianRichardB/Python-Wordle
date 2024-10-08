import PySimpleGUI as sg
from nltk.corpus import words
import random
setofwords=set(words.words())
L = ["start","house","mango","grape","twice",
     "movie","month","march","enjoy","chess",
     "sport","bring","build","ethic","there",
     "video","right","angle","value","daily","rated","order"]
def word_gen():                #We are generating a random word from the list 
    idx = random.randrange(0,len(L))
    word = L[idx]
    return word

def maine():
    round_count=1

    def check_al(b):
        for i in range (0,len(b)):
            if b[i] not in "abcdefghijklmnopqrstuvwxyz":  #We check each element of the input string if it contains a numeric
                return False
            
    def final(c):
        if check_al(c)== False:  #If numeric is present False
            window["err"].update('It cannot contain special characters',visible=True,background_color= "saddlebrown")
            return None
        if len(c)!=5:#If length is not equal to 5 False
            window["err"].update('It doesn\'t contain 5 letters',visible=True,background_color= "saddlebrown")
            return None
        if c not in setofwords:#If it isnt a real word
            window["err"].update('It\'s not word',visible=True,background_color= "saddlebrown")
            return None
        
        else:
            return True
        
    def compare(sword,a):
            for i in range (0,5):
                if a[i] in sword:            #round number + index
                    if a[i] == sword[i]:
                        window[str(round_count)+str(i)].update(background_color='green')
                        window[str(round_count)+str(i)].update(a[i].upper())
                    else:
                        window[str(round_count)+str(i)].update(background_color='orange')
                        window[str(round_count)+str(i)].update(a[i].upper())
                else:
                    window[str(round_count)+str(i)].update(background_color='grey')
                    window[str(round_count)+str(i)].update(a[i].upper())
            if sword==a:
                return True

    
    sword=word_gen()  
    si = (13, 3)
    sg.set_options(text_element_background_color="burlywood",font=("Arial",12,'bold'))


    l1 = [sg.Text("Round 1",background_color='saddlebrown',key='1',size=si),sg.Text(key='10',size=si),sg.Text(key='11',size=si),sg.Text(key='12',size=si),sg.Text(key='13',size=si),sg.Text(key='14',size=si)]
    l2 = [sg.Text("Round 2",background_color='wheat',key='2',size=si)      ,sg.Text(key='20',size=si),sg.Text(key='21',size=si),sg.Text(key='22',size=si),sg.Text(key='23',size=si),sg.Text(key='24',size=si)]
    l3 = [sg.Text("Round 3",background_color='saddlebrown',key='3',size=si),sg.Text(key='30',size=si),sg.Text(key='31',size=si),sg.Text(key='32',size=si),sg.Text(key='33',size=si),sg.Text(key='34',size=si)]
    l4 = [sg.Text("Round 4",background_color='wheat',key='4',size=si)      ,sg.Text(key='40',size=si),sg.Text(key='41',size=si),sg.Text(key='42',size=si),sg.Text(key='43',size=si),sg.Text(key='44',size=si)]
    l5 = [sg.Text("Round 5",background_color='saddlebrown',key='5',size=si),sg.Text(key='50',size=si),sg.Text(key='51',size=si),sg.Text(key='52',size=si),sg.Text(key='53',size=si),sg.Text(key='54',size=si)]
    l6 = [sg.Text("Round 6",background_color='wheat',key='6',size=si)      ,sg.Text(key='60',size=si),sg.Text(key='61',size=si),sg.Text(key='62',size=si),sg.Text(key='63',size=si),sg.Text(key='64',size=si)]
    

    col_layout = [l1,l2,l3,l4,l5,l6]

    sg.theme('DarkBrown3') 
    layout = [
        [sg.Titlebar("W O R D L E", key = 't1')],
        [sg.Text("RULES",text_color= "lavenderblush",size=(12,1),justification='center',expand_x=True)],
        [sg.Text(" ",background_color= "grey",size=(12,1),justification='left'),sg.Text("The letter is not in the word")],
        [sg.Text(" ",background_color= "orange",size=(12,1),justification='left'),sg.Text("The letter is in the word but in wrong place")],
        [sg.Text(" ",background_color= "green",size=(12,1),justification='left'),sg.Text("The letter is in the word and in right place")],
        [sg.Text("PICK PLAYER", key = 't2', visible = False)],   
        [sg.Column(col_layout,element_justification='center', expand_x=True)],
        [sg.Column([[sg.Input(size=(18,4),justification='center',key = "inp",do_not_clear=False)]],element_justification='center', expand_x=True)],
        [sg.Column([[sg.Text(font=("Arial",12,'bold'),size=(30,2),visible=False,justification='center',key = "err")],[sg.Button(key='rst',button_text="Reset",button_color="purple")]],element_justification='center', expand_x=True)],    
        [sg.Button(key='ext',button_text="Exit",button_color="purple")]
        
    ]

    window = sg.Window("demo",layout,size=(1000,700),finalize=True)


    window['inp'].bind("<Return>", "_Enter")

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            return False
            break 
        elif event == "inp" + "_Enter":
            aword = values["inp"].lower()
            if final(aword)==True:                
                if compare(sword,aword)!=True:
                    window['err'].update(visible=False)
                    round_count+=1
                    if round_count==7:
                        window["err"].update('GAME OVER\n The word is '+sword,visible=True,background_color='indianred',text_color='black')
                        window['inp'].update(visible=False)      
                else:
                    window["err"].update('YOU WON',visible=True,background_color='light green',text_color='black')
                    window['inp'].update(visible=False)
        elif event == "rst":
            window.close()
            return True
            break
        elif event == 'ext':
            window.close()
            return False
            break


while True:
    
    if maine()!=False:
        pass
    else:
        break


