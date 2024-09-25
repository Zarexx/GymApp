### MVP-LOCAL-GYMSERVER-APPLICATION-DOCUMENTATION
---


---
## Webapplication
### Backend
port: 5000
**api endpoints**
- `/init_ui/<username>`
    Typ: Api endpoint 
    Funktion: liefert daten für die ui

**websocket endpoints**
- ``
    Typ: websocket 
    Funktion: liefert daten für die ui

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