# backend_todo

Project: Design a simple To-Do List App using Django
Description: You need to design backend for a web-based To-do List application, as per the
given requirements:
1. Create a Django app with appropriate models to store information for the To-do List
app. The app should be able to store the following information:
a. Timestamp: Timestamp at which a task was created.
Should be auto-set when creating a new entry. A user should not be able to
edit this.
b. Title: Title of the task to be done.
i. A user can set this while creating a new entry. A user can also change
this while updating an existing entry.
ii. Max length: 100 characters.
iii. Mandatory field
c. Description: Description of the task to be done.
i. A user can add details about this task.
ii. Max length: 1000 characters
iii. Mandatory field
d. Due Date: Expected due date to finish the task
i. A user can set this while creating a new entry. A user can also change
this while updating an existing entry.
ii. Optional field
e. Tag: One or more tags that the user can add to the entry
i. A user can set this while creating a new entry. A user can also change
this while updating an existing entry. Multiple tags can be added to the
same entry
ii. Optional field
iii. Multiple tags with the same value should be saved only once.
f. Status: Shows status of a task
i. Should be one of these values.
1. OPEN (Default value)
2. WORKING
3. DONE
4. OVERDUE
ii. Mandatory field
2. Django Admin interface should be enabled for the model(s). The admin site should
have the following:
a. Appropriate validation checks are in place. The ones defined in Point 1 above
should be enforced.
(Ex: In 1.a, A user should not be able to edit the timestamp.)
b. Proper changelist view with filters for every model
c. Proper fieldsets for every model
3. The following REST APIs should be created using DRF (DjangoRestFramework):
a. CREATE a todo item
b. READ one todo item
c. READ all todo items
d. UPDATE a todo item
e. DELETE a todo item
4. Create & Share a working Postman Collection which can be used to test all the APIs
mentioned in Point 3. Above.
5. Enable support for Basic Authentication for all the APIs.


# How to run the project:

1.After Extracting the zip file, You need to run the following commands,

2.Create a virtual enviroinment or use existing virtual enviroinment.

3. Next you have to run the following command,
# pip install -r requirements.txt

4. After that,
# cd todoapp

5. Now run the following command,
# python manage.py runserver

6. after that the page will look like this:

![image](https://github.com/Karthik-02/backend_todo/assets/81423983/e86c89b1-8de6-443b-b40c-ebb645030481)


7. After that change the url to '/admin'

8. Now you can see the admin portal:

Enter username as 
#'karthik' 
and
password as 
#'admin'

9. Now you can see the django admin site:

![image](https://github.com/Karthik-02/backend_todo/assets/81423983/ed7cd153-b9d2-44f0-a66c-6146baf751d2)
