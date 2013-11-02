import md5

__author__ = 'akshay'


class SessionService:
    def generateSessionId(self, user_email_id):
        hashString = 'MW' + user_email_id
        return md5.new(hashString).hexdigest()

    def authenticateUser(self, sessionId, user_email_id):
        hashString = 'MW' + user_email_id
        return sessionId == md5.new(hashString).hexdigest()
