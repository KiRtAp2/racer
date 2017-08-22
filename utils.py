import settings


def supported(version):
    mvmajor, mvminor = version.split('.')
    vmajor, vminor = settings.map_version.split('.')

    if vmajor > mvmajor:
        return False
    else:
        if vminor > mvminor:
            return False
    return True
