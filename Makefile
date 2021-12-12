.PHONY: dev
dev:
	cd example_project && poetry run ./manage.py runserver


.PHONY: release
release:
	poetry build
	poetry publish


.PHONY: push
push:
	git push origin master --tags


.PHONY: patch-version
patch-version:
	echo "Making a patch release"
	poetry bump2version patch


.PHONY: minor-version
minor-version:
	echo "Making a minor release"
	poetry run bump2version minor
