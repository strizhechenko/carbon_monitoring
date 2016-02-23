env:
	virtualenv env
	bash -c "source env/bin/activate; pip install -r requirements.txt"
lint:
	pylint carbon_monitoring/
clean:
	rm -f *.pyc carbon_monitoring/*.pyc
