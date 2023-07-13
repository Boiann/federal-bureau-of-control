<!-- Code for readme adapted from author's own project (Portfolio 2),
https://github.com/Boiann/budget-calculator -->

# FEDERAL BUREAU OF CONTROL

FEDERAL BUREAU OF CONTROL is a Project 4 for Code Institute Full-stack development program: Full-Stack Toolkit. Made with passion for anyone interested in Control, a game by Remedy Entertainment Plc. Federal Bureau of Control (FBC) is a part of the game narrative and much of the game lore & events are presented through FBC documents found in-game. This Project was an attempt to bring the FBC to life, and imagine how it would look like in real life.

<!--Am I Responsive image -->

Visit the live site [Here.](https://federal-bureau-of-control.herokuapp.com/ "Link to Federal Bureau pf Control")

---

## CONTENTS

* [Project Overview](#project-overview)
  * [Project Goals](#project-goals)

* [User Experience](#user-experience)
  * [User Expectations](#user-expectations)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Imagery](#imagery)
  * [Structure](#structure)
  * [Database Design](#database-design)
  * [Wireframes](#wireframes)

* [Agile Project Management](#agile-project-management)

* [Features](#features)

* [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Programs Used](#programs-used)

* [Deployment](#deployment)

* [Testing](#testing)

* [Credits](#credits)
  * [Code used and adapted](#code-used-and-adapted)
  * [Websites visited for info and solutions](#websites-visited-for-info-and-solutions)
  * [Acknowledgments](#acknowledgments)

---

## **Project Overview**

The idea for the project was concieved when brainstorming about what can be made that is like a blog, but not an actual blog. After finding the inspiration in FBC, the wireframes and flowcharts were developed, keeping Agile methodology in mind.
Using mainly Django, a Python back-end development framework and Bootstrap, front-end (CSS) framework, this project was brought to life.
The idea was to develop a website representing secretive fictional government. This meant there is little to none of the kind expressions (please, thank you) and the instructions/messages for the user are serious and to the point (warning modals). This does not take away from ux in general, everything is made to run smoothly and without errors with intuitive website navigation.
The admin (Director) has the power to view, approve/deny, delete and modify user reports and comments (CRUD). Additionaly. the admin can censor any text from the Django admin page.
The user can add/modify/delete and view their own report of strange/unusual/paranatural event (CRUD), submit comments to any report and approve or deny reports (like/dislike). The user is taking on a role of an Agent of the FBC while registered/logged in on the website, and the admin is the Director. 
Adding all of these things together (and much more) will hopefuly give any user an rewarding and exciting experience, letting them immerse themselves in Control fiction.

---

### **Project Goals**

 - Develop FBC website using Django and Bootstrap frameworks
 - Present the website in a clean and easy to understand manner
 - Keep good UX principles regarding layout/colours/interaction
 - Robust Python code without issues/bugs
 - Fully responsive and immersive

[Back to top ⇧](#federal-bureau-of-control)

---

## **User Experience**

### **User Expectations**

 - Able to quickly understand what the purpose of the site is
 - Intuitive navigation
 - Responsive across many different devices and screen sizes
 - Able to find basic information
 - Find additional info if needed
 - Every interaction has feedback
 - User-friendly

### **User Stories**

#### **First Time Visitor**
   - I want to know what FBC is
   - I want to navigate the website intuitively
   - I want to find additional information
   - I want to check out Control(game)
   - I want to become an Agent of the FBC

  #### **Returning User/Agent**
   - I want to log in securely
   - I want to submit my own report
   - I want to see my report submission
   - I want to modify my report
   - I want to delete my report
   - I want to add my comment to a report
   - I want to approve/deny a report

  #### **Website Admin/Director**
   - I want to log in securely and have admin access
   - I want to approve and publish user reports
   - I want to see published and approved user reports
   - I want to modify user reports and comments
   - I want to delete user reports and comments 

[Back to top ⇧](#federal-bureau-of-control)

---

## **Design**

### **Colour Scheme**

The color scheme used in the project is not explicitly defined. Using Bootstrap CSS class selectors and templates, the color scheme is a combination of light and dark colors, with white, gray, and other colors depending on the specific CSS styles applied (red/green for update/delete report). If not for the background image, it would be dark/black text over white background. This is done on purpose to maintain site cleanliness and appear more official/governmental.


### **Imagery**

Only couple of images are used that are not user-submitted; 
 - the background inverted pyramid - [Cloudinary link](https://res.cloudinary.com/boiann/image/upload/v1688484957/c1b9dbyz6skmpuslnycf.png "Link to inverted pyramid background image")
 - the inverted pyramid spinning logo(used for favicon too) - [Cloudinary link](https://res.cloudinary.com/boiann/image/upload/v1688470337/Pyramid_Shape_lilgag.webp "Link to inverted pyramid logo image")
 - FBD Seal image found on intro/splash page (used as a report placeholder too) - [Cloudinary link](https://res.cloudinary.com/boiann/image/upload/v1688458922/fbc-seal-color_ppeq9n.png "Link to FBC Seal image")
 - FBD offices image found on home - [Cloudinary link](https://res.cloudinary.com/boiann/image/upload/v1688585865/wallpaperflare.com_wallpaper_nrvimz.jpg "Link to FBC offices image")

All other images are user-submitted for their own report, first couple of created to represent what this website could look like with more users.  

### **Structure**

  - FBC website is structured in a user friendly and easy to navigate way.

  - *Intro/Splash and home pages:*

    - When the index first loads, the user is presented with intro/splash page explaining the basic purpose of the site.
    - Upon first load of the index page, content disclaimer/warning modal will fire. Any subsequent page visit will not fire the disclaimer modal automatically, but user can revisit it later with pressing 'Launch Content Disclaimer' at the bottom of every page.
    - Using MVT-based framework (Model, View, Template) base template is created with head, navigation and footer being the same on all pages, adding specific page content to it.
    - User can enter the home page using 'Enter' button presented at the middle of intro page, or use navigation link at the top of the page.
    - User can open home page with more detailed info about the FBC and various phenomena. Each phenomenon has a card with short description, and a button that fires a modal allowing for more detail on each phenomenon type.
    - User can come back to the intro/splash page by clicking on the FBC logo or title text with handy tooltips explaining this. 

  - *Registernig, logging in/out:*  
    - First time/unregistered user may click on 'Reports' and 'Create Report' nav links but will be met with 'ACCESS RESTRICTED TO AUTHORIZED AGENTS ONLY' modal message. The modal itself contains links to register/login pages.
    - First time user can register on the register page. The page contains redirect links to login if the user is mistakenly on register page, and link to login page if the user wishes to use GitHub authorisation to access site.
    - If using GitHub auth, the user is brought to the 'Log in via Github' page where the user can continue with GitHub authorization.
    - Upon registering, the 'Register' link is replaced by 'Logout' link, allowing the user to sign out from the site.
    - Logged in users will see their username displayed in the top right corner, in the style of 'FBC Agent: "username"'.
    - The user can now open the 'reports' and 'create report' pages.
    - If the logged in user is admin, instead of 'FBC Agent: "username"', the right corner will read 'Director: "username"'.
    - Logged in admin user will also have additional link in the navbar - 'Director Access' which opens admin site in a separate tab.
    - When logging in the user is brought to the home page instead of index/splash page.
    - When logging out, the user is asked 'Are you sure' before signing out.
    - When signed out, the user is brought to the index/splash page.

  - *Reports page:*
    - The user is presented with a paginated view of published and approved report submissions.
    - Each report card consists of image, title, author, time of submission, and approval/denial counters.
    - If the user clicks on a report, the main text is presented, along image, title, author, time of submission, and approval/denial counters.
    - The approve/deny buttons (thumbs up and down) are clickable and interactive, change if the user clicks them.
    - The user can add comment to the report with success message after submission, there is no admin approval for comments.
    - The user can see other people's comments .

  - *My Reports page:*
    - This page contains user's submitted reports, even if they are not published/approved.
    - The user can click on a report, and 'Update/Edit' and 'Delete' buttons are now visible under the report text, colored brightly green and red to attract attention. The Update and Delete buttons are shown to the user if the user opent theit own report from Reports page too.
    - Update and Delete buttons lead the user to their respective pages. If updated, the user is returned to the report being updated, if deleted the user is brought back to 'My Reports' page.

  - *Footer:*
    - Footer is retained across all pages and contains links to the Control Wiki Fandom, Control Remedy developer site and this project GitHub repository, all opening in separate tabs.
    - Footer also contains opyright for both this project and intellectual property rights.
    - Already mentioned 'Launch Content Disclaimer' button for modal is situated the bottom of every page.

### **Database Design**

<!-- Description and schema -->
 
### **Wireframes**

<!-- Description and images -->

[Back to top ⇧](#federal-bureau-of-control)

---

## **Agile Project Management**

[Back to top ⇧](#federal-bureau-of-control)

---

## **Features**

<!-- Features images/gifs -->

[Back to top ⇧](#federal-bureau-of-control)

---

## **Future Implementations**

<!-- Description -->

[Back to top ⇧](#federal-bureau-of-control)

---

## **Technologies Used**

### **Languages Used**

### **Programs Used**

[Back to top ⇧](#federal-bureau-of-control)

---

## **Deployment**

[Back to top ⇧](#federal-bureau-of-control)

---

## **Testing**

Testing information can be found in a separate testing file [TESTING.md](/TESTING.md).

[Back to top ⇧](#federal-bureau-of-control)

---

## **Credits**

### **Code used and adapted**

### **Websites visited for info and solutions**

###  **Acknowledgments**

[Back to top ⇧](#federal-bureau-of-control)

***