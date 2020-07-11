import requests
class main3(): 
 def maildb(email):
    if  ("@" and ".com") or ("@" and ".in") in email:
        req=requests.get("https://api.hunter.io/v2/domain-search?domain="+email+"&api_key=fc9b0adbc318cfd40d5ed18ecced6465d957c150")
        j=req.json()
        print("Breaching from "+email+"...\n")
        for i in range(len(j['data']['emails'])):
            print("Email ID   :",j['data']['emails'][i]['value'])
            print("First Name :",j['data']['emails'][i]['first_name'])
            print("Last Name  :",j['data']['emails'][i]['last_name'])
            if j['data']['emails'][i]['position']!=None:
                print("Position   :",j['data']['emails'][i]['position'])
            if j['data']['emails'][i]['linkedin']!=None:
                print("Linkedin   :",j['data']['emails'][i]['linkedin'])
            if j['data']['emails'][i]['twitter']!=None:
                print("Twitter    :",j['data']['emails'][i]['twitter'])
            print()
    else:
        print("Error: Invalid Email Address")



