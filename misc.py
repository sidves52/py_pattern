def say(msg, voice=None, rate=None):
    import os
    s = ['say']
    if voice:
        s.append('-v')
        s.append('"' + voice + '"')
    if rate:
        s.append('-r')
        s.append(str(rate))
    s.append('"' + msg + '"')
    # print(s)
    cmd = ' '.join(s)
    # print(cmd)
    os.system(cmd)

def p(msg):
    print(msg)

