#!/usr/bin/env python

import cgitb
import cgi

cgitb.enable()

dictionaryOfMorseCode = {'A': '.-',   'B': '-...',    'C': '-.-.',    'D': '-..',
       'E': '.',    'F': '..-.',    'G': '--.',     'H': '....',
       'I': '..',   'J': '.---',    'K': '-.-',     'L': '.-..',
       'M': '--',   'N': '-.',      'O': '---',     'P': '.--.',
       'Q': '--.-', 'R': '.-.',     'S': '...',     'T': '-',
       'U': '..-',  'V': '...-',    'W': '.--',     'X': '-..-',
       'Y': '-.--', 'Z': '--..',

       '0': '-----',    '1': '.----',   '2': '..---',   '3': '...--',
       '4': '....-',    '5': '.....',   '6': '-....',   '7': '--...',
       '8': '---..',    '9': '----.',   ' ': '\n'
        }

print("""
<html>
<head>
    <meta charset="utf-8">
    <title>Translator | Código Morse</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    
    <div class="app">
        <div class="screen join-screen active">
            <div class="form">
                <h2>Código Morse Translator</h2>
                <form action="" method="post">
                    <div class="form-input">
                        <label>Digite seu texto</label>
                        <input type="text" name="text" id="username">
                    </div>
                    <div class="form-input">
                        <button id="join-user">Traduzir</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
""")

form = cgi.FieldStorage()
text = form.getvalue("text")
text.upper()

inMorse = ''

if text:
    for char in text:
        if char != ' ':
            inMorse = inMorse + dictionaryOfMorseCode.get(char) + ' '
        else:
            inMorse = inMorse + ' '

print("""
    <br>
    <h2><span class="form">Tradução: {inMorse}</span></h2>
""")

print("""</body></html>""")