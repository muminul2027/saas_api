#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___

#CODE SECTION->
#PyTest with HTTPx

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import web_app
from app.db.database_session import get_db
from app.models.base_table import Base
from app.models import user_model,team_model,task_model


#Test Database URL
test_database="sqlite:///./tests/test_database.db"

#Make Engine for Connection
engine=create_engine(test_database)

#Create Session to Connect
SessionThread=sessionmaker(autocommit=False,bind=engine)

#Fake Database-Dependency Override
def override_get_db():
    fake_db=SessionThread()
    try:
        yield fake_db
    finally:
        fake_db.close()

#Now Replace get_db dependency with fake
web_app.dependency_overrides[get_db]=override_get_db

#Setup and Tear Down the Database
@pytest.fixture(scope="module")
def setup_db():
    Base.metadata.create_all(bind=engine) #Set-up Table
    yield
    Base.metadata.drop_all(bind=engine) #Tear-down Table

#Setup a Fake Client
@pytest.fixture(scope="module")
def client_setup():
    with TestClient(web_app) as test_client:
        yield test_client



#START THE TEST
#############################################################################


#TEST CASE 1: Login as Admin
def test_login_admin(setup_db,client_setup):
    response_is=client_setup.get('/auth/admin')
    assert response_is.status_code==200
    print(response_is.json())


#TEST CASE 2: Register as Member
def test_register_member(setup_db,client_setup):
    response_is=client_setup.post('/auth/register',json={"userID":100,
                                                        "userPass":"0000",
                                                        })
    assert response_is.status_code==200
    print(response_is.json())

    response_is=client_setup.post('/auth/register',json={"userID":101,
                                                         "userPass":"0000"})
    assert response_is.status_code==200
    print(response_is.json())


#TEST CASE 3: Login as Member
def test_member_login(setup_db,client_setup):
    response_is=client_setup.post('/auth/login',json={"userID":100,
                                                    "userPass":"0000"})
    assert response_is.status_code==200
    print(response_is.json())

'''
#Make Admin As Fixture
@pytest.fixture(scope="module")
def act_as_admin(setup_db,client_setup):
    response_is=client_setup.get('/auth/admin')
    assert response_is.status_code==200
    return client_setup
'''
#TEST CASE 4: Make Admin Log In Again
def test_login_admin_again(setup_db,client_setup):
    response_is=client_setup.get('/auth/admin')
    assert response_is.status_code==200
    print(response_is.json())

#TEST CASE 5: Add Team
def test_add_team(setup_db,client_setup):
    response_is=client_setup.post('/teams/',json={"teamID":2000,
                                                  "teamName":"test_team",
                                                  "teamOwnerID":100})
    assert response_is.status_code==200
    print(response_is.json())


#TEST CASE 6: View Team
def test_view_team(setup_db,client_setup):
    response_is=client_setup.get('/teams/')
    assert response_is.status_code==200
    print(response_is.json())


#TEST CASE 7: Add Member to Team
def test_add_member_to_team(setup_db,client_setup):
    response_is=client_setup.post('/teams/2000/101') #teamID/memberID
    assert response_is.status_code==200
    print(response_is.json())


#TEST CASE 8: Add Task
def test_add_task(setup_db,client_setup):
    response_is=client_setup.post('/tasks/',json={"task_id":10,
                                                  "task_title":"test_task",
                                                  "task_description":"task_description_here",
                                                  "task_status":"waiting",
                                                  "task_priority":"low",
                                                  "task_due":"2026-04-04",
                                                  "task_user":101,
                                                  "task_team":2000 })
    assert response_is.status_code==200
    print(response_is.json())



#TEST CASE 9: View Task
def test_view_task(setup_db,client_setup):
    response_is=client_setup.get('/tasks/2000/?status=waiting&page=1')
    assert response_is.status_code==200
    print(response_is.json())


#TEST CASE 10: Change Task Status
def test_change_task_status(setup_db,client_setup):
    response_is=client_setup.put('/tasks/10',json={"task_status":"ongoing"})
    assert response_is.status_code==200
    print(response_is.json())


#TEST CASE 11: Delete Task
def test_delete_task(setup_db,client_setup):
    response_is=client_setup.delete('/tasks/10')
    assert response_is.status_code==200
    print(response_is.json())