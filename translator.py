from tkinter import *
from translate import Translator

Screen = Tk()
Screen.title("Language Translator")

inputLanguageChoice = StringVar()
translateLanguageChoice = StringVar()

languageChoices = {'Chinese','English', 'French', 'German', 'Hindi', 'Japanese', 'Russian', 'Spanish'}
inputLanguageChoice.set('Hindi')
translateLanguageChoice.set('English')

def Translate():
    translator = Translator(from_lang = inputLanguageChoice.get(), to_lang = translateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

inputLanguageChoiceMenu = OptionMenu(Screen, inputLanguageChoice, *languageChoices)
Label(Screen, text="Choose a Language").grid(row=0, column=1)
inputLanguageChoiceMenu.grid(row=1, column=1)

newLanguageChoiceMenu = OptionMenu(Screen, translateLanguageChoice, *languageChoices)
Label(Screen, text="Translated Language").grid(row=0, column=2)
newLanguageChoiceMenu.grid(row=1, column=2)

Label(Screen, text="Enter text").grid(row=2, column=0)
TextVar = StringVar()
TextBox = Entry(Screen, textvariable=TextVar).grid(row=2, column=1)

Label(Screen, text="Output text").grid(row=2, column=2)
OutputVar = StringVar()
TextBox = Entry(Screen, textvariable=OutputVar).grid(row=2, column=3)


B = Button(Screen,text="TRANSLATE",command=Translate, relief = GROOVE).grid(row=6,column=2,columnspan = 1)
mainloop()

