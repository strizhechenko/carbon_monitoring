env:
	virtualenv env
	bash -c "source env/bin/activate; pip install -r requirements.txt"
lint:
	pylint carbon_monitoring/
clean:
	rm -f *.pyc carbon_monitoring/*.pyc
vm:
	yum -y install gcc vim python python-devel python-virtualenv python-pip
metrics:
	bash -c 'source export.sh; git clone $(METRICS_REPO) $(METRICS)'
metrics_update:
	bash -c 'cd $(METRICS); git pull origin master'
