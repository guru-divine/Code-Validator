
# 1 -> find id with name "welcome-section"                                                              (completed)
# 2 -> Your #welcome-section element should contain an h1 element.                                      (completed)
# 3 -> You should not have any empty h1 elements within #welcome-section element                        (completed)
# 4 -> find id "projects"
# 5 -> Your portfolio should contain at least one element with a class of project-tile.
# 6 -> contain atleast one link (i.e. atleast one <a>)
# 7 -> navbar with id "navbar"
# 8 -> Your #navbar element should contain at least one a element whose href attribute starts with #
# 9 -> one link with id "profile-link" which links to my github profile
# 10 -> Your #profile-link element should have a target attribute of _blank.
# 11 -> Your portfolio should use at least one media query.                                             (remaining)
# 12 -> navbar should always be at the top of the viewport (i.e. top=0, z-index=max)                    (remaining)


import requests
from bs4 import BeautifulSoup

with open("index.html", "r", encoding='utf-8') as file:
    html_doc = file.read()
soup = BeautifulSoup(html_doc, 'html.parser')

idNames = [("welcome-section", 1), ("projects", 4), ("navbar", 7)]  # Example list of ID names with corresponding indices
# tagNames = [("h1", )]

illegal_tags = {"hr", "br", "img", "input", "button", "select", "table"}

isPresent = {}


# 2, 3 -> The welcome section should have an h1 element that contains text
welcome_section = soup.find(id="welcome-section")
h1_tags = welcome_section.find_all('h1')
h1_tag_find = welcome_section.find('h1')
if h1_tag_find:
    print("Task 2 completed")
for h1_tag in h1_tags:
    if h1_tag.text.strip():
        print("Task 3 completed")
        break


# 5, 6 -> Your portfolio should contain at least one element with a class of project-tile.
project_id = soup.find(id="projects")
if project_id:
    if project_id.find('a'):
        print("Task 5 completed")
    project_children = project_id.find(class_="project-tile")
    if(project_children):
        print("Task 6 completed")

# 1, 4, 7
for idName, index in idNames:
    if soup.find(id=idName) is not None:
        print(f"Task {index} completed")
        isPresent[index] = True
    else:
        isPresent[index] = False

# 8 -> Your #navbar element should contain at least one a element whose href attribute starts with #
navbar_id = soup.find(id="navbar")
a_tags = navbar_id.find_all('a')

for a_tag in a_tags:
    href_attribute = a_tag.get('href')
    if href_attribute and href_attribute.startswith('#'):
        matching_link_found = True
        print("Task 8 completed")
        break  # Exit the loop if a matching link is found

# 9, 10

a_tags = soup.find_all('a')
for a_tag in a_tags:
    if a_tag.get('id') and a_tag.get('id') == 'profile-link':
        my_github = "https://github.com/guru-divine"
        href_attribute = a_tag.get('href')
        if href_attribute == my_github:
            print("Task 9 completed")
            target_attribute = a_tag.get('target')
            if(target_attribute == "_blank"):
                print("task 10 completed")



# 12(do it again)
    
# first_container = soup.body.find_next()
# while first_container.contents == None:
#     first_container = soup.body.find_next()
# if first_container and 'id' in first_container.attrs and first_container['id']=='navbar':
#     print("Navbar element is at the top")

print(isPresent)

