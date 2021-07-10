#!/usr/bin/env python

import cgitb

cgitb.enable()

print("""
<html>
<head>
    <meta charset="utf-8">
    <title>Chat | Chat Room</title>
    <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
    
    <div class="app">
        <div class="screen chat-screen active">
            <div class="header">
                <div class="logo">Sala de Bate-Papo</div>
                <button id="exit-chat">Sair</button>
            </div>
            <div class="messages">   
            </div>
            <div class="typebox">
                <input type="text" id="message-input">
                <button id="send-message">Enviar</button>
            </div>
        </div>
    </div>
""")

print("</body></html>")