
import random
import html


def clean_questionaire_data(data):

    formatted_questions = []
    question = {}
    choices = []
    incorrect = []
    
    for items in data:
        incorrect = [html.unescape(data) for data in items['incorrect_answers']]
        choices = incorrect + [ items['correct_answer'] ]
        random.shuffle(choices)
        question = {
            'question': html.unescape(items['question']),
            'correct': html.unescape(items['correct_answer']),
            'choices': choices
        }
        formatted_questions.append(question)
        choices = []
        incorrect = []
        question = {}
 
    return formatted_questions


def get_right_answers(data):
    right_answers = {}
    number = 0
    for items in data:
        right_answers[number] = html.unescape(items['correct_answer'])
        number +=1

    
    return right_answers