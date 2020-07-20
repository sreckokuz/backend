### Recommended Start
```

$ cd path/to/your/dev/folder
$ mkdir channels-rapid
$ cd channels-rapid
$ git clone https://github.com/codingforentrepreneurs/Rapid-ChatXChannels .
$ git reset 2a3f180b94d682efd30fd1d2a394a16bab1008a3 --hard
$ git remote remove origin
$ virtualenv -p python3 .
$ source bin/activate
(channels-rapid) $ cd src
(channels-rapid) $ pip install -r requirements.txt
(channels-rapid) $ python manage.py createsuperuser
... do the creation
(channels-rapid) $ python manage.py createsuperuser
... create second super user 
```


### Install Redis
1. Download Redis
    - Using [Homebrew](http://brew.sh):
        ```
        brew install redis

        brew services start redis
        ```
        Brew permission errors? Try `sudo chown -R "$USER":admin /usr/local`

    - Direct [Download](http://redis.io/download)
