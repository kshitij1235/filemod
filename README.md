[![Downloads](http://pepy.tech/badge/opencv-python)](http://pepy.tech/project/opencv-python)

## File Mod

File mod is easy to perform file operations with the help of  good method names 
and less arguments to pass

### Installation and Usage

1. use `pip install file-mod`
2. Make sure that your `pip` version is updated `pip install --upgrade pip`. 
3. Select the correct package for your environment:
4. Import the package: ``import filemodpakage``

### Functions in the module 

1) This is a file reader method reads file content and returns it as string
`filemodpakage.reader(filename)`

2) This file writer method writes contents to the file 
`filemodpakage.writer(filename,content,method)`

3) This read_specific_line reads a specific line of the file and returns it as string 
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

| Color             | Hex| args|
| ----------------- | ---|----------|
| Reader|Reads file| filename|    
| writer | writes content to file|filename,content,method|
| read_specific_line| read_specific_line |filename,line|



## Usage/Examples

### read file

```javascript
import filemodpakage

filemodpakage.reader('demo_file.txt')
```

### write file

```javascript
import filemodpakage

filemodpakage.writer('demo_file.txt',content="new line ", method='w')
```


### read_specific_line

```javascript
import filemodpakage

filemodpakage.read_specific_line("demo_file.txt",1)
```

  
## Badges


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/kshitij1235/filemod/blob/main/LICENSE)

  
## Authors

- [@kshitij1235](https://github.com/kshitij1235)

  
