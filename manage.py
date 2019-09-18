#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chores.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


"""
Task planner app

Has a list of tasks that are scheduled for when they must be done.
Daily, weekly, etc.

Bigger concept:
Point system
mandatory tasks are worth a large amount of points, say 1000
optional but important tasks are worth 100 
nice things that are special but not required are worth 10

brush teeth 1000
shower 1000
homework 1000
feed cat 1000
practice piano 100
clean litter box 100
work out 100
read 100
clean toilet 10 - lingers and gains value if not done over days. Shows back up after a week and repeats.
wash mirror 10
shake welcome mat 10




There could be a design where these points are required for rewards
6000 - Got it together
6010 - Nice job
6400 - Doin great
6700 - Holy Moly
6710 - bonus 1
6720 - bonus 2
6730 - bonus 3

This should be used to grant acheivement badges for the day and for streaks etc.

These badges should be required for redemption for some rewards.
i.e. unlocking netflix, allowance, snapchat, video games

There could be a photo validation system. 
Take a photo of the empty sink and mom validates that dishes are done.

Should be a way for mom to add a bounty if something comes up. For example, rake leaves for 200.
"""