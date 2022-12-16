from pytest import *;
from pyteal import *;
from fairtrade_contract import Stage

def test_smart_contract():
    # Initialize the Stage object
    stage = Stage()
    
    # Test application creation
    txn_args = [b'Title', b'Summary', b'Batch', b'Attachment']
    assert stage.application_creation().run(note = b'fairtrade:uv1', application_args = txn_args) == Approve()
    
    # Test application deletion
    assert stage.application_deletion().run(sender = Global.creator_address()) == True
    
    # Test application start
    assert stage.application_start().run(application_id = 0, application_args = txn_args) == Approve()
    assert stage.application_start().run(on_completion = OnComplete.DeleteApplication, sender = Global.creator_address()) == True
    
    # Test approval program
    assert stage.approval_program().run(application_id = 0, application_args = txn_args) == Approve()
    assert stage.approval_program().run(on_completion = OnComplete.DeleteApplication, sender = Global.creator_address()) == True
    
    # Test clear program
    assert stage.clear_program().run() == 1
