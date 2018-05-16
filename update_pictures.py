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

    lightbox_description = picture["title"].replace('"', '&quot;') + ", " + picture["medium"].replace('"', '&quot;') + ", " + picture["details"].replace('"', '&quot;')

    print("<a href=\"/images/" + picture["filename"].replace('"', '&quot;') + "\" title=\"" + lightbox_description + "\">")
    print(" <div class=\"gallery-img-container\">")
    print("  <img class=\"gallery-img\" src=\"/images/"  + picture["filename"].replace('"', '&quot;') + "\"></img>")
    print("  <div class=\"gallery-text\">")
    print("     <span class=\"title\">" + picture["title"].replace('"', '&quot;') + "</span>")
    print("     <span class=\"medium\">" + picture["medium"].replace('"', '&quot;') + "</span>")
    print("     <span class=\"details\">" + picture["details"].replace('"', '&quot;') + "</span>")
    print("  </div>")
    print(" </div>")
    print("</a>")
