# Karla

- zarizeni nahraje zvuk
- posle zvuk na preklad
- zarizeni si zaktualizuje event, protoze:
  - backend zpracoval zvuk, prelozil ho a vytvoril event s now() a textem co ma byt recen
  - potom se pokracuje na [Jakmile se ma event provest](#jakmile-se-ma-event-provest)
  - zaroven vytvoril i session, pokud byla potreba

## Aktualizace eventu v zarizeni

- zarizeni se periodicky bude dotazovat, jestli je jeho event aktualni
- v pripade hodinek se dotaz bude posilat vzdy po:
  - poslani hlasu
  - provedeni eventu
  - probuzeni ??

## Event

- aktualni event je prvni pokud jsou razeny podle activation_time vzestupne
  - event neni hotov, dokud jedno ze zarizeni neda vedet, ze event provedlo
    - potom [Aktualizace eventu](#aktualizace-eventu)
- pokud je event v minulosti, jeho activateIn = 0
- kazde zarizeni bude mit jedinecnou priority (napr:)
  - 0 pocitac
  - 1 hodinky
  - 2 mobil

## Jakmile se ma event provest
  
- vsechna zarizeni (ktera mohou = jsou zapnuta) 
  - zobrazi text + vibrace
  - requesty (pravidelne) s vlastnim device_id a event_id
- pokud backendu prijde request s device_id a event_id
  - pokud event_id != aktualni_event_id
    - vraci se aktualni event_id
  - pocet vterin od zacatku eventu // DEVICE_TIME_DELAY=5 >= device_id.priority 
    - event je hotov, provadi se [Aktualizace eventu](#aktualizace-eventu)
    - vraci se aktualni event_id a HTTP status 201
      - v tuhle chvili dane device promluvi
  - else
    - vraci se stejne event_id, jake bylo v requestu

## Aktualizace eventu
  
- prenastavi se jeho cas/smaze se, podle typu

## Session

- kazdy account muze mit jenom jednu session
- faze dotazu (return v tomhle pripade znamena vytvoreni eventu now() s textem)
  - "hey karla" (account nema zadnou session)
    - zalozi se session kde 
      - session.command = null
      - session.faze = 0
      - session.account_id = ...
    - return - "what do you need"
  - pokud session.command == null
    - command starter + ending - "set timer for & minutes"
      - pokud odpovida nejakemu commandu, tak 
        - session.command = command_name
      - jinak return - "I did not understand"
        - session se maze
  - dokud session.faze < command.fazeCount
    - provola se command
    - jinak se session maze
    
## Command

- command je python script s rozhranim:
  - --account account.id
  - --faze faze commandu
  - --data rozpoznany text 
    - pri faze==0 se ocekavaji data vyparsovane z regexu, jinak se regex provadi az ve scriptu
  - --port port aplikace
- command s aplikaci komunikuje pres http provolavanim endpointu na vytvoreni eventu (mluveni)
- zaroven je to zaznam v tabulce command
  - fazeCount - pocet fazi
  - command - jmeno python scriptu (PK)
  - starters - text array (regex)
  - endings - text array (regex)
    - starters a endings se spoji dohromady a porovnaji se s mluvenym textem (to provadi aplikace)
    - potom (protoze je to prvni faze) se vlozi vyparsovana data
    
