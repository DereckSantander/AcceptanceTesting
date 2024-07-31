
# Define a list to represent the to-do list
to_do_list = []

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    # Set the to-do list as an empty list
    global to_do_list
    to_do_list = []

# Step 2: When the user adds a task "Buy groceries"
@when('the user adds a task "{task}"')
def step_impl(context, task):
    # Add the task to the to-do list
    global to_do_list
    to_do_list.append(task)

# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    # Check if the task is in the to-do list
    assert task in to_do_list, f'Task "{task}" not found in the to-do list'

@given('the to-do list contains tasks: {task_list}')
def step_impl(context, task_list):
    global to_do_list
    to_do_list = []
    task_descriptions = task_list.split(',')
    for i, description in enumerate(task_descriptions, start=1):
        to_do_list.append({'ID': i, 'Description': description})

@when('the user lists all tasks')
def step_impl(context):
    global to_do_list
    context.output = to_do_list

@then('the output should contain: {expected_output}')
def step_impl(context, expected_output):
    expected_tasks = []
    task_descriptions = expected_output.split(';')
    for description in task_descriptions:
        task_id, task_description = description.split(', Description: ')
        task_id = int(task_id.split(': ')[1])
        expected_tasks.append({'ID': task_id, 'Description': task_description})
    
    # Compare the output to the expected result
    assert context.output == expected_tasks, f"Expected {expected_tasks} but got {context.output}"

@given('the to-do list contains tasks: {task_ids}')
def step_impl(context, task_ids):
    global to_do_list
    to_do_list = []
    task_ids = task_ids.split(', ')
    for task_id in task_ids:
        tasks.append({'ID': int(task_id), 'Description': f'Task {task_id}', 'Completed': False})

@when('the user marks task "{task_description}" as completed')
def step_impl(context, task_description):
    for task in tasks:
        if task['Description'] == task_description:
            task['Completed'] = True
            break

@then('the to-do list should show task "{task_description}" as completed')
def step_impl(context, task_description):
    for task in tasks:
        if task['Description'] == task_description:
            assert task['Completed'], f"Task '{task_description}' should be marked as completed"
            return
    assert False, f"Task '{task_description}' not found in the to-do list"