
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

[Link to erd pdf](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/erd-pdf-correct.pdf)
![erd](https://github.com/bobshort4bobby4/PP4-Civ1/blob/main/pp4-erd-png-correct.png)































![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome bobshort4bobby4,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
