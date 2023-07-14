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
<!-- ADD IMG -->
<details>
<summary>Assessment guide wireframe</summary>

![Assessment guide wireframe](img-link)
</details>
<!-- ADD IMG -->
<details>
<summary>Project planning wireframe</summary>

![Project planning wireframe](img-link)
</details>

There are three wireframes for the project. Using Agile, the basic or Minimal Viable Product (MVP) was to be made first, then if time allows it the scope can increase, making the project grow towards Enhanced and finally Superior project.

Differences between scopes were considered early as to allow for the use of Agile methodology. Personal, work, family, dependants and health situations were considered to have impact on time available for the project. Ideally, maximum time was to be taken to finish the project making the scope bigger.
<!-- ADD IMG -->
<details>
<summary>MVP wireframe</summary>

![MVP wireframe](img-link)
</details>
<!-- ADD IMG -->
<details>
<summary>Mobile wireframe</summary>

![Mobile wireframe](img-link)
</details>
<!-- ADD IMG -->
<details>
<summary>Enhanced wireframe</summary>

![Enhanced wireframe](img-link)
</details>
<!-- ADD IMG -->
<details>
<summary>Superior wireframe</summary>

![Superior wireframe](img-link)
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
<!-- ADD IMAGE -->
<details>
<summary>FBC Timeboxing/Project Flow Image</summary>

![FBC Timeboxing/Project Flow Image](img-link)
</details>

---

Unfortunately medical and other issues prevented full use of all this planning. After a lenghty hiatus from working on the project, the MVP epics/tasks/user stories were placed in BACKLOG Milestone to signify this. Work on the project continued from there. After talking to a mentor, it was decided not to close unfinished epics/tasks/user stories. The explanation was that this is what happens in real-life development too (unfinished things), and FBC Project Board reflects that.

---

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