import sys  #importing sys module
records=0   #variable to store student records
sum_score=0 #variable to store sum of scores of all students
avg=0       #variable to store average score
score_list=[] # list to store score values
READ_FILE='scores.txt' 
WRITE_FILE='log.txt'
read_mode='r'#reading mode
write_mode='w'#writing mode

try:
        score=open(READ_FILE,read_mode)# opening scores.txt
        log=open(WRITE_FILE,write_mode)# opening log.txt
        with score,log:
                for line in score:      # loop for each line in read file
                        name,score=line.split() #splits the string at whitespace
                        try:          
                                score_list.append(int(score)) #score from string is appended into list
                        except ValueError as error: #passing value error exception
                                log.write(f'Bad score value for {name}, ignored.\n')
                                print(f'Bad score value for {name}, ignored.')
                        else:
                                records+=1 #incrementing record by 1
                avg=int(sum(score_list)/len(score_list))# calculating average score
                

                log.write(f'The class average is {avg} for {records} students.\n')# writing output to log file
                print('The class average is',avg,'for',records,'students')

except OSError as error:# passing the OS error exception
        print('Unable to open',READ_FILE,'.Error Message:',error)
        sys.exit(0)


