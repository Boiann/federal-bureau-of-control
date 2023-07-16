<!-- Code for readme adapted from author's own project (Portfolio 2),
https://github.com/Boiann/budget-calculator -->

# FEDERAL BUREAU OF CONTROL

FEDERAL BUREAU OF CONTROL is a Project 4 for Code Institute Full-stack development program: Full-Stack Toolkit. Made with passion for anyone interested in Control, a game by Remedy Entertainment Plc. Federal Bureau of Control (FBC) is a part of the game narrative and much of the game lore & events are presented through FBC documents found in-game. This Project was an attempt to bring the FBC to life, and imagine how it would look like in real life.

![Responsive website image](assets/images/general/fbc-responsive-img.png)

Visit the live site [Here.](https://federal-bureau-of-control.herokuapp.com/ "Link to Federal Bureau of Control")

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

The idea for the project was conceived when brainstorming about what can be made that is like a blog, but not an actual blog. After finding the inspiration in FBC, the wireframes and flowcharts were developed, keeping Agile methodology in mind.
Using mainly Django, a Python back-end development framework and Bootstrap, front-end (CSS) framework, this project was brought to life.
The idea was to develop a website representing secretive fictional government. This meant there is little to none of the kind expressions (please, thank you) and the instructions/messages for the user are serious and to the point (warning modals). This does not take away from ux in general, everything is made to run smoothly and without errors with intuitive website navigation.
The admin (Director) has the power to view, approve/deny, delete and modify user reports and comments (CRUD). Additionally, the admin can censor any text from the Django admin page.
The user can add/modify/delete and view their own report of strange/unusual/paranatural event (CRUD), submit comments to any report and approve or deny reports (like/dislike). The user is taking on a role of an Agent of the FBC while registered/logged in on the website, and the admin is the Director. 
Adding all of these things together (and much more) will hopefully give any user an rewarding and exciting experience, letting them immerse themselves in Control fiction.

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
 - the background inverted pyramid - [Cloudinary link](https://res.cloudinary.com/boiann/image/upload/v1689443363/Mine/site-imgs/fbc-background-image_ldmqvl.png "Link to inverted pyramid background image")
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

  - *Registerig, logging in/out:*  
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
    - The user can add comment to the report with success message after submission, there is no admin approval for comments. This was advised by project mentor, having comments without approval will ease things with project assessment but still work as intended.
    - The user can see other people's comments .

  - *My Reports page:*
    - This page contains user's submitted reports, even if they are not published/approved.
    - The user can click on a report, and 'Update/Edit' and 'Delete' buttons are now visible under the report text, colored brightly green and red to attract attention. The Update and Delete buttons are shown to the user if the user opens their own report from Reports page too.
    - Update and Delete buttons lead the user to their respective pages. If updated, the user is returned to the report being updated, if deleted the user is brought back to 'My Reports' page.

  - *Footer:*
    - Footer is retained across all pages and contains links to the Control Wiki Fandom, Control Remedy developer site and this project GitHub repository, all opening in separate tabs.
    - Footer also contains copyright for both this project and intellectual property rights.
    - Already mentioned 'Launch Content Disclaimer' button for modal is situated the bottom of every page.

  - *Error pages*
    - Two error pages are supported, 404 (page not found) and 500 (internal server error), both with buttons that guide the user back to the home page.   

### **Database Design**

  - Two classes were made for this project; Event and Comment.

The Event class is the main custom class in this project as the function of the site is for the users/Agents to share their reports on paranatural phenomena to the FBC.
The Comment class is used to represent text that a user creates and attaches to a particular report. Report can have many comments but each comment can only belong to one report/event. Each comment can have only one author, but each user can write many comments on multiple reports.

  - Database Relationships:
    - User-Event is one-to-many = user can have many Reports but each Report can belong to only one user
    - Event-Like/Dislike is many-to-many = Report can have have likes/dislikes from many users and user can like/dislike many Reports
    - Event-Comment is one-to-many = Report can have many comments but each comment can belong to only one Report
    - Comment-User is one-to-many = user can have many comments but each comment can belong to only one user

  - Database schema:

  - *Event*

| Field Name      | Field Type              | Description                                   |
| --------------- | ----------------------- | --------------------------------------------- |
| id              | IntegerField (PK)       | Primary key for the event                     |
| title           | CharField               | The title of the event                        |
| slug            | SlugField               | A slugified version of the title for URL purposes |
| author_id       | ForeignKey (User)       | Foreign key to the User table                  |
| featured_image  | CloudinaryField         | Cloudinary field for the featured image        |
| excerpt         | TextField               | Excerpt of the event                           |
| updated_on      | DateTimeField           | The datetime when the event was last updated   |
| content         | TextField               | The content of the event                       |
| created_on      | DateTimeField           | The datetime when the event was created        |
| approved        | BooleanField            | Indicates whether the event is approved        |
| status          | IntegerField            | Status of the event (0 for Draft, 1 for Published) |
| likes           | ManyToManyField (User)  | Users who liked the event                      |
| dislikes        | ManyToManyField (User)  | Users who disliked the event                   |

  - *Comment*

| Field Name  | Field Type              | Description                                   |
| ----------- | ----------------------- | --------------------------------------------- |
| id          | IntegerField (PK)       | Primary key for the comment                    |
| post_id     | ForeignKey (Event)      | Foreign key to the Event table                 |
| name        | CharField               | Name of the commenter                          |
| email       | EmailField              | Email of the commenter                         |
| body        | TextField               | The comment text                               |
| created_on  | DateTimeField           | The datetime when the comment was created      |
| approved    | BooleanField            | Indicates whether the comment is approved      |
| status      | IntegerField            | Status of the comment (0 for Draft, 1 for Published) |

The provided database schema consists of two tables: Event and Comment. The Event table contains fields: event's unique identifier, title, slug for URL purposes, author reference, featured image, excerpt, content, creation and update timestamps, approval status, and a status indicator. Additionally, there are many-to-many fields for users who liked or disliked the event. The Comment table includes fields like the comment's ID, associated event, commenter's name and email, comment body, creation timestamp, approval status, and a status indicator. This schema enables the storage and organization of events with their respective comments, providing a structured and efficient way to manage and retrieve event-related data.

### **Wireframes**

Wireframes for the project were developed right after the idea for the project was chosen.
Wireframes for Assessment Guide and Project Planning & Ux were made before the ones for the content of the pages themselves.

<details>
<summary>Assessment guide wireframe</summary>

![Assessment guide wireframe](assets/wireframes/portfolio-4-assessment-guide.png)
</details>

<details>
<summary>Project planning wireframe</summary>

![Project planning wireframe](assets/wireframes/portfolio-4-planning-and-ux.png)
</details>

There are three wireframes for the project. Using Agile, the basic or Minimal Viable Product (MVP) was to be made first, then if time allows it the scope can increase, making the project grow towards Enhanced and finally Superior project.

Differences between scopes were considered early as to allow for the use of Agile methodology. Personal, work, family, dependants and health situations were considered to have impact on time available for the project. Ideally, maximum time was to be taken to finish the project making the scope bigger.

<details>
<summary>MVP wireframe</summary>

![MVP wireframe](assets/wireframes/fbc-mvp-wireframe.png)
</details>

<details>
<summary>Mobile wireframe</summary>

![Mobile wireframe](assets/wireframes/fbc-mobile-wireframe.png)
</details>

<details>
<summary>Enhanced wireframe</summary>

![Enhanced wireframe](assets/wireframes/fbc-enhanced-wireframe.png)
</details>

<details>
<summary>Superior wireframe</summary>

![Superior wireframe](assets/wireframes/fbc-superior-wireframe.png)
</details>

[Back to top ⇧](#federal-bureau-of-control)

---

## **Agile Project Management**

This project was developed using the Agile methodology.
The key principles adopted were; focus on the essential features first, work in small iterations and add extra features/expand scope as time permitted.
GitHub's kanban board was used for organization of milestones, epics, issues, labels, and project features.

- [FBC Project Board](https://github.com/users/Boiann/projects/11/views/6)

The project was divided into 5 Milestones : MVP, Enhanced Project, Superior Project, Backlog and Submission Prep.
Backlog milestone was used to place all the issues not finished in previous iteration into it.

- [FBC Milestones](https://github.com/Boiann/federal-bureau-of-control/milestones)

The structure of development was: Milestone => Epic => Task/User Story.
Epics were considered as iterations, and all of them contained 5 issues. Using the MoSCoW prioritization technique, they were separated into 60% as Must Have, 20% Should Have and 20% Could Have.

Three templates were used to create the respective Epic, Task and User Story:
  - [EPIC](https://github.com/Boiann/federal-bureau-of-control/issues/new?assignees=&labels=&projects=&template=epic.md&title=EPIC%3A+TITLE)
  - [TASK](https://github.com/Boiann/federal-bureau-of-control/issues/new?assignees=&labels=&projects=&template=task.md&title=TASK%3A+TITLE)
  - [USER STORY](https://github.com/Boiann/federal-bureau-of-control/issues/new?assignees=&labels=&projects=&template=user-story.md&title=USER+STORY%3A+TITLE)

Colored text was used when possible (using Tex) for organizing, color-coding and visual distinction.

**Agile Planning**

Before writing any code, everything was considered and planned as much as possible.

<details>
<summary>Timeboxing - GLOBAL</summary>
As this is a project being developed with agile methodology, the following calculations are not set in stone, and there is a lot of flexibility calculated in the final numbers. I've decided to do the calculations to mainly help myself, to put the available time in perspective regarding the development.
Things can change and there can always be an event or something might happen ( when developing my PP3 the PC's PSU died and that set me back a week ).
This is why it makes it easier for me if I have these calculations beforehand and can adjust accordingly.


PP4 Due 03.07.2023 12:00

Project needs to be ready ideally a week before to account for:
								- possible issues with internet connection  
								- issues with development environment
								- any other act of "divine power"

= CALCULATION =

PP4 Due 26.06.2023

Project start date: 17.04.2023

Available weeks for development: 10

Days off per week: 3

Account for springtime chores and tasks (outside work, mowing, repairs etc) : two 1/2 days per week (get up early and work on project for half a day),
or one full day

On days that working in the store: 2 hrs/day


= CALCULATION = 

Full days available per week: 2 (12hrs/day ideally, 10 more likely) = 20 hrs
When working in store = 4 days = 8 hrs


= FINAL PREDICTION =

Can invest about 28 hrs/week = round up to 30


IDEAL TOTAL HRS FOR PROJECT DEVELOPMENT = 30 hrs x 10 weeks === 300 Hrs


The actual number will probably be lower accounting for out of my control situations,

FINAL TOTAL === 250 hrs.
            === 25 hrs/week
</details>

<details>
<summary>Timeboxing Milestones-Epics</summary>
Epic = weekly timebox (2 days off from work, could be split in two - Epic/day)Prepare th

Weeks Available = 10

1. Milestone - MVP = 5 weeks timebox

1. EPIC - Django Setup and early deployment
2. EPIC - Set up models and views
3. EPIC - User registration/login, CRUD
4. EPIC - Content and navigation - basic
5. EPIC - Content and navigation beautify/Testing

2. Milestone - Enhanced Project = 2 weeks timebox

6. EPIC - Logic/functionality enhancements
7. EPIC - Ux/content enhancements

3. Milestone - Superior Project = 2 weeks timebox

8. EPIC - Logic/functionality enhancements
9. EPIC - Ux/content enhancements

4. Milestone - README = 1 week timebox

10. EPIC - README update and finish up
</details>

<details>
<summary>Timeboxing - ITERATION</summary> 
Similar to Time calculations - GLOBAL, these calculations are not set in stone (they're agile!) but serve as a guide/organizing tool for myself.


- Task to be finished in a day preferably
- Include revisions
- Timeboxing - goal oriented, iteration/meeting/milestone level
- MoSCoW technique = Must, Should, Could, Won't HAVE in each iteration/milestone
- Must have - 60%, should have 20%, could have 20%, add labels for each


= ITERATION TIMEBOXING = 

- Iteration being on a daily basis for days off ( 10 hrs/day ) 
- The day before, preferably prepare the next day's iteration plan using Projects Board/Issues and do a revision of work done
- The rest of the days when working in store - deal with bugs/problems/plan ahead


= EPIC/MILESTONE TIMEBOXING = 

- Epic/Milestone should be on a weekly basis ( approx 25 hrs )
- The day before, preferably prepare the next week's milestone plan using Projects Board/Issues and do a revision of work done
</details>

<details>
<summary>FBC Timeboxing/Project Flow Image</summary>

![FBC Timeboxing/Project Flow Image](assets/images/general/fbc-timeboxing.png)
</details>

---

**Version Control**
Git branching/squashing and merging was used in this project. When work was to be done a separate branch was made, using author's own created [Guide](https://github.com/Boiann/branching-merging-squashing). The strategy was to have each branch dedicated to one feature/fix/issue or epic/iteration. After the work was completed on a particular branch, the branch would be squashed and merged to the main branch. The squashed branches are then usually deleted, but they are left as is in this project to demonstrate development.

---

Unfortunately medical and other issues prevented full use of all this planning. After a lengthy hiatus from working on the project, the MVP epics/tasks/user stories were placed in BACKLOG Milestone to signify this. Work on the project continued from there. After talking to a mentor, it was decided not to close unfinished epics/tasks/user stories. The explanation was that this is what happens in real-life development too (unfinished things), and FBC Project Board reflects that.

---

[Back to top ⇧](#federal-bureau-of-control)

---

## **Features**

All of the features presented in this sections are fully responsive on all devices and screen widths.
Please refer to [TESTING.md](/TESTING.md) for more information about responsiveness testing.

### **Intro/splash/index**

<details>
<summary>Content disclaimer firing when opening the page for the first time, not firing on subsequent visit, spinning logo and animated center text</summary>

![Content disclaimer](assets/features/1-intro-modal.gif)
</details>

<details>
<summary>Content disclaimer firing when the user clicks on it, link inside the modal opens in a new tab, close modal button</summary>

![User Content disclaimer](assets/features/2-content-modal-link.gif)
</details>

<details>
<summary>Footer links open in a new tab, tooltips present on logo, title and footer links</summary>

![Footer links](assets/features/3-footer-links.gif)
</details>

### **Home**

<details>
<summary>Unregistered user can open home page, warning modals for reports/create reports</summary>

![Unregistered user modals](assets/features/4-unregistered-modals.gif)
</details>

<details>
<summary>Unregistered user warning modal links and close button</summary>

![Unregistered user warning modal links and close button](assets/features/5-unregistered-modal-links.gif)
</details>

<details>
<summary>Home page 'More Info' modals</summary>

![Home page 'More Info' modals](assets/features/6-home-modals.gif)
</details>

### **Sign Up**

<details>
<summary>Cross-links between Sign-up and Log In</summary>

![Cross-links between Sign-up and Log In](assets/features/7-register-login-cross-links.gif)
</details>

<details>
<summary>Successful registering success message</summary>

![Successful registering success message](assets/features/8-registering-success.gif)
</details>

### **Log In/Out**

<details>
<summary>Successful login success message, Agent name in top right corner</summary>

![Successful login success message, Agent name in top right corner](assets/features/9-login-success.gif)
</details>

<details>
<summary>GitHub log in</summary>

![GitHub log in](assets/features/10-github-register.gif)
</details>

<details>
<summary>Sure you want to log out page, logging out success message, no Agent name in top right corner</summary>

![Sure you want to log out page, logging out success message, no Agent name in top right corner](assets/features/11-logout-success.gif)
</details>

### **Reports**

<details>
<summary>Paginated view of reports with like/dislike counters, next/back page button</summary>

![Paginated view of reports with like/dislike counters, next/back page button](assets/features/12-reports-paginated.gif)
</details>

<details>
<summary>Open an report, like/dislike buttons</summary>

![Open an report, like/dislike buttons](assets/features/13-open-report.gif)
</details>

<details>
<summary>Adding a comment, comments counter updating, if no comments - message</summary>

![Adding a comment, comments counter updating, if no comments - message](assets/features/14-comment.gif)
</details>

### **Create Report**

<details>
<summary>Adding a report, template image if no image uploaded, director approval needed message and redirect to My-Reports page, added report not visible on Reports page</summary>

![Adding a report, template image if no image uploaded, director approval needed message and redirect](assets/features/15-add-report.gif)
</details>

### **My Reports**

<details>
<summary>Paginated view of user's reports, unique for each user, Update/Edit and Delete buttons show up for user's own report</summary>

![Paginated view of user's reports, unique for each user, Update/Edit and Delete buttons show up for user's own report](assets/features/16-user-report.gif)
</details>

<details>
<summary>Update Report and success message</summary>

![Update Report and success message](assets/features/17-update-report.gif)
</details>

<details>
<summary>Delete Report, 'are you sure' question and success message</summary>

![Delete Report, 'are you sure' question and success message](assets/features/18-delete-report.gif)
</details>

### **Admin/Director site differences**

<details>
<summary>Director access extra nav link for admin opening admin page in a separate tab, top right corner changes from Agent: *user* to Director: *user*</summary>

![Director access extra nav link for admin opening admin page in a separate tab, top right corner changes from Agent: *user* to Director: *user*](assets/features/19-admin-login.gif)
</details>

<details>
<summary>Reports and Create Report has no warning text for admin</summary>

![Reports and Create Report has no warning text for admin](assets/features/20-admin-no-warning.gif/)
</details>

### **Admin page**

<details>
<summary>Admin can approve and publish report, visible on Reports page to a normal user</summary>

![Admin can approve and publish report, visible on Reports page to a normal user](assets/features/21-admin-report-approve.gif)
</details>

<details>
<summary>Admin can create a draft report</summary>

![Admin can create a draft report](assets/features/22-admin-draft.gif)
</details>

<details>
<summary>Admin can change a report, censoring perk</summary>

![Admin can change a report, censoring perk working](assets/features/23-admin-censor.gif)
</details>

<details>
<summary>Admin can delete a report and user</summary>

![Admin can delete a report and user](assets/features/24-admin-delete.gif)
</details>

<details>
<summary>Admin can approve and change a comment</summary>

![Admin can approve and change a comment](assets/features/25-admin-comment-change.gif)
</details>

<details>
<summary>Admin can delete a comment</summary>

![Admin can delete a comment](assets/features/26-admin-delete-comment.gif)
</details>

### **Error pages**

<details>
<summary>Error 400 (page not found) page with 'Go Home' button</summary>

![Error 400 (page not found) page with 'Go Home' button](assets/features/27-error-400.gif)
</details>

<details>
<summary>Error 500 (internal server error) page with 'Go Home' button</summary>

![Error 500 (internal server error) page with 'Go Home' button](assets/features/28-error-500.gif)
</details>

---

[Back to top ⇧](#federal-bureau-of-control)

---

## **Future Implementations**

The following features could be added to FBD in the future. Project deadline influenced heavily what was left out.

  - Fix naming of the classes vs pages, for example the event class is used to produce Report. The event class was conceived early in the project and left as is rather than to risk breaking the code somewhere, rendering the project submission in danger.
  - After user submits a comment, the success message is rendered at the top of the page, it would be a better UX if the user is left where the comment was entered.
  - Ability for the user to modify/delete their comments
  - Adding a event/report type selector for the user, so when the user is submitting a report there is a choice of what type of event/report it is (AWE, AI, OoP)
  - Make dedicated page with image carousel for each type of report (AWE, AI, OoP)
  - Use some kind of text censoring API, to make censoring of the reports automated
  - Add email required, working email verification and password recovery
  - More social sign-in options
  - GitHub sign in button on Register page
  - Clean up of style.css. The css file is very big, consisting of more than 10 000 lines of code (not minified). The solution was looked for ([PurgeCSS](https://medium.com/dwarves-foundation/remove-unused-css-styles-from-bootstrap-using-purgecss-88395a2c5772)) and tried but was not successful within the project submission timeframe.

These were only some of project enhancements that could be done. Using other Django apps and other API-s, logic and creativity could make this project into something really wonderful.

[Back to top ⇧](#federal-bureau-of-control)

---

## **Technologies Used**

### **Languages Used**

- [HTML](https://en.wikipedia.org/wiki/HTML5) - For adding content and formatting.
- [CSS](https://en.wikipedia.org/wiki/CSS) - For adding style and colours.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - For adding interactive features.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - High-level, general-purpose programming language.

### **Django and Python Packages**

- [Django](https://www.djangoproject.com/) - A Python-based web framework that follows the model-template-view architectural pattern, used for building the project.
- [django-allauth](https://django-allauth.readthedocs.io/) - A Django application used for account registration, management, and authentication.
- [cloudinary_storage](https://cloudinary.com/) - A Django storage backend for Cloudinary, used for image hosting and storage.
- [django_summernote](https://django-summernote.readthedocs.io/) - A Django application that integrates the Summernote WYSIWYG editor into Django projects.
- [crispy_forms](https://django-crispy-forms.readthedocs.io/) - A Django application that makes it easy to style Django forms.
- [crispy_bootstrap5](https://pypi.org/project/crispy-bootstrap5/) - A package that provides Bootstrap 5 styling for Django crispy-forms.

### **Programs/Tools Used**

- [GitHub](https://github.com/) - Source code hosted on GitHub, deployed using Git Pages.
- [GitPod](https://www.gitpod.io/) - Used to commit, comment and push code during the development process.
- [Font Awesome](https://fontawesome.com/) - Font Awesome use dto source necessary icons used in the project.
- [Balsamiq](https://balsamiq.com/) - Used to create wireframes and website structure map for the project.
- [Google Keep](https://keep.google.com/) - Used to make notes during the project duration.
- [LanguageTool](https://languagetool.org/) - Used for general spell-check.
- [Google Fonts](https://fonts.google.com/) - Used to import fonts to the project.
- [GifCap](https://gifcap.dev/) - Used to capture gif-s of the project .
- [Heroku](https://www.heroku.com/) - Used to deploy the project.
- [Lucidchart](https://www.lucidchart.com/pages/examples/flowchart-maker) - Used to make the iteration flowchart for the project.
- [Bootstrap clean blog](https://startbootstrap.com/theme/clean-blog) - Bootstrap blog template imported in for content management and CSS.
- [ElephantSQL](https://www.elephantsql.com/) - Free and open-source relational database management system (RDBMS).
- [Bootstrap5](https://getbootstrap.com/) - Used for adding predefined styled elements and creating responsiveness.
- [JsHint](https://jshint.com/) - Used for validating the javascript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validating the python code.
- [HTML W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - Used for validating the HTML.
- [CSS Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - Used for validating the CSS.
- [Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - For debugging the project.
- [W.A.V.E.](https://wave.webaim.org/) - Used for testing accessibility.
- [LightHouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used for testing performance.

[Back to top ⇧](#federal-bureau-of-control)

---

## **Deployment**

- Clone Code Institute Template Repository
- Initialize GitPod Workspace by clicking on the GitPod button on the repository
- Install support libraries and Django according to the guide on Code Institute
- Create requirements.txt
- Create Django project
- Set up ElephantSQL Account
- Set up Cloudinary Account
- Create env.py to hold sensitive data
- Create Heroku app
- For the final deployment, the debug setting in settings.py must be set to false
- Before final deployment, the DISABLE_COLLECTSTATIC config var in Heroku was removed
- From Heroku connect to github repository 
- Deploy from selected GitHub branch
- Click on Deploy button => project is now deployed.

An early deployment guide was made before project start to ensure success in creating the project:
<details>
<summary>Early deployment guide</summary>

---

Create repo as usual, from template

Create user stories/issues - LOOK UP PREVIOUS GUIDE ABOUT PROJECTS/about milestones etc

GITPOD

IF ERROR BUILDING IMAGE - REFRESH PAGE
- pip3 install 'django<4' gunicorn
- pip3 install dj_database_url==0.5.0 psycopg2
- pip3 install dj3-cloudinary-storage
- pip3 freeze --local > requirements.txt

=====  DONT FORGET THE FULL STOP  ====

<django-admin startproject PROJ_NAME .>   


python3 manage.py startapp APP_NAME

=== in settings.py, to INSTALLED_APPS array, add APP_NAME

python3 manage.py migrate

python3 manage.py runserver  ===> for TESTING, should see django install congrats

DO NOT COMMIT

HIDING SECRET KEY
- Create File => .env
- Cut this from settings.py =>
- SECRET_KEY = '-----your secret key-----'
- Paste in .env
- Write this in settings.py =>
- from decouple import config
- SECRET_KEY = config("SECRET_KEY")
- Write this in terminal or cmd =>
- pip install python-decouple

FOLLOW HEROKU INSTRUCTIONS

FOLLOW ESQL INSTRUCTIONS

in env.py 
- import os
- os.environ["DATABASE_URL"]="<copiedURL>"     === url from ESQL
- os.environ["SECRET_KEY"]="my_super^secret@key"    === Django Secret key

in settings.py
- import os
- import dj_database_url
- if os.path.isfile('env.py'):
- import env

replace Django secret with === SECRET_KEY = os.environ.get('SECRET_KEY')

replace this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
  }
}
```
with this:
```
 DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }
```

!!! IMPORTANT  -  CTRL+S everything

python manage.py migrate

CONNECTION CHECK ON ESQL

Add, commit, push
RE CHECK python3 manage.py runserver

Add secret key and secret database to heroku config vars, key=PORT value=8000

Cloudinary
- in env.py do 
- os.environ["CLOUDINARY_URL"] = 'API_KEY_HERE'
- add it to Heroku config vars
- add to Heroku config vars:
- key=DISABLE_COLLECTSTATIC    value=1


to INSTALLED_APPS in settings.py add:
```
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'blog',
```

below STATIC_URL = '/static/'  add
- STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
- STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

- MEDIA_URL = '/media/'
- DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

below BASE_DIR = Path(__file__).resolve().parent.parent add
- TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

update to this:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

update ALLOWED_HOSTS = ['<APP NAME>.herokuapp.com', 'localhost']

CREATE FOLDERS
- media, templates, static

create Procfile and put === web: gunicorn codestar.wsgi

git add, commit and push

deploy from Heroku via GitHub.
</details>

[Back to top ⇧](#federal-bureau-of-control)

---

## **Testing**

Testing information can be found in a separate testing file [TESTING.md](/TESTING.md).

[Back to top ⇧](#federal-bureau-of-control)

---

## **Credits**

### **Code used and adapted**

 - Previous projects of the developer were used, [Boudoir Studio](https://boiann.github.io/boudoir-studio/index.html) ( GithHub repository [here](https://github.com/Boiann/boudoir-studio) ), [Budget Calculator](https://boiann.github.io/budget-calculator/) ( GithHub repository [here](https://github.com/Boiann/budget-calculator) ) and [Space Quiz](https://space-quiz.herokuapp.com/) ( GithHub repository [here](https://github.com/Boiann/space-quiz) ) as a source for looking up the code/solutions for CSS and README purposes mainly.

 - [Federal Bureau of Control / Records Archive System](https://control-records.netlify.app/document/593134886/ai80-ue-movie-camera-supplement) was used as a project inspiration and as a source of Reports entries text, as well as censoring text inspiration. Code (text for generating example reports) was used with blessing of the FBC Archive System author, [Lou Huang](https://louhuang.com/), whose permission was asked for through email.

 - All characters, events and situations depicted (except for user self-made entries) are products of and copyrighted by [Remedy Entertainment Plc](https://www.remedygames.com/).

 - All images and text for describing AWE's, AI's and OoP's were sourced from [Control Wiki](https://control.fandom.com/wiki/Control_Wiki).

 - Code Institute guide/lessons were heavily relied on while working on development, mainly for the back-end. After the back end was developed the front end was adjusted.

 - [Django documentation](https://docs.djangoproject.com/en/4.2/) was relied on to find code for back-end solutions and code.

 - [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) was relied on to find code for front-end solutions and code. 

 - How do create url to django Admin within user page (HTML), code found on [Stack Overflow](https://stackoverflow.com/questions/55917136/how-do-create-url-to-django-admin-within-my-user-page-html).

 - Error pages how-to, found [here](https://frontendshape.com/post/bootstrap-5-404-page-examples) and [here](https://studygyaan.com/django/how-to-use-custom-500-error-template-in-django).

 - How to force refresh of the entire local storage, found on [Stack Overflow](https://stackoverflow.com/questions/75389242/how-can-i-force-refresh-of-the-entire-local-storage).

 - Adding Social Authentication to Django, found [here](https://testdriven.io/blog/django-social-auth/).

 - Changing Text Animation CSS, found on [CodePen](https://codepen.io/codingyaar/pen/LYJQaBe).

 - Censor Bars Text Animation For Del Text, found [here](https://codemyui.com/censor-bars-%E2%96%88%E2%96%88%E2%96%88%E2%96%88-text-animation-for-del-text/).

 - CSS 3D Rotate Animation, found on [CodePen](https://codepen.io/sungaila/pen/LzMgjE).

 - How to trigger bootstrap modal just once, found on [Stack Overflow](https://stackoverflow.com/questions/60539856/how-to-trigger-bootstrap-modal-just-once-and-using-browser-localstorage-to-detec).

 - Bootstrap templates used, [Clean Blog](https://startbootstrap.com/theme/clean-blog), [The Big Picture](https://startbootstrap.com/template/the-big-picture) and [Small Business](https://startbootstrap.com/template/small-business).

### **Websites visited for info and solutions**

There were many sites visited during the duration of the project.
[Google](https://google.com/ "Google home page") was used to produce results of the specific query, and [Stack Overflow](https://stackoverflow.com/ "Stack Overflow home page") proved to be the best source of information for various queries/issues. 

Standouts are [Django documentation](https://docs.djangoproject.com/en/4.2/), [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) and [Django-blog](https://djangocentral.com/building-a-blog-application-with-django/) that helped immensely.

A lot of other projects were looked into to help with development, standouts are [Bawarchi Khana](https://github.com/eleanorbucke21/PP4), [BookShelf](https://github.com/Code-Institute-Submissions/ci-project-21), [Just-beats](https://github.com/johnrearden/just-beats), [Italianissimo](https://github.com/useriasminna/italianissimo-booking-website) and [Support Hub](https://github.com/ianmeigh/support-hub).



###  **Acknowledgments**

This whole project is dedicated to my passion of otherworldly and strange events and unexplainable things. The conflict between science based approach to life and the possibility of events/things we humans cannot yet comprehend will always be present. 

Special thanks to the developers of Control game, it was a wild and strange experience playing Control (back when I had spare time!).

Without support I got from other people, this project would never be realized. I'll try and remember to thank everyone and everything I can!

- M., my wife, thank you for your support and cheering me on, lifting me back up when it got hard. Thank you for taking care of all the housework and food, children and numerous other responsibilities while I was busy with full time job and doing this project on the side. Without you this journey would never be possible. And when it got hard and complicated, you never gave up on me and this dream of career change.
- A., G. and V., my three beautiful girls. Thank you for being so understanding during the project work. Thank you from the bottom of my heart for being who you are, wonderful and delightful souls. You make me proud to be your dad.
- Boris, my brother, thank you for testing my project so thoroughly, and for your support.
- Marija and Boris, my mother and father, thank you for making me feel like a superstar when I announced I'm starting this journey and your support throughout it.
- John, my friend, thank you for starting me on this path, and for your support, chats and sharing the things you learned.
- Helen from Code Institute, thank you believing in me and making this change possible.
- Slack community, thank you for being a constant source of good information and solutions.
Special mentions are Allen and Roman, whose attention to detail and suggestions made this project better after it was submitted for peer review.
- Koko, my mentor, thank you for being an incredible source of solutions and good advice, your support meant a great deal during the project.
- Student support of Code Institute, thank you for granting the project deadline extension, it was much needed and appreciated.
- C8H10N4O2 in a cup. Thank you for existing.

[Back to top ⇧](#federal-bureau-of-control)

***