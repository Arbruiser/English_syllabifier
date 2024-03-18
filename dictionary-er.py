import regex as re
import string

substitutions = {
    "AA": "ɑː",
    "AE": "æ",
    "AH": "ʌ",
    "AO": "ɔː",
    "AW": "aʊ",
    "AY": "aɪ",
    "B": "b",
    "CH": "tʃ",
    "D": "d",
    "DH": "ð",
    "EH": "ɛ",
    "ER": "ɜr",
    "EY": "eɪ",
    "F": "f",
    "G": "ɡ",
    "HH": "h",
    "IH": "ɪ",
    "IY": "i",
    "JH": "dʒ",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "NG": "ŋ",
    "OW": "oʊ",
    "OY": "ɔɪ",
    "P": "p",
    "R": "r",
    "S": "s",
    "SH": "ʃ",
    "T": "t",
    "TH": "θ",
    "UH": "ʊ",
    "UW": "u",
    "V": "v",
    "W": "w",
    "Y": "j",
    "Z": "z",
    "ZH": "ʒ"
    # "BEFORE": "AFTER",
}

#write the lexc code
header = """LEXICON Root
        IPAbracket ;
        Prefixes ;

LEXICON IPAbracket
/ IPA ;
        
LEXICON IPA 
ɒ IPA ;
æ IPA ;
ʌ IPA ;
ɔ IPA ;
a IPA ;
ə IPA ;
b IPA ;
t IPA ;
d IPA ;
ð IPA ;
ɛ IPA ;
ɜ IPA ;
e IPA ;
ɪ IPA ;
f IPA ;
ɡ IPA ;
h IPA ;
ɪ IPA ;
i IPA ;
d IPA ;
k IPA ;
l IPA ;
m IPA ;
n IPA ;
ŋ IPA ;
o IPA ;
ɔ IPA ;
p IPA ;
r IPA ;
s IPA ;
ʃ IPA ;
t IPA ;
θ IPA ;
ʊ IPA ;
u IPA ;
v IPA ;
w IPA ;
j IPA ;
z IPA ;
ʒ IPA ;
ː IPA ;
%: IPA ;
/ IPA ;
%. IPA ;
ˈ IPA ;
' IPA ;
ˌ IPA ;
# ; ! done

LEXICON Prefixes ! just some of the most common ones 
un:ʌn# Stems ;
dis:dɪs# Stems ;
in:ɪn# Stems ;
im:ɪm# Stems ;
il:ɪl# Stems ;
ir:ɪr# Stems ;
re:riː# Stems ;
under:ʌndər# Stems ;
up:ʌp# Stems ;
Stems ;

LEXICON Stems
"""



# read the CMU dictionary file
with open('cmudict', 'r') as file:
    lines = file.readlines()

# adapt the dictionary to lexc format
with open('lexc.lexc', 'w', encoding='utf-8') as file:
    file.write(header)
    for line in lines:
        words = line.split()
        words[0] = words[0].lower() # lowercases the first word (the spelling)
        del words[1] # removes the index of pronunciation
        words = ['ə' if word=='AH0' else word for word in words] # change 'AH0' (unstressed ʌ) to schwa 
        words = ['iː' if word=='IY1' else word for word in words]# changes IY1 to i:
        words = [''.join(ch for ch in word if not ch.isdigit()) for word in words] #removes all digits
        words = [substitutions.get(word, word) for word in words] # replace CMU's phonetic notation with IPA
        words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words] # remove all punctuation like quotes, exclamation marks etc
        joined_IPA = words[0] + ':' + ''.join(words[1:]) + ' Suffixes ;\n'  # remove spaces in transcriptions
        file.write(joined_IPA)  # write to the file



#the rest of the lexc file including suffixes
footer = """
LEXICON Suffixes
ing:#ɪŋ Suffixes; ! doing
er:#ər Suffixes; ! teacher
r:#ər Suffixes; ! driver
ism:#ɪzəm Suffixes; ! capitalism
ize:#aɪz Suffixes; ! capitalize
ise:#aɪz Suffixes; ! capitalise
ish:#ɪʃ Suffixes; ! feverish
able:#əbəl Suffixes; ! drinkable
ible:#əbəl Suffixes; ! convertible
ery:#ɛri Suffixes; ! brewery
ry:#ri Suffixes; ! bakery
y:#i Suffixes; ! silvery
ular:#juːlər Suffixes; ! cellular
age:#ɪdʒ Suffixes; ! package
ous:#əs Suffixes; ! dangerous
ive:#ɪv Suffixes; ! effective
ant:#ənt Suffixes; ! assistant
ance:#əns Suffixes; ! consultance
ment:#mənt Suffixes; ! statement
nce:#ns Suffixes; ! emergence
ate:#eɪt Suffixes; ! activate
less:#ləs Suffixes; ! painless
ness:#nəs Suffixes; ! saneness
ly:#li Suffixes; ! perplexingly

# ; ! done here

END
"""
with open('lexc.lexc', 'a', encoding='utf-8') as file:
    file.write(footer)