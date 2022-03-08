# Restaurant Booking.
![Image](assets/images/screenshots/mock-up.png?raw=true)
This is a table booking service for a restaurant where users can book a table and the amount of people. The data is then updated into a Google worksheet where the restaurant can see all bookings.

You can view the live site here. [Restaurant booking](https://restaurant-booking-project.herokuapp.com/)

## User Experience

### User Stories

### As a site creator:
- I want the programme to be easy for users to make a booking.
- I want to see bookings in the google sheet presented in an easily readable way.
- I want to make it easy for the user so they return to the programme.

### As a first time user:
- I want to be able to make a booking easily.

### As a returning user:
- I want to remember how to use the programme. 
- I want to be able to make a new booking easily.

## Flowchart 
![Image](assets/images/screenshots/flowchart.png?raw=true)
I made a flowchat to help witht the process of malking my functions. 

## Features

### Intro
![Image](assets/images/screenshots/intro.png?raw=true)

When the programme is first opened, you will see a greetings message and a short introdcution on how to make a booking.

### First and last name
![Image](assets/images/screenshots/first-name.png?raw=true)
![Image](assets/images/screenshots/last-name.png?raw=true)

The first thing the programme will ask for is your first name and then your last name. This is what will be used for the name on the booking. You can only enter letters for the iunput, amything else will be invalid.

### People
![Image](assets/images/screenshots/number-of-people.png?raw=true) 

You'll then be asked how many people you would like to make the booking for. You can only enter numbers for the input, amything else will be invalid.

### Updating worksheet
![Image](assets/images/screenshots/updating-worksheet.png??raw=true)

When the number of people has been submitted, you then see two messages to show that the booking sheet is updating and when it has been updated.

### Confirmation  
![Image](assets/images/screenshots/confirmation.png??raw=true) 

There is then a message to say the booking is confirmed.
The last message instructs the user how to make another booking if they wish to.

### Future Features
- Have a max amount of tables available and the programme will show if the restaurant has any availablity.
- To add a fucntion where the user can input their email and receive a confirmation of their booking. 
- Have a menu that the user can go back and change details if entered incorrectly.

## Testing 

### PEP8
I used the [PEP8 Validation service](http://pep8online.com/)
No errors were found. 

## Deployment 

1. Ensure all the dependencies are included by adding them to the requirements.txt file by running the following command in the terminal: pip3 freeze > requirements.tx
2. Ensure the project has been fully committed and pushed to git 
3. Go to your heroku account, if you don't have one create one
4. On the home screen click on the create new app button
5. Enter a name for the project and select your region to the correct region.
6. On the next screen select settings
7. Go to config vars and click reveal config vars
8. Switch to the program file and where you are keeping your credentials copy these and then on heroku enter a name for the key and paste the code into the config vars value box and click add
9. Now scroll down to buildPacks and click add build packs
10. First select python and click save changes
11. Click back into build packs and choose node.js and click save again
12. Ensure that the Python  build pack is at the top of the list you are abe to drag and drop if you need to rearrange
13. Now select deploy
14. From the deployment method select GitHub
15. Then click on the connect to github button that appears
16. Click into the search box and search for the project name
16. Once located select connect
17. Then click deploy branch, this will then be shown in the box below
18. You can the click view to show the app in a browser

## Credits 

### Acknowledgements 
- To the Slack community.
- Stack Overflow as valuable source of information.
- [W3Schools](https://www.w3schools.com/) 
- Deployment instructions from (https://github.com/steveforrest/Disposable-Income#contents)