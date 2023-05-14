"""Test the tasks.add() API function."""

import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer."""

    # GIVEN a new task is added
    # WHEN a new task is added
    # THEN returned task_id is of time int
    new_task = Task( 'do something' )
    task_id = tasks.add( new_task )
    
    assert isinstance( task_id, int )

    
@pytest.mark.smoke
def test_added_task_has_id_set():
    """Make sure the task_id field is set by tasks.add()."""

    # GIVEN an initialized task db
    #  AND a new task is added
    new_task = Task( 'sit a chair', owner = 'me', done = True )
    task_id = tasks.add( new_task )

    # WHEN task is retrieved
    task_from_db = tasks.get( task_id )

    # THEN task_id matches id field
    assert task_from_db.id == task_id

@pytest.fixture( autouse=True )
def initialized_task_db( tmpdir ):
    """Connect to db before testing, disconnect after."""

    # Setup : start db
    tasks.start_tasks_db( str( tmpdir), 'tiny' )

    yield

    # Teardown : stop db
    tasks.stop_tasks_db()