def writer(filename, content, method):
    try:
        with open(filename, method) as file:
            file.write(content)
        file.close()
    except:
        pass


def reader(filename):
    try:
        with open(str(filename), "r+") as file:
            content = str(file.read())
            file.close()
            return content
    except:
        pass

def read_specific_line(filename,line):
    file = open(filename)
    content = file.readlines()
    content=content[line]
    file.close()
    return content