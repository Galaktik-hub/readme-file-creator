#!/usr/bin/python3
'''
This program lets you create freely a README file for your GitHub profile or your projects.

Throught a graphical interface, you can type in your text and the way you want to formate it.

Once you're done creating your README file, you can press the 'Finished!' button and it will create the file in your current directory.

In the commentary of the README, there will always be a credit to this program, I do not restreint you to remove it, thought crediting someone for their work is always good!
'''
##########################################
#           IMPORTING SECTION            #
##########################################
#import PySimpleGUI as sg
import tkinter
import os
##########################################
#               GLOBAL VAR               #
##########################################
TYPE_FORMAT = {
    'header1' : ['# ', ''],
    'header2' : ['## ', ''],
    'header3' : ['### ', ''],
    'normal' : ['', ''],
    'line_break' : ['', '\n'],
    'bold' : ['**', '**'],
    'italic' : ['__', '__'],
    'crossed' : ['~~', '~~'],
    'bolditalic' : ['***', '***'],
    'sub' : ['<sub>', '</sub>'],
    'sup' : ['<sup>', '</sup>'],
    'quote' : ['> ', '\n'],
    'code' : ['\n```\n', '\n```\n'],
    'comment': ['<!--', '-->']
    }
##########################################

#TODO: Implement every functionnality that markdown offers (Maybe not the 3D model though) https://docs.github.com/fr/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
#TODO: Implement a graphical interface. Using tkinter ? Or rather PySimpleGUI ?
#TODO: Show how the text is interpreted in a window or a sub-section of the main window
#TODO: Add credit at the beginning (In a commentary)
#TODO: Once all the text is done, write it in a file


if __name__ == '__main__':

    writing = list()    # We're going to append every line and type of format wanted in this list

    while True:
        ask_type = input('What kind of thing do you want to write ? ')
        if ask_type == 'write':
            break
        elif ask_type == 'line_break':
            ask_texte = ''
        else:
            ask_texte = input('Insert your text: ')
        
        writing.append(TYPE_FORMAT[ask_type][0] + ask_texte)    # Writing the start of your line with the said text

        if ask_type in ['comment', 'code']: # If you're writing something that goes on multiple lines, it asks you if you want to continue to write in the said section
            while True:
                ask_texte = input(f'Any more text in the {ask_type} section ? ')
                if ask_texte == 'close':
                    break
                writing[len(writing)-1] += '\n' + ask_texte

        writing[len(writing)-1] += TYPE_FORMAT[ask_type][1] # Writing the closing argument

    # This is the part where everything you wrote is going to be put into a README.md file
    with open('README_test.md', 'w') as file:
        file.write('<!--\n')
        file.write('Thank you for using my program, it really means a lot to me!\n')
        file.write('If you have any question, suggestion, or you just want to say hi, don\'t hesitate to check my GitHub page: https://github.com/Galaktik-hub\n')
        file.write('Don\'t forget to leave the repository of this project a star!\n')
        file.write('-->\n')
        file.write('\n')
        for line in writing:
            file.write(line)
        