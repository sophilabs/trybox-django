# -*- coding: utf-8 -*-
from trybox.model import Step, RunCommandConsoleHint

step = Step(
    title='Create your first Django application',
    tooltip='Create project',
    description='Throughout this tutorial, we’ll walk you through the creation of a basic poll application.\n\n'\
                'It’ll consist of two parts:\n'\
                '* A public site that lets people view polls and vote in them.'\
                '* An admin site that lets you add, change and delete polls.'\
                '*Where to get help:*\n'\
                'If you’re having trouble going through this tutorial, please post a message to django-users or '\
                'drop by #django on irc.freenode.net to chat with other Django users who might be able to help.',
    hints=[
        RunCommandConsoleHint(
            title='Start project',
            tooltip='Start project',
            description='If this is your first time using Django, you’ll have to take care of some initial setup. '\
                        'Namely, you’ll need to auto-generate some code that establishes a Django project – '\
                        'a collection of settings for an instance of Django, including database configuration, '\
                        'Django-specific options and application-specific settings.\n\n'\
                        'From the command line, cd into a directory where you’d like to store your code, '\
                        'then run the following command:\n\n'\
                        '`django-admin.py startproject demo`',
            command='django-admin.py startproject demo'),
        RunCommandConsoleHint(
            title='Bye for now...',
            tooltip='Bye guys!',
            description='To be continued...\n\n'\
                        'For now run the following command:\n\n'\
                        '`echo "bye"`',
            command='echo "bye"')
    ]
)