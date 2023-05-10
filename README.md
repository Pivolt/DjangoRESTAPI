# DjangoRESTAPI
 
W celu uruchomienia aplikacji wraz z serwerem danych wymagane jest:
zainstalowanie języka Python w najnowszej stabilnej wersji 
-> https://www.python.org/downloads/
zainstalowanie PostgreSQL
-> https://www.postgresql.org/download/

Gdy mamy już obydwa narzędzia zainstalowane chcemy utworzyć środowisko wirtualne oraz je uruchomić
https://docs.python.org/3/library/venv.html

A następnie zainstalować potrzebne paczki
pip install django
pip install djangorestframework
pip install djangorestframework_simplejwt

Po zainstalowaniu paczek należy skonfigurować plik settings.py
aby działał z naszą bazą danych, w tym celu należy widoczne poniżej pola ustawić zgodnie
z naszą bazą PostgreSQL do której chcemy zapisywać dane.
image.png
Gdzie:
Name -> nazwa naszej bazy danych
User -> nazwa użytkownika do logowania się do bazy
Password -> hasło do logowania się do konta użytkownika
Host -> adres serwera na którym znajduje się nasza baza
Port -> port służący do połączenia się z usługą

Następnie należy w nadrzędnym katalogu RecrutimentAPI wykonać komendy:
python manage.py makemigrations
python magane.py migrate
oraz:
python manage.py runserver

