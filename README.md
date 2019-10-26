# Bakebook
Bakebook is a recipe sharing site designed to allow users to contribute baking recipes with the community.

It can be viewed [here]("https://bake-book-milestone.herokuapp.com/).

New bakers can search through the content to gain inspiration and try new recipes whilst more experienced can submit recipes for users to try.
Users can view all recipes without logging in or signing up.

From the home page, any user can search for relevant recipes using the search bar at the top which looks in the title and sub-title of recipes for the keywords.
On signing up, then logging in, users have the additional functionalities of saving any recipe and submitting, editing and deleting their own recipes. 

## UX
### Goals
The goal of this site is to create a collaborative baking community where bakers can try others and share their own recipes. As a recipe owner my goal is to create this community and benefit from members submitting their recipes which I can then try in my own kitchen.
As a member using the site, my goal is to find new recipes and share my own recipes so I can get feedback on them.
Ultimately this website is for baking lovers, keen bakers who want to find more recipes and share their own.

### User Stories
I used the below user stories to help plan my features:

- As a baker, I want to be able to search for recipes using keywords, so that I can find the recipes most relevant to me.
- As a user I want to be able to browse through recipes quickly and have key information easily displayed so I can choose a recipe to make.
- As a baker, I want to share my recipes, so that other people can use them.
- As a baker, I want to be able to edit or delete my own recipes, so that they can be updated as I keep perfecting them.
- As a frequent baker, I want to be able to save and unsave my favourite recipes so that I can easily find them again later. 
- As a user I want to be able to contact the owner of the site in case of any questions.
- As a frequent user of the site I want to be able to track my saved recipes, recipes I have submitted and have these associated to my account.
- As a user I want to be able to view recipes in the same standard format with an easy to follow layout.

I also created some basic wireframes, which I used as the starting point for my designs. I wanted the recipe cards to have a picture to draw the eye and provide some contrast and for users to be able to scroll through if they just wanted to browse.

## Layout
I wanted to keep the layout consistent and intuitive.

The design concept changed a little as I built and used the website and some functionalities shown in the wireframes (such as ratings) have not yet been implemented the overall design is simple.

### The wireframes:
The initial wireframes can be viewed [here](https://github.com/kmaaallen/bake_book/tree/master/static/images/wireframes).

### Design decisions
#### Font

- I wanted to keep the design of the site fairly simple so that users would be drawn to the recipe images as the main focal point.
- As such I chose a neutral font (Roboto) as the main font and a cursive font for the Bakebook logo to differentiate it form the main site text (Courgette) both of which are available from google fonts (https://fonts.google.com)

#### Colours

- I also wanted to use web-safe colours where possible to keep the user experience consistent between browsers.
- Using color-hex.com/216-web-safe-colors/ I chose a web safe colour as my base. Dark green, #003333. I then used sessions,edu/color-calculator/ to generate a complimentary colour (a lighter green), #219E66. 
- Using https://www.colortools.net/color_make_web-safe.html I converted this green into a web safe colour, #339966.
- The rest of the palette is made up of two web safe greys and white.
- To check that the colours had good contrast I used https://webaim.org/resources/contrastchecker/ to check which colours would work best together according to WCAG AA and WCAG AAA.

## Features
### Existing Features
#### Common features (across all pages)

##### Top Navbar (Desktop)
- This site is responsive and as such has two navigation bars. The desktop navigation will display on screen sizes of 993px or wider.
- It always contains the ‘BakeBook’ logo in the top left corner which is a link back to the homepage when clicked.
- Grouped to the right of the navigation bar (to make viewing easier) are several links that will depend on whether the user is logged in or not.
- If the user is NOT logged in, there will be three links to the right.
    - ‘Home’ will return the user to the homepage
    - ‘About’ will take the user to the About page
    - ‘Login/Signup’ will take the user to the Login page

- If the user IS logged in there will be four links to the right.
    - ‘Home’ will return the user to the homepage
    - ‘About’ will take the user to the About page
    - ‘Submit a recipe’ will take the user to the Submit a Recipe page. This link is included in the main navigation as it is a key feature of the site and one users would commonly used.
    - ‘Username’. This is a dropdown (denoted by the small, downward pointing arrow) and is dynamic. It will display the logged in user’s username. The dropdown menu links are grouped together as actions that are associated with the user’s profile. On clicking the dropdown menu will appear with the following items:

- 'My Recipes’ which takes the user to the My Recipes page.
- ‘My Saved Recipes’ which takes the user to the My Saved Recipes site.
- ‘Logout’ which ends the user session and redirected the now logged out user to the homepage.

##### Mobile Navbar (Mobile)

- The mobile navbar will display on screens 992px wide or narrower.
- It always contains the ‘BakeBook’ logo in the top left corner which is a link back to the homepage when clicked. This is consistent with the desktop navigation bar.
- In this nav all links are collapsed under a single burger menu icon to the right of the navbar.
- I chose the burger icon because it is widely used to denote a drop-down menu and is therefore intuitive for the user.
- If the user is NOT logged in, on click the burger menu drop-down will contain the following links:
    - ‘Home’ will take the user to the homepage
    - ‘About’ will take the user to the About page
    - ‘Login/Signup’ will take the user to the Login page
- If the user IS logged in, on click the burger menu drop-down will contain the following links:
    - ‘Home’ will return the user to the homepage
    -‘About’ will take the user to the About page
    - ‘Submit a Recipe’ will take the user to the Submit a Recipe page
    - ‘My Recipes’ will take the user to the My Recipes page
    - ‘My Saved Recipes’ will take the user to the My Saved Recipes page
    - Logout will end the user session and take the now logged out user to the homepage.

All links in the navigation bars change colour from white to dark green (as per colour scheme) when hovered over. This is for consistent styling and so the user can clearly see what they are hovering over whilst remaining subtle enough so as not to distract from the rest of the site.

##### Homepage

- Search Bar
    - Allows users to search through recipes based on keywords they input. This searches for those keywords in the title and sub-title of the recipes in the database and displays the filtered results. This functionality is available for all users whether logged in or not.
    - Users can enter a word or phrase, each word in a phrase will be searched for individually. For example, if a user searched for “Christmas Pie”, they would receive results that had either “Christmas” or “Pie” or both in the title or sub-title.
    - Users can initiate the search after typing in the word either by hitting enter on their keyboard or clicking the search button to the right of the search bar.
    - The icon on the search button is a magnifying glass to align with common convention for searches and is an intuitive choice. It is a standout colour so the user can easily find it.
    - If the user enters no words into the search bar and hits the search button OR if a user enters keywords but there are no matches a ‘Sorry that search returned no results’ alert message appears at the top of the screen.

- Recipe cards
    - Each recipe is displayed in a common format in the form of cards. 
    - The cards have an image at the top which is formatted to be the same size, with no overlap and without any image skewing.
    - Underneath, in large text is the recipe title and slightly smaller text the recipe sub-title for easy viewing.
    - Users can quickly assess the image, title and sub-title when scrolling through the recipes.
    - At the bottom of each recipe card is a ‘View Recipe’ button that is in a stand out colour according to the colour scheme and is easy to read. This clearly directs the user to click if they want more detail on the recipe.

- About Page
    - Jumbotron header image to visually break up the page
    
- Contact details
    - For the purposes of this project I have created an email address. When a user clicks on the email address link it will open their default email programme with the ‘to’ field already filled out to the site’s address ‘bakebooksite@gmail.com’. When a user composes and sends an email to this account it will be received at the site account.

- Full recipe view (presented when a user clicks on a ‘View Recipe’ button anywhere within the site)
    - Recipe image on left of screen at larger screen sizes and at top of screen at smaller screen sizes.
    - The recipe image is displayed again in a card format for consistency but is styled to take up half of the screen width and will no border to give it a better look. This is responsive and will become narrower (without becoming skewed/squashed) when the screen is made smaller.
    - Underneath the recipe image is a caption showing the recipe creator’s username.
    - At smaller screen sizes the recipe image displays at the top of the screen so as to be eye catching and draw the user in to the recipe below.
    - Save Button

- The save button will only display if the user is logged in.
- It is a contrasting dark green (from the colour scheme) for prominence and is as wide as the recipe card again for prominence. This will always be underneath the recipe credit (created by).
- When a user saves a recipe a message will pop up at the top of the screen saying ‘Recipe has been saved’.
- If the user has already saved this recipe a message will flash up on the screen saying ‘You have already saved this recipe’.

- Edit button
    - The edit button is styled to match the save button and is only visible if a user is logged in and the recipe they are viewing has been created by the logged in user.

- Recipe details are displayed on the right of the screen on larger screens or underneath the above features on smaller screens.
- The title and subtitle are large and prominent whereas ‘makes’ and ‘takes’ are smaller fonts as they are less important details for the recipe.
- The ingredients and method labels are underlined as these sections are key elements and are most likely to be looked at first when viewing the recipe.
- Ingredients are bullet pointed for easy reading and method steps are numbered for ease of execution.

##### My Recipes
- The My Recipes page displays recipe cards as described under homepage features. However, these cards contain two extra buttons, described below.
    - Edit Recipe – this takes the user to the edit recipe page where they can edit the selected recipe by updating the fields in the form. These fields are pre-populated with the selected recipes details.
    - Delete Recipe – this deletes the recipe from the site and redirects the user back to the My Recipes page.
- The recipe cards displayed on this page are only the recipes the logged in user has created themselves.
- If the user has not created any recipes they see a message "You haven't submitted any recipes yet! Click on Submit a Recipe to get started." Where ‘Submit a Recipe’ is a link to the Submit a recipe page.

##### My Saved Recipes
- If the user has not saved any recipes yet they see a message “You haven't saved any recipes yet. Browse the collection here.” Where ‘here’ is a link to the homepage.
- If the user has saved recipes those recipes are displayed in the same format as on the homepage.
- On each recipe card the user also has the option to ‘unsave’ the recipe using the unsave button. Clicking this refreshes the page and the unsaved recipe is removed.

##### Login page
- I created a login form with a basic username and password functionality.
- In order for a user to login they have to have a valid username / password combination stored in the database.
- If a user enters an incorrect combination of username and password they are shown an error message to that effect.
- Password entry is hidden and both fields are case sensitive.
- The login page also gives the user the option to sign up if they have not yet already.

##### Sign up page
- When a user signs up they are prompted to enter a username and password combination.
- On submitting this combination there is first a check in the database to see if that username already exists. If it does the user is prompted to choose another username.
- Passwords are stored as encrypted strings using bcrypt in the database.
- After successfully signing up, users are re-directed to the login page to complete login. Upon successfully logging in, users are redirected to the homepage and their username appears in the top right corner of the nav bar.


##### Submit a recipe / Edit a recipe
- This view displays a form that allows a user to enter or edit details for a recipe they want to submit or have already submitted to the site.
- A user has to be logged in to view this form.
- The form fields are all mandatory except for the recipe url input.
- Key features include:
    - Required data input
    - Ability to add and remove additional ingredient and method fields using plus and delete buttons
    - Dynamic recipe image preview (defaults to default image when recipe url is invalid or empty)
- If on edit recipe view form data is pre-populated from selected recipe object.

##### My Recipes
- When logged in, the user can view all of the recipes they have submitted on this view.
- Key features include:
    - Ability to view, edit or delete their recipes.
    - The delete button is in a contrasting colour to prevent users clicking it by mistake.

##### Features Left to Implement
- Ideally I would like to implement a comment section in the full recipe view. This would allow logged in users to leave a comment on the recipe which provides valuable feedback to the user who submitted the recipe as well as information for other members using the recipe.
- In tandem with this I would like to add a rating system so that users can see the average rating out of five stars beneath the recipe.
- Currently the user can only submit an image url to add an image to their recipe. I would like to implement a better file upload and image storage system to allow greater flexibility for the user however I felt I did not have these skills whilst working on this project.


## Technologies Used
### Cloud9 on AWS
This project was written on Cloud9 via the AWS site:[https://aws.amazon.com/](https://aws.amazon.com/)

### Heroku
This project was deployed using Heroku : [https://id.heroku.com/login](https://id.heroku.com/login">https://id.heroku.com/login)

### Languages
#### Python
Used to write backend functionality in flask application: [https://www.python.org/](https://www.python.org/)

#### JavaScript
Used as a base language to provide functionality and logic :[https://www.w3schools.com/js/default.asp](https://www.w3schools.com/js/default.asp)

#### JQuery
This project uses JQuery to assist in execution of javaScript features:[https://jquery.com/](https://jquery.com/)

#### HTML
Used as a baseline to structure pages:[https://www.w3.org/TR/html/](https://www.w3.org/TR/html/)


#### CSS
Used to style pages:[https://www.w3.org/Style/CSS/Overview.en.html](https://www.w3.org/Style/CSS/Overview.en.html)


#### Jijna
Used as a templating language with Python to render HTML on site:[https://palletsprojects.com/p/jinja/](https://palletsprojects.com/p/jinja/)

### Validators
Online validators were used to check code was valid for HTML and CSS and to help catch errors in Javascript and Python.
- HTML validator:[https://validator.w3.org](https://validator.w3.org">https://validator.w3.org)
- CSS Validator:[http://jigsaw.w3.org/css-validator/](http://jigsaw.w3.org/css-validator/)
- JavaScript correction tool:[https://jshint.com/](https://jshint.com/)
- Python validator:[http://pep8online.com/checkresult](http://pep8online.com/checkresult)

### Libraries
#### Bootstrap
Used to build a responsive site:[https://getbootstrap.com/](https://getbootstrap.com/)

#### Bcrypt
Used to encrypt passwords stored in the database:[https://www.npmjs.com/package/bcrypt](https://www.npmjs.com/package/bcrypt)

#### PyMongo
Library used to work with MongoDB from Python:[https://api.mongodb.com/python/current/](https://api.mongodb.com/python/current/)

#### WTForms
Library used to create, render and validate forms with Python:[https://wtforms.readthedocs.io/en/stable/](https://wtforms.readthedocs.io/en/stable/)
	
#### Google Fonts
Main theme font "Roboto" and the logo font “Courgette” were imported from Google fonts:[https://fonts.google.com/](https://fonts.google.com/)

### Frameworks
#### Flask
Web framework used to construct and render pages:[https://flask.palletsprojects.com/en/1.1.x/](https://flask.palletsprojects.com/en/1.1.x/)

#### Jasmine
Framework used to automate tests of JavaScript:[https://jasmine.github.io/](https://jasmine.github.io/)

#### Python Unittest
Framework was used to automate Python tests:[https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)

### Version control
Git was used for version control and a local git repository was pushed to a remote repository on GitHub:

[https://git-scm.com/](https://git-scm.com/)

[https://github.com/](https://github.com/)

### Tools
An online favicon generator was used to create a favicon for my site.The favicon image can be viewed [here](https://github.com/kmaaallen/bake_book/blob/master/static/favicon.ico).

The online generator tool is available at: [https://www.favicongenerator.com/](https://www.favicongenerator.com/)

### Database
MongoDB Atlas was used as the database for this project :[https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)

## Testing
For this project I opted to carry out detailed and thorough manual testing as the baseline. My reasoning behind this was that the success of this website would depend on a good user experience to keep users coming back. By documenting and carrying out extensive manual testing I can more easily replicate the user experience.    

Please see full manual test script and connectivity test outline here : [Manual Testing Documentation](https://github.com/kmaaallen/bake_book/tree/master/Testing/manualTesting)

### Automated testing
I used Jasmine to carry out automated testing on my Javascript functions.

HTML index page to run tests from can be viewed here:[https://github.com/kmaaallen/bake_book/blob/master/Testing/jasmine/index.html](https://github.com/kmaaallen/bake_book/blob/master/Testing/jasmine/index.html)

The test specifications can be viewed here:[https://github.com/kmaaallen/bake_book/tree/master/Testing/jasmine/spec](https://github.com/kmaaallen/bake_book/tree/master/Testing/jasmine/spec)

#### What was tested:
- addIngredient() function that adds an extra ingredient input when plus button clicked
- addStep() function that adds an extra method step input when plus button clicked
- removeInput() function which removes parent input when delete button is clicked
- showEditPreview() function which shows recipe url image preview on edit recipe page
- showSubmitPreview() function which shows recipe url image preview on submit recipe page
- These functions can be found in:[https://github.com/kmaaallen/bake_book/blob/master/static/javascript/script.js](https://github.com/kmaaallen/bake_book/blob/master/static/javascript/script.js)


#### How to run these tests
- As I did: run the file /documentation/automatedTesting/index.html in preview in cloud9 or preview in browser.
- Or follow these instructions from the Jasmine documentation on how to install and run Jasmine available at: https://github.com/jasmine/jasmine#installation
- These tests must be run in sequential order (untick run tests in random order).

#### Python testing using unittest
I created some automated tests for Python for this project. However, as I struggled to mock my mongodb database I couldn’t properly test my route functions as they all utilise the database to carry out functions.
I didn’t want to spend more time on this because the functions have been exhaustively tested by manual testing (documented above). However this is something I would like to improve for this project in future and an area where further study is required.
I have included a test.py file available here which contains a few simple tests that can be run to check the ‘about’ page route (which requires no interaction with the database) and the ‘page_not_found’ function work as expected as well as the password check logic.

## Deployment
### How to deploy this project to Heroku
1. Go to the Heroku website (https://id.heroku.com/login)and login to your account.
2. Create a new application by clicking “New” in your dashboard. Name this app and set the region to Europe.
3. Configure the deployment option for your app to be direct from GitHub and link to your repository containing the project code.
4. Set configuration variables in Heroku by going to the ‘settings’ section of your application. Set them as follows:

- IP	0.0.0.0
- PORT	5000
- MONGO_URI	mongodb+srv://<username>:<password>@<cluster_name>- wg6jm.mongodb.net/<database_name>?retryWrites=true&w=majority
    - *To get your Mongo URI read the following documentation:[https://docs.atlas.mongodb.com/driver-connection/](https://docs.atlas.mongodb.com/driver-connection/)
- SECRET	*your secret key
- DEBUG	FALSE
    - *This would be TRUE whilst developing the project

- In order to deploy to Heroku you need to make sure your project has a requirements.txt file
- Create by running the following command in your terminal: 
 > pip freeze –local  > requirements.txt
- You will also need a Procfile
    - Create by running the following command in your terminal:
> Echo web: python app.py > Procfile (where app.py is the name of your python file for the app.
- Add, commit and push those additions to your GitHub repo

### How to run this project locally
- To run this project locally you will need the following installed on your machine:
    - Python
    - Git
    - Pip
- As well as an account for MongoDB Atlas (you can set one of these up at: https://www.mongodb.com/cloud/atlas) which is running locally
- Open the command prompt on your computer
- Go to https://github.com/kmaaallen/bake_book and download the repository and unzip the file.
- Navigate to the working directory where the downloaded code is stored using the ‘cd’ command in command prompt or by opening the command prompt directly from the downloaded file in finder (mac) or windows explorer.
- Ensure all modules are imported from requirements.txt file using the following command:
> pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt
- To run the project use the following command:
> Python app.py

## Credits
### Content
Recipes used to populate the site were taken from BBC Good Food website and from family and friends.
For a comprehensive list of these sources please view the resources documentation, available [here](https://github.com/kmaaallen/bake_book/blob/master/resources.md)

### Media
The photos used in this site were obtained from google, using an advanced image search, searching for images that were free to use and modify, even commercially. For a full list of source images please view the resources document, available [here](https://github.com/kmaaallen/bake_book/blob/master/resources)

## Acknowledgements
Code snippets that have been sourced from elsewhere are documented in my project by comments and in the resources documentation [here](https://github.com/kmaaallen/bake_book/blob/master/resources.md)
