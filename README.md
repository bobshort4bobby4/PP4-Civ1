
# **Hotel Room BOOKING APP**

(CTRL + Click to open links in new window)

The deployed site can be found [here](https://pp4.herokuapp.com/)

Github repository can be accessed [here](https://github.com/bobshort4bobby4/PP4-Civ1


MOCKUP TOGO HERE




# **Introduction**

This is the fourth project I have completed as part of the[Code Institute Full Stack Diploma Course](https://codeinstitute.net).  

The project sets out to create a website for a fictitious hotel.  Rooms can be booked and cancelled via the site, as well as extended if availability exsists for that room,  if the  current room is booked  another room of the same type will be suggested if available.  
The room should only be cancelled if the check in date is not more than 7 days away.

The imaginery product owner has also requested that rooms are put on sale if occupancy drops below a set percentage.  
She also requested a review section where customers could leave feedback on their stay at the hotel.
  
# User Experience/User Interface (UX/UI)

<details>  
            
<summary>User Experience/User Interface (UX/UI)</summary>    
  
  
  
   
  
The AGIILE methodology for project development will be used to produce this project, this method involves continual collaboration between all parties and improvments   at every stage. It helps to ensure good quality products are produced within time and financial constraints.
  
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
  - to be able to easly extend my stay if possible to manage my booking .
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
  
  - implement basic html and django structure
  - implement user registration and login
  - implement home pages
  - implement room booking management system
  - implement user feedback system
  - optimise the django admin panel to aid hotel management functions.
  
  The user stories were prioritised using the MoSCoW technique and the Kanban Board feature built-in to Github will be used as an information radiator.
  The user stories were broken down into tasks and these were listed under their respective Epic in the initial Kanban Board/
  Care was taken to ensure should-have proioritised user stories are not greater than 60% of the total.
  
  ### Wireframes
  A full set of wireframes was produced, they can be viewed via the link following.
  (CTRL + click to open on new page)
  [Link to wireframes pdf](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/pp4-ci-wireframesv2.pdf)  
    
    ##### Typography
  I choose '' as the font for the site. It is a big bold type that stands out from the background well and is easy to read.
    
  
  
  

  
  
  
  
  
  
  
  
  
</details>


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
  booked:boolean  
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
  
  
  This process did not work seamlessly for me, below I list some the problems I encountered whilst trying to deployment the project.
  
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
  All pages of the app were tested using the lighthouse function built in to the google chrome browser.
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
  This will be fixed for the submitted version.  
  
  
  ### WAVE Web Accessibility Evaluation Tool
  The WAVE tool was used to test all, bar one of the apps pages. The 'myaccount' page caused a server error when it's url was submitted to the WAVE website, I do not know the reason for this error but could not replicate it on any other platform.  
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
    
  The one error shown is as above, concerning a form field having no visible label, I plan to fix this before submitting.
  
  
  
</details>




















