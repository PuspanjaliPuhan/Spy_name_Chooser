#import
from guizero import App,Text,PushButton
from random import choice
#Functios
def choose_name():
    # print("Button was pressed")
    first_names = ["Barbara","Woody","Tiberius","Smokey","Jennifer","Ruby"]
    last_names = ["Spindleshanks","Mysterioso","Dungeon","Catseye","Darkmeyer","Flamingobreath"]
    spy_name= choice(first_names)+" "+choice(last_names)
    # print(spy_name)
    name.value= spy_name


#App
app=App(title='Top Secret!!')
app.bg='#228B22 '

#Widgets
title=Text(app,'Press the button to find out your Spy Name.')
title.text_size=15
button=PushButton (app,choose_name,text='Tell Me??')
button.bg='#FF7F50'
button.text_size=20
button.text_color='#ffffff'
name=Text(app,text=" ")

app.display()