import json
from pprint import pprint

with open('picture_data.json') as f:
    picture_data = json.load(f)

picture_data.sort(key=lambda x: x["year"], reverse=True)

currentYear = picture_data[0]["year"]
print("<h3>" + str(currentYear) + "</h3>")

for picture in picture_data:
    if picture["year"] != currentYear:
        currentYear = picture["year"]
        print("<h3>" + str(currentYear) + "</h3>")

    print("<a href=\"/images/" + picture["filename"].replace('"', '&quot;') + "\" title=\"" + picture["title"].replace('"', '&quot;') + "\">")
    print(" <img src=\"/images/"  + picture["filename"].replace('"', '&quot;') + "\"></img>")
    print("</a>")
