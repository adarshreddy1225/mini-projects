# TexttoSpeechAndLanguageTranslator-project
# introduction

A pleasant application where the client will be given buttons like play,reset and exit. The client can enter the content which he/she needs tochange over into a speech or System generated voice.The Application takes contribution from the client and converts the accompanying content to speech or PC generated voice with the assistance of a button called play. A reset button and Exit button arelikewise given to the client to reset the application or to leave the application.The Tkinter GUI framework in python is utilized to make the design andlayout of the application.
    


# create framework
To introduce necessary modules, use pip command. Bringing the modules.
showcasing the GUI window (Tkinter). Characterizing the capacities.

➢ Import Libraries
• Start by bringing in the libraries, tkinter, playsound, gTTS

Introducing window:
- Tk() to introduced tkinter which will be utilized for GUI
- geometry() used to set the width and stature of the window
- configure() used to get to window ascribes
- bg will used to set the shade of the foundation
- title() set the title of the window
- Label() widget is utilized to show at least one than one line of text that clients can't ready to adjust.
- module is the name which we allude to our window
- text which we show on the mark
- font in which the content is composed
- pack organized gadget in block
- result is a string type variable
- Entry() used to make an information text field
wrap = WORD will stop the line after the final word that will fit.
- place() organizes gadgets by setting them in a particular situation in the parent gadget
- Message variable will stores the estimation of entry_field
- text is the sentences or text to be perused.
- lang takes the language to peruse the content. The default language is English.
- speech stores the changed over voice from the content
- speech.save('ADARSH.mp3') will saves the changed over record as adarsh as mp3 document
- playsound() used to play the sound
- Characterize Combobox to choose the language
language gets all the qualities from the 'Dialects' word reference as a rundown. ttk.Combobox() gadget is a class of ttk modules. It is a drop-down list, which can hold multi- worth and show each thing in turn. Combobox is helpful to choose one alternative from numerous choice.

Characterize Function to translate.
The Translate capacity will interpret the message and give the yield.
src gets the language chosen as information text language
dest gets the language select to decipher
text gets the information text entered by the user."1.0′′ implies that the info ought to be perused from zero characters to line one
The END part intends to peruse the content until the end is reached
translator = Translator() used to make a Translator class object
Output_text.delete(1.0, END) erase all the content from line one to end
Output_text.insert (END, translated.text) will embed the deciphered content in Output_text
Make an translate button
At the point when we click on the Translate button it will call the decipher work button() gadget used to show button on our window
command is called when we click the button
activebackground sets the foundation tone to utilize when the catch is dynamic

Function to Exit:
module.destroy() will quit the program by halting the mainloop().

Function to Reset:
Reset function set Msg variable to purge strings.

Characterize Buttons:
Button() widget used to show button on the window
module.mainloop() is a technique that executes when we need to run our program.



# System Design

1. The programming language to be used is Python.
2. The python framework tkinter gui will be used to implement a graphical interface.
The application requires the client to enter a text .Then he/she must click on the play button which converts the text to a pc generated voice .
In this content TTS converter application ,client's are furnished with a choice to enter the necessary content that client needs to change over to a voice,i.e 'ENTER TEXT'
Client's will likewise be furnished with choices, for example, 'play' , 'rest', 'exit' .which will permit the client to play the content or reset the content or leave the application.
This application additionally permit clients to change over the information text of any language into any ideal language by tapping on button 'TRANSLATE' which makes it not the same as the remainder of tts converter applications
.
Background interface will be rendered using tkinter using various in­built python modules



# FEATURES:
• Customizable speech­specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
• Customizable text pre­processors which can, for example, provide pronunciation corrections.



