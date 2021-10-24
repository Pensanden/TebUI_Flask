A Small REST Api made as part of TebUI's interview process using Flask and MongoDB

To run this program you'll need an installation of Python 3, Pipenv, MongoDB

To run on your local machine:

```bash
$ pipenv install

$ pipenv shell

$ pipenv app.py
```
this will run the app on port 5000 of your localhost

The app is also dockerized for easier deployment
run as root if you get permission errors.

```bash

$ docker image build -t tebui-code-test . 

$ docker run -p 5000:5000 -d tebui-code-test

```

The MongoDB configuration is done for localhost on standard mongo port without authentication
you can add your own username and password or custom port in app.py MONGO_Setting dictionary 

