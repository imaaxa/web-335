# ===========================================
# Title: Exercise 9.2
# Author: Cory Gilliam
# Date: 14 Dec 2019
# Modified By:
# Description: Querying and Creating Documents
# ===========================================

# Using the “Create Document Example” and “FindOne Query Example 2, ” complete the following:
# x  1.Create a new folder under your web-335 directory and name it week-9.
# x  2.Add a new file under your week-9 directory and name it < lastname > -user-service.py
# x  3.Import
#     a.pymongo
#     b.pprint
#     c.datetime
# x  4.Connect to your local MongoDB instance
# x  5.Create a new user document(follow the code provided in the “Create Document Example”)
#   6.Insert the new user document(follow the code provided in the “Create Document Example”)
#   7.Output the auto-generated user_id
#   8.Query the users collection using the “find_one()” method(follow the code provided in the FindOne Query Example 2)
#   9.Print the document returned from the FindOne Query
# Note: You are essentially recreating the “Create Document Example”

# Imports
from pymongo import MongoClient
import pprint
import datetime

# Database
client = MongoClient('localhost', 27017)
db = client.web335

# User
user = {
  'first_name': 'Peter',
  'last_name': 'Quill',
  'email': 'pquill@nowhere.com',
  'employee_id': '2037879',
  'date_created': datetime.datetime.utcnow()
}

# Insert user
user_id = db.users.insert_one(user).inserted_id

# Print id of new user
print(user_id)

# Find and print employee: 2037879
pprint.pprint(db.users.find_one({'employee_id': '2037879'}))
