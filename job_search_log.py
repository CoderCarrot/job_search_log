from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from clint.textui import colored

questions = [
    {
        'type': 'input',
        'name': 'job_title',
        'message': 'What is the title of the job:',
    },
    {
        'type': 'input',
        'name': 'job_description',
        'message': 'What is the job description:',
    },
    {
        'type': 'input',
        'name': 'cover_letter',
        'message': 'Enter the cover letter written for this job:'
    },
    {
        'type': 'input',
        'name': 'application_date',
        'message': 'Enter the application date:'
    }        
]

answers = prompt(questions)
print(answers)