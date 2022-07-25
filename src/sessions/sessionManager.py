
import time

from src.sessions.session import Session

class SessionManager:

    sessions = []

    @staticmethod
    def doSession(text, ip):
        session = SessionManager.activeSession(ip)
        if (not session or time.time() - session.lastAction > 30):
            if (session):
                SessionManager.sessions.remove(session)

            session = Session(ip)
            text = session.createSession(text)
            if (text):
                SessionManager.sessions.append(session)
                return "What do you need"
            return ""
            
        if (session.command == None):
            if (text.startswith("nothing")):
                SessionManager.sessions.remove(session)
                return "I am ending this session"
            text = session.findCommand(text)
            if (not text):
                return "I did not catch that"

        ret = session.doCommand(text)

        if (session.isDone()):
            SessionManager.sessions.remove(session)
        return ret

    @staticmethod
    def activeSession(ip):
        for session in SessionManager.sessions:
            if (session.ip == ip):
                return session
        return False
        