import requests

class main2(): 
 def Phonenumber(ph):
    print ('Getting Phone number Details...' + '\n')
    api="fe14e1a990b25cafe5eb8ea8e9a411c7"
    url = ("http://apilayer.net/api/validate?access_key="+api+"&number="+str(ph))
    response=requests.get(url) 
   
    if response.status_code ==200:
                get=response.json()
                print("Number: "+get['number'])
                print("Type: "+get['line_type'])
                print("CountryCode: "+get['country_code'])
                print("Country: "+get['country_name'])
                print("Location: "+get['location'])
                print("Carrier: "+get['carrier'])
                print("")
    else:
                print("Error: Invalid Mobile Number")
    

