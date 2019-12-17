# ===========================================
# Title: Exercise 9.2
# Group: 1
# Team Developers: Cory Gilliam, Tyler Librandi, Thip Rattanavilay and Loren Wetzel
# Date: 15 Dec 2019
# Modified By:
# Description: Queries for milestone 4
# ===========================================

# Imports
from pymongo import MongoClient
import pprint
import datetime

# Variables


# Database
client = MongoClient('localhost', 27017)
db = client.web335

# Create Database
db.nodeflixUser

##
 #  User Insert
 #
 # Insert a user into the database
 #
 #   @param firstNameRaw (string) users first name
 #   @param lastNameRaw (string) users last name
 #   @param userNameRaw (string) users username
 #   @param passwordRaw (string) hashed user password
 #   @param ageRaw (int) users age
 #   @param genderRaw (string) users gender
 #   @param phoneNumberRaw (string) users phone number
 #   @param emailRaw (string) users email address
 #   @param accessLevel (object) Options that user has access to
 #   @param active (bool) is user account currently active
 #   @param address (array) array of address linked to this account
 #   @param payment (object) payment method details
 #   @return id of the inserted user
 ##
def userInsert( firstNameRaw, lastNameRaw, userNameRaw, passwordRaw, ageRaw, genderRaw, phoneNumberRaw, emailRaw, accessLevel, active, address, payment ):
  user = {
    'firstName': firstNameRaw,
    'lastName': lastNameRaw,
    'userName': userNameRaw,
    'password': passwordRaw,
    'age': ageRaw,
    'gender': genderRaw,
    'phoneNumber': phoneNumberRaw,
    'email': emailRaw,
    'accessLevel': accessLevel,
    'activeAccount': active,
    'startDate': datetime.datetime.utcnow(),
    'address': address,
    'payment': payment
  }
  return db.nodeflixUser.insert_one(user).inserted_id

 # List active users
 ##

##
 # Updates a users active status
 #  @param userName (string) username on the account
 #  @param state (bool) true/false
 ##
def userUpdateActive(userName, state):
  db.nodeflixUser.update_one(
    {
      'userName': userName
    },
    {
      '$set': {
        'activeAccount': state
      }
    }
  )

##
 # Updates a users access level
 #  @param userName (string) username on the account
 #  @param level (string) basic/plus/premium
 ##
def userUpdateAccessLevel(userName, level):
  # Make update
  db.nodeflixUser.update_one(
    {
      'userName': userName
    },
    {
      '$set': {
        'accessLevel': level
      }
    }
  )

##
 #  Prints list of user(s) by key:value
 #
 #  @param key (string) database key
 #  @param value (varies) value of the field looking for
 ##
def usersListBy(key, value):
  results = db.nodeflixUser.find(
      {
          key: value
      },
      {
          'firstName': 1,
          'lastName': 1,
          'email': 1,
          'accessLevel': 1,
          'activeAccount': 1,
          '_id': 0
      }
  )
  for result in results:
    pprint.pprint(result)
    print('\n')

##
 #  Prints list of all active user(s)
 #
 #  @param key (string) database key
 #  @param value (varies) value of the field looking for
 ##
def usersListActive():
  results = db.nodeflixUser.find(
    {
        'activeAccount': 'true'
    },
    {
        'firstName': 1,
        'lastName': 1,
        'age': 1,
        'gender': 1,
        'phoneNumber': 1,
        'email': 1,
        'accessLevel': 1,
        'startDate': 1,
        'address': 1,
        '_id': 0
    }
  )
  for result in results:
    pprint.pprint(result)
    print('\n')

##
# Build Payment method object
#
# * This is just for the exercise. *
# * Credit card data is to NEVER be stored in a database *
#
#   @param name (string) card name
#   @param cardNumber (int) card number
#   @param expiration (date) card expiration date
#   @param cvc (int) card cvc number
#   @return payment method object
##
def buildPayment(name, cardNumber, expiration, cvc):
  return {
    'name': name,
    'number': cardNumber,
    'expiration': expiration.strftime("%m/%y"),
    'cvc': cvc
  }

##
 # Build Address
 #
 #   @param street1 (string) main part of address
 #   @param street2 (string) secondary part of address
 #   @param city (string) city
 #   @param state (string) state (full name)
 #   @param postalCode (string) postal code
 #   @param country (string) country name (full name)
 #   @param misc (string) miscellaneous information
 #   @param addressType (string) type of address (home, billing, etc)
 #   @return address object
 ##
def buildAddress( street1, street2, city, state, postalCode, country, misc, addressType ):
  return {
    'street1': street1,
    'street2': street2,
    'city': city,
    'state': state,
    'postalCode': postalCode,
    'country': country,
    'misc': misc,
    'type': addressType
  }


# Test mongoDB functions

# Insert user
#address_1 = [buildAddress('123 Main St', 'Apt. 23', 'Star City', 'Texas', '54321-1234', 'United State', 'No live animals', 'Home'), buildAddress('123 123 St NW', 'Suit 94', 'Star City', 'Texas', '54323-1234', 'United State', 'No dead animals', 'Billing' )]
#payment = buildPayment('Visa', 4111111111111111, datetime.datetime(2024, 6, 30), 123)
#lastUser = userInsert('Lynda', 'smith', 'lsmith', 'test', 24, 'female', '(321) 978-1234', 'lsmith@gmail.com', 'plus', 'true', address_1, payment)
#
#for result in db.nodeflixUser.find({'_id': lastUser}):
    #pprint.pprint(result)
    #print('\n')

# Update user active
#usersListBy('userName', 'lsmith')
#print('Updating....\n')
#userUpdateActive('lsmith', 'true')
#usersListBy('userName', 'lsmith')

# Update user access
#usersListBy('userName', 'lsmith')
#print('Updating....\n')
#userUpdateAccessLevel('lsmith', 'premium')
#usersListBy('userName', 'lsmith')

# List user by key/value
#usersListBy('userName', 'lsmith')

# List all active users
#usersListActive()
