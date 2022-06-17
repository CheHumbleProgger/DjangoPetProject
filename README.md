# PetProject
This is my PetProject using Django

Directories:

  PetProject: config files for this project
  files in it:
    
      asgi.py -- ASGI configuration for this project
      settings.py -- file with all settings of this project
      urls.py -- url adresses to project application
      wsgi.py -- WSGI configuration for this project
      
  home: app with frontend and backend of the home page + registration form
  files in it:
  
      apps.py -- home application configurator
      urls.py -- url addresses of application home
      views.py -- here is just a simple view named HomeView
      /templates/home/main.html -- front of the home page
      /templates/registration/login.html -- front of the registration form
      
  notes: directory containing the frontend and backend of app 'Notes' it is a CRUD made usable for many users.
  files in it:
      
      admin.py -- creates an admin form representation for Note model
      apps.py -- notes application configurator
      models.py -- contains a Note model, which includes: title of note, text of the note, dates of creation and last update and its owner as foreign key
      urls.py -- url addresses of application notes
      views.py -- views for creating, updating and deleting notes, also with providing list and detailed views of notes. Some methods (such as get_queryset and form_valid) are overriden in order to implement ownership of notes
      /templates/notes/note_confirm_delete.html -- front of form of deletion confirmation
      /templates/notes/note_detail.html -- front of page, that provides the detailed view of the specific note
      /templates/notes/note_form.html -- front of the form, providing the creation or update of user's note
      /templates/notes/note_list.html -- front of showing the list of all of the user's notes
     
     
# Starting the project
After downloading the project open the command line, get to the directory of this project and execute

  python manage.py runserver <the_port_you_have_avaliable>
  
example: python manage.py runserver 8000
