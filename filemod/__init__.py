import re


def writer(filename, content, method):
    """writes the data to the file
    just takes filename your data as content and method to open the file"""
    try:
        with open(filename, method) as file:
            file.write(content)
        file.close()
    except:
        pass


def reader(filename):
    """Reads data and returs a all the content as 
    string """
    try:
        with open(str(filename), "r+") as file:
            content = str(file.read())
            file.close()
            return content
    except:
        pass


def read_specific_line(filename, line):
    """reads a specific line from a file 
    just takes filename and line number"""
    file = open(filename)
    content = file.readlines()
    content = content[line]
    file.close()
    return content


def extract_numbers_from(filename):
    """Returns all the numerical values as list"""
    try:file = reader(filename)
    except:print("FIle ERROR")
    temp = re.findall(r'\d+', file)
    return list(map(int, temp))
