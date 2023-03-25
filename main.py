# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# generate python list of random int numbers from 1 to 100

# generate python list of random int numbers from 1 to 10
# generate python list of random int numbers from 1 to 100

import random


def generate_random_list(size, start, end):
    random_list = []
    for i in range(size):
        random_list.append(random.randint(start, end))
    return random_list


def main():
    random_list = generate_random_list(10, 1, 100)
    print(random_list)
    target_sum: int = random.randint(1, 100)

    # insert the random_list into new set
    random_set = set(random_list)
    for num in random_list:
        if (target_sum - num) in random_set:
            print(num, target_sum - num, target_sum)
            break


# Create code that get the current year and return 1 if it's leap year and 0 if it's not
# get the current system year

def get_current_year():
    import datetime
    return datetime.datetime.now().year


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


## horrible code  ##
# Write a function to convert pdf file into word file
# import the required modules
import PyPDF2
import docx

# open allows you to read the file
# open tkinter window to get the pdf file from the user
from tkinter import filedialog, Tk

root = Tk()
filename = filedialog.askopenfilename(initialdir="/", title="Select file")
pdfFileObj = open(filename, 'rb')

# convert pdf file into word file
pdfReader = PyPDF2.PdfReader(pdfFileObj)
wordFile = docx.Document()
for pageNum in range(len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    wordFile.add_paragraph(pageObj.extract_text())
wordFile.save('sample.docx')


# PL/SQL CODE TO GET THE CURRENT YEAR
# get the current year
# select to_number(to_char(sysdate, 'YYYY'))
# #case switch in leap year
# from dual
# where to_number(to_char(sysdate, 'YYYY')) % 4 = 0
#
# from dual;

def is_leap_year_2(year):
    if year % 400 == 0:
        return 1
    elif year % 100 == 0:
        return 0
    elif year % 4 == 0:
        return 1
    else:
        return 0
