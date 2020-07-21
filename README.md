# Property Manager - Django Project
This is a property manager system for a website.  It incorporates many models related to a multi-office propery company and links them together - agent, office, city.  Pages are searchable for all models containing linked information.

## MODELS


## WHO IS IT FOR?

## SITE ADMIN
- list_display used in PropertyAdmin to display all agents next to a property.
- Inlines used to allow adding and editing other models within property model admin page.

## SITE PAGES

## TESTING
- Handling 0 properties returned - displaying different templates
- Ensuring no properties with pub_date in the future appear - on searches and DetailView
- Testing ON_DELETE has desired effect on ForeignKey fields.

## SKILLS COVERED
- Admin list_display used to display bespoke information next to object names in admin.
- Many to many relationships
- Reverse many to many queries using object.object_set.all()
- Foreign keys
- Verbose plural names added to models to fix admin display issue - 'Citys', 'Propertys' etc.
- FORMS - dynamically created fields using ModelChoiceField
- Defining __str__ for all model names to give human readable names in admin.
- Template tags - |length_is and |linebreaks
- Q - querying on mulitple fields



