# mysite_seedstar
django app 
 
Django App
This is an application that stores names and email addresses in a database (SQLite is fine)
 
Assonptions:
 
- The application should be developed following a Model-View-Controller framework
- A SQLite database should be created with the necessary fields and right datatypes- to store data
- User should be able to insert, update and delete Name-email records from the database
- Form inputs should be validated 
- CSRF, XSS and SQL injection should be taken into consideration
 
 
Solution
 
* The application is developed following the MVC framework provided by django , thus routes are
contained in the urls.py file, views are contains in the views.py file and models (database data)
are contains in the models.py file.
 
* The application uses the SQLite database included in python. Fields for name and email have been
created with the respective datatype CharField and EmailField and can not be null. A Unique attribute
has been added to the field email to prevent redundancy of email addresses.
 
* The user is able to view complete list of names and emails, to edit or to delete a specific
Name-email record from the list.He can also add new record from the menu 'add contact'. 
 
* Name and email inputs are required in order to be saved in the database. Email address format is 
checked and validated as aright email format (username@yahoo.fr).
 
* The application is protected against malicious users to execute hijacking attack as all forms are using the CSRF token to transmit POST data. All SQL queries are escaped by using django's queryset to prevent SQL injection attack.
The application files are built using django's template inheritance ({{ var }}), thus preventing XSS attack.


admin : username=sedoyehoue
       password=sedoyehoue
 
