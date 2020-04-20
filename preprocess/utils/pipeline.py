from collections import OrderedDict
from preprocess import basic, shallow

def pipeline(text: str,flow=None) -> str:
    """An easier function that allows to make a full Pipeline
    with the subprocess that users wants. Read the restriction-
    matrix to see what sequences of subprocess are imppossible.

    Parameters
    ----------
    text: string to parse, generally a sentence.

    steps: string list with the ordered sequence of subprocesses to
        apply.

    Returns
    -------

    parsed result : string output
                    Initial text preprocessed with techniques def
                    in the pipeline.
    """
    #TODO: make a matrix to restrict impossible sequences.
    
    steps = OrderedDict()
    bad_steps = []

    DEFAULT_FLOW = ['replace_urls','abbreviations','expand_contractions']

    #If flow is not defined do the default flow.
    if flow is None:
        print('Runing default pipeline')
        return pipeline(text,DEFAULT_FLOW)

    #If flow is defined check the functions
    for step in flow:
        if step in basic.__techniques__:
            steps[step]=basic.__techniques__[step]
        elif step in shallow.__techniques__:
            steps[step]=shallow.__techniques__[step]
        else:
            bad_steps.append(step)
            print("the %s technique could not be found" % step)

    #TODO:Check if the order is possible in the matrix of possible
    #sequences

    #Apply correct functions
    for step in steps:
        try:
            text = steps[step](text)
        except:
            print("%s technique can be concatenated" % step)
            return False
    
    return text
