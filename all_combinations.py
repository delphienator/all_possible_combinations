import csv


def generate_combinations(list1, list2, list3):
    '''
    This function will do a combination of input data into a matrix.
    Each combination should represent a row.
    Since, we don't know how many elements we will have on input - we can't define how many arguments to have. 

    Input: as input should enter an array with elements. Each element can be a list of elements to be combined.
    Return: as return - it will be an array with elements. Each element will represent a row with combination
    '''
    len1=len(list1)
    len2=len(list2)
    len3=len(list3)
    new_list = []

    for a in range(0,len1):
                                    #start cycle depth 1
        for b in range(0,len2):
                                    #start cycle depth 2
            for c in range(0,len3):
                                    #start cycle depth 3
                #print(list1[a])
                #print(list2[b])
                #print(list3[c])
                new_list.append(list1[a])   #creating element from list1 
                new_list.append(list2[b])   #creating element from list2 
                new_list.append(list3[c])   #creating element from list3
                 
    #print(new_list)
    
    return(new_list)
    


def write_to_csv(combination_list):
    '''
    This function will dump with all possible combinations into .csv file
    Information should be written in file row by row, meaning 1 row = 1 combination

    Input: list with all combinatios
    Return: create .csv file with all data inside row by row
    '''
    
    with open('/home/devasc/lab-25/combinations.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file)

                                                # Need to brake entire list to rows.
        nlen=len(combination_list)              # Each row will represent the combination of elements from each list.   
        for i in range(0, nlen,3):              # Here we go in cycle with step of 3 (number of input original lists for combinations)
            row=[]                              
            row.append(combination_list[i])     
            row.append(combination_list[i+1])   
            row.append(combination_list[i+2])
            #print(row)
            writer.writerow(row)                # magic !!!

    pass




a=['DES','3DES','AES-128']
b=['DH2','DH5','DH14']
c=['md5','sha']


new_list=generate_combinations(a,b,c)

write_to_csv(new_list)

