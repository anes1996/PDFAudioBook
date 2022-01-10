# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyttsx3
import PyPDF2
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book = open('info.pdf', "rb")
    pdfreader = PyPDF2.PdfFileReader(book)
    fulltext = ""
    speaker = pyttsx3.init()
    speaker.setProperty("rate", 200)
    for nun in range(pdfreader.numPages):
        page = pdfreader.getPage(nun)
        text = page.extractText()
        fulltext += text
    speaker.save_to_file(fulltext, "aa.mp4")
    speaker.runAndWait()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
