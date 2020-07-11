import requests

class main2(): 
 def Phonenumber(ph):
    print ('Getting Phone number Details...' + '\n')
    api="2f8c8e865a0b25bbf4da08c4db039b8d"
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
    

