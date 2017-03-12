def say(msg, v=None, r=None):
    import os
    s = ['say']
    if v:
        s.append('-v')
        s.append('"' + v + '"')
    if r:
        s.append('-r')
        s.append(str(r))
    s.append('"' + msg + '"')
    # print(s)
    cmd = ' '.join(s)
    # print(cmd)
    os.system(cmd)

def p(msg):
    print(msg)

