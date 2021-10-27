# Oira
Oira is a flask like dispatcher with the mindset to keep everything simple and avoiding third parties as much as we can.

# How to Use
```python
from oira import RouterController, Endpoint, Application, json, html, setup_jinja, jinja, redirect
from oira.status import forbidden, ok
from oira.static import serve_static
from oira.exceptions import UnauthorizedError

control = RouterController(debug=True, langs=['fa', 'en'])

@control.route(method=['POST', 'GET'], route='/file')
class PostFile(Endpoint):
    def post(request, response):
        form = request.body
        fileitem = form['userfile']
        filename = fileitem.filename.replace('\\','/').split('/')[-1].strip()
        with open(filename, 'wb') as f:
            while True:
                data = fileitem.file.read(1024)
                if not data:
                    break
                f.write(data)
        print('name: ', form['fname'].value)
        print('last name: ', form['lname'].value)
        print('None', form.getvalue('lnam'))
        return "hello"

    def get(request, response):
        file = serve_static("<path-to-file>", response)
        return file

app = Application(control)

```

## How to serve
```
gunicorn <path_to_application>:<application>
```
