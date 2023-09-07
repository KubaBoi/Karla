# Karla

- device listen and send sound file to bc
  - bc return text from speech
- device send the text to bc to understanding
  - bc create session and return answer as text and boolean (shouldSpeak)
  - bc also send this answer and shouldSpeak to other connected devices (wip... there will be only one device and shouldSpeak will always be true)
- device show answer as text
- if shouldSpeak == true
  - device send answer as text to be translated into sound file and device play it

