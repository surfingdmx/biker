# Biker

Biker aims to be a web platform for biking competition. It allows users to track themselves as well as build local
communities and challenge each other.

As soon as the application starts to evolve and 'real' features are being implemented, there will be a short description of features here. For now, see the [drafts](drafts/README.md) for some ideas and planned features.


## Philosophy

This project is intended to be free and open source. It is only available under the AGPLv3.

Because this platform will have a huge potential of disclosing privacy and creating pretty detailed profiles of users, it is mandatory that the user **always has the choice to give away their data or not**. The only thing that is absolutely necessary is an email address for holding back spammers at registration and provide password recovery for users. This app will never ask for a real name, for your age, address, telephone number, credit card information or whatsoever. Why should it?

This implies that some of the features of the application rely on the honesty of the users. The platform will respect users who do not want to give away their location or the times when they decide to ride the bike. If a feature collects sensitive user data (e.g. the automatic route creation by GPS track) the user will be explicitly asked if he/she is willing to do so. If **at any time** the user wishes to revoke a decision and have sensitive data deleted, this will be respected, even if I have to rummage in the database by hand for this.

If anyone has concerns about data that may be collected **please contact me**, either here on the platform or by email (surfingdmx@tutanota.com) if you want. This is **super important**.


## Get in touch

There are numerous ways to get help on the project and discuss with me and/or other members:
- Use GitHub capabilites (issues, PR, PM)
- Write me an email: surfingdmx@tutanota.com
- Use [Riot messenger](https://riot.im/) (to be more precise, use the [Matrix](https://matrix.org/) infrastructure) chat with:
  - Public chat room: #thebiker:matrix.org
  - Private chat with me: @surfingdmx:matrix.org

As soon as there are other contributors to this project, you may contact them as well (if they decide so of course).


## Contributing

Any contribution is WELCOME!!!

**Security Issues** should not be sent publicly before there is a fix or at least a workaround. Please send them to my mail address or in a private matrix chat.

One of the most important things: I don't care about the way the information gets to me (or any of core project team members in the future). You may use the GitHub features like Issues and Pull Requests, but if you don't want to (e.g. if you do not want to create a GitHub account) you may send me anything from sketches to snippets or patch files by mail (surfingdmx@tutanota.com) and I will publish it in an appropriate way here in the repo.

How to get started? What can I do? Pretty much everything you come up with :) Some ideas:
- Contribute to the features, ideas, UI etc. (see [drafts](drafts/README.md))
- Create/Improve project graphics like logo, UI sketches, etc (as I am a total design n00b)
- Write something related to the project you consider helpful for others, that may be posted here in the README or on a Wiki page
- Improve code quality: if you feel like there are some files with inconsistent coding style, missing comments or documentation (though I really try to produce high-quality code)
- Provide the project with hints about design issues that may bite us in the future
- File structured issues, that may be enhancements, bugs etc.
- Implement new features (including code documentation and tests :) )
- Support the development setup: Create CI configuration and infrastructure
- Extend this list if you feel something should be done but you don't want to / cannot do it yourself.


## Development setup

This is a standard Django project. It currently runs with Python 3.5 and uses Django 2.2.4.

It is highly recommended to use a virtualenv, otherwise you may unlock a secret hard mode with different dependency versions and other python applications suddenly crashing on your system.
```
$ git clone https://github.com/surfingdmx/biker.git
$ cd biker
$ virtualenv -p python3 venv
$ . venv/bin/activate
(venv) $ pip3 install -r requrements.txt
(venv) $ cd biker
(venv) $ python3 manage.py migrate
(venv) $ python3 manage.py createsuperuser
(venv) $ python3 manage.py runserver
```
This starts a development server on localhost:8000.

For getting started with Django see the [documentation](https://docs.djangoproject.com/en/2.2/).

Personally, I use [PyCharm](https://www.jetbrains.com/pycharm/) Community Edition for development. Though Jetbrains is a company that is interested in selling their products, PyCharm CE is free (at least in terms of money) and open source. There is a professional version with explicit django support out there, but I have not missed any features in CE so far.  
But feel free to use and provide your own suggestions for a development setup, from other (ideally free) IDEs to vim & shell setup. I deliberately kept the project files out of the repository.

I am an absolute Linux fanboy. If someone insists on developing on a Windows machine, I cannot provide you with more than the django docs. If someone thinks that a Windows development setup description is something that is missing, please file an issue/PR and provide some hints.
