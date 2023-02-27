
# Django Blog App

This is a simple blog application built using Django. It allows superusers to create, read, update and delete blog posts, and allows normal users to view upcoming events, pictures and comment. The application also integrates with Cloudinary for image uploads.

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/am%20i%20responsive.png?raw=true)

# User experience

### New User Stories
- As a new user, I want to be able to easily navigate the website and find relevant information on different travel events and experiences in and around Birmingham UK.
- I want to be able to access infomration that can be read in a short amount of time, such as 5 minutes or less.
- As someone planning a trip, I want to be able to find events to plan on a budget.
- I want to be able to leave comments on events posted.

### Returning User Stories
- As a returning user, I want to be able to quickly access the features I’m interested in, such as browsing new events or searching for specific activities.
- As a returning user, I want to be able to access premium content such as travel guides and recommendations, to enhance my travel experiences.
- I want to be able to create an account and log into my created account. 
- I want to be able to play a quiz on the website.

# Features
- The home page serves as the main hub for all other pages. It includes the header and footer of the website, and contains the links to the CSS and JavaScript files used throughout the website and navigation links. Users can create an account and/or log in. It displays a hero image with a call-to-action button to encourage users to explore the website further. It also includes a section for featured events.

- clicking on any of the events at the bottom of the page displays the upcoming events, including the date, time, location, and a brief description. Users can comment here if they're logged in, otherwise they can only read comments by other logged in users.

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20event%20info.png?raw=true)


- The quiz page includes an interactive quiz game that tests the user's knowledge of travel destinations. Users can select their answer from multiple choices and receive immediate feedback on whether they answered correctly or not with a score.

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20game.png?raw=true)


- The gallery page displays a collection of photos from various travel destinations and past events.

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20gallery.png?raw=true)


- The registration form can be accessed by clicking on the "Register" button on the navigation bar. The user will be prompted to enter their username, email address (optional), and password.

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20signup%20better.png?raw=true)


    Once registered, the user can login in. After logging in, the user can log out by clicking on their profile name on the navigation bar. 

- The user can also leave comments on an event by filling out the comment form at the bottom of the event details page. These comments will be displayed on the event details page, but will need to be approved or rejected by an admin user first.

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/comment%20awaiting%20approval.png?raw=true)


- Admin users have additional permissions, such as editing and deleting events, approving comments, and viewing user attendance lists. Admin users can be created in the Django admin interface by setting the "is_staff" and "is_superuser" flags to True for a user account.

- The Footer
The footer section includes links to the social media sites and the links will open to a new tab to allow easy navigation.

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20Footer.png?raw=true)


# Testing
- Functionality testing:
I used Microsoft Edge's developer tools for testing, problem solving problems issues and different screen sizes(inc mobile devices) 
- To ensure the project adheres to web standards, I 
have validated the CSS using the W3C CSS Validator. The following badge indicates that our CSS is valid:
- <p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

- Lighthouse in developer settings:

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Lighthouse%20Desktop.png?raw=true)


# Design

- The design of the travel blog was carefully crafted to provide an enjoyable user experience. The site uses HTML, CSS, JavaScript, and Python to provide a seamless experience to the user.

### Colours and Shades:

- The site features a simple colour palette to create a clean and professional look. The background colour and the text colours contrasts making the content easy to read. The navigation bar and footer use a light shade of grey, and buttons use a shade of white to create a visual hierarchy.

### Typography
- The site uses Google Fonts to create a unique typography experience. The logo uses the "Montserrat" font, while all other text on the site uses the standard Bootstrap framework font stack, which consists of a number of simple, legible sans-serif fonts targeted at a range of different viewing devices and operating systems.

### Imagery
- The homepage features a beautiful landscape image of Birmingham to set the tone for the site. The pre-written events feature thumbnails with images that are relevant to the pages topic as the user scrolls down the page.

### Icons
- Font Awesome icons are used throughout the site to enhance the user interface and create a consistent visual experience. 

Overall, the design of the travel blog provides a professional, user-friendly experience that encourages users to engage with the content and explore the site.



# Django admin panel

-  ![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20Django%20admin.png?raw=true)

- Managing User Accounts: The admin panel allows the super user (SU) to create, modify, and delete user accounts:

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20Django%20admin%20users.png?raw=true)


- managing user comments: approve, edit or delete:

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20Django%20admin%20comments.png?raw=true)


- Managing events: SU can add, modify, and delete content on the website using the admin panel. This includes event, location images, , and other media.

![Responsive Image](https://github.com/passportpowell/django-project-4/blob/main/media/Readme%20Images/Am%20I%20Django%20admin%20events.png?raw=true)


- Managing Site Settings: SU can manage various site settings such as site name, URL, and other important details.

- Managing Permissions: SU can manage permissions for different users and user groups. This allows you to restrict access to certain parts of the admin panel or website and upgrade users to admin staff.


# Future Features
Here are some potential features that could be added to the site in the future:

- User authentication and profiles: Currently, there is no user authentication or profile system. In the future, users could create accounts and have personalized experiences, such as marking themselves as attending certain events.

- Search functionality: The site currently only displays the most recent events on the home page. Adding search functionality would allow users to easily find events based on keywords, dates or categories.

- sign up using social media.

- User-generated content: so that users can participate in community discussions.

- Social media integration: Adding social media integration would allow users to easily share posts on their social media accounts and increase the site's visibility.

- Multi-language support: Adding multi-language support would allow the site to reach a wider audience and provide content in different languages for users who prefer to read articles in languages other than English.

- Newsletter Subscription - Allow users to subscribe to a newsletter that features latest event and updates.

- Interactive Maps - Create interactive maps with points of interest or travel routes that users can click on to access articles and information.

- Video Content - Add video content to the blog to showcase destinations, events and travel experiences.

# Technology
### Languages Used

- Python 3.8
- Django 3.2.5
- HTML
- CSS
- JavaScript

### Frameworks, Libraries & Programs Used
- Bootstrap
- Font Awesome 6
- jQuery
- Django
- Pillow
- PostgreSQL
- Gunicorn
- Heroku
- Cloudinary
- ElephantSQL


# Website development Issues 

<br>

- Issue: href to take a user from any page (except home page) to the home page events section. it works only on the home page but not from any other.

  - Solution: Tried many different potential "solutions" but nothing worked so i left it in the end

<br>

- Issue: collapsing navbar wasn't workig correctly and in the end couldnt get it to collapse after exanding.

  - Solution: Eventually got it to expand by deleteing the whole nav bar section and coding it out again. used a video from the youtube channel "thenewboston" but as the video was 6 years old, i could only get the navbar to expand when clicked but would not collapse if clicked again.

<br>

- Issue: game.html file wasn't loading my script.js adn was receiving server eroor 500 after i had debug off.

  - Solution: Realised that i was putting the script.js file in assets/js instead of my static folder. once i changed it and corrected the path in my src it work.

<br>

- Issue: html files weren't loading my style.css files

  - Solution: Realised that i was putting the style.css file in assets/css instead of my static/css folder. once i changed it and corrected the path in my src it work.

<br>

- Issue: When trying to load the event details it wasn't loading

  - Solution: I was using the wrong model names completely. i was using blog."" instead of event."".

<br>

- Issue: Couldn't get the attending count to show , allow user to click attending and incremement.

  - Solution: Tried a few different ways but in the end decided not to use it. Left it in the project to try again in the future to get it to work

<br>

- Issue: Consisitent issue of updating view.py, models.py, urls.py and forgetting to "makemigrations" and "migrate" this caused many issues with pages not loading.

  - Solution: Used slack code institute channel and "greg" has a look through my code and asked if i had migrated..... I then made the migrations

<br>

- Issue: kept receveing error (AttributeError at /admin/blog/usercomment/add/'str' object has no attribute 'username'), when trying to post a UserComment: 
  - solution: checking through the code i saw that i needed to change the user field to a foreign key in the User model

<br>

- Issue: was receiveing TypeError at /event-test-this-is-the-slug/ call() missing 1 required keyword-only argument: 'manager'

  - Solution: change the method of likes_count to def likes_count(self, *, manager): found that solution on the first page of google.

<br>

- Issue: AttributeError at /event-test-this-is-the-slug/ c'ManyToManyDescriptor' object has no attribute 'filter'

  - Solution: changed code "if Event.likes.filter(id=self.request.user.id).exists():" by making the capital "E" from Event into a lower case "e". 

<br>

- issue: An email from gitguardian informed me that my django secret key had been exposed within git hub

  - solution: Added the sqlite database to .gitignore 

<br>

# Installation and Deployment
- Clone the repository
 
- Create a virtual environment and activate it

      python3 -m venv venv


- Install the dependencies

      pip install -r requirements.txt

- Create a new PostgreSQL database on ElephantSQL and copy the URL

- Create a cloudinary account

- Create a .env file in the root directory and add the environment variables: and fill the "" with your info

        import os

        os.environ["DATABASE_URL"] = ""
        os.environ["SECRET_KEY"] = ""
        os.environ["CLOUDINARY_URL"] = ""

- add the following to the settings.py file:

        import os

        import dj_database_url
        if os.path.isfile("env.py"):
            import env

- create a heroku account and a new app.
    
    add 4 configs

        PORT 8000
        DATABASE URL (from elephantSQL)
        SECRET KEY (your secret key)
        CLOUDINARY_URL (from cloudinary website)

- add 'cloudinary' to settings.py install_apps section


- Be sure to add to your settings.py

        ALLOWED_HOSTS = ["YOUR_PROJECT_NAME_IN_HEROKU.herokuapp.com", "localhost"]

- also these to settings.py templates section

        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,

- create a new file named "Procfile" in the root folder

- Deploy the static files to Cloudinary, follow the steps in the Cloudinary documentation, making sure to set the appropriate environment variables.

- Make migrations and migrate the database:

        python manage.py makemigrations
        python manage.py migrate

- In heroku go to deploy tab scroll down to connect app to github and then at the bottom of the same page deploy branch.

- Commit and push your changes to your Git repository.

- Run the server:

        python manage.py runserver




