.PHONY: dev
dev:
	cd example_project && poetry run ./manage.py runserver

.PHONY: check
check:
	./setup.py sdist bdist_wheel
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: release
release:
	make check
	twine upload dist/*

.PHONY: push
push:
	git push origin master --tags


.PHONY: patch
patch:
	echo "Making a patch release"
	poetry bump2version patch


.PHONY: minor
minor:
	echo "Making a minor release"
	poetry run bump2version minor
