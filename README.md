# Property Manager - Django Project
This is a multi-office, multi-agent property management system for a website.  It allows employees to log into the admin and add, edit and delete properties.  The system would work for a growing company as users can also add office locations, cities, and new agents who are assigned to look after each property.  It is set up so more than 1 agent can be the contact/s for a property.
The models are linked together in a relational database.
The site visitor can make use of a 'quick search' and an 'advanced property search', as well as viewing office locations and agent contact details to make an enquiry.

## MODELS AND FIELDS
Property - city(foreign key), bedrooms, bathrooms, description, address details, price, published date.
Agent - name, property(many to many) , email
City - name
Office - name (geographical name), address

## SITE ADMIN
- Property - add property details and assign agents to a property
- Office - add, modify office details 
- Agents - agents details added, assigned to an office
- City - can be added and modified - each property has a city

## SITE PAGES
index - 'quick search' form, 5 latest properties
agents/ meet the team - shows basic contact information for each agent
offices - displays addresses for each office
quick search page - allows search by city
advanced search - 

## TESTING
- Handling 0 properties in the db - displays a coming soon template
- Ensuring no properties with pub_date in the future appear - on searches and DetailView
- Testing ON_DELETE on foregn key fields doesn't delete properties eg. if an agent or city is deleted.

## SKILLS REFERENCE
VIEWS
- Generic classes for views - ListView, DisplayView
MODELS
- Many to many relationships
- Foreign keys
- Class Meta - Verbose name/s corrects display of 'citys' 'propertys'
- Defining __str__ creating human readable names for admin.
- Help text on fields
- Bespoke functions and display in admin using .short_description
ADMIN
- list_display to configure display of items in list view of each object
- list filter - allows filtering of large numbers of objects
- fieldsets - put fields into groups
- inlines - display foreign key and many to many fields 
FORMS
- FORMS - dynamically created fields using ModelChoiceField
QUERIES
- Reverse many to many queries using object.object_set.all()
- Q - querying on mulitple fields





