
# **Hotel Room BOOKING APP**

(CTRL + Click to open links in new window)

The deployed site can be found [here](https://pp4-civ1.herokuapp.com/)

Github repository can be accessed [here](https://github.com/bobshort4bobby4/PP4-Civ1)


![mockup of website](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/mockup-pp4.png)




# **Introduction**

This is the fourth project I have completed as part of the[Code Institute Full Stack Diploma Course](https://codeinstitute.net).  

The project sets out to create a website for a fictitious hotel.  Rooms can be booked and cancelled via the site, as well as extended if availability exsists for that room.  
The room should only be cancelled if the check in date is not more than 7 days away.

The imaginery product owner has also requested that rooms are put on sale if occupancy drops below a set percentage.  
She also requested a review section where customers could leave feedback on their stay at the hotel.
  
# User Experience/User Interface (UX/UI)

<details>  
            
<summary>User Experience/User Interface (UX/UI)</summary>    
  
  
  
   
  
The AGIILE methodology for project development will be used to produce this project, this method involves continual collaboration between all parties and improvements   at every stage. It helps to ensure good quality products are produced within time and financial constraints.
  
   ### User Stories  
  
   #### Casual Visitor Goals
   As a Casual Visitor I want:
  - to be easily able to ascertain information on the hotel and it's locality to aid my purchasing decision.
  - to be able to check availability for my room choice on any particular set of dates to aid my purchasing decision.
  - to navigate easily around the site to avoid frustration whilst using the site and to engender positive emotions towards the business.
  - to have any incorrect input rejected and the error explained clearly and quickly so I do not have any frustrating emotions using the site. 
  - to be able to read reviews about the hotel to determine the quality of the product and aid my purchasing decision.
    
  #### Customer Goals
  As a Customer I want:
  - to be able to easily book a room.
  - to be able to easily cancel a booking if there is more than 7 days to check in to manage my booking.
  - to be able to easily extend my stay if possible to manage my booking .
  - to be easily able to view my booking and account details to make using the site as easy as possible.
  - to be easily able to change account details to make use as easy as possible.
  - to have all actions confirmed to me so as to avoid any confusion or mis-understandings.
  - to be able to leave a review of the hotel to improve my experience using the site/business.  
    
  #### Site Owner/Administrator
  As a Site Owner/Administrator I want:
  - to be able to view and analyse bookings to enable proper planning.
  - to be able to view/change rooms to keep room inventory current.
  - to be able to view customer information to enable efficient communication.
  - to provide a quality website in order to drive sales and increase profits.
  
  #### Epics
  Using the user stories as a frame of reference the following Epics were formulated;
  
  - Epic 01 implement basic html and django structure
  - Epic 02 implement user registration and login
  - Epic 03 implement room booking management system
  - Epic 04 implement customer account management system
  - Epic 05 implement user feedback system
  - Epic 06 optimise the django admin panel to aid hotel management functions.
  
  The user stories were prioritised using the MoSCoW technique and the Kanban Board feature built-in to Github will be used as an information radiator.
  The user stories were broken down into tasks and these were listed under their respective Epic in the initial Kanban Board.  
  Care was taken to ensure should-have proioritised user stories are not greater than 60% of the total.
  
  ##### Table Showing User Story Allocation to Epics    
    
    
    
        
        
      
  
  |                                    User Story                                                                                                |     EPIC     |
  |----------------------------------------------------------------------------------------------------------------------------------------------|--------------|
  | to be easily able to ascertain information on the hotel and it's locality to aid my purchasing decision.                                     |      01      |
  | to be able to check availability for my room choice on any particular set of dates to aid my purchasing decision.                            |      03      |
  | to navigate easily around the site to avoid frustration whilst using the site and to engender positive emotions towards the business.        |      01      |
  | to have any incorrect input rejected and the error explained clearly and quickly so I do not have any frustrating emotions using the site.   |      01      |
  | to be able to read reviews about the hotel to determine the quality of the product and aid my purchasing decision.                           |      05      |
  |                                                                                                                                              |              |
  | to be able to easily book a room.                                                                                                            |      03      |
  | to be able to easily cancel a booking if there is more than 7 days to check in to manage my booking.                                         |      04      |
  | to be able to easily extend my stay if possible to manage my booking .                                                                       |      04      |
  | to be easily able to view my booking and account details to make using the site as easy as possible.                                         |      04      |
  | to be easily able to change account details to make use as easy as possible.                                                                 |      04      |
  | to have all actions confirmed to me so as to avoid any confusion or mis-understandings.                                                      |      01      |
  | to be able to leave a review of the hotel to improve my experience using the site/business.                                                  |      05      |
  |                                                                                                                                              |              |
  | to be able to view and analyse bookings to enable proper planning.                                                                           |      06      |
  | to be able to view/change rooms to keep room inventory current.                                                                              |      06      |
  | to be able to view customer information to enable efficient communication.                                                                   |      06      |
  | to provide a quality website in order to drive sales and increase profits.                                                                   |      01      |
  
  
  
  
  
  
  
  ### Wireframes
  A full set of wireframes was produced, they can be viewed via the link following.
  This document shows three reviews per page on the reviews page, this number was changed to five in the deployed app, as it displayed better.  
  Please note that no wireframe was provided for the staff page as it was  a late addition to the project on advice from my Mentor that there should be some role based   accessability function within the site.  
  (CTRL + click to open on new page)
  [Link to wireframes pdf](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/pp4-ci-wireframesv2.pdf)  
    
  ### Typography
  I choose The Playfair Display Font  as the  main font for the site.   
    
  ![playfair display font example](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/typography/playfairfont-pp4.png)  
  
  The Playfair font did not display well in the various form fields especially at smaller screen sizes so I choose the Koulen font for these elements.  
    
  ![example of the koulen font](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/typography/koulenfont-pp4.png)  
    
  Both fonts were downloaded from [Google fonts](https://fonts.google.com/).  
  
  ### Images
  
  All images used in this site were obtained from the [Pexels Website](https://www.pexels.com/) and are free to use.
   
  ### Colours
  Colours used are shown below. Black was used for some of the form fields as it was clearer.  
    
![](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/colours-pp4.png)
    
  
  
  
  
  
  
  
  
  
</details>

# Data Schema
<details>
  <summary>Data Schema</summary>
  
  ### Database Relations
  
  Roombook App Models
  
  **RoomType**  
  type:charfield  
  description:textfield  
  price:decimalfield  
  image_url: urlfield  
  image:imagefield  
  
  **Room**  
  room_number: integerfield  
  type:foreginKey(roomtype)  
  occupied:boolean  
  
  **Booking**  
  user:foreginkey(AUTH_USER_Model)  
  room_number:foreginkey(Room)  
  check_in:datefield  
  check_out:datefield  
  is_active:boolean    
  
  
  Reviews App Model
  
  **Reviews**  
  user:foreginkey(AUTH_USER_Model)    
  text:textfield  
  created_on:datefield  
  approved:boolean  
  featured:boolean  

[Link to erd pdf](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/erd-pdf-correct.pdf)
![erd](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/pp4-erd-png-correct.png)  
    
    
  ### Django View Types
  I used a mixture of function and Class based views.  
  The Generic views used were 
  - TemplateView
  - DeleteView
  - ListView
  - CreateView  
    
  Two built-in mixins were used also  
  - SuccessMessageMixin
  - LoginRequiredMixin  
  
  The login_required decorator was also used.  
  
  

</details>

# Features
<details>
  <summary>Features</summary>
  
  ### Home Page  
  The major element of the landing page is a display inviting the user to check availability for the various room types the hotel offers.  
  Price and a brief description of the rooms are also displayed.  
  The nav-bar is displayed at the top along with various links.  
  The nav-bar is based on a standard bootstrap one and is fully responsive, collasping to  a  hamburger menu at smaller screen sizes.  
  The nav-bar is part of the base template and is displayed on all pages.  
  When a user logs in the 'log out', 'myaccount' and 'logged in as ...' links are displayed.    
  A carousel of featured reviews is placed on the lower part of the screen.  
    
  ![image of home screen](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/home-pp4.png)
  
    
  ### Information Page
  The information page is accessed from the drop down menu from the nav-bar.  
  It contains a brief paragraph of general information on our imaginery hotel and an embedded google map showing it's supposed location.  
    
  ![image of the information page](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/infopage-pp4.png)
  
  ### Reviews Page
  The Reviews page displays all approved reviews in groups of 5 per page, the page uses django's ListView's built-in pagination feature to handle this.  
  This page is accessed from the drop down menu in the nav-bar.  
  There is a button to enable logged in users to leave a review, any logged out user is shown an alert and redirected to the home page if they try to submit a review.    
  ![image of review page](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/reviewpage-pp4.png)
    
  ### Create Review Page
  A simple page containing a text area for users to input their review, the form validates for content, on submitting the user is alerted with a thank you message and redirected to the home page.  The reviews will not be displayed untill approved via the admin panel or the staff area, only reviews set to featured = true will be displayed on the home page slider.
    
  ![image of the create review page](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/createreviewpage-pp4.png)  
    
  ### Staff Page
  This page is available only to users who are staff.  It is used to approve reviews submitted by customers.  
    
  ![staff page image](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/staffpage-pp4.png)
  
  ### Check Availability Page
  This page contains a short description of the type of room the user chose on the home page and a form to input the desired check-in and check-out dates.  
  The form validates the inputted dates for format and correctness.  
  The 'Check Availability' button directs the user to either the booking procedure if there is a room free or to the home page with an informative message if not.  
    
  ![image of the check availability page](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/checkavail-pp4.png)  
    
  ### Book Page
  The book page displays the details of the booking and a button to confirm the booking.  If the occupancy rate for that period is below 50% a banner is displayed showing a 10% discount on the booking price. Please see note on how this was calculated in testing section.  
  On booking the user is thanked, a confirmation email sent, the details shown again and re-directed to the home page.
    
  ![image of the booking screen](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/bookpage-pp4.png)  
    
  ### MyAccount Page
  
  Available only to logged in users this page lists that customers bookings as well as the option to extend the stay if available, cancel the booking if enough notice(7 days) and an option to change password.  
    
  ![image of the my account page](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/myaccountscreen-pp4.png)  
    
  ### Extend Booking Page
  
  Page used to extend the check-out date for the room if free. It displays the details of the booking and a form field to enter the new desired checkout date.  The form data is validated  and the booking is altered if possible, the user is shown a message, sent an confirmation email and redirected to the myaccount page if data is invalid.  
    
  ![image of extend booking page](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/extendbookingpage-pp4.png)  
    
  ### Cancel Booking Page 
  This page will be used to cancel the booking (details are displayed ) if there is enough notice. If there is not a message is displayed, if there is the booking is deleted from the database and action confirmed to user via an alert and an email. 
    
  ![image of the cancel booking page](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/cancelbookingpage-pp4.png)
    
  ### User Authentification
  All user authentification functions are implemented using the django all-auth package.  The templates are customisied to match the style of website.  
  
  ### Confirmation Emails
  The booking, cancel booking and extend booking function are all confirmed via email to the user's email address.  
     
  ### Footer  
  All pages have a footer which contains working links to the hotel for both telephone and email.  
    
  ### Custom Model Manager
  I added a custom model manager into the bookings model which marks all out of date bookings as in-active.  ie. if a booking's check-out date is in the past, then the booking's 'is_active' field is set to false.  
  
  ### Admin Panel Features
  
  I made some small additions to the admin panel features, these were functions which I imagined would be useful to a hotel manager in a real-life scenario.  
  ##### Occupancy Rate in roomtype 
  I added two columns in the roomtype relation display which show the ocupancy rate for each room type over 14 and 30 days.  
    
  ![image of occupancy rate display in admin panel](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/occupancyrate-pp4.png)  
       
    
 ##### Actions on Review Relation Display  
  I added three actions to the dropdown list on the review relation display. These allow the manager to process reviews in a more efficient manner.  
   
  ![image of dropdown list on reviews display](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/reviewactions-pp4.png)
  
  ##### Custom Filters
  I added several custom filters to some of the relation displays via the admin.py file  
    
  ![image of custom admin panel filters](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/features-readme/customfilters-pp4.png)
  
  
  
  
  
  
  
 </details>
 
 # Technologies Used
<details>
  <summary>Technologies Used</summary>
  
  #### Languages Used
  
  - Python
  - CSS  
  - HTML  
  - CSS  
  
  #### Development Environment
    
  I used the gitpod-full-template for gitpod provided by Code Institute.  
  The app was built using the Django framework.  
  I used the Django setup cheat sheet provided as course material to start and set basic settings for the application.
  
  
  #### Applications Used
  
  - [Balsamiq](https://www.balsamiq.com) was used to create wireframes for this project.
  - [LucidChart](https://www.lucidchart.com) used for the ERD in readme file.
  - [Git](https://git-scm.com/) Git was used for version control.
  - [GitHub](https://github.com/) GitHub is used to store the projects code.
  - [Heroku](http://www.heroku.com/) Heroku.com was used to deploy the site.
  - [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) used for layout and responsive testing.
  - [Wave](https://wave.webaim.org/) used for accessibility testing.
  - [W3 Validator](https://jigsaw.w3.org/css-validator/) used to test css code.
  - [w3 HTML Validator](https://validator.w3.org/) was used for html validation.
  - [pep8online](http://pep8online.com/) pep8online used to validate python code
  - [Windows snip & sketch](https://www.microsoft.com/en-us/p/snip-sketch/9mz95kl8mr0l?activetab=pivot:overviewtab) used to capture screenshots for readme file.
  - [techsini.com](https://techsini.com/) used to create the mock-up used in the readme file.
  - [Freeconvert.com](https://www.freeconvert.com) was used to convert the background image file to the  webp format.  
  - [autoprefixer.github.io](https://autoprefixer.github.io/) used to improve browser compatibility.  
  - [Cloudinary.com](https://cloudinary.com/) used to store media.
  
  #### Django/Python Libaries Used
  I installed the following libraries.  
  
  - Django: The framework used to build the app.
  - Pillow:used to handle image files.
  - Cloudinary: used to serve/store media and css files.
  - Coverage: used in testing to determine how comphrensive testing is.
  - Gunicorn:WSGI application server (Web Server Gateway Interface)used to handle interaction between the web server and the app.
  - Django-allauth: Handles user verification and authorisation.
  - pytz:Library used to make handling timezones easier.
  - psycopg2:Library used to connect to database.
  - dj-database-url: Django utility which allows database URLs to be used to configure the app.
  - backports.zoneinfo; Timezone support.
  - Django-crispy-forms: used to format forms within Django, I did not actually need to use this package.
 
  
  
  </details>
  

  
# Deployment and Version Control
<details>  
            
<summary>Deployment</summary>    
  
  
 ### Version Control
  
  Git is an open source version control system and was used for this project. Github was used to store the repository.   
  Git is run locally whereas Github is cloud based.
  
  ###### Forking
  Forking a Github repository is the process of making a copy of any repository that you can use without affecting the original, this original is known as the 
  "upstream repository".
  The process for forking a repository is set out below.
  1. Go to the Github page that hosts the repository you wish to fork.
  1. On the top-right of the page there is a button "Fork".
  1. Click this button.
  1. This creates a repository in your Github home page which is a copy of the original. You can submit and receive changes to the code by using pull requests 
  and/or syncing with the upstream repository.
    
  (Taken from the Github Docs guide "Forking Projects")
    
###### Cloning 
  Cloning a repository involves making a full copy of that repository on your local machine. This makes working on the code easier.  Changes can be pushed back up to the 
  GitHub site or changes from other sources pulled to your local copy. To make a clone follow the process below.
  1. Goto the repository page on GitHub.
  1. Above the file list click on the green button titled "Code".
  1. You can choose to download a zip file of the repository, unpack it on your local machine and open it in your IDE or,
  1. Clone using HTTPS by copying the URL under the HTTPS tab.
  1. Open a terminal window, set current directory to the one you want to contain the clone.
  1. Type `git clone `and paste the URL copied from the GitHub page.
  1. The repository clone will be created on your machine.
    
  (Taken from the Github Docs guide "Cloning a repository")
  
  ### Deployment
  
  ### Heroku

Heroku is a cloud based platform that allows the user to deploy and manage apps easily. The completed version of this project was deployed using Heroku.   
Heroku is fully managed meaning that all the hardware/server issues are taken care of.
It  previously allowed the linking of github repositories which made deploying easier but following a security issue this is not possible currently.
Projects must now be deployed through the heroku app via the terminal command line.  
  
To deploy my project I followed the steps below.
  
  - Remove the collectstatic variable from heroku settings and set debug to false in settings.py
  - login to Heroku:  
  `heroku login -i`  
  - check the apps name on heroku  
  `heroku apps`  
  - link the gitpod workspace with the app  
  `heroku git:remote -a pp4-civ1`  
  - use git commands to update repository  
  `git add .`  `git commit -m "commit message"`  
  - push to github  
  `git push origin main`  
  - push to heroku  
  `git push heroku main`  
  
  
  This process did not work seamlessly for me, below I list some the problems I encountered whilst trying to deploy the project.
  
  Because I had not created a runtime.txt file in my root, which specifies which  version of python I was using the build failed.
  [link to information on this issue](https://devcenter.heroku.com/articles/python-runtimes)  
  creating the said file with the contents `python-3.8.10 ` fixed this problem.
  
  I then got the H14  heroku error which indicates no web dynos are running, the documentation suggests that using the scale command should fix this  
  `heroku ps:scale web=1`, this did not work in my case and after further investigation I discovered my Procfile was  
  `web:gunicorn hotelapp.wsgi`   when it needed to be `web: gunicorn hotelapp.wsgi` note extra space after colon.  
  
  I had several more issues serving the static and media files due to having incorrect settings in the settings.py file of the django project.  
  
  
 </details>
 
 




# Testing
<details>
  <summary>Testing</summary>
  
 ### Lighthouse
  All pages of the app were tested using the lighthouse function built in to the Google Chrome browser.
  A summary of results is shown as well as links to the indivual results.  
  
  ![summary of lighthouse results](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lightresults-all-pp4.png)  
    
  [link to home page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-home-pp4.png)  
  [link to info page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-info-pp4.png)  
  [link to contact page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-contact-pp4.png)  
  [link to reviews page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-review-pp4.png)  
  [link to check availability page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-checkavail-pp4.png)  
  [link to book page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-book-pp4.png)  
  [link to extend page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-extend-pp4.png)  
  [link to cancel page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-cancel-pp4.png)  
  [link to myaccount page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-myaccount-pp4.png)  
  [link to create review page lighthouse result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-createreview-pp4.png)
  
  The two lowest scores are for the create review and the extend booking pages (89 for accessability ), this concerns the lack of a label on a form field.  
  These two errors have been fixed as shown below.  
    
  ![create review lighthouse result fixed](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-createreview-fixed-pp4.png)  
    
  ![extend page lighthouse result fixed](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/lighthouse-results/lighthouse-extend-fixed-pp4.png)  
    

  
  
  ### WAVE Web Accessibility Evaluation Tool
  The WAVE tool was used to test all, bar one of the apps pages. The 'myaccount' page caused a server error when it's url was submitted to the WAVE website, I do not know the reason for this error but could not replicate it on any other platform.  
  I subquently installed the WAVE Chrome extension and was able to use the WAVE checker via the extension, result included below.
  As before a summary of results is shown as well as links to the individual results.  
    
  ![summary of wave accessability tool results](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-all-pp4.png)  
    
  [link to home page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-home-pp4.png)  
  [link to book page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-book-pp4.png)  
  [link to cancel page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-cancel-pp4.png)  
  [link to check availability page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-checkavail-pp4.png)  
  [link to contact page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-contact-pp4.png)  
  [link to create review page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-createreview-pp4.png)  
  [link to extend bookig page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-extend-pp4.png)  
  [link to info page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-info-pp4.png)  
  [link to reviews page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-reviews-pp4.png)  
  [link to myaccount page WAVE result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wavemyaccount-pp4.png)  
    
  The one error shown is as above, concerning a form field having no visible label, this was fixed as shown below.  
    
  ![](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/wave-results/wave-extend-fixed-pp4.png)
    
  ### CSS Validation  
   I used The W3C CSS Validation Service-Jigsaw to validate the css used in the app.  
  Any errors found were fixed to obtain no errors and 2 warnings as shown below.  
  The warning concerned the importing of fonts from google fonts.
  Please note that a auto-prefixed version of this css file is used in the deployed version.  
  This version also has no errors but 38 warnings extra.  
  All of these extra warnings relate to vendor extensions  
    
  ![css validation results](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/css-html%20-validation-results/cssvalidation-pp4.png)  
  
  
 
  
  
  
 ### HTML VALIDATION  
  Each page of HTML was checked using the W3C HTML validator.  
  All errors were remedied leaving three warning which concerned the aria label for the reviews slider on the home page.  
    
  ![html warning](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/css-html%20-validation-results/htmlwarnings-pp4.png)
 
    
  
  
  
  
 ### Python Validation
  All python code was validated using the PEP8 online validator.  All errors were cleared, a link to screen-grabs of these results is below.  
[Link to PeP8 results for python code](https://docs.google.com/document/d/1seRhPVNkAd9ZI-dmfUxzx1te3_IKNzYoB3pL-h_-G-8/edit?usp=sharing)  

  NB There are a small number of lines that are one or two characters too long (ie. over 79), rather than break these onto several lines I preferred to leave as one line even if it does cause an error in the linter.  
  I had to add the line   
  `objects=models.Manager()`  
  into all models which did not have objects defined to stop the linter showing the "'Model' does not have an 'objects' attribute" wherever the objects model manager was used.
   
  The linter also produced the "unable to import 'django.db'" error in quite a few of the files.  I generated a pyintrc file using  
  `pylint --generate-rcfile > .pylintrc`  
  and added django to the plugin settings therein  
  `load-plugins=django`  
   [credit to https://forum.djangoproject.com/t/unable-to-import-django-dbpylint-import-error/6893/4](https://forum.djangoproject.com/t/unable-to-import-django-dbpylint-import-error/6893/4)   
     
  There are a few variables which do not conform to the snake_case format, in some instances these are one or two character words.
    
 ### Javascript Validation 
  There was a small amount of Javascript used to close messages, this script was passed through the jshint validator. the result is shown below.  
    
  ![jshint result](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/jshint-pp4.png)  
    
  
 ### Testing Application For Achievement of User Goals.  
    
  
   
  
  
   |                          Goal                                                      |                  Outcome                              |
   |------------------------------------------------------------------------------------|-------------------------------------------------------|
   |to be easily able to ascertain information on the hotel.                            |Information Page easily accessible                     |
   |to be able to check availability for my room choice on any particular set of dates. |Function provided on home page                         |
   |to navigate easily around the site.                                                 |Intutitive navigation links provided                   |
   |to have any incorrect input rejected and the error explained clearly.               |All input validated and feedback provided              |
   |to be able to read reviews about the hotel.                                         |Review facility provided                               |
   |to be able to easily book a room.                                                   |Easy booking process provided with neccessary feedback |
   |to be able to easily cancel a booking                                               |Simple process to cancel booking provided              |
   |to be able to easly extend my stay                                                  |Simple process to extend stay if available             |
   |to be easily able to view my booking and account details                            |Dedicated page for customer's account                  |
   |to be easily able to change account details                                         |Ability to change password                             |
   |to have all actions confirmed to me so as to avoid any confusion                    |All information relayed to customer                    |
   |to be able to leave a review of the hotel                                           |Ability to leave a review provided                     |
   |to be able to view and analyse bookings                                             |Possible through admin panel                           |
   |to be able to view/change rooms                                                     |Possible through admin panel                           |
   |to be able to view customer information                                             |Possible through admin panel                           |
   |to provide a quality website                                                        |to be determined                                       |
   
   
  
   
  ### Responsive Testing
  
  The website was tested for responsiveness using the built-in tool in the Google Chrome browser. As I worked through each breakpoint I fixed any display issues I encountered.  
  A set of images of the homepage at each breakpoint is shown.  
  There is a link provided which shows the results of each other page in a spreadsheet.  
    
  ![homepage at 320px](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/responsive-images/home-320px-pp4.png)  
  HomePage at 320px.  
    
  ![homepage at 375px](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/responsive-images/home-375px-pp4.png)  
  HomePage at 375px.  
    
  ![homepage at 425px](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/responsive-images/home-425px-pp4.png)  
   HomePage at 425px.  
    
  ![homepage at 768px](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/responsive-images/home-768px-pp4.png)  
  HomePage at 768px.  
    
  ![homepag at 1024px](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/responsive-images/home-1024px-pp4.png)  
  HomePage at 1024px.  
    
  ![homepage at 1440px](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/responsive-images/home-1440px-pp4.png)  
  HomePage at 1440px.  
    
  ![homepage at 2000px](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/media/responsive-images/home-2000px-pp4.png)  
  HomePage at 2000px.
  
  
    
  [Link to responsive testing](https://docs.google.com/spreadsheets/d/1LyncF4JuYmWrfmwA610n0NtrX4EGbiZRYUCYySV0JWY/edit?usp=sharing)  
    
  
  ### Automated Tesing
  
  I wrote tests using the unit test functionality built into django. The coverage rate of these tests for the entire app was 85%.  
  The coverage for the individual apps is listed below.  
  - Home APP 99% 
  - MyAccount APP 73%  
  - Reviews APP 96%  
  - Roombook APP 84%  
  
  [These results are shared at this link](https://docs.google.com/spreadsheets/d/1RWi0MxZxObRYifLkKv-LtTtAoNW04lpUWkk4_LFDsOM/edit?usp=sharing)  
  I felt that this testing did not cover many of the aspects/functionality that would be neccessary so also tested manually.  
    
  ### Manual Testing of User Input and Functions  
  I systematically tested all user inputs and functionality in the website to compare feedback/results against expected results.  
  Any unexpected output/outcomes were fixed.  
  [The results of this testing can be found here](https://docs.google.com/spreadsheets/d/1OmOLO1755Cwm_MdL_q3j_q5kEfDmpSuUcT__er4jC2Y/edit?usp=sharing)  
    
  ### Known Issues, Solved Bugs and Unfixed Bugs
  
  ##### Method of calculating Flash sale
  The method I used to determine whether the room should be put on sale (occupancy_rate.py in the booking_code folder) whilst not incorrect is perhaps not the best method. In hindsight I should have used a method such as the one used to calculate the occupancy rate in the admin panel for each room type (roombook/admin.py).  
    
  The latter method uses each specific room type to calculate the percentage of nights booked over a set period whereas the former uses all rooms and simply checks if the check-in date of the new booking falls with the range of all current bookings.  
  It would not, I'd imagine be too difficult a task to change the occupancy_rate function in the future if required.
  
  ##### User Extending a Booking into Another Booking of Theirs in the same Room.  
  If a customer attempts to extend a booking in a specific room overlapping the time period of another booking of theirs in the same room the program will not allow it.  
  
  For example if a customer has a booking for room 3 from  1/1/2022 to 7/1/2022 and another for the same room from 10/01/2022 to 17/01/2022,  if they try to extend the first booking to 9/01/2022 (ie bridging the gap between the bookings) the app will allow it,  provided the room 3 is free.  
  If however the customer overlaps the second booking, an error will be shown and the extension to the booking refused. From an UE viewpoint it would be preferable to flag to the customer that they had already booked that room for some of the chosen extension period.  
  
  ##### Unit Testing
  Although the coverage percentage is 85%, I feel that there were many aspects of the program I didn't manage to write tests for.  
  These aspects were adequately tested in manual testing, I believe.
  
  ##### Git Push Sizes
  My CI Mentor has pointed out that some of the earlier git commits are too large.  This is because I had written and tested some parts of the functionality/logic and tests in different coding environments, consequently I was able to commit larger batches of tested code to the repository.  
  
  ##### Time Incorrect
  The time used in the app is one hour behind local time.  If i set the Timezone setting to 'Europe/Dublin' it displays the correct local time in the templates and on the admin panel.  The Django documentation suggests that UTC is a better option for this setting.  I also tried the template tag `localtime on` and also using the TIME_ZONE context processor, I haven't found a fix for this error at this time.
  
  ##### Incorrect Default setting used in Review Model.
  I used the default value of `auto_now` for the `created_on ` field in the Review model, `auto_now_add` would have been a better choice. In this case I don't think it matters as the reviews are not editable, I was reluctant to change the model as I feared it may affect currently written records.  
  
  ##### 'Approved by' field in Reviews Model
  There should be an "Approved By" field in the reviews model to record which member of staff approved that particular review.  It would be automatically set at review time to the currently loggged in user.  
  
  
  ##### Unauthorised Viewing of Booking Details.
   Late in the developement process I noticed that a logged in user could view (but not change) another user's booking details by entering a random value into the extend booking and cancel booking URLs.  I put an id check into the get method of both views and this solved the issue, I left the previous checks in the code as an additional safeguard.  
  
  ##### Email Address
  Rather than create a email address for the project I elected to use a personal email, similarly I used the default site address created by django.  
  
  ##### Confirmation Email Url not Clickable on Mobile Devices
  On some mobile devices using certain email services the confirmation email URL used to confirm email address during the registration process was not clickable, but had to be copied and pasted into the address bar to work.  
  After an internet search I added the below settings to settings.py which has resolved the issue.  
    
   `ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False`    
   `ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL`    
   `ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL`    
  
  
  
  </details>
  
  
  # Credits
  <details>
  <summary>Credits</summary>
  
  - Bootstrap I used standard bootstrap templates for several of the elements on the site, these were adapted to suit as needed. The Nav-bar, Review-Slider and the table on the My Account page are all taken from the [Bootstrap site](https://getbootstrap.com/).  
  - The Css used to format the embedded google map on the information page was taken from this blog[blog.duda](https://blog.duda.co/responsive-google-maps-for-your-website). 
  - Information on making custom model managers was found [here](https://www.youtube.com/watch?v=YGwSNkdwAEs). 
  - Stackoverflow for general information [](https://stackoverflow.com/).  
  - Javascript script used to close the Django messages was taken from one of the course material examples.
  - Course Materials.    
  - I used several sources as I was researching a good way to implement the room booking function and site layout.  I studied several systems and wrote my own version using methods from these sources. Some of the main sources are listed  
    1. https://www.geeksforgeeks.org/find-k-bookings-possible-given-arrival-departure-times/  
    2. https://www.youtube.com/watch?v=yenjz1Wv9Yo&t=1s
    3. https://www.youtube.com/watch?v=8Yv6eQSGK0w 
    4. https://www.youtube.com/watch?v=5bSd2uI5gWg&t=40s
  - My CI Mentor Mr Ben Kavanagh.  
  
  </details>




















