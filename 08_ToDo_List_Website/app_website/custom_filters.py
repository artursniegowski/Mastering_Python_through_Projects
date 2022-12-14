# custom filter added to flask jinja
from app_website import app
from app_website.models import Task

# check how mnay task are undone !
@app.template_filter('unchecked_count')
def unchecked_count_filter(tasks: list[Task]) -> int:
    """
    this function checks a list of task and returns the number of task
    that are marked as undone / unchecked in the database
    """
    count = 0
    for task in tasks:
        if not task.done:
            count += 1

    return count 