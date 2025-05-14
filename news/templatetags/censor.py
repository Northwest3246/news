from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value, bad_words="плохое,злой,недобро"):
    bad_list = [word.strip() for word in bad_words.split(',')]
    result = value
    for word in bad_list:
        result = result.replace(word, '*' * len(word))
    return result