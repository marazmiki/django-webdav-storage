project_name=django_webdav_storage

.PHONY: test
test:
	pip install -e .
	python setup.py test
	pip uninstall -y .


.PHONY: release
release:
	python setup.py sdist --format=zip,bztar,gztar register upload
	python setup.py bdist_wheel register upload


.PHONY: flake8
flake8:
	flake8 ${project_name} .


.PHONY: clean
clean:
	python setup.py develop --uninstall
	rm -rf *.egg-info *.egg
	rm -rf htmlcov
	rm -f .coverage
	find . -name "*.pyc" -exec rm -rf {} \;

.PHONY: tox
tox:
	tox
