#!/usr/bin/env python

import cgitb, cgi

cgitb.enable()

print("""
<html>
<head>
    <meta charset="utf-8">
    <title>Home | Chat Room</title>
    <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
    <div class="app">
        <div class="screen join-screen active">
            <div class="form">
                <h2>Junte-se ao Chat</h2>
                <form action="" method="get">
                    <div class="form-input">
                        <label>Apelido</label>
                        <input type="text" id="username" name="uname">
                    </div>
                    
                    <div class="form-input">
                        <button id="join-user">Entrar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
""")

getForm = cgi.FieldStorage()
uname = getForm.getvalue("uname")

if uname != " ":
    print("""
    <head>
        <meta http-equiv="refresh" content="0;URL='chat.py'">
    </head>
    """)
else:
    print("""
    <br>
    <h1><span>Insira um Nickname</span></h1>
    """)

print("</body></html>")