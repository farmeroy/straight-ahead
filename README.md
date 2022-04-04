# Straight Ahead
A Twilio phone tree built with Python

To run this app locally:
- set up a Twilio trial account [here](https://www.twilio.com/try-twilio)
- find a number that can accept calls
- download this code 
```
git clone https://github.com/farmeroy/straight-ahead.git
```
- create environmental variables
```
export FLASK_APP=straight_ahead_hotline
export FLASK_ENV=development
```
- create a `.env` file that contains your twilio account sid, twilio auth token, along with any forwarding numbers you would like to use (see `.env.example`)
- set up a virtual environment
```
python3 -m venv venv
source ./venv/bin/activate
```
- install the requirements:
```
pip install -r requirements.txt
```
- install the straight_ahead_hotline package:
```
pip install -e .
```
- start the server:
`
flask run
`
- start ngrok
- copy the ngrok url and paste it into your Twilio number's webhook field

If you don't have ngrok, download it [here](https://ngrok.com/download). Ngrok is a service that temporarily serves your code on a real server.


## User Stories and Gehrkins 

### As a user I can reach my legal aid team from prison
- GIVEN: The user is calling from a prison phone
- WHEN: Twilio answers
- THEN: Tiwlio confirms the call by pressing <number>

### As a user I can leave a voicemail after working hours
- GIVEN: The user’s call is connected
- WHEN: It’s outside of working hours
- THEN: The user is directed to voicemail

### As a user I can reach a list of directory options 
- GIVEN: The user’s call is connected
- WHEN: IT’s in working hours
- THEN: the user is presented directory options

### The user can select a number
- GIVEN: The user selects press request
- WHEN: the user presses <number>
- THEN: The communications phone number is dialed


### As a user I can contact Fundraising
- GIVEN: The user selects ‘Fundraising’
- WHEN: the user presses <number>
- THEN: The Developement Manager’s  phone number is dialed

### As a user I can contact a spanish speaker
- GIVEN: The user selects “Spanish”
- WHEN: the user presses <number>
- THEN: The Spanish speaking political educator’s phone number is dialed

### As a user I can contact Organizing
- GIVEN: The user selects “Organizing”
- WHEN: the user presses <number>
- THEN: The user is connected to Regional Options

### As a uer I can connect with an organizer in my region
- GIVEN: The user is presented with regional options
- WHEN: The user selects a region by pressing <number>
- THEN: The Regional Organizer’s number is dialed

### The user can try correct an invalid input
- GIVEN: The user is presented with regional options
- WHEN: the user selects an invalid input <number>
- THEN: The user is presented with the regional option again

### The User can finally be connected with the operator
- GIVEN: The selected number has been dialed
- WHEN: The line operator is reached
- THEN: The user can speak with the operator

### As a user I can leave a voicemail
- GIVEN: The selected number has been dialed
- WHEN: the line operator does not answer
- THEN: The user can leave a voicemail

### As a user I can correct an incorrect input
- GIVEN: The user entered an incorrect menu option
- WHEN: The user presses the wrong button
- THEN: Twilio sends back to the main menu


