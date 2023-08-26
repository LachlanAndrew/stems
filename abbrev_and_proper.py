#!/usr/bin/python

full = {}
count = 0
for word in open ("ranked.txt", "r") :
  full[word.strip()] = count
  count += 1

checked = set()
for word in open ("checked_words.txt", "r") :
  checked.add(word.strip())

name_prefixes = {
"minister",
"commissioner",
"mayor",
"ambassador",
"secretary",
"premier",
"governor",
"judge",
"chairman",
"al",
"speaker",
"justice",
"chancellor",
"van",
"writer",
"officer",
"senator",
"prosecutor",
"superintendent",
"el",
"king",
"justices",
"phase",
"la",
"de",
"auditor",
"supervisor",
"actress",
"administrator",
"attorney",
"rabbi",
"congresswoman",
"pope",
"treasurer",
"archbishop",
"operation",
"inspector",
"chairwoman",
"general",
"l'",
"magistrate",
"actor",
"writers",
"congressman",
"cardinal",
"emperor",
"corporal",
"advocate",
"director",
"coroner",
"sheriff",
"principal",
"marshal",
"correspondent",
"admiral",
"editor",
"commander",
"chair",
"agent",
"specialist",
"god",
"chairperson",
"ayatollah",
"pharaoh",
"chief",
"bishop",
"professor",
"detective",
"singer",
"warden",
"guardian",
"solicitor",
"leader",
"adviser",
"captain",
"deputy",
"sophomore",
"private",
"lady",
"councilman",
"psychiatrist",
"witness",
}

proper_nouns = {}
for word in full :
  if word :
    first = word[0]
    if first.islower() and not word in checked :
      cap = first.upper() + (word[1:] if len(word) > 1 else "")
      if cap in full and 2*full[cap] < full[word] :
        parts = word.split('_')
        if len(parts) != 3 or (parts[0] not in full or parts[1] not in full
                                or full[parts[1]] < full[parts[0]]) :
          #print (cap, full[cap], full[word])
          count += 1
        else :
          if parts[0] in name_prefixes :
            for n in parts[1:3] :
              if any([letter.islower() for letter in n]) :
                if n in proper_nouns :
                  proper_nouns[n] += 1
                else :
                  proper_nouns[n] = 1

for word in sorted(proper_nouns, key=lambda x: -proper_nouns[x]) :
  if word.lower() not in checked :
    print ('"%s",' % word)
