from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json

questions = [
    {
        'type': 'input',
        'title': 'job_title',
        'message': 'What is the title of the job',
    }
]

answers = prompt(questions)
print_json(answers)