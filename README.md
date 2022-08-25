Original tutorial published on [jankowski.dev](https://dev.to/dtuidmaciek/todo-list-with-django-drf-alpine-js-and-axios-1h0e)

- base_todo_list - Skeleton implementation of the site, no interactions
- alpine_todo_list - The end result of the jankowski.dev tutorial, there is an alpine 2.x and alpine 3.x version in lists/templates
- django_unicorn_todo_list - Native Django Unicorn implementation of the site. Heavily leverages Django for most things. No Websocket/SSE support.
- htmx_todo_list - Native HTMX implementation of the site, uses Django templates for replacing the elements. No Websocket/SSE async updates.
- turbo_todo_list - Native Turbo implementation of the site, uses Django templates for replacing the elements. No Websocket/SSE async updates.
- unpoly_todo_list - Implementation of the Todo list with unpoly. It's a partial implementation since the DELETE requests were getting remapped and I didn't want to figure out what the actual request was.


Select a directory and run:
```bash
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
LOG_LEVEL=DEBUG ALLOWED_HOSTS=<public ip> DEBUG=TRUE DJANGO_SECRET_KEY=<your key> ./manage.py runserver 0.0.0.0:<port>
```
