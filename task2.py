import sys #importing sys module
from collections import Counter #importing Counter from collections module

READ_FILE='book.txt'
WRITE_FILE='summary.txt'
read_mode='r'# reading mode
write_mode='w'#writing mode


try:
    book=open(READ_FILE,read_mode)# opening book file
    summary=open(WRITE_FILE,write_mode)# opening summary file
    
    content=book.readline()# to read the content of file in one operation
    output_values=Counter(content.upper())# storing the elements as dictionary keys and their counts as dictionary values

    with book,summary:
        uniq_alpha_count=0 # variable to count unique alphabets
        for i in sorted(output_values.items()):#perform sorting of the dict values
            if i[0].isalpha(): # checks if the characters are alphabets and returns True
                uniq_alpha_count+=1 #incrementing the variable
                summary.write(f'{str(i[0])} {str(i[1])}\n') # writing the output to summary file
                print(f'{str(i[0])} {str(i[1])}')
        
        if uniq_alpha_count==26:# total number of english alphabets
            summary.write(" It has all letters")# writing the output to summary file
            print(" It has all letters")
        else:
            summary.write("It doesnot have all letters")# writing the output to summary file
            print("It doesnot have all letters")

except OSError as error:#passing the OSError exception
    print('Unable to open',READ_FILE,'.Error Message:',error)
    sys.exit(0)           
