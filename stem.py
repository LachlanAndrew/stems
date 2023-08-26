#!/usr/bin/python

import pdb
from known_errs import *

known_errs.update (deliberate_misspellings)

suffixes = {
  'bility': [('ble', 2)],
  'a': [('on', 4)],
  'abad': [('', 3)],
  'able': [('', 2), ('e', 3)],
  'ae': [('a', 2)],
  'age': [('e', 2), ('', 2)],
  'al': [('e', 2), ('', 2)],
  'an': [('a', 4)],
  'ance': [('e', 2), ('', 2)],
  'ant': [('', 2), ('e', 2)],
  'ar': [('a', 4), ('', 3)],
  'ary': [('e', 2), ('', 2)],
  'ate': [('', 4), ('e', 3)],
  'ation': [('e', 2), ('', 2), ('al', 3)],
  'ator': [('ate', 3)],
  'atory': [('ate', 2), ('e', 4)],
  'bly': [('ble', 2)],
  'bound': [('', 2)],
  'ce': [('t', 2)],
  'children': [('child', 2)],
  'ction': [('xion', 2), ('x', 2)],
  'cy': [('ce', 2), ('te', 2), ('t', 2)],
  'd': [('', 2, 'd')],
  'dom': [('', 3)],
  'ean': [('ea', 2)],
  'aux': [('au', 2)],
  'ed': [('e', 2), ('', 2, 'e')],
  'ee': [('er', 3), ('or', 3)],
  'ence': [('end', 2), ('', 2)],
  'ent': [('', 2)],
  'er': [('e', 2), ('', 2), ('ing', 2), ('ee', 4)],
  'ery': [('e', 3)],
  'es': [('e', 2), ('', 2), ('is', 2)],
  'ess': [('', 3)],
  'est': [('', 2), ('e', 2)],
  'eth': [('s', 2)],
  'ette': [('', 3)],
  'faction': [('fy', 2)],
  'fold': [('', 2)],
  'ful': [('', 2)],
  'genic': [('', 2)],
  'gery': [('geon', 2)],
  'girl': [('boy', 2)],
  'gram': [('graph', 2)],
  'graphy': [('graph', 2), ('logy', 2)],
  'hand': [('', 3)],
  'hood': [('', 2)],
  'how': [('', 2)],
  'i': [('us', 3), ('', 3)],
  'ia': [('ium', 2), ('e', 3)],
  'ial': [('e', 2), ('y', 2), ('', 2)],
  'ian': [('ia', 2), ('i', 3), ('', 2), ('y', 3)],
  'iary': [('', 2)],
  'ible': [('', 2), ('e', 3)],
  'ic': [('y', 2), ('ia', 2), ('', 2), ('e', 2), ('i', 2)],
  'ical': [('ics', 2), ('y', 2)],
  'ically': [('ic', 2)],
  'ication': [('y', 2)],
  'ices': [('ix', 3)],
  'icity': [('ic', 2)],
  'ied': [('y', 2)],
  'ier': [('y', 2)],
  'ies': [('y', 2)],
  'iest': [('y', 2)],
  'iful': [('y', 2)],
  'ify': [('y', 2)],
  'ile': [('', 2)],
  'ily': [('y', 2)],
  'iness': [('y', 2)],
  'ing': [('e', 2), ('', 2)],
  'ion': [('e', 2), ('', 2)],
  'ionaire': [('ion', 2)],
  'ious': [('ion', 2)],
  'ise': [('', 2), ('e', 2)],
  'ish': [('', 2), ('e', 2)],
  'ism': [('e', 2), ('', 2), ('ist', 2), ('ite', 2)],
  'ist': [('e', 2), ('y', 2), ('', 2)],
  'ite': [('', 4)],
  'ity': [('ous', 2), ('e', 2), ('', 2)],
  'ive': [('ion', 2), ('e', 2), ('', 2)],
  'ivity': [('ive', 2)],
  'ize': [('', 2)],
  'kind': [('', 2)],
  'less': [('', 2)],
  'let': [('', 4)],
  'like': [('', 2)],
  'lves': [('lf', 2)],
  'ly': [('le', 2), ('', 2)],
  'man': [('', 3)],
  'men': [('man', 2)],
  'ment': [('e', 2), ('', 2)],
  'more': [('', 2)],
  'most': [('', 1)],
  'ness': [('', 2)],
  #'ogen': [('o', 2)],
  'ology': [('', 2), ('on', 2), ('os', 2), ('o', 2), ('ic', 2), ('e', 2), ('y', 2), ('ism', 2), ('us', 2), ('al', 2), ('a', 2), ('olic', 2)],
  'or': [('', 2)],
  'ore': [('ear', 0)],
  'ous': [('e', 2), ('y', 2), ('', 2)],
  'people': [('person', 2)],
  'proof': [('', 2)],
  'r': [('', 2, 'r')],
  's': [('', 2, 's')],
  'saurus': [('saur', 3)],
  'ship': [('', 2)],
  'side': [('', 3)],
  'some': [('', 2)],
  'st': [('', 3), ('e', 3)],
  'stan': [('', 2)],
  'stic': [('sm', 2)],
  'th': [('s', 2)],
  'tial': [('ce', 2)],
  'tic': [('sis', 4), ('', 4)],
  'tion': [('', 2), ('e', 2)],
  'tory': [('', 2), ('e', 3)],
  'trate': [('ter', 2)],
  'tress': [('tor', 2), ('ter', 2)],
  'trix': [('tor', 2)],
  'try': [('ter', 3), ('t', 3)],
  'ular': [('le', 3)],
  'ure': [('', 4)],
  'vert': [('verse', 2)],
  'ves': [('f', 2)],
  'ware': [('', 3)],
  'way': [('', 3)],
  'ways': [('', 3)],
  'wise': [('', 2)],
  'wn': [('w', 1)],
  'woman': [('man', 2)],
  'y': [('', 2), ('e', 3)]
}

# To debug
"""
floodwall(s)
embattlement(s)
donut(s)

"""

## dump rules
#suffixes = {}
#for p in rules :
#  for r in rules[p] :
#    suff = r[1]
#    if not suff in suffixes :
#      suffixes[suff] = []
#    suffixes[suff].append((r[0], r[2]))
#print (suffixes)

double_rules = [
   'al', 'ed', 'en', 'ence', 'ent', 'er', 'es', 'est', 'ing', 'ous', 'y'
]

dont_stem = {
  'apply', 'attic', 'band', 'billion', 'canal', 'career', 'city', 'class',
  'differ','door',
  'early', 'final', 'finance', 'goal', 'good',
  'hammer', 'her', 'herd', 'imply', 'is', 'kind',
  'laud', 'legal', 'legion', 'letter', 'live',
  'mand', 'manner', 'many', 'mayor', 'mend', 'mention', 'meter', 'million',
  'moment', 'moral', 'mother',
  'need',
  'onion', 'only', 'offer', 'offence', 'place', 'power',
  'seal', 'seance', 'sentence', 'should', 'shoulder', 'sober',
  'tend', 'tenable', 'tenant',
  'wass', 'wind', 'wither', 'wood', 'word', 'world', 'youth',
}

not_a_stem = {
#  'ac', 'ag', 'al', 'as', 'ass', 'be', 'both', 'co', 'com', 'da', 'de', 'di', 'du', 'ex', 'for', 'ha', 'he', 'hi', 'ho', 'in', 'ind', 'inn', 'ins', 'is', 'la', 'las', 'les', 'li', 'los', 'me', 'na', 'no', 'not', 'on', 'or', 'pe', 're', 'san', 'sec', 'she', 'st', 'the', 'tim', 'to', 'un', 'us', 'wa', 'we'
  'all', 'and', 'are', 'as', 'ass', 'at',
  'bee', 'both', 'but', 'doe', 'for', 'fri', 'from',
  'has', 'him', 'his', 'inn', 'ins', 'is',
  'mag', 'mam', 'not', 'of', 'outs', 'overs', 'pharma',
  'sec', 'sci', 'she', 'the', 'these', 'they', 'tri', 'was', 'wei',
}

known_stems = {
  'a': 'an',
  'ads': 'ad',
  'an': 'one',
  'begun': 'begin',
  'brethren': 'brother',
  'canny': 'ken',
  'comment': 'mental',
  'distraught': 'distress',
  'does': 'do',
  'doer': 'do',
  'doable': 'do',
  'elsewhere': 'where',
  'everybody': 'every',
  'goer': 'go',
  'goes': 'go',
  'going': 'go',
  'ground': 'grind',
  'herself': 'self',
  'its': 'it',
  'ifs': 'if',
  #'manic': 'mania',
  'perhaps': 'hap',
  'romance': 'roman',
  'said': 'say',
  'sonic': 'sound',
  'sticken': 'strike',
  #'swore': 'swear',
  'swung': 'swing',
  #'tension': 'tense',
  'their': 'they',
  'throughout': 'through',
  'today': 'day',
  'told': 'tell',
  'took': 'take',
  'vehicular': 'vehicle',
  'woken': 'wake',
}

other_known = {
  'widespread',
  'moreover',
  'nevertheless',
  'beneath',
  'whatsoever',
  'furthermore',
  'nonetheless',
  'meantime',
  'albeit',
  'nowadays',
  'underneath',
  'withdrawn',
  'grandchildren',
  'asleep',
  'grassroots',
  'lifelong',
  'suing',
  'mankind',
  'notwithstanding',
  'withdrew',
  'farenheit',
  'celsius',
  'utmost',
  'aforementioned',
  'whichever',
  'impunity',
  'humility',
  'gunfire',
  'emeritus',
  'superannuation',
  'longstanding',
  'embattled',
  'heartfelt',
  'arrears',
  'memorabilia',
  'enbridge',
  'beforehand',
  'withheld',
  'measles'
  'statewide',
  'expats',
  'admin',
  'erstwhile',
  'oversaw',
  'cybersecurity',
  'rallied',
  'liquefied',
  'heartbroken',
  'hydropower',
  'apiece',
  'opium',
  'nineteen',
  'handwritten',
  'introductory',
  'hitherto',
  'adrift',
  'dilapidated'
  'paparazzi',
  'pentiction',
  'firsthand',
  'downright',
  'newfound',
  'fibrosis',
  'spinoff',
  'eastside',
  'windswept',
  'methadone',
  'awash',
  'silicone',
  'oftentimes',
  'hitman'
  'rollercoaster',
  'gastrointestinal',
  'ecoboost',
  'ablaze',
  'onsite',
  'mounties',
  'phosphorus',
  'paraphernalia',
  'voiceover',
  'oncoming',
  'southbound',
  'aback',
  'coriander',
  'elves',
  'solmonella',
  'stateside',
  'gubernatorial',
  'northbound',
  'midwifery',
}

prefixes = {
  'afore': ('', 3),
  'al': ('', 3),
  'ante': ('', 3),
  'anti': ('', 3),
  'auto': ('', 3),
  'be': ('', 3),
  'co': ('', 3),
  'counter': ('', 3),
  'cyber': ('', 3),
  'de': ('', 3),
  'dis': ('', 3),
  'down': ('', 3),
  'electro': ('', 3),
  'ex': ('', 3),
  'extra': ('', 3),
  'fore': ('', 2),
  'giga': ('', 3),
  'here': ('', 1),
  'hetero': ('', 3),
  'homo': ('', 3),
  'hyper': ('', 3),
  'hydro': ('', 3),
  'ill': ('l', 3),
  'imm': ('m', 3),
  'in': ('', 3),
  'irr': ('r', 3),
  'inter': ('', 3),
  'kilo': ('', 3),
  'mal': ('', 5),
  'mega': ('', 3),
  'meta': ('', 3),
  'micro': ('', 3),
  'mid': ('', 3),
  'milli': ('', 3),
  'mis': ('', 3),
  'mono': ('', 3),
  'multi': ('', 3),
  'nano': ('', 3),
  'non': ('', 3),
  'omni': ('', 3),
  'out': ('', 3),
  'over': ('', 3),
  'para': ('', 3),
  'per': ('', 3),
  'pico': ('', 3),
  'poly': ('', 2),
  'post': ('', 3),
  'pre': ('', 3),
  'pro': ('', 3),
  'pseudo': ('', 3),
  'psycho': ('', 3),
  're': ('', 3),
  'semi': ('', 3),
  'sub': ('', 3),
  'super': ('', 3),
  'sym': ('', 3),
  'tele': ('', 3),
  'there': ('', 1),
  'trans': ('', 3),
  'tri': ('', 3),
  'ultra': ('', 3),
  'un': ('', 3),
  'under': ('', 3),
  'uni': ('', 2),
  'up': ('', 3),
  'where': ('', 1),
  'whom': ('who', -1),
}

def pick_stem (possible) :
  # Prefer to derive from known stems
  checked = [w for w in possible if w[0] in checked_words]
  if checked :
    possible = checked

  # Of the remaining, select the most likely
  if possible:
    if len(possible) == 1 :
      return possible[0][0]
    else :
      scores = [(first_in_tree[stem[0]]*stem[1], stem[0])
                for stem in possible
                if stem[0] in first_in_tree]
      if scores :
        scores.sort()
        return (scores[0][1])

  return None


def stem (word, all_words) :
  if word in known_stems :
    return known_stems[word]

  if not word in dont_stem :
    possible_stems = []
    possible_stems_err = []
    for p in range(min (max_suffix, len(word)), 0, -1) :
      s = word[-p:]
      if s in suffixes :
        stem = word[:-p]
        for r in suffixes[s] :
          if len (stem) > r[1] and (len(r) < 3 or not stem.endwith(r[2])) :
            if stem + r[0] in known_errs :
              possible_stems_err.append ((stem + r[0], p))
            elif stem + r[0] in all_words and len(stem) > r[1] :
              possible_stems.append ((stem + r[0], p))

    # near-duplicate of below
    p = pick_stem (possible_stems)
    if p :
      return p
    #if possible_stems :
    #  if len(possible_stems) == 1 :
    #    return possible_stems[0][0]
    #  else :
    #    scores = [(first_in_tree[stem[0]]*stem[1], stem[0])
    #              for stem in possible_stems]
    #    scores.sort()
    #    return (scores[0][1])

    for rule in double_rules :
      if word.endswith(rule) and len (word) > len(rule)+2:
        stem = word[:-len(rule)-1]
        after = word[-len(rule)-1]
        if stem.endswith(after) and stem in all_words :
          return stem

    for p in prefixes :
      if word.startswith(p) :
        stem = word[len(p):]
        if len (stem) > 3 and stem in all_words :
          return stem

    p = pick_stem (possible_stems_err)
    if p :
      return p
    ## near-duplicate of above
    #if possible_stems_err :
    #  if len(possible_stems_err) == 1 :
    #    return possible_stems_err[0][0]
    #  else :
    #    scores = [(first_in_tree[stem[0]]*stem[1], stem[0])
    #              for stem in possible_stems_err]
    #    scores.sort()
    #    return (scores[0][1])

  return None


def print_recursive(word, history='', sep="->", depth = 0) :
  if depth < 100 :
    h = (":" if (not word in children and not word in not_a_stem)
             else " ") if not history else ""
    h += (history + sep) if history else "%7d " % first_in_tree[word]

    if word not in known_errs :
      print (h + word + ("" if word in checked_words else (">" if word in part_classified_words else "?"+), rank[word])

    if word and word in children :
      for c in children[word] :
        print_recursive (c,  h+word, "->", depth+1)

    if word and word in children_err :
      for c in children_err[word] :
        print_recursive (c,  h+word, "=>", depth+1)

# Read non-stems into memory
for word in open('non_stems.txt', 'r') :
  w = word.strip()
  word = ("".join([w for w in word if w in ' *abcdefghijklmnopqrstuvwxyz'])
            .strip()
            .split()
         )
  #if len(word) == 0 :
  #  continue
  #elif len(word) > 1 and word[0] == '*' :
  #  word = word[1]
  #else :
  #  word = word[0]
  #
  #not_a_stem.add(word)

  if len(word) == 1 :
    not_a_stem.add(word[0])



# File containing list of words to be stemmed.
# Should be able to be overridden by the command line
wordlist = 'rank_order.txt'
wordlist = 'word2vec_lowercase.txt'

# Read all words into memory
all_words = []

full_count = 10000000
count = full_count

first_in_tree = {}
rank = {}
index = 0
for word in open(wordlist, 'r') :
  word = word.strip()
  first_in_tree[word] = index
  rank[word] = index
  if not word in not_a_stem :
    all_words.append(word)
    count -= 1
    if not count :
      break
  index += 1

print ('A')

# Load list of (probably) valid words
checked_words = set()
for word in open ('checked_words.txt', 'r') :
  #w = "".join ([w for w in word.lower() if (w>='a' and w<='z') or w in "_'"])
  w = word.strip().lower()
  checked_words.add(w)

# Load list of processed-but-not-fully-classified words
part_classified_words = set()
for word in open ('part_classified.txt', 'r') :
  #w = "".join ([w for w in word.lower() if (w>='a' and w<='z') or w in "_'"])
  w = word.strip().lower().split()
  if len (w) > 1 :
    part_classified_words.add(w[1])

print ('B')

max_suffix = max([len(s) for s in suffixes])
max_prefix = max([len(p) for p in prefixes])

# Dump list of words derived from (probably) valid words
# with the purpose of identifying valid-but-unknown words
if False :
  labelled = set()
  for word in open ('maybe_new_labelled.txt', 'r') :
    labelled.add (word.split()[1])

  for word in open(wordlist, 'r') :
    word = word.strip()
    if word not in checked_words and word not in known_errs :
      s = stem (word, all_words)
      if s in checked_words and not word in labelled :
        print (s, "->", word)
  exit()

# Dump list of (probably) valid words derived from invalid words
# with the purpose of identifying valid-but-unknown words
if False :
  labelled = set()
  for word in open ('maybe_new_labelled.txt', 'r') :
    labelled.add (word.split()[1])

  count = 0
  for word in open(wordlist, 'r') :
    count += 1
    word = word.strip()
    if word in checked_words :
      s = stem (word, all_words)
      #if s and len(word) > 4 :
      #  print (s, word, s not in checked_words, s not in known_errs, word not in labelled)
      #  pdb.set_trace ()
      if s and s not in checked_words and s not in known_errs and word not in labelled :
        print (s, "->", word)
  print (count)
  exit()

if False:
  as_is = []
  for word in open(wordlist, 'r') :
    word = word.strip()
    if word.endswith('as') or word.endswith('is') :
      st = word[0:-2]
      if st in all_words and not st in as_is :
        count = 0
        found = []
        for suff in ('i', 'a', 'is', 'as') :
          if st+suff in all_words :
            count += 1
            found.append(suff)
        if count :
          as_is.append((-count, st, found))

  for s in sorted(as_is) :
    print (s[1], -s[0], s[2])

  exit()

# Remove suffixes from words
roots = []
parents = {}
parents_err = {}

count = full_count;
for word in open(wordlist, 'r') :
  word = word.strip()
  if word in known_errs :
    parents_err[word] = known_errs[word]
  else :
    s = stem(word, all_words)
    if s :
      if not word :
        continue
      parents[word] = s
      #print (word, "<-", s)
    else :
      roots.append(word)
      #print (word)
  count -= 1
  if not count :
    break

print ('C')

# Invert  parents  to form a tree
children = {}
children_err = {}

for group in ((parents, children), (parents_err, children_err)) :
  par = group[0]
  chld = group[1]
  for child in par :
    p = par[child]
    if p not in chld :
      chld[p] = []
    chld[p].append(child)

    # add words from known_stems, if not already present
    for w in (child, p) :
        if w not in first_in_tree :
          full_count += 1
          first_in_tree[w] = full_count
          rank[w] = full_count
      
    if first_in_tree[child] < first_in_tree[p] :
      first_in_tree[p] = first_in_tree[child]

# Dump list of invalid words from which at least two others are derived
# with the purpose of identifying valid-but-unknown words
if False :
  stems_by_fecundity = []
  for word in all_words :
    #if word not in checked_words and word not in known_errs : pdb.set_trace()
    if word not in checked_words and word not in known_errs :
      knowns = (len ([w for w in children[word] if w in checked_words])
                if word in children else 0)
      unknowns = ([w for w in children[word] if w not in checked_words]
                  if word in children else [])
      errs = len (children_err[word]) if word in children_err else 0
      child_count = knowns + len (unknowns) + errs
      if child_count :
        stems_by_fecundity.append ((-child_count, -int(len(word)/5), word, unknowns))

  for w in sorted (stems_by_fecundity) :
    print (-w[0], w[-2], w[-1])
  exit()

print (len (children_err))

# Print the tree
for r in roots :
  print_recursive(r, '', "->")
