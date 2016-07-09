
from bs4 import BeautifulSoup
import urllib3
import re
http = urllib3.PoolManager()
response = http.request('GET', "http://www.pointstreak.com/players/players-team-roster.html?teamid=611032")
response.data
soup = BeautifulSoup(response.data, "lxml")

#print(soup.find_all('td', class_= "lightGrey",class_= "mediumGrey"))
stats=""
count=0
for link in soup.find_all(class_="lightGrey"):
   count=count+1
   stats+=link.get_text()
#print(stats)


mylist= re.split("[\n\t\r\s"  "]+",stats)
del(mylist[0])


statistics = ('#', 'NAME', 'GP', 'G', 'A', 'PTS', 'PIM', 'PP', 'SH', 'GWG', 'PPGA')


def teamstats():
    i=0
    x=0
    y=0
    newdick ={}
    dlist=[]

    for x in range(len(mylist)-1):
           if mylist[y]== "Salvador":
               break
           if statistics[i] == "NAME":
               if mylist[y] == "Jean-":
                   newdick[statistics[i]] = mylist[y] +" " + mylist[y+1]+" " + mylist[y+2]
                   i+=1
                   y+=3
                   continue

               newdick[statistics[i]] = mylist[y] +" " + mylist[y+1]
               i+=1
               y+=2
               continue

           if i==10:
               dlist.append(newdick.copy())

               i=0
               y+=1
               continue




           newdick[statistics[i]] = mylist[y]
           i+=1
           y+=1
    allplayers={}
    for i in range (len(dlist)-1):
        allplayers[dlist[i]["NAME"]]= dlist[i]

               #

    return allplayers

chups= teamstats()

def most(team,stat):
    check={}
    for key in chups:
        check[key]=chups[key][stat]

    maximum = max(check , key=check.get)
    #print(maximum , check[maximum])
    minimum = min(check , key=check.get)
    return("The Person who has the most"+ " "+ stat +" "+ "is" + " "+  maximum + " "+ "with" + " "+ check[maximum]+ " " +" "+stat)

def least(team,stat):
    check={}
    for key in chups:
        check[key]=chups[key][stat]

    maximum = max(check , key=check.get)
    #print(maximum , check[maximum])
    minimum = min(check , key=check.get)
    return("The Slacker of the team for least"+ " "+ stat +" "+ "is" + " "+  minimum+ " "+ "with" + " "+ check[minimum]+ " " +" "+stat)
#check=records(chups,"PTS")
#print(check)
'''
def main():
    WhatStat = input("What Stat are you interested in: ")
    records(chups,WhatStat)

main()
'''
