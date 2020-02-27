from selenium import webdriver
from datetime import datetime
from selenium.webdriver.firefox.options import Options
import psycopg2 as psy

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get("https://silverwastes.loltools.net/")

total = driver.find_element_by_id("bestValue").text
timestamp = int(datetime.now().timestamp())

dictionary = {"timestamp": timestamp, "total": total}
Ids = ["wood", "leather", "cloth", "ore"]
for name in Ids:
    ID = "value-table-{}".format(name)
    tier3 = driver.find_element_by_xpath(f"//table[@id=\"{ID}\"]/tbody/tr[3]/td[3]").text
    tier4 = driver.find_element_by_xpath(f"//table[@id=\"{ID}\"]/tbody/tr[4]/td[3]").text
    dictionary[name + "3"] = tier3
    dictionary[name + "4"] = tier4

names = ""
values = []

for key in dictionary:
    names += key + ","
    values.append(dictionary[key])
driver.close()

print(values)
#                                                      ts, tot, l3, l4, o3, o4, c3, c4, w3, w4
query = f"insert into Silverwastes ({names[:-1]}) Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
print(query)
conn = psy.connect(host="localhost",database="gw", user="postgres")
cur = conn.cursor()
cur.execute(query, values)
conn.commit()

count = cur.rowcount
print (count, "Record inserted successfully into mobile table")

cur.close()
conn.close()

# create table Silverwastes (timestamp int, total float, leather3 float, leather4 float, ore3 float, ore4 float, cloth3 float, cloth4 float, wood3 float, wood4 float)