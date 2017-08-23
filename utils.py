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

def show_text(text: str, font, position: tuple, color: tuple, window):
    text_field = font.render(text, True, color)
    window.blit(text_field, position)
