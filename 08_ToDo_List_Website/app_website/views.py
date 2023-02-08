from app_website import app
from app_website.custom_decorators import user_logged_or_redirect
from app_website.forms import ListForm, TaskCreateForm, TaskEditForm
from app_website.models import db, Task, ToDoList
from datetime import datetime
from flask import (
    abort, 
    flash, 
    jsonify, 
    render_template, 
    redirect, 
    Response,
    url_for, 
    )
from flask_login import current_user, login_required


# current year - global variable
# current year
current_year = datetime.now().strftime("%Y")

# Flask routes
# home website
@app.route("/")
def index() -> str:
    """
    the index - home - view
    """
    return render_template(
        'index.html',
        current_year = current_year, 
    )

# mylist website
@app.route("/mylists")
@user_logged_or_redirect(redirect_url='login')
def mylists() -> str:
    """
    my lists website view
    """
    return render_template(
        'mylists.html',
        current_year = current_year, 
    )


# create list
@app.route("/createlist", methods = ['GET','POST'])
@login_required
def create_list() -> str:
    """
    create list view
    """
    
    list_form = ListForm()
    
    # if form is validated then it has to be a POST request
    if list_form.validate_on_submit():

        # creating the list in the database
        
        new_list = ToDoList(
            title = list_form.title.data.strip(),
            date_created = datetime.now().strftime("%d/%m/%Y"),
            list_creator = current_user,
        )

        # saving the new user in the database
        db.session.add(new_list)
        db.session.commit()

        # flash message for one session
        flash(f"A new ToDo list was created ({new_list.title}).")

        # after adding a list redirecting to mylists view page 
        return redirect(url_for('mylists'))

    return render_template(
        'create_list.html',
        current_year = current_year,
        form = list_form,
    )


# edit list
@app.route("/editlist/<int:list_id>", methods = ['GET','POST'])
@login_required
def edit_list(list_id: int) -> str:
    """
    Edit a list view
    """
    # checking if a list with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_todolist = db.get_or_404(ToDoList, list_id)

    # checking if the list with the given id was created by the current user
    # and if not raise a 401 - error - Unauthorized
    if not selected_todolist.list_creator_id == current_user.id:
        return abort(401)

    # create form with pre filled data from the database
    list_form = ListForm(
        obj=selected_todolist
        )

    # if form is validated then it has to be a POST request
    if list_form.validate_on_submit():

        # updating the value of the title
        selected_todolist.title = list_form.title.data.strip()
        # saving the data in the database
        db.session.commit()

        # flash message for one session
        flash(f"The ToDo list was updated with '{selected_todolist.title}'.")

        # after updating a list redirecting to mylists view page 
        return redirect(url_for('mylists'))

    return render_template(
        'create_list.html',
        current_year = current_year,
        form = list_form, 
    )

# delete list
@app.route("/deletelist/<int:list_id>")
@login_required
def delete_list(list_id: int) -> str:
    """
    deleting a list view
    """
    # checking if a list with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_todolist = db.get_or_404(ToDoList, list_id)

    # checking if the list with the given id was created by the current user
    # and if not raise a 401 - error - Unauthorized
    if not selected_todolist.list_creator_id == current_user.id:
        return abort(401)

    # deleting the list from the database
    db.session.delete(selected_todolist)
    db.session.commit()

    # flash message for one session
    flash(f"The ToDo list '{selected_todolist.title}' was deleted.")

    # after deleting a list redirecting to mylists view page 
    return redirect(url_for('mylists'))


# detail list
@app.route("/detaillist/list-<int:list_id>", methods = ['GET','POST'])
@login_required
def detail_list(list_id: int) -> str:
    """
    detail list view page
    """
    # checking if a list with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_todolist = db.get_or_404(ToDoList, list_id)

    # checking if the list with the given id was created by the current user
    # and if not raise a 401 - error - Unauthorized
    if not selected_todolist.list_creator_id == current_user.id:
        return abort(401)

    # create a task create form
    task_form = TaskCreateForm()

    # if form is validated then it has to be a POST request
    if task_form.validate_on_submit():
        
        # if title is not empty than add it to database
        if (new_taks_name := task_form.task_name.data.strip()):

            # adding the task to the database
            new_task = Task(
                task_name = new_taks_name,
                tasks_todo_list = selected_todolist,
            )

            # saving the data in the database
            db.session.add(new_task)
            db.session.commit()

            # flash message for one session
            flash(f"A new task to '{selected_todolist.title}' was added.")

            # refresh website - back to detail list view
            return redirect(url_for('detail_list', list_id=selected_todolist.id))

    return render_template(
        'detail_list.html',
        current_year = current_year,
        current_list = selected_todolist,
        form = task_form, 
    )


# delete task
@app.route("/deletetask/list-<int:list_id>/task-<int:task_id>")
@login_required
def delete_task(list_id: int, task_id: int) -> str:
    """
    delete a task view
    """
    # checking if a list with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_todolist = db.get_or_404(ToDoList, list_id)

    # checking if the list with the given id was created by the current user
    # and if not raise a 401 - error - Unauthorized
    if not selected_todolist.list_creator_id == current_user.id:
        return abort(401)

    # checking if a task with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_task = db.get_or_404(Task, task_id)

    # checking if the given task belongs to the given list
    if not selected_task.todo_list_id == selected_todolist.id:
        return abort(401)

    # deleting the task from the database
    db.session.delete(selected_task)
    db.session.commit()

    # flash message for one session
    flash(f"Task '{selected_task.task_name}' was deleted.")

    # refresh website - back to detail list view
    return redirect(url_for('detail_list', list_id=selected_todolist.id))


# edit task
@app.route("/edittask/list-<int:list_id>/task-<int:task_id>", methods = ['GET','POST'])
@login_required
def edit_task(list_id: int, task_id: int) -> str:
    """
    edit a task view
    """
    # checking if a list with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_todolist = db.get_or_404(ToDoList, list_id)

    # checking if the list with the given id was created by the current user
    # and if not raise a 401 - error - Unauthorized
    if not selected_todolist.list_creator_id == current_user.id:
        return abort(401)

    # checking if a task with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_task = db.get_or_404(Task, task_id)

    # checking if the given task belongs to the given list
    if not selected_task.todo_list_id == selected_todolist.id:
        return abort(401)

    # variable to prepopulate the date time object in the form
    predefined_date = None
    if selected_task.due_date != 'No due date':
        predefined_date = datetime.strptime(selected_task.due_date, '%Y-%m-%d')

    # creating form for the task
    form_edit_task = TaskEditForm(
        color_tag = selected_task.color_tag,
        done = selected_task.done,
        due_date = predefined_date,
        stared = selected_task.stared,
        task_name = selected_task.task_name,
    )

    # if form is validated then it has to be a POST request
    if form_edit_task.validate_on_submit():

        # updating the database
        selected_task.done = form_edit_task.done.data
        selected_task.color_tag = form_edit_task.color_tag.data

        if form_edit_task.due_date.data:
            selected_task.due_date = form_edit_task.due_date.data 
        else:
            selected_task.due_date = "No due date"

        # selected_task.due_date = "No due date"
        selected_task.stared = form_edit_task.stared.data
        selected_task.task_name = form_edit_task.task_name.data

        db.session.commit()

        # flash message for one session
        flash(f"Task '{selected_task.task_name}' was updated.")

        # refresh website - back to detail list view
        return redirect(url_for('detail_list', list_id=selected_todolist.id))


    return render_template(
    'edit_task.html',
    current_year = current_year,
    current_task = selected_task,
    current_list = selected_todolist,
    form = form_edit_task, 
    )


# marking a task as checked
# edit task
@app.route("/task/check/list-<int:list_id>/task-<int:task_id>", methods = ['PATCH'])
@login_required
def check_the_task(list_id: int, task_id: int) -> Response | str:
    """
    editing status done view - only for patch request
    returns a json respond with a redirect url and the status code of the htttp request.
    """
    # checking if a list with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_todolist = db.get_or_404(ToDoList, list_id)

    # checking if the list with the given id was created by the current user
    # and if not raise a 401 - error - Unauthorized
    if not selected_todolist.list_creator_id == current_user.id:
        return abort(401)

    # checking if a task with the given id exists !
    # Fetch the first row or raise a 404 error if it dosent exists.
    selected_task = db.get_or_404(Task, task_id)

    # checking if the given task belongs to the given list
    if not selected_task.todo_list_id == selected_todolist.id:
        return abort(401)


    # updating value in the databse - done
    selected_task.done = 1
    db.session.commit()


    return jsonify(
        url_redirect = url_for('detail_list', list_id=selected_todolist.id),
    ), 200