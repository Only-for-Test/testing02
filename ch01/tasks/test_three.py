"""Test Task data type"""

from collections import namedtuple

Task = namedtuple( 'Task', ['summary', 'owner', 'done', 'id'] )
Task.__new__.__defaults__ = (None, None, False, None)

def test_defailts():
    """Defaults should be used if parameters not passed"""

    t1 = Task()
    t2 = Task( None, None, False, None )
    assert t1 == t2

def test_member_access():
    """Test property .field namedtuple"""

    t1 = Task( 'Buy milk', 'brian' )
    assert t1.summary == 'Buy milk'
    assert t1.owner == 'brian'
    assert (t1.done, t1.id) == (False, None)

