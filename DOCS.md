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
### Frontend  