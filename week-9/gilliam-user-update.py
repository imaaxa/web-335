# ===========================================
# Title: Exercise 9.3
# Author: Cory Gilliam
# Date: 14 Dec 2019
# Modified By:
# Description: Updating and Deleting  Documents
# ===========================================

# Using the “Update Document Example,” complete the following:
# x  Add a new file under your week-9 directory and name it <lastname>-user-update.py
# x  Import
# x    pymongo
# x    pprint
# x    datetime
# x  Connect to your local MongoDB instance
# x  Update the user document created in Exercise 9.2 by changing the email field to your Bellevue University email address (follow the code provided in the “Update Document Example”).
# x  Using the findOne() function, output the following fields (follow the code provided in the FindOne query from Exercise 9.2)
# x    email
# x    employee_id
# x    first_name
# x    last_name

# Imports
from pymongo import MongoClient
import pprint
import datetime

# Database
client = MongoClient('localhost', 27017)
db = client.web335

# Update user
user_id = db.users.update_one(
  {
    'employee_id': '2037879'
  },
  {
    '$set': {
        'email': 'pquill@my365.bellevue.edu'
    }
  }
)

# Find and print employee: 2037879
pprint.pprint(db.users.find_one(
  {
    'employee_id': '2037879'
  },
  {
      'email': 1,
      'employee_id': 1,
      'first_name': 1,
      'last_name': 1,
      '_id': 0
  }
))
