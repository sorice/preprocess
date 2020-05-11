#https://www.researchgate.net/post/What_is_the_best_technique_to_detect_abbreviations_in_a_text
#
# First Approach
# --------------
#
# James Dominic O'Shea
# Manchester Metropolitan University
# I have developed a "brute force" approach for a similar problem I had
# with recognising what is someone's actual name in a text string. You
# could use a similar (divide and conquer" scheme. First, you could use
# a list of the most frequently occuring cases of positive cases
# (abreviations / acronyms). Second you could use a list of most
# frequently occurring words in the english language to rule out
# negative cases. This will leave a set of uncertain wrods which have
# lower frequency of occurrence to deal with. At this point I would
# investigate using an n-gram based classifier (e.g. trigrams or
# quadragrams of letters) trained on the two high frequency sets.
#
# Whatever approach you took, I would work by winnowing down the
# unknown cases in successive stages.
#
# You need to take account of misclassification - misses and false
# alarms which may occur either because an acronym is actually a real a
# real word e.g. Fuzzy Algorithm for Similarity Testing (FAST) or
# because a real word is so obscure it looks like an  abbreviation e.g.
# syzygy - an alignment of three celestial objects.
#
# Whatever apporach you take it sounds like it's going to be fun.!

# Second approach
# ---------------
#
# Tiago A. Almeida
# Universidade Federal de São Carlos
# We have designed a framework to normalize and expand noise and short
# text messages, such as SMS, tweets, etc. Basically, the most common
# slangs, typos, symbols and abbreviations are detected and replaced
# for their standard english words. You can also enrich the text sample
# by inserting concepts semantically related with the message context.
#
# We have proved that such preprocessing can greatly improve the
# classification and clustering performances.
#
# The TextExpansion tool is open-source and publicly available at
# http://lasid.sor.ufscar.br/expansion/
#
# Moreover, you can find other uselful machine learning tools available
# at http://lasid.sor.ufscar.br/ml-tools/