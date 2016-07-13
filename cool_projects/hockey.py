
from bs4 import BeautifulSoup
import urllib3
import re
http = urllib3.PoolManager()
response = http.request('GET', "http://www.pointstreak.com/players/players-team-roster.html?teamid=611032")
response.data

soup = BeautifulSoup(response.data, "lxml")


stats=""
count=0
for link in soup.find_all(class_="lightGrey"):
    count=count+1
    stats+=link.get_text()



mylist= re.split("[\n\t\r\s"  "]+",stats)






statistics = ('#', 'NAME', 'GP', 'G', 'A', 'PTS', 'PIM', 'PP', 'SH', 'GWG', 'PPGA')


del(mylist[0])


listsize=int(len(mylist)/11)

allstats=statistics*(listsize)
#print(listsize)
#print(allstats)
#print(len(allstats))


i=0
y=0

newdick ={}
dlist=[]
for x in range(30):
    newdick[allstats[i]] = mylist[y]
    i+=1
    y+=1
    #newdick['NAME']=i
    if i==10 or i==20:
        dlist.append(newdick.copy())
print(dlist)


"""
d['data']=i
dlist.append(d.copy())
print(d)


{'data': 0}
{'data': 1}
{'data': 2}
>>> print dlist
[{'data': 0}, {'data': 1}, {'data': 2}]
    if mylist[x]== "Salvador":
        break
    if allstats[i] == "NAME":
        if mylist[x] == "Jean-":
            newdick[allstats[i]] = mylist[x] +" " + mylist[x+1]+" " + mylist[x+2]
            i+=1
            x+=3
            continue

        newdick[allstats[i]] = mylist[x] +" " + mylist[x+1]
        i+=1
        x+=2
        print(newdick)
        print('x is'+ str(x))
        print('i is'+ str(i))
        continue

"""


#print(newdick)
