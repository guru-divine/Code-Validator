# Web Development Assignment Validator
This repository contains a validator tool designed for evaluating code submissions for a learning platform's Web Development assignment. The validator provides clear feedback to users, indicating any areas where their code does not meet the specified criteria.

## Features
Validates code submissions based on a set of predefined criteria.
Provides detailed feedback to users on areas of improvement.
Supports checking for the following criteria:
* Your portfolio should have a "Welcome" section with an id of welcome-section.
* Your #welcome-section element should contain an h1 element.
* You should not have any empty h1 elements within #welcome-section element.
* You should have a "Projects" section with an id of projects.
* Your portfolio should contain at least one element with a class of project-tile.
* Your #projects element should contain at least one a element.
* Your portfolio should have a navbar with an id of navbar.
* Your #navbar element should contain at least one a element whose href attribute starts with #.
* Your portfolio should have an a element with an id of profile-link.
* Your #profile-link element should have a target attribute of _blank.
* Your portfolio should use at least one media query.
* Your #navbar element should always be at the top of the viewport.
  
## Approach
Here's a refined breakdown of my approach:

1. **Modular Functions**: I've meticulously crafted a collection of modular functions, each tailored to assess a specific criterion. This deliberate design choice not only bolsters code readability and maintainability but also sets the stage for effortless expansion with additional criteria.

2. **Readability**: By adhering to a structured and intuitive code organization, I've ensured that every aspect of my implementation is comprehensible at a glance. This approach not only facilitates easy comprehension but also lays a solid foundation for future collaborators to seamlessly integrate new criteria.

3. **Parameterization**: My functions are elegantly parameterized, affording them the flexibility to adapt to diverse inputs. For instance, the `check_no_empty_tag_in_id_name()` function gracefully accommodates variations in tag names, ID identifiers, and BeautifulSoup objects, empowering it to assess any tag within any designated ID element effortlessly.

4. **HTML and CSS Parsing**: Leveraging the robust capabilities of BeautifulSoup for HTML parsing and cssutils for CSS parsing, I've equipped my validator with formidable tools for dissecting and manipulating code submissions. This potent combination ensures efficient extraction of pertinent information, laying the groundwork for smooth expansion with additional validation requirements.

5. **Iterative Checking**: Through a systematic and methodical approach, I meticulously iterate through each criterion, harnessing dedicated functions to ascertain compliance. This meticulous methodology not only fosters comprehensive validation but also paves the way for seamless integration of new criteria into the evaluation process.

6. **Feedback Generation**: Armed with a judiciously crafted feedback mechanism, I furnish users with insightful guidance on areas warranting enhancement. This constructive feedback not only empowers users to rectify deficiencies but also serves as a roadmap for refining the validator with additional validation criteria.

7. **Scalability**: A cornerstone of my implementation lies in its inherent scalability. By encapsulating validation logic within modular functions and embracing parameterization, I've architected a solution poised for expansion. With minimal effort, new criteria can seamlessly integrate into the existing framework, ensuring the validator remains adaptable to evolving requirements.

## Getting Started
To get started with exploring the code, simply navigate to the respective file of interest. You can review the code files directly on GitHub or clone the repository to your local machine for a more in-depth analysis.
### Clone the Repository:

Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/guru-divine/Code-Validator.git
```
### Install Dependencies:

Before running the validation script, make sure to install the required Python packages. You can do this using pip:
```bash
  pip install beautifulsoup4 cssutils requests
```
### Run the Validation Script:

Once the dependencies are installed, you can execute the validation script. Navigate to the cloned repository directory and run the Python file:
```bash
  cd Code-Validator
  python app.py
```
This will execute the validation script, which will analyze your HTML and CSS files against the predefined criteria and provide feedback on areas that need improvement.

By following these steps, you can quickly set up the environment and evaluate your code submissions using the validation script.
