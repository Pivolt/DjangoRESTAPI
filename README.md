# DjangoRESTAPI
 
W celu uruchomienia aplikacji wraz z serwerem danych wymagane jest:<br/>
zainstalowanie języka Python w najnowszej stabilnej wersji <br/>
-> https://www.python.org/downloads/<br/>
zainstalowanie PostgreSQL<br/>
-> https://www.postgresql.org/download/<br/>

Gdy mamy już obydwa narzędzia zainstalowane chcemy utworzyć środowisko wirtualne oraz je uruchomić<br/>
https://docs.python.org/3/library/venv.html<br/>

A następnie zainstalować potrzebne paczki<br/>
pip install django<br/>
pip install djangorestframework<br/>
pip install djangorestframework_simplejwt<br/>

Po zainstalowaniu paczek należy skonfigurować plik settings.py<br/>
aby działał z naszą bazą danych, w tym celu należy widoczne poniżej pola ustawić zgodnie<br/>
z naszą bazą PostgreSQL do której chcemy zapisywać dane.<br/>
![obraz](https://github.com/Pivolt/DjangoRESTAPI/assets/131452769/f15d3659-f5ed-4332-8314-5fe66a32379a)<br/>
Gdzie:<br/>
Name -> nazwa naszej bazy danych<br/>
User -> nazwa użytkownika do logowania się do bazy<br/>
Password -> hasło do logowania się do konta użytkownika<br/>
Host -> adres serwera na którym znajduje się nasza baza<br/>
Port -> port służący do połączenia się z usługą<br/>

Następnie należy w nadrzędnym katalogu RecrutimentAPI wykonać komendy:<br/>
python manage.py makemigrations<br/>
python magane.py migrate<br/>
oraz:<br/>
python manage.py runserver<br/>

