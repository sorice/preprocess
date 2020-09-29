from .normalize import replace_urls
from .normalize import replace_symbols
from .normalize import replace_dot_sequence
from .normalize import multipart_words
from .abbreviation import expand_abbrevs
from .abbreviation import normalize_abbrevs
from .normalize import expand_contractions
from .normalize import replace_punctuation
from .normalize import lowercase
from .normalize import extraspace_for_endingpoints
from .normalize import add_doc_ending_point
from .normalize import del_tokens_len_one
from .hyphen import hyphenation
from .normalize import del_digits

TECHNIQUES = {
    'lowercase':lowercase,
    'replace_urls':replace_urls,
    'replace_symbols':replace_symbols,
    'replace_dot_sequence':replace_dot_sequence,
    'multipart_words':multipart_words,
    'expand_abbrevs':expand_abbrevs,
    'normalize_abbrevs':normalize_abbrevs,
    'expand_contractions':expand_contractions,
    'replace_punctuation':replace_punctuation,
    'extraspace_for_endingpoints':extraspace_for_endingpoints,
    'add_doc_ending_point':add_doc_ending_point,
    'del_tokens_len_one':del_tokens_len_one,
    'hyphenation':hyphenation,
    'del_digits':del_digits,
    }

# append all verified techniques in module importing argument ALL
__all__ = []
__techniques__ = {}

for technique in TECHNIQUES:
	__all__.append(technique)
	__techniques__[technique] = TECHNIQUES[technique]