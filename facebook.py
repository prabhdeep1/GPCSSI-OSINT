import requests
from bs4 import BeautifulSoup

out=[]
class main5():
 def user(username):

    search_string = "https://en-gb.facebook.com/" + username

    response = requests.get(search_string)

    soup = BeautifulSoup(response.text, 'html.parser')


    
    main_div = soup.div.find(id="globalContainer")

    
    def find_name():
        name = main_div.find(id="fb-timeline-cover-name").get_text()
        print("\n"+"Name:"+name)

    def find_eduwork_details():
        try:
            education = soup.find(id="pagelet_eduwork")
            apple=education.find(attrs={"class":"_4qm1"})
            if (apple.get_text() != " "):
                for category in education.find_all(attrs={"class":"_4qm1"}):
                    print(category.find('span').get_text() + " : ")
                    for company in category.find_all(attrs={"class":"_2tdc"}):
                        if (company.get_text() != " "):
                            print(company.get_text())
                        else:
                            continue
            else:
                print("No work details found")
        except Exception as e:
            print(str(e))
        print()

    def find_home_details():
        if(soup.find(id="pagelet_hometown") !=" "):
                home = soup.find(id="pagelet_hometown")
                for category in home.find_all(attrs={"class":"_4qm1"}):
                    print(category.find('span').get_text() + " : ")
                    for company in category.find_all(attrs={"class":"_42ef"}):
                        if (company.get_text() != " "):
                            print(company.get_text())
                        else:
                            continue
        else:
            print("No Home details found")


    if ("200" in str(response)):
        find_name()
        find_eduwork_details()
        find_home_details()

    elif ("404" in str(response)):
        print("Error: Profile not found")
    else:
        print("Error: some other response")
    return()
