### MVP-LOCAL-GYMSERVER-APPLICATION-DOCUMENTATION
---


## Serverapplication
port: 5001
**server endpoints**
- `/init_thread/<ip>`
    Typ: Api endpoint 
    Funktion: Baut websocket verbindung mit Client auf 
- 



---
## Webapplication
### Backend
port: 5000
**server endpoints**
- `/init_ui/<username>`
    Typ: Api endpoint 
    Funktion: liefert daten für die ui
- `/req_thread/<username>`
    Typ: Api endpoint
    Funktion:anfrage an serverapp zum start des ExerciseScannerThread

**DB-Format**
- ``User+id``
  - ``base_data``
    - id -> 'int'
    - full_name -> 'string'
    - pp -> 'url'
  - ``trainingsplan``
    - ``base_data``
      - start_date -> string, 'DD-MM-YYYY'
      - trainer -> string, 'FName_LName'
      - ziele -> list, ['G1','G2']
    - ``uebungen``
      - uebung+id
        - geraete_nummer -> int
        - saetze -> int
        - wiederholungen -> string, "xx-yy, xx-yy, xx-yy, ..."

### Frontend  