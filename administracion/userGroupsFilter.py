def isClient(user):
    return user.groups.filter(name='Cliente').exists()

def isAdmin(user):
    return user.groups.filter(name='Admin').exists()

def isMozo(user):
    return user.groups.filter(name='Mozo').exists()