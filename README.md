Original tutorial published on [jankowski.dev](https://dev.to/dtuidmaciek/todo-list-with-django-drf-alpine-js-and-axios-1h0e)

- base_todo_list - Skeleton implementation of the site, no interactions
- alpine_todo_list - The end result of the jankowski.dev tutorial, there is an alpine 2.x and alpine 3.x version in lists/templates
- htmx_todo_list - Native HTMX implementation of the site, uses Django templates for replacing the elements
- tailwind_toto_list - I forget what this was supposed to be
- turbo_todo_list - Future - implement with Turbo

Also - may try unicorn and unpoly.


Select a directory and run:
```bash
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
LOG_LEVEL=DEBUG ALLOWED_HOSTS=<public ip> DEBUG=TRUE DJANGO_SECRET_KEY=<your key> ./manage.py runserver 0.0.0.0:<port>
```
