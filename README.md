#PROJECT_NAME:    SaaS_API
#HANDLE: _MUMINUL__ISLAM___


##**A SaaS(Software as A Service) Project**
SaaS_API- Multi-User Team Task Management(Production MVP)
A Prodcution-ready Backend Service for Streamline Task Management for Teams,
Offering User Authentication,Authorization,Team-based Task Assignment and a
Scalable SQLite to PostgreSQL Database Architecture.
**Developed using Python 3.12+,FastAPI,SQLAlchemy,PyJWT,Argon2**
This is a MVP Version, hoping to upgrade with Skin and Update.
This MVP is secure,high-performance and Maintainable Solution for
Task Management in a Team.
Also It used **ES256** for its High Performance and Robust Security.
It is Cloud-Based.It Can be Deployed with Skins, Upgrades and Subcription Model.

**Key Features:**
-User Authentication and Authorization with Cryptography and JSON Web Token.
-ROLE based Access Control.
-Team Management with Supervisor Role.
-Task Management with Create ,Update, Delete Task.
-SQL Database with Migration Facility (**Alembic**).
-Pagination.
-Dockerized Deployment.
-Clean Architecture.
-ES256 for Fast and Strong Security.

**Tech Stack**
-Backend Framework: FastAPI
-Database: SQLite,PostgreSQL,SQLAlchemy
-Authentication: JWT(PyJWT), Argon2, Cryptography
-Testing: Pytest
-Deployment: Docker, Uvicorn(Server)
-Python Version: 3.12+

**Project Version**
-Project_Version: 0.1.0

**API EndPoints**
-Auth: User Registration,Sign-in and Admin Access with JWT Token.
-Teams: CRUD Operations on Teams.
-Tasks: CRUD Operations on Tasks.

This Project For Demonstration of Practice On Building Scalable,Maintainable,Secure API
for Task Management. Ideal for Startup and Small Team Seeking a Fast and Reliable Solution.

[Github](https://github.com/muminul2027/saas_api)


## Table of Contents

-[Installation]
-[Usage]
-[Screenshot]
-[AUTHOR]
-[License]

##Installation

1.Clone the repository
    `git clone github_url`

2.Install Dependency with Pip
    `pip install -r requirements.txt`

##Usage

1.Move Your Working Directory to SaaS_API Folder
    cd to_SaaS_api_folder

2.Run From main.py With
    uvicorn app.main:web_app --reload

3.Run Test With
    python3 -m pytest

3.Use Browser with API
    For Admin Access ,Use this:
    localhost:8000/auth/admin
    
4.Other API Included:
    Method: GET , localhost:8000/auth/admin
    Mehtod: POST, localhost:8000/auth/register
    Method: POST, localhost:8000/auth/login

    Method: POST , localhost:8000/tasks/
    Method: GET , localhost:8000/tasks/?status=&page=
    Method: PUT , localhost:8000/tasks/{id}
    Method: DELETE, localhost:8000/tasks/{id}

    Method: POST, localhost:8000/teams/
    Method: GET, localhost:8000/teams/
    Method: POST, localhost:8000/teams{id}/members

Other CRUD are Not Implemented Yet.

##Screenshot

Not Included Yet.

##AUTHOR

[MUMINUL ISLAM : _MUMINUL__ISLAM___]
Vist Github Page For More Fun Projects

##License

This Project is **Proprietary** and For **Job Evaluation Purpose Only**.
Not to Build to Mimicing any Existing Software Service.
All Codes From Author.
Thank You For Visiting the Code Base.
[Muminul Islam] [2026]

##References

-[GitHub](https://github.com/muminul2027/saas_api)
