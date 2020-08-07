#!/bin/bash
# This is a Django, Project-specific Cron script.
# Separate Projects would need a copy of this script 
# with appropriate Settings export statments.

PYTHONPATH="${PYTHONPATH}:/home/fluper/viewed"
export PYTHONPATH
export DJANGO_SETTINGS_MODULE=mysite.settings

python/path/to/django/project/directory/mysite/cron.py
