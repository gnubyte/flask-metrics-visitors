from setuptools import setup, find_packages

setup(
    name="flask-metrics-visitors-demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask==2.0.1",
        "Flask-Login==0.5.0",
        "Flask-SQLAlchemy==2.5.1",
        "geopy==2.2.0",
        "user-agents==2.2.0",
        "requests==2.26.0",
        "Werkzeug==2.0.1",
        "SQLAlchemy==1.4.23",
    ],
) 