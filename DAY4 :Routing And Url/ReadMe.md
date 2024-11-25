Routes -> this is a path that is triggered when we visit certain urls.
Url -> this is the string we type into the browser to access certain resources.
URL SYNTAX : protocol://DomainName/Path/to/resource
the path/to/resource is the route and is handled by our server
example in the local development when we run the server the browser opens at :
                  http://127.0.0.1:8000/task/field
                  where : http ->protocol 127.0.0.1->domainName /task/field -> our route
In django routes are created in the urls.py file .
it is good to separate the urls for each app.
when working with urls from an app always remember to include it using the include method.
CREATED A SIMPLE TO-DO List to show working of various routes. 
