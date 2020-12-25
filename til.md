1. pip install `django djangorestframework psycopg`
   1. pip wanted me to upgrade, so I did.
2. `django-admin startproject chatter`
3. `python manage.py startapp backend`
4. Add 'backend' and 'rest_framework' to list of install apps in `settings.py`
5. We want postgres as our database
   1. created postgres database for the project
      1. CLI with `createdb chatterdb` or in psql with `CREATE DATABASE chatter;`
      2. psql `create user chatter_user with encrypted password <youwishyouknew>;
      3. `grant all privileges on database chatterdb to chatter_user;
   2. Add postgres settings to our app in settings.py
      ```
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'chatterdb',
              'USER': 'chatter_user',
              'PASSWORD': 'password',
              'HOST': '127.0.0.1', # apparently can also use 'localhost'
              'PORT': '5432', # default is 5432
          }
      }
      ```
6. Can run `python manage.py migrate` now if we want just to get things going.
   1. If I go into postgres now, I can see an auth user table.
7. I then created an admin user:
   1. `python manage.py createsuperuser`, gave it a name, email, and password
      1. I can now see this user in the auth_user table
   2. I can see the fields on the model if I go into the shell and import User and check the _meta fields:
      ```
      from django.contrib.auth.models import User

      User._meta.fields
      # If I want to shoe the relatioships too, I can use get_fields()
      User._meta.get_fields()
      # For just the names, I can use a list comp or map
      [f.name for f in User._meta.fields]
      ```
8. Before I get carried away, I'll make sure I can see React. since I'm trying to figure out auth with relation to the frontend. Before any DRF stuff or whatever, let's do webpack, babel, and react. `npm init` to create your package.json file.
9. `npm install --save-dev webpack webpack-cli  "webpack-bundle-tracker@<1" @babel/core babel-loader @babel/preset-env @babel/preset-react react react-dom`
   1.  Something about webpack bundle tracker needed to be lower than 1. I'll have to check.
9. create `webpack.config.js`
   ```
   const path = require('path');
   const BundleTracker = require('webpack-bundle-tracker');
   // const { CleanWebpackPlugin } = require('clean-webpack-plugin');

   module.exports = {
     // the base directory for resolveing the entry option
     // context: __dirname
     // The entry point that will have all the js, don't need extension because of resolve
     entry: '.index',
     output: {
       // where we want the bundle to go
       path: path.resolve('./assets/bundles/'),
       // convention for webpack
       filename: '[name]-[hash].js',
       // below solved the publicPath issue with autoMain
       // publicPath: ''
     },
     plugins: [
       // new CleanWebpackPlugin(),
       // stores data about bundles here
       new BundleTracker({
         filename: './webpack-stats.json'
       })
     ],
     module: {
       rules: [
         {
           // tells webpack to use the below loaders on all jsx and jsx files
           test: [/\.jsx?$/, /\.js?$/],
           // avoid node modules cause this will take forever
           exclude: /node_modules/,
           loader: 'babel-loader',
         }
       ]
     },
     resolve: {
       // extensions to resolve modules
       extensions: ['.js', '.jsx']
     }
   }
   ```
10. create `.babelrc`
   ```
   {
     "presets": ["@babel/preset-env", "@babel/preset-react"]
   }
   ```
11. Create js file where React hooks in:
    1.  `mkdir -p assets/js`, `touch assets/js/index.js`
12. `index.js`
13. `templates/index.html` so react has the element to hook into
14. Integrate React with Django
    1.  `pip install django-webpack-loader`
    2.  add `webpack_loader` to apps in settings
    3. show webpack loader where to find the bundles:
       ```
       STATICFILES_DIRS = (
           os.path.join(BASE_DIR, 'assets'),
       )

       WEBPACK_LOADER = {
           'DEFAULT': {
               'BUNDLE_DIR_NAME': 'bundles/',
               'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json')
           }
       } 
       ```
    4. update tamplate dirs in settings:
       ```
       TEMPLATES = [
           {
               'BACKEND': 'django.template.backends.django.DjangoTemplates',
               'DIRS': [os.path.join(BASE_DIR, 'templates')], # <-- this line
               'APP_DIRS': True,
               'OPTIONS': {
                   'context_processors': [
                       'django.template.context_processors.debug',
                       'django.template.context_processors.request',
                       'django.contrib.auth.context_processors.auth',
                       'django.contrib.messages.context_processors.messages',
                   ],
               },
           },
       ]
       ```
    5. Make sure '/' goes to the index html template. To do this, update top level url conf, `urls.py`:
       ```
       from django.contrib import admin
       from django.urls import path
       from django.views.generic import TemplateView # <-- added this

       urlpatterns = [
           path('admin/', admin.site.urls),
           path('', TemplateView.as_view(template_name='index.html')) # <-- added this
       ]
       ```

### User Auth Notes
1. Need to specify custom user before first migration
   1. First don't forget to register the app
2. In models, import `AbstractUser` from `django.contrib.auth.models`
3. Make a `User` class that inherits from `AbstractUser`
4. In settings, add `AUTH_USER_MODEL = '<app_name>.User` so it knows where to find this new user.
5. Then, since we created a new model, run `python manage.py makemigrations <app_name>`, and then `python manage.py migrate`
6. If you want it available in the admin panel, go to admin.py to register the User
   ```
   from django.contrib import admin
   from .models import User

   # Register your models here.
   admin.site.register(User)
   ```
7. To access the model, can't do normal import. User `django.contrib.auth.get_user.model()`
   1. in shell run `from django.contrib.auth import get_user_model`
   2. `get_user_model().objects.all()` gets all users