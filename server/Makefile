run:
	fastapi dev main.py

unicorn:
	uvicorn monitor_app.main:app --reload

install:
	pip3 install fastapi[standard] sqlalchemy
