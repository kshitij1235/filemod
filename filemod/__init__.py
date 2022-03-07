'''
# MIT License

# Copyright (c) 2021 Kshitij

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
'''

from re import findall
from mmap import mmap,ACCESS_READ


def writer(filename, content, method):
    """writes the data to the file
    just takes filename your data as content and method to open the file"""
    try:
        with open(filename, method) as file:
            file.write(content)
        file.close()
    except:
        print("ERROR LOADING FILE")


def reader(filename):
    """Reads data and returs a all the content as
    string """
    try:
        with open(filename, mode="r", encoding="utf8") as file_obj:
            with mmap(file_obj.fileno(), length=0, access=ACCESS_READ) as mmap_obj:
                return mmap_obj.read().decode('UTF-8')
    except FileNotFoundError:
        print("ERROR LOADING FILE")


def read_specific_line(filename, line):
    """reads a specific line from a file 
    just takes filename and line number"""
    try:
        file = open(filename)
    except FileNotFoundError:
        print("ERROR LOADING FILE")
    content = file.readlines()
    content = content[line]
    file.close()
    return content


def extract_numbers_from(filename):
    """Returns all the numerical values as list"""
    try:
        file = reader(filename)
    except FileNotFoundError:
        print("FIle ERROR")
    temp = findall(r'\d+', file)
    return list(map(int, temp))


def remove_word(filename, excludedWord):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        newLines = [' '.join([word for word in line.split() if word != excludedWord])
                    for line in lines]
        with open(filename, 'w') as f:
            for line in newLines:
                f.write("{}\n".format(line))
        return True
    except FileNotFoundError:
        return False


def number_of_lines(filename):
    """this gets the number of lines in a file"""
    with open(filename) as myfile:
        total_lines = sum(1 for _ in myfile)
    return total_lines


def delete_specific_line(filename, line):
    try:
        with open(filename, "r") as f:
            contents = f.readlines()
        # remove the line item from list, by line number, starts from 0
        contents.pop(line-1)

        with open(filename, "w") as f:
            contents = "".join(contents)
            f.write(contents)
        return True
    except FileNotFoundError:
        return False

def write_specific_line(filename,line,content):
    """
    this write a specific line
    """
    try: 
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.readlines()

        data.append(" ")
        data[line-1] = content

        with open(filename, "w", encoding='utf-8') as file:
            file.writelines(data)
    except FileNotFoundError:
        return False