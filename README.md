# Createed using django2.1.5-adminlte3-template (also my repo)

You can then do a manual registration of accounts.
For Google sign-ins, you can go to 'settings.py' and replace the 'GAUTH_CLIENTID' and 'GAUTH_SECRET' variables with the ones I commented out beside them.
Take note that 'ADMIN_EMAIL_UN' and 'ADMIN_EMAIL_PW' also needs to be set/changed for password reset request emails to be sent.

The site's 'settings.py' include MY OWN Google client and key for OAuth2 (django-allauth). Not like you will be able to use it in production but it's good for testing so, I left it there. Should you want to implement the same on your production-ready websites, you'll have to create your own client-key-secret on https://console.developers.google.com. I strongly suggest that you use your researching skills and watch Django-Allauth tutorials on Youtube.

This sample template includes a "home" and a "user" app which, I think, are essential for any project website. If you plan to create a blog site, add a "blog" app and practice linking models, templates and urls yourself. That will definitely help you a lot. As in A LOT! ;)

Speaking of a "blog" app, I also added ckeditor to the "installed apps" list for Rich Text Editing. You'll just have to create your models and add the specific attributes you need.

Also, password-related stuffs were tested and are working as intended. You can modify the templates on "user/templates/password-reset/xxxxx.html". Just setup the fields needed by the system to send emails to users in "settings.py".

## Setting-up your production environment
I was able to setup a website on NameCheap.com using everything I included here. You can check it out and send me feedbacks: teppy@teppy.rocks. Site is https://teppy.rocks.
If you need help setting-up a Django website on NameCheap's shared hosting, this article was what helped me: https://pythonfusion.com/deploy-django-on-shared-hosting/. 

## Running this on Django 3.0 showed no problems at all in the development environment but PyMySQL can only work on Django 2.1 on Namecheap's shared hosting

Just keep in mind that we (me and pythonfusion) specifically used Django 2.1 because we need support for PyMySQL database on NameCheap. We purchased the cheapest plan: Stellar (https://www.namecheap.com/hosting/shared/) so, we only have access to MySQL Databases. I'm not sure yet if using Django 3.0 can be set to support PyMySQL. If you purchase the Stellar Plus or Stellar Business plans tho, you'll have access to PostgreSQL databases and you can use the latest version of Django. Setting-up your PostgreSQL database, you will just need to watch tutorials. ;)

## Thank you.
 
