records=0
sum_score=0
avg=0
score_list=[]
READ_FILE='scores.txt'
WRITE_FILE='log.txt'
read_mode='r'
write_mode='w'

try:
        score=open(READ_FILE,read_mode)
        log=open(WRITE_FILE,write_mode)
        with score,log:
                for line in score:
                        name,score=line.split()
                        try:          
                                score_list.append(int(score))
                        except ValueError as error:
                                log.write(f'Bad score value for {name}, ignored.\n')
                                print(f'Bad score value for {name}, ignored.\n')
                        else:
                                records+=1
                avg=int(sum(score_list)/len(score_list))
                

                log.write(f'The class average is {avg} for {records} students.\n')
                print('The class average is',avg,'for',records,'students')

except OSError as error:
        print('Unable to open',READ_FILE,'.Error Message:',error)


