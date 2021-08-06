# Property Manager - Django Project

## INTRO
A property website with a back end admin system where users can create properties, add images, assign agents to the property, create new office locations and add new towns or cities where properties are rented.

The front end has a quick search by city and a more advanced search which fiters the properties based on number of bedrooms, price and location.

(If you're learning Django, this could be a good practice web application to try out after the polls app tutorial. See skills covered below.)

## FEATURES
### Models and Fields
- Property - city (foreign key), image field, bedrooms, bathrooms, description, address details, price, published date.
- Agent - name, property (many to many field) , email
- City - name
- Office - name (geographical name), address

### Forms
- Quick Search Form - uses ModelChoiceField to display all 'City' objects and allows user to search by city
- Advanced Form - numerous ChoiceFields - max price, min bedrooms etc.

### Site Admin
- Property - add property details and assign agents to a property
- Office - add, modify office details 
- Agents - agents details added, assigned to an office
- City - can be added and modified - each property has a city

### Site Pages
- index - 'quick search' form + 5 latest properties displayed
- agents/ meet the team - shows basic contact information for each agent
- offices - displays addresses for each office
- quick search page - allows search by city
- advanced search - allow advanced search preferences

## TOOLS
- Django
- Bootstrap
- python-decouple
- Pillow

## SCREENSHOTS

### Homepage

![homepage](https://github.com/richardgourley/property-manager-django-project/blob/master/screenshots/homepagequicksearch.png)

### Advanced Search

![advancedsearch](https://github.com/richardgourley/property-manager-django-project/blob/master/screenshots/advancedsearch.png)

### Property Listing

![propertylisting](https://github.com/richardgourley/property-manager-django-project/blob/master/screenshots/propertydisplayview.png)

## GETTING STARTED

```
virtualenv (any virtual env directory name you like here) -p python3
cd (virtual env name)
source bin/activate
pip install django
django-admin startproject property-manager-project
cd property-manager-project
```

- Set up a database for the project. (OR you can use SQLlite for testing the project.)
- Create a .env file similar to below (in the same dir as 'manage.py') - (Dont add db details to .env if only using SQLlite)
- See 'settings.py' - decouple replaces the variables in 'settings.py' with your variables in the .env file.
```
SECRET_KEY=12345etc.
DEBUG=True
DB_NAME=dbname
DB_USER=newusername
DB_PASSWORD=password
DB_HOST=127.0.0.1
PORT=3306
```

Install python decouple and any database client you require (MySQL example used here) 

```
pip install python-decouple
pip install mysqlclient
```

```
python manage.py startapp properties

python manage.py makemigrations properties
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## SKILLS REFERENCE
This could be a good Django practice website.  Here are some of the skills covered in building the site.

VIEWS
- Generic classes for views - ListView, DisplayView
- Pagination added to city_view
- HttpRedirect used in quick_search

CUSTOM CONTENT PROCESSOR
- Bespoke function 
- Obtains 5 most recent properties - available for every page in the app

MEDIA
- Saving and displaying images - using Pillow

MODELS
- Many to many relationships
- Foreign keys
- Class Meta - Verbose name/s corrects display of 'citys' 'propertys'
- Defining __str__ creating human readable names for admin.
- Help text on fields
- Bespoke functions and display in admin using .short_description

ADMIN
- prepopulated_fields used to auto fill in slug from the name of city/ property
- list_display to configure display of items in list view of each object
- list filter - allows filtering of large numbers of objects
- fieldsets - put fields into groups
- inlines - display foreign key and many to many fields 

FORMS
- FORMS - dynamically created fields using ModelChoiceField

QUERIES
- Reverse many to many queries using object.object_set.all()
- Q - querying on mulitple fields

TESTING
- Test Case used.
- Testing divided into 3 files - forms, views, models





