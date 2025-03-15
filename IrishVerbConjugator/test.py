import re

def isIrregular(inputVerb: str) -> bool:
  # checks to see if the input verb stem is an irregular
  # or regular verb. Irish only has 11 irregular verbs
  # so this function compares the verb root that is input
  # with a list of irregular verb roots
  irregular_verbs = {"abair", "beir", "bí", "clois", "déan", "ith", "faigh", "feic", "tabhair", "tar", "téigh"}
  return inputVerb in irregular_verbs
  


def determineVerbConjugation(stem: str) -> str:
  #determines to which conjugation a regular verb stem belongs
    # Check for one-syllable words
    if len(re.findall(r'[aeiouáéíóú]+', stem)) == 1:
        return "First Conjugation"
    
    # Check for words ending in -áil
    if stem.endswith("áil"):
        return "First Conjugation"
    
    # Check for words ending in -áin, -óil, or -úir
    if stem.endswith(("áin", "óil", "úir")):
        return "First Conjugation"
    
    # If none of the above conditions are met, it's Second Conjugation
    return "Second Conjugation"