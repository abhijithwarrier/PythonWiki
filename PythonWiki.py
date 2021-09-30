# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO GET INFORMATION ABOUT USER-ENTERED INPUT FROM WIKIPEDIA USING wikipedia LIBRARY

# Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
# In the following script, Wikipedia API is used to retrieve data from Wikipedia
#
# The module can be installed using the command - pip install wikipedia

# Importing necessary packages
import wikipedia
import webbrowser
import tkinter as tk
import tkinter.scrolledtext as sb_text
from tkinter import *

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    inputLabel = Label(root, text="SEARCH :", bg="lightblue4")
    inputLabel.grid(row=0, column=0, padx=10, pady=5)

    wordEntry = Entry(root, width=25, bg='azure3', textvariable=inputWord)
    wordEntry.grid(row=0, column=1, padx=10, pady=5)

    searchButton = Button(root, text="SEARCH", command=searchFor)
    searchButton.grid(row=0, column=2, padx=10, pady=5)

    urlLabel = Label(root, text="PAGE URL:", bg="lightblue4")
    urlLabel.grid(row=1, column=0, padx=10, pady=5)

    root.urlEntry = Label(root, width=35, bg='azure3', fg="blue", cursor="hand2")
    root.urlEntry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

    summaryLabel = Label(root, text="SUMMARY :", bg="lightblue4")
    summaryLabel.grid(row=2, column=0, padx=10, pady=5)

    root.summary = sb_text.ScrolledText(root, width=40, height=3, bg='azure3')
    root.summary.grid(row=3, column=0, rowspan=5, columnspan=3, padx=10, pady=5)
    # Making Text Widget uneditable by setting state parameter of config() to DISABLED
    root.summary.config(state=DISABLED, font = "Calibri 15", wrap="word")

    completeDataLabel = Label(root, text="DETAILS : ", bg="lightblue4")
    completeDataLabel.grid(row=8, column=0, padx=10, pady=5)

    root.completeData = sb_text.ScrolledText(root, width=40, height=15, bg='azure3')
    root.completeData.grid(row=9, column=0, rowspan=5, columnspan=3, padx=10, pady=5)
    # Making Text Widget uneditable by setting state parameter of config() to DISABLED
    root.completeData.config(state=DISABLED, font = "Calibri 15", wrap="word")

# Defining the callback() function with url as the parameter
def callback(url):
    # Opening the Wikipedia Page of the searched input in a new browser tab using the
    # open_new_tab() method of webbrowser which accepts the url as the parameter
    webbrowser.open_new_tab(url)

# Defining the searchFor() to get the wikipedia details of the entered input
def searchFor():
    # Storing the user-entered input in the search_for variable
    search_for = inputWord.get()
    # Retrieving the url of the page using the url property
    url_output = wikipedia.page(search_for).url
    # Displaying the url in the respective label
    root.urlEntry.config(text=url_output, cursor="arrow")
    # Binding callback function to label to open the Wikipedia Page in the browser
    root.urlEntry.bind("<Button-1>", lambda e: callback(url_output))
    # Summary of a searched input can be retreived using the summary() method.
    summary_output = wikipedia.summary(search_for)
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.summary.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.summary.delete('1.0', END)
    # Displaying the summary of the searched input in the summary Widget
    root.summary.insert("end", summary_output)
    # Making Widget uneditable again after the displaying list of news from feed
    root.summary.config(state=DISABLED)
    # Complete plain text content of a Wikipedia page, can be retreived using the
    # content property of the page object. It doesn't contain images, tables, etc.
    metadata_output = wikipedia.page(search_for).content
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.completeData.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.completeData.delete('1.0', END)
    # Displaying complete data from the Wikipedia Page in the completeData Widget
    root.completeData.insert("end", metadata_output)
    # Making Widget uneditable again after the displaying list of news from feed
    root.completeData.config(state=DISABLED)


# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize
# & disabling the resizing property
root.title("PythonWiki")
root.geometry("442x530")
root.config(background="lightblue4")
root.resizable(False, False)
# Creating the tkinter variables
inputWord = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
