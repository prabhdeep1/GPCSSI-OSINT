import sys
from Phonenumber import *
from Twitter import *
from facebook import *
from maildb import *
from Insta import *

def banner():
   return("""   ____ ____   ____ ____ ____ ___       ___  ____ ___ _   _ _____ 
  / ___|  _ \ / ___/ ___/ ___|_ _|     / _ \/ ___|_ _| \ | |_   _|
 | |  _| |_) | |   \___ \___ \| |_____| | | \___ \| ||  \| | | |  
 | |_| |  __/| |___ ___) |__) | |_____| |_| |___) | || |\  | | |  
  \____|_|    \____|____/____/___|     \___/|____/___|_| \_| |_|  
                                                                  """)
def mainmenu():
	print ("""
ENTER 0 - 5 TO SELECT OPTIONS

1. PHONENUMBER                   Gather  information  about Phonenumber

2. INSTAGRAM                     Extract Account info. from Instagram

3. TWITTER                       Extract Account info. from Twitter

4. FACEBOOK                      Extract Account info. from Facebook

5. DOMAIN                        Gather  information  about  given DOMAIN

0. EXIT                          Exit from  GPSCSSI to your terminal """)

print(banner())	
while(True):
	mainmenu()
	n=int(input("\nEnter your choice : "))

	if n==1:
      			ph=input("\nEnter number(with country code) : ")
      			main2.Phonenumber(ph)


	elif n==2:
      		user=input("\nEnter Username : ")
      		main1.ig = main1(user)
      		main1.ig.print_data()
	
	elif n==3:
       		username=input("Enter Username : ")
       		info(username)
       		print("#------------------------ Media Files-----------------------------# ")
               
       		twiiter_media(username)
       		print("#----------------------- Tweet Records--------------------------#")
       		df = tweets_to_data_frame(username)
       		print(df)
       		path_for_csv='{}/{}.csv'.format(username,username)
       		df.to_csv(path_for_csv, index=False,encoding='utf-8')
    
	elif n==4:
      		nameuser=input("Enter Username: ")
      		main5.user(nameuser)


	elif n==5:
      		email=input("\nEnter Domain Name : ")
      		main3.maildb(email)

	elif n==0:
			exit
			print("\nSuccessfully Exit")
			break

	else:
    		print("\nInvalid Input")
			


