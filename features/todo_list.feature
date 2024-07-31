# language: en

Feature: To-do list manager
@add_task
Scenario: Add a task to the to-do list
    Given the To-Do list is empty
    When the user adds a task "Buy groceries"
    Then the To-Do list should contain "Buy groceries"

@list_tasks
Scenario: List all tasks in the to-do list
    Given the To-do list contains tasks: Buy groceries, Pay bills
    When the user list all tasks
    Then the output should contain: ID: 1, Description: Buy groceries ; ID: 2, Description: Pay bills

@mark_task_complete
Scenario: Mark a task as completed
    Given the to-do list contains tasks: 1 
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

@clear_tasks
Scenario: Clear the entire to-do list
    Given the to-do list contains tasks: Buy groceries , Pay bills
    When the user clears the to-do list
    Then the to-do list should be empt

