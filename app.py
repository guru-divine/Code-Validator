# 1 -> Your portfolio should have a "Welcome" section with an id of welcome-section.
# 2 -> Your #welcome-section element should contain an h1 element.
# 3 -> You should not have any empty h1 elements within #welcome-section element.
# 4 -> You should have a "Projects" section with an id of projects.
# 5 -> Your portfolio should contain at least one element with a class of project-tile.
# 6 -> Your #projects element should contain at least one a element.
# 7 -> Your portfolio should have a navbar with an id of navbar.
# 8 -> Your #navbar element should contain at least one a element whose href attribute starts with #.
# 9 -> Your portfolio should have an a element with an id of profile-link.
# 10-> Your #profile-link element should have a target attribute of _blank.
# 11-> Your portfolio should use at least one media query.
# 12-> Your #navbar element should always be at the top of the viewport.


import cssutils
from bs4 import BeautifulSoup

def read_html_file(file_path):
    """Read HTML file and return BeautifulSoup object."""
    with open(file_path, "r", encoding="utf-8") as file:
        html_doc = file.read()
    return BeautifulSoup(html_doc, "html.parser")

def is_navbar_fixed(css_file, selector, properties):
    """Check if navbar has fixed positioning with specified properties."""
    parser = cssutils.CSSParser()
    css = parser.parseFile(css_file)
    for rule in css.cssRules:
        if isinstance(rule, cssutils.css.CSSStyleRule) and selector in rule.selectorText:
            for property in rule.style:
                if property.name == "top" and property.value == "0" and \
                        rule.style.getPropertyValue("position") == "fixed":
                    return True
    return False

def contains_media_query(css_file):
    """Check if CSS file contains any media queries."""
    parser = cssutils.CSSParser()
    css = parser.parseFile(css_file)
    for rule in css.cssRules:
        if isinstance(rule, cssutils.css.CSSMediaRule):
            return True
    return False

def check_element_height(css_file, selector, property):
    # Parse the CSS file
    parser = cssutils.CSSParser()
    css = parser.parseFile(css_file)

    # Iterate over each CSS rule
    for rule in css.cssRules:
        # Check if the rule matches the specified selector and sets height to 100vh
        if isinstance(rule, cssutils.css.CSSStyleRule) and \
           rule.selectorText == selector and \
           property in rule.style and rule.style[property] == '100vh':
            return True  # Rule found
    return False  # Rule not found

def find_element_by_id(soup, id_name):
    """Find element in HTML by ID."""
    return soup.find(id=id_name)

def check_no_empty_tag_in_id_name(tag_name, id_name, soup):
    """
    Check if there are any empty <tag_name> elements within the #id_name.
    Args:
        soup (BeautifulSoup): Parsed HTML document.

    Returns:
        bool: True if #id_name have an <tag_name> element that contains text, False otherwise
    """
    # Find the #id_name element
    idname_section = soup.find(id=id_name)
    
    if idname_section:
        # Find all <tag_name> elements within #id_name
        x_tags = idname_section.find_all(tag_name)
        
        for x_tag in x_tags:
            # Check if the <tag_name> element has non-empty text content
            if not x_tag.text.strip():
                return False  # Empty <tag_name> element found
        return True  # No empty <tag_name> elements found within #welcome-section
    else:
        return False  # id_name not found
    
def check_link_with_href_starting_with(hash_links):
    """Check if there's at least one link with href starting with '#'."""
    for link in hash_links:
        if link.get("href", "").startswith("#"):
            return True
    return False

def check_profile_link(profile_link, website_link, target_attr):
    """Check if profile link exists and has target attribute set to _blank."""
    if profile_link:
        href_attribute = profile_link.get("href")
        if href_attribute == website_link:
            target_attribute = profile_link.get("target")
            return target_attribute == target_attr
    return False
    
def check_element_has_child_with_tag(parent_element, tag_name):
    """Check if parent element has a child with specified tag name."""
    return parent_element and parent_element.find(tag_name)

def check_element_has_child_with_class(parent_element, class_name):
    """Check if parent element has a child with specified class."""
    return parent_element and parent_element.find(class_=class_name)
    



# Read HTML file
html_soup = read_html_file("index.html")
# CSS file to check
css_file = "styles.css"


# List of ID names to find in the HTML
id_names = ["welcome-section", "projects", "navbar"]

# Check if specified ID elements exist in the HTML                          (1, 4, 7)
for id_name in id_names:
    if find_element_by_id(html_soup, id_name):
        print(f"Element with ID '{id_name}' found.")
    else:
        print(f"Element with ID '{id_name}' not found.")

# Check if #id_name element should contain an tag_name element              (2)
id_name = "welcome-section"
tag_name = "h1"
welcome_section = find_element_by_id(html_soup, id_name)
if check_element_has_child_with_tag(welcome_section, tag_name):
    print(f"#{id_name} contains at least one element with tag '{tag_name}'.")

# Check if #id_name has an <tag_name> element that contains text            (3)
tag_name = "h1"
id_name = "welcome-section"
if check_no_empty_tag_in_id_name(tag_name, id_name, html_soup):
    print(f"Element {tag_name} found with text in {id_name}'s container")


# Check if project section contains one element with class class_name       (5)
id_name = "projects"
projects_section = find_element_by_id(html_soup, id_name)
class_name = "project-tile"
if check_element_has_child_with_class(projects_section, class_name):
    print(f"Portfolio contains at least one element with class '{class_name}'.")


# Check if project section contains one element with tag tag_name           (6)
tag_name = "a"
if check_element_has_child_with_tag(projects_section, tag_name):
    print(f"Portfolio contains at least one element with tag '{tag_name}'.")


# Check if navbar contains at least one link with href starting with #      (8)
id_name = "navbar"
navbar_element = find_element_by_id(html_soup, id_name)
if navbar_element:
    hash_links = navbar_element.find_all("a")
    if check_link_with_href_starting_with(hash_links):
        print("Navbar contains at least one link with href starting with #.")
    else:
        print("Navbar does not contain any links with href starting with #.")


# Check if profile link exists and has target attribute set to target_attr       (9)
id_name = "profile-link"
website_link = "https://github.com/guru-divine"
profile_link = find_element_by_id(html_soup, id_name)
target_attr = "_blank"

if check_profile_link(profile_link, website_link, target_attr):
    print(f"Profile link exists and links to GitHub profile ({website_link}) with target attribute set to {target_attr}.")
else:
    print("Profile link does not meet the specified criteria.")


# Check if CSS file contains media queries                                  (10)
if contains_media_query(css_file):
    print(f"The CSS file ({css_file}) contains media queries.")
else:
    print(f"No media queries found in the CSS file ({css_file}).")


# Check if the height of the welcome-section is equal to the height of the viewport  (11)
selector = "#welcome-section"
property = "height"
if check_element_height(css_file, selector, property):
    print(f"The CSS file contains a rule to set the height of {selector} to 100vh.")
else:
    print("No such rule found in the CSS file.")


# Check if navbar has is always at top of viewport                          (12)
selector = "#navbar"
if is_navbar_fixed(css_file, selector, "top: 0; position: fixed;"):
    print("The navbar has fixed positioning in the CSS file.")
else:
    print("The navbar does not have fixed positioning in the CSS file.")