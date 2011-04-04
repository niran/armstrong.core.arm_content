from django.core.exceptions import ObjectDoesNotExist


def generate_author_link(user, html_class=u'author'):
    '''Returns an <a> tag that links to the author's absolute URL.

    The author's full name will be the text of the <a> tag. If the user
    doesn't have a profile or a get_absolute_url method, the author's unlinked
    full name will be returned.'''
    name = user.get_full_name()
    url = ''

    try:
        profile = user.get_profile()
        if hasattr(profile, 'get_absolute_url'):
            url = profile.get_absolute_url()
    except ObjectDoesNotExist:
        pass

    if not url:
        return name
    else:
        return u'<a href="%(url)s" class="%(html_class)s">%(url)s</a>' \
            % locals()
