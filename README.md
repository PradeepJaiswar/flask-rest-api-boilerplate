### Tutorial for setting up a basic Flask REST APIs only application

#### Install dependencies
```
$ pip install virtualenv  #make sure you do this
$ virtualenv .pyenv
$ source .pyenv/bin/activate
$ pip install -r requirements/base.txt
```

#### Run

```
$ python run.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
* Restarting with stat
```

Now hit `http://localhost:5000/v1/api/users` in your browser
Now hit `http://localhost:5000/v1/api/customers` in your browser
