<h2>Istruzioni utilizzo autoposter</h2>

1) Inserire ID applicazione in file secrets.ini
2) Inserire ID pagina FB in file secrets.ini
3) Genera un token di accesso app tramite facebook.dev debugger
4) Inserire token di accesso in secrets.ini
----------------------------------------------
5) Crea <nome_task>.py seguendo il template 'basic.py'
6) Importa il task creato all'interno di main.py
7) Chiama funzione schedule() sui tasks che si vogliono programmare, trovi maggiori dettagli nei commenti all'interno di main.py