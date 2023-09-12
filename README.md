# Karla

- device listen and send sound file to bc
  - bc return text from speech
- device send the text to bc to understanding
  - bc create session and return answer as text and boolean (shouldSpeak)
  - bc also send this answer and shouldSpeak to other connected devices (wip... there will be only one device and shouldSpeak will always be true)
- device show answer as text
- if shouldSpeak == true
  - device send answer as text to be translated into sound file and device play it

- zarizeni se periodicky bude dotazovat pomoci event_id, jestli je jeho next event aktualni
  - bc posle jeden bajt 
  - pokud neni aktualni, tak zaktualizuje

- aktualni event je prvni pokud jsou razeny podle activation_time vzestupne
- event neni hotov, dokud jedno ze zarizeni neda vedet, ze event provedlo
  - potom aktualizace eventu
- kazde zarizeni bude mit jedinecnou priority (napr:)
  - 0 pocitac
  - 1 hodinky
  - 2 mobil

- jakmile se ma event provest
  - vsechna zarizeni (ktera mohou = jsou zapnuta) 
    - zobrazi text + vibrace
    - requesty (pravidelne) s vlastnim device_id a event_id
  - pokud backendu prijde request s device_id a event_id
    - pokud event_id != aktualni_event_id
      - vraci se aktualni event_id
    - pocet vterin od zacatku eventu // DEVICE_TIME_DELAY=5 >= device_id.priority 
      - event je hotov, provadi se aktualizace eventu
      - vraci se aktualni event_id
        - v tuhle chvili dane device promluvi
    - else
      - vraci se stejne event_id, jake bylo v requestu

- aktualizace eventu
  - prenastavi se jeho cas/smaze se, podle typu
