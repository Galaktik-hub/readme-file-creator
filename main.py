#!/usr/bin/python3
'''
This program lets you create freely a README file for your GitHub profile or your projects.

Throught a graphical interface, you can type in your text and the way you want to formate it.

Once you're done creating your README file, you can type the 'Finished!' button and it will create the file in your current directory.

In the commentary of the README, there will always be a credit to this program, I do not restreint you to remove it, thought crediting someone for their work is always good!
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
TYPE_FORMAT = ['header1', 'header2', 'header3', 'normal', 'line_break', 'bold', 'italic', 'crossed', 'bolditalic', 'sub', 'sup', 'quote', 'code']
TYPE_FORMAT_FOR_FILE_OPENING = ['# ', '## ', '### ', '', '', '**', '__', '~~', '***', '<sub>', '<sup>', '> ', '```\n']
TYPE_FORMAT_FOR_FILE_CLOSING = ['', '', '', '', '', '**', '__', '~~', '***', '</sub>', '</sup>', '', '\n```']     # Some formats requires closing arguments, such as bold, italic, etc.
##########################################

#TODO: Implement every functionnality that markdown offers (Maybe not the 3D model thought) https://docs.github.com/fr/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
#TODO: Implement a graphical interface. Using tkinter ? Or rather PySimpleGUI ?
#TODO: Find a way to show how it is interpreted in a window or a sub-section of the main window
#TODO: Add credit at the beginning (In a commentary)
#TODO: Once all the text is done, write it in a file




if __name__ == '__main__':

    writing = list()    # We're going to append every line and type of format wanted in this list

    while True:
        ask_type = input('What kind of thing you want to write ? ')
        if ask_type == 'write':
            break
        elif ask_type == 'line_break':
            ask_texte = ''
        else:
            ask_texte = input('Insert your text: ')
        writing.append((TYPE_FORMAT.index(ask_type), ask_texte))

    # This is the part where everything you wrote is going to be put into a README.md file
    with open('README_test.md', 'w') as file:
        file.write('<!--')
        file.write('Thank you for using my program, it really means a lot to me!')
        file.write('If you have any question, suggestion, or you just want to say hi, don\'t hesitate to check my GitHub page: https://github.com/Galaktik-hub')
        file.write('Don\'t forget to leave the repository of this project a star!')
        file.write('-->')
        file.write('\n')
        for line in writing:
            file.write(TYPE_FORMAT_FOR_FILE_OPENING[line[0]] + line[1] + TYPE_FORMAT_FOR_FILE_CLOSING[line[0]] + '\n')
        