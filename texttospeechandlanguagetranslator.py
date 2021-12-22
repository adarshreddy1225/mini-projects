
from tkinter import *
from gtts import gTTS
from playsound import playsound
from googletrans import Translator , LANGUAGES from tkinter import ttk
# object of tkinter
# and background set for white
module = Tk() module.geometry('500x550') module.configure(bg = 'white') module.title('Adarsh ­ TEXT_TO_SPEECH')
# Variable Classes in tkinter result = StringVar();
# Creating label for each information
# name using widget Label
# Creating lebel for class variable
Label(module,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=300,y=50) Input_text = Text(module,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)
Label(module,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60) Output_text = Text(module,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)
language = list(LANGUAGES.values())
src_lang = ttk.Combobox(module, values= language, width =22) src_lang.place(x=20,y=60)
src_lang.set('choose input language')
dest_lang = ttk.Combobox(module, values= language, width =22) dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')
##text variable
e = Entry(module, width = 50) e.place(x=185, y=70)
def Text_to_speech(): Text = e.get() language='en',
'af' #afrikaans, 'sq'#albanian', 'am'#amharic, 'ar'#arabic, 'hy'#armenian, 'az'#azerbaijani, 'eu'#basque, 'be'#belarusian, 'bn'#bengali, 'bs'#bosnian,'bg'#bulgarian,
'ca'#catalan,'id'#indonesian, 'ga'#irish,
'it'#italian, 'ja'#japanese, 'jw'#javanese, 'kn'#kannada, 'kk'#kazakh, 'km'#khmer, 'ko'#korean, 'ku'#kurdish (kurmanji), 'ky'#kyrgyz,
'lo'#lao,
'la'#latin,
'lv'#latvian,
'lt'#lithuanian, 'lb'#luxembourgish, 'mk'#macedonian, 'mg'#malagasy, 'ms'#malay, 'ml'#malayalam, 'mt'#maltese,
'mi'#maori,
'mr'#marathi, 'mn'#mongolian, 'my'#myanmar (burmese), 'ne'#nepali, 'no'#norwegian,
'or'#odia, 'ps'#pashto, 'fa'#persian, 'pl'#polish, 'pt'#portuguese, 'pa'#punjabi,
'ceb'#cebuano, 'ny'#chichewa, 'zh­cn'#chinese (simplified), 'zh­tw'#chinese (traditional), 'co'#corsican,
'hr'#croatian, 'cs'#czech, 'da'#danish, 'nl'#dutch, 'en'#english, 'eo'#esperanto, 'et'#estonian, 'tl'#filipino, 'fi'#finnish, 'fr'#french, 'fy'#frisian, 'gl'#galician, 'ka'#georgian, 'de'#german, 'el'#greek, 'gu'#gujarati, 'ht'#haitian creole, 'ha'#hausa, 'haw'#hawaiian, 'iw'#hebrew ' 'he'#hebrew, 'hi'#hindi, 'hmn'#hmong, 'hu'#hungarian, 'is'#icelandic, 'ig'#igbo,
'ro'#romanian, 'ru'#russian, 'sm'#samoan, 'gd'#scots gaelic, 'sr'#serbian, 'st'#sesotho, 'sn'#shona, 'sd'#sindhi, 'si'#sinhala, 'sk'#slovak, 'sl'#slovenian, 'so'#somali, 'es'#spanish, 'su'#sundanese, 'sw'#swahili, 'sv'#swedish, 'tg'#tajik, 'ta'#tamil, 'te'#telugu, 'th'#thai, 'tr'#turkish, 'uk'#ukrainian, 'ur'#urdu, 'ug'#uyghur,
'uz' #uzbek, 
'vi' #vietnamese, 'cy'#welsh, 'xh'#xhosa, 'yi'#yiddish, 'yo'#yoruba, 'zu'#zulu
speech = gTTS(text=Text) speech.save('Adarsh.mp3') playsound('ADarsh.mp3')
def Exit(): module.destroy()
def Translate():
translator = Translator()
translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest =
dest_lang.get())
Output_text.delete(1.0, END) Output_text.insert(END, translated.text)
def Reset(): result.set("")
# creating a button using the widget
# Button that will call the submit function
Button(module, text ="PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=50, y=440)
Button(module,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=110,y=440)
Button(module, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =440) trans_btn = Button(module, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 490, y = 180)
module.mainloop()