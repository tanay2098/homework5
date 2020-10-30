import sys
from collections import Counter

READ_FILE='book.txt'
WRITE_FILE='summary.txt'
read_mode='r'
write_mode='w'


try:
    book=open(READ_FILE,read_mode)
    summary=open(WRITE_FILE,write_mode)
    
    content=book.readline()
    results=Counter(content.lower())

    with book,summary:
        counter=0
        for item in sorted(results.items()):
            if item[0].isalpha():
                counter+=1
                summary.write(f'{str(item[0]).capitalize()} {str(item[1])}\n')
                print(f'{str(item[0]).capitalize()} {str(item[1])}')
        
        if counter==26:
            summary.write(" It has all letters")
            print(" It has all letters")
        else:
            summary.write("It doesnot have all letters")
            print("It doesnot have all letters")

except OSError as error:
    print('Unable to open',READ_FILE,'.Error Message:',error)
    sys.exit(0)           
