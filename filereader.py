import csv

with open('OSDHsituationupdate2021-08-24.csv', newline='', encoding="ISO-8859-1") as csvfile:
    data = csv.DictReader(csvfile)
    lis_word = ['FOR RELEASE','New Cases']
    dic_lis = {}
    lis_word = []
    for row in data:
         body_len = row['Body'].split(',')
         for itm in range(0,len(body_len)):
              for word in lis_word:
                  if strip_data.find(word)>= 0:
                       s_ind = strip_data.index(word)
                       ls=body_len[s_ind].split(':')
                       f=open('new_file.csv','w', newline='')
                       obj=csv.DictWriter(csvfile, fieldnames=fields)
                       obj.writeheader(lis_word)
                       obj.writerows(ls[1])
                       f.close()
                                                   
                       
    
