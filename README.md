<h1>Python-based API using Django</h1>
<p>This is a simple Django REST API that allows users to manage app details<br>
The API provides the following endpoints:</p><hr>
<ul>
    <li>POST /api/add-app/ - Add app details to the database.</li>
    <li>GET /api/get-app/{id}/ - Retrieve app details by ID.</li>
    <li>DELETE /api/delete-app/{id}/ - Remove an app by ID.</li>
</ul>

<h2>Setup Instructions</h2>
<ul>
    <li>Download python Latest version</li>
    <li>Install all required library</li>
    <li>Create a directory and install Django </li>
    <li>Create project by running <b>django-admin startproject djangoAPI</b></li>
    <li>Create app by running <b>python manage.py startapp API</b></li>
</ul>
<h2>Code Implementations</h2>
<p>Add neccessary code in different-different files or modules like- </p>
<ul>
    <li>djangoAPI -> setting.py -> install "API & rest_framekwork" </li>
    <li>djangoAPI -> urls.py -> add url of "API -> urls.py" </li>
    <li>API -> models.py -> add model</li>
    <li>And so on like(views, etc)</li>
</ul>
<h2>API Endpoints</h2>
<p>Run the server by using <b>python manage.py runserver</b> commond using terminal . </p>
<ul>
    <li> Add an App <br>
        http://127.0.0.1:8000/api/AppDetails</li>
</ul>
