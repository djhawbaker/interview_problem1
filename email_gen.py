#!/usr/bin/env python

"""Bug 1: Python3.3 PEP399 requires each module in the standard library to have
a pure Python version, so it doesn't need the separate C accelerated version 
cPickle. In Python3.3+ the pure Python library pickle is used instead.
Removed the "from cPickle" portion of the import to just use pickle
"""
import pickle

def getItemString(item):
    """Bug 2: Task name wasn't defined in the scope that it was being 
    used in, so was undefined when adding the task name to the 
    item_string. Set it to the value of item['content'] since there 
    are other possibilities than 'design' or 'first build'
    """
    task_name = item['content']

    if item['content'] == 'design':
        task_name = "Design/Concept"
    elif item['content'] == 'first build':
        task_name = "First Build"

    item_string = 'Task Date Change\n'
    item_string += 'Task Name: %s\n' % task_name
    item_string += 'Link: %s\n' % item['entity']['code'][0]
    item_string += 'Parent Build: %s\n' % item['sg_parent_build']['code'] if item['sg_parent_build'] else ''
    item_string += 'Start: %s\n' % item['start_date']
    item_string += 'End: %s\n' % item['due_date']

    return item_string

def main():
    with open('test_data.pkl', 'rb') as f:
        data = pickle.load(f)

    email_body = ''
    for item in data:
        item_string = getItemString(item)
        email_body += '%s\n' % item_string

    """Bug 3: Python3 requires parenthesis around print content. Added them"""
    print(email_body)

if __name__ == '__main__':
    main()
