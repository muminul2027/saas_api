#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___

from setuptools import setup,find_packages

setup(
    name="SaaS_API",
    version="0.1.0",
    package=find_packages(),
    install_requires=[
        'python>=3.12',
        'argon2-cffi>=25.1.0',
        'cryptography>=46.0.5',
        'fastapi>=0.129.0',
        'psycopg2-binary>=2.9.11',
        'pyjwt>=2.11.0',
        'sqlalchemy>=2.0.46',
        'uvicorn>=0.41.0',
    ],
    description="A SaaS for Multi User/Team Task Management",
    author="MUMINUL ISLAM",
    author_email="contact over github",
    url="github.com/",
    classifiers=[
        'Programming Language :: Python ::3',
        'Operating System :: OS Independent',
        'HANDLE :: _MUMINUL__ISLAM___',
    ],
)