
# eMenu
Cloud Services - Zadanie rekrutacyjne

Zadanie zostało przygotowane do uruchemiania za pomocą [Dockera](www.docker.com).

## Instrukcja uruchomienia:
1.  Zaktualizowanie zmiennym środowiskowych w pliku `.env`
2.  Zbudowanie obrazów i uruchomienie kontenerów:
		```docker-compose up --build -d```
3.  Inicjalizacja danych:
		```docker-compose exec web python manage.py loaddata init_data```
4. Stworzenie superusera
		```docker-compose exec web python manage.py createsuperuser```
5. Aplikacja powinna działać na: [htttp://localhost:1337](htttp://localhost:1337).
	Swagger: [http://localhost:1337/api/schema/swagger-ui/](http://localhost:1337/api/schema/swagger-ui/).

## Testowanie:
1. Uruchomienie testów:
		```docker-compose exec web coverage run --source='.' manage.py test```
2. Raport pokrycia:
		```docker-compose exec web coverage report```
3. Raport w formie html:
		```docker-compose exec web coverage html```
		```docker-compose cp web:/usr/src/app/htmlcov/ <sciezka_na_hoscie>```
	
	
