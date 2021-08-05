# Property Manager - Django Project

## INTRO

## FEATURES
### Models and Fields
- Property - city(foreign key), image field, bedrooms, bathrooms, description, address details, price, published date.
- Agent - name, property(many to many) , email
- City - name
- Office - name (geographical name), address

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





