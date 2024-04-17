import cssutils
import requests
from bs4 import BeautifulSoup

"""Read HTML file(if url is false, it will read locally from 'file_path' else from the given url) and return BeautifulSoup object."""
def read_html_file(file_path, url):
    if url:
        r = requests.get(url)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(r.text)
    with open(file_path, "r", encoding="utf-8") as file:
        html_doc = file.read()
    return BeautifulSoup(html_doc, "html.parser")


def check_tag_with_attr(tag, tag_attr_type, tag_attr_val, soup):
    if tag:
        if tag_attr_type:
            # If both tag and tag_attr_type are specified, find tags with the specified attribute
            tags_with_attr = []
            for t in soup.find_all(tag):
                # Check if the tag has the specified attribute
                if tag_attr_type in t.attrs:
                    # If the attribute type is 'class', handle multiple class values
                    if tag_attr_type == 'class':
                        # Check if the attribute value is a list
                        if isinstance(t[tag_attr_type], list):
                            # If it's a list, check if any of the values match tag_attr_val
                            if tag_attr_val in t[tag_attr_type]:
                                tags_with_attr.append(t)
                        else:
                            # If it's not a list, split the string value and check if tag_attr_val is among them
                            if tag_attr_val in t[tag_attr_type].split():
                                tags_with_attr.append(t)
                    else:
                        # For other attribute types, compare the attribute value directly
                        if t[tag_attr_type] == tag_attr_val:
                            tags_with_attr.append(t)
            return tags_with_attr
        else:
            # If only the tag is specified, find tags without considering attributes
            return soup.find_all(tag)
    else:
        # If tag is not specified, find tags with the specified attribute type and value
        tags = soup.find_all(attrs={tag_attr_type: tag_attr_val})
        return tags

# Example usage:
# Check tags with class="welcome-section"
# tags = check_tag_with_attr(False, 'class', 'welcome-section', soup)


def check_tag_with_attr_has_child_with_attr(parent_tag, parent_attr_type, parent_attr_val, child_tag, child_attr_type, child_attr_val, soup):
    p_tags = check_tag_with_attr(parent_tag, parent_attr_type, parent_attr_val, soup)
    
    if child_tag or child_attr_type:
        # If child_tag or child_attr_type is provided, recursively check child tags
        c_tags = []
        for p_tag in p_tags:
            # Find child tags with the specified attributes
            c_tag = check_tag_with_attr(child_tag, child_attr_type, child_attr_val, p_tag)
            c_tags.extend(c_tag)
        # If no child tags are found with the specified attributes, return False
        return c_tags
    else:
        # If no child_tag or child_attr_type is provided, return True if parent tags exist, else False
        return p_tags
    
# Example usage:
# Check if any div tags with class="parent-class" have children with class="child-class"
# result = check_tag_with_attr_has_child_with_attr('div', 'class', 'parent-class', 'div', 'class', 'child-class', soup)


def check_media_query(sheet, max_width, attr_type, attr_value, property_type, property_value):
    # Parse CSS file
    # sheet = cssutils.parseFile(css_file)

    # Iterate through each rule
    for rule in sheet:
        # Check if the rule is a media rule
        if isinstance(rule, cssutils.css.CSSMediaRule):
            # Check if the media query matches the max-width criteria
            media_text = rule.media.mediaText
            if f'max-width: {max_width}' in media_text:
                # Iterate through each rule inside the media query
                for sub_rule in rule.cssRules:
                    # Check if the rule is a style rule and matches the attribute selector
                    if isinstance(sub_rule, cssutils.css.CSSStyleRule):
                        # Check if the rule matches the specified attribute selector
                        if attr_type in sub_rule.selectorText and attr_value in sub_rule.selectorText:
                            # Check if the property exists and matches the specified value
                            if sub_rule.style.getPropertyValue(property_type) == property_value:
                                return True
    return False

# Example usage:
# Check if any tag with attr_type=".section" in media query with max-width=max-width has property_type="top" and property_value = '0'
# result = check_media_query(sheet, '500px', '.section', '', 'top', '0')

def check_css_rules(sheet, selector, attributes):

    # Initialize a variable to track if the selector is found
    selector_found = False

    # Iterate through each rule
    for rule in sheet:
        # Check if the rule is a style rule (CSSStyleRule)
        if isinstance(rule, cssutils.css.CSSStyleRule):
            # Check if the rule matches the given selector
            if selector in rule.selectorText:
                # Set selector_found to True as the selector is found
                selector_found = True

                # Get the style declaration of the rule
                style = rule.style

                # Iterate over the attributes to check
                for attr_name, attr_value in attributes.items():
                    # Check if the rule contains the attribute and its value
                    if style.getPropertyValue(attr_name) != attr_value:
                        # If any attribute does not match, return False
                        return False

    # If the selector is not found, return False
    if not selector_found:
        return False

    # If all attributes match, return True
    return True

# Example usage:
# Check if any class="welcome-section" has attributes = {"top": "0", "position": "fixed"}
# result = check_css_rules(sheet, '.welcome-section', attributes)


# Read HTML file
soup = read_html_file("index.html", False)

# Read CSS file
css_file = "styles.css"
sheet = cssutils.parseFile(css_file)



if check_tag_with_attr('div', 'class', 'welcome-section', soup):
    print("found")

if check_tag_with_attr(False, 'href', 'www.google.com', soup):
    print("found :)")

if check_tag_with_attr_has_child_with_attr('div', 'id', 'parent-class', False, False, False, soup):
    print("found")
else:
    print("Not found")


max_width = '500px'
attr_type = '.section'
attr_value = ''
property_type = 'top'
property_value = '0'

result = check_media_query(sheet, max_width, attr_type, attr_value, property_type, property_value)
print(result)


selector = ".nav"
attributes = {"top": "0", "position": "fixed", "left": "0"}

result = check_css_rules(sheet, selector, attributes)
print(result)
    

