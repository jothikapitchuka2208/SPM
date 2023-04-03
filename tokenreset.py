from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def token(rollno,seconds):
    s=Serializer('sdgiuwiuiuhi*',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
