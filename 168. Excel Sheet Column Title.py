import string

def convertToTitle(columnNumber: int) -> str:
    columnName = ''
    while(True):
        rem = (columnNumber - 1) % 26
        columnNumber = (columnNumber - 1)//26
        columnName = string.ascii_uppercase[rem] + columnName
        if columnNumber < 1:
            break
    return columnName

print(convertToTitle(701))