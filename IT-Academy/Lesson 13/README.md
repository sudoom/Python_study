Задача 0

Реализовать систему хранения информации о футбольном чемпионате. Информация опирается на следующие основные классы: Team (команда), Player (игрок), Match (матч). Эти классы связаны друг с другом посредством ассоциации.

Атрибуты классов

Team

id — уникальный численный идентификатор.
name — имя.
players — игроки, играющие за данную команду в рамках чемпионата.

Player

id — уникальный численный идентификатор.
name — имя
team – команда.

Match

id — уникальный численный идентификатор.
date — дата.
location — место.
result — счёт.
team1 — первая команда.
team2 — вторая команда.
players – игроки, участвовавшие в матче.

Реализовать возможность сохранения записей в файл, а также возможность поиска информации о матчах в указанные даты (предусмотреть возможность поиска по временному периоду) с выводом информации по командам и игрокам, участвовавшим в матчах.
