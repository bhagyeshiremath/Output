from bs4 import BeautifulSoup
import subprocess as sb
def Start():
    file=open('output.json','w')
    URL="New Lead.html"
    soup = BeautifulSoup(open("New Lead .html"), "html.parser")

    #Extracting name
    for x in soup.find_all(attrs={'style':'font-family: Arial, sans-serif; font-size: 14px; color: #333333;'}):
        temp=x.get_text().split()
        if('Name' in temp):
            #print(temp)
            file.write(str('{\n"name":'+'"'+temp[1]+' '+temp[2]+'",\n'))

    #Extracting email
    for x in soup.find_all(attrs={'style':'font-family: Arial, sans-serif; font-size: 16px;'}):
        #print(x.get_text())
        file.write(str('"email":'+'"'+x.get_text()+'",\n'))

    #Extracting Phone number
    for x in soup.find_all(attrs={'style':'font-family: Arial, sans-serif; font-size: 20px; color: #fff;'}):
        file.write(str('"phone":'+'"'+x.get_text()+'",\n'))

    #Extracting number of Beds and Bathrooms
    for x in soup.find_all(attrs={'class':'font12'}):
        #print(x.get_text())
        temp=x.get_text().split()
        if 'Beds' in temp:
            file.write(str('"beds":'+temp[1]+',\n'))
            file.write(str('"baths":'+temp[3]+',\n'))

    #Extracting address
    for x in soup.find_all(attrs={'class':'font12'}):
        #print(x.get_text())
        if len(x.get_text().split(','))>2:
            file.write(str('"address":'+'"'+x.get_text()+'",\n}'))
    file.flush()
    file.close()
    path=sb.getoutput('pwd')
    print('output file generated as output.json in '+path)
    print('Do you want to display it now. Enter y if yes')
    if(input()=='y'):
        print('------------------- '+path+'/output.json----------------------------------------')
        sb.Popen(['cat',str(path+'/output.json')])
    else:
        print('You can manually open the output file generated as output.json by navigating to '+sb.getoutput('pwd'))
Start()