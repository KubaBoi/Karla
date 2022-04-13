
from python.sessions.session import Session

class SessionManager:

    sessions = []

    @staticmethod
    def doSession(text, pindex):
        if (pindex == -1):
            session = Session()
            text = session.createSession(text)
            if (not text):
                return "I did not catch that", False, -1
            
            pindex = len(SessionManager.sessions)
            session.index = pindex
            SessionManager.sessions.append(session)

        for ses in SessionManager.sessions:
            if (ses.index == pindex):
                ret = ses.doCommand(text)

                if (ses.isDone()):
                    SessionManager.sessions.remove(ses)
                    return ret, True, pindex
                return ret, False, pindex

        return "I did not catch that", False, pindex
        