## File Mod

File mod is easy to perform file operations with the help of  good method names 
and less arguments to pass

### Installation and Usage

1. use `pip install file-mod`
2. Make sure that your `pip` version is updated `pip install --upgrade pip`. 
3. Select the correct package for your environment:
4. Import the package: ``import filemod``

### Functions in the module 

1) This is a file reader method reads file content and returns it as string
`filemod.reader(filename)`

2) This file writer method writes contents to the file 
`filemod.writer(filename,content,method)`

3) This read_specific_line reads a specific line of the file and returns it as string 
`filemod.read_specific_line(filename,line)`

4) This extract_numbers_from reads a numbers from the file and returns all the collection of numbers in a list
`filemodpakage.read_specific_line(filename,line)`


## Run Locally

Clone the project

```bash
  git clone https://github.com/kshitij1235/filemod/tree/main/dist
```

Install

```bash
  pip install file-mod
```
## List of Functions

| Methods            |Process| args|
| ----------------- | ---|----------|
| Reader|Reads file| filename|    
| writer | writes content to file|filename,content,method|
| read_specific_line| read_specific_line |filename,line|
|extract_numbers_from|extracts number form file|filename



## Usage/Examples

### read file

```javascript
import filemod

filemod.reader('demo_file.txt')
```

### write file

```javascript
import filemod

filemod.writer('demo_file.txt',content="new line ", method='w')
```


### read_specific_line

```javascript
import filemod

filemod.read_specific_line("demo_file.txt",1)
```

### extract_numbers_from

```javascript
import filemodpakage

filemodpakage.extract_numbers_from("demo_file.txt")
```

  
## Badges


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/kshitij1235/filemod/blob/main/LICENSE)

  
## Authors

- [@kshitij1235](https://github.com/kshitij1235)

  
