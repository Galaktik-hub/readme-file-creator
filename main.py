#!/usr/bin/python3
'''
This program lets you create freely a README file for your GitHub profile or your projects.

Throught a graphical interface, you can type in your text and the way you want to formate it.

Once you're done creating your README file, you can type the 'Finished!' button and it will create the file in your current directory.

In the footer of the README, there will always be a credit to this program, I do not restreint you to remove it, thought crediting someone for their work is always good!
'''
##########################################
#           IMPORTING SECTION            #
##########################################
import PySimpleGUI as sg
import tkinter
import os
##########################################
#               GLOBAL VAR               #
##########################################
TYPE_FORMAT = ['header1', 'header2', 'header3', 'normal', 'line_break']
TYPE_FORMAT_FOR_FILE = ['#', '##', '###', '', '']
##########################################

#TODO: Implement every functionnality that markdown offers (Maybe not the 3D model thought) https://docs.github.com/fr/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
#TODO: Implement a graphical interface. Using tkinter ? Or rather PySimpleGUI ?
#TODO: Find a way to show how it is interpreted in a window or a sub-section of the main window
#TODO: Add credit at the end (in a footer)
#TODO: Once all the text is done, write it in a file




if __name__ == '__main__':

    writing = list()    # We're going to append every line and type of format wanted in this list

    while True:
        ask_type = input('What kind of thing you want to write ? ')
        if ask_type == 'write':
            break
        if ask_type == 'line_break':
            ask_texte = ''
        else:
            ask_texte = input('Insert your text: ')
        writing.append((TYPE_FORMAT.index(ask_type), ask_texte))
    with open('README_test.md', 'w') as file:
        for line in writing:
            file.write(TYPE_FORMAT_FOR_FILE[line[0]] + line[1] + '\n')
        