def hyphenation(text :str, collocations :list) -> str:
    """Made originally to underscored the collocations in the original text
    The recursive looking for collocations allow to find important 
    expressions that define topic (of course there are better techniques
    to do this, using Deep Learning and more complex techniques.)

    Once the collocations are hyphenated these turns into single words
    and are not mixed with the rest. For example, if you hypenate de 
    collocation: [natural,language] as "natural_language" will be more 
    informative in a Luhn term evaluation than just using "natural" and
    "language" separately.

    Parameters
    ----------
    text: str
          normalized text

    collocations: tuple list
                  List of collocations

    Return
    ------
    text: str
          same text with all collocations hyphenated with underscore char

    """
    for tuple in collocations:
        expression = ''
        replacement = ''
        for word in tuple:
            expression += ' ' + word
            replacement += '_' + word
        expression = expression.strip()
        replacement = replacement[1:]

        text = text.replace(expression,replacement)
    return text
