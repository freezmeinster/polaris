run:
	@python manage.py runserver
initdev:
	@rm -f *.sqlite3
	@python manage.py migrate
	@python manage.py createsuperuser --username admin --no-input --email admin@admin.com 
	@echo "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.set_password('admin'); user.save()" | python manage.py shell
