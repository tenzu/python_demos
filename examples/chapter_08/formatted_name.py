def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name.title() + ' ' + middle_name.title(
        ) + ' ' + last_name.upper()
    else:
        full_name = first_name.title() + ' ' + last_name.upper()
    # return full_name.title()
    return full_name


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
