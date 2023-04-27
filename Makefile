venv:
	python3 -m venv venv
	${SHELL} -c ". venv/bin/activate && pip install -r requirements.txt"

clean:
	-rm -r venv
.PHONY: clean

run-server: venv
	. venv/bin/activate && python -m flask --app server/app run
.PHONY: run-server

grade: venv
	. venv/bin/activate && python3 grade.py

