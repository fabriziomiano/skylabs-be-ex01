# SkyLabs Exercise

## Domande e relative risposte

* Cosa si intende per API REST ?
    - Il Representational state transfer (REST) è uno standard di architettura
      software per applicazioni che utilizzano servizi Web. Un API REST manda
      richieste con un dato protocollo - in genere HTTP - a un dato URI e
      riceve risposte con payload formattato in HTML, XML, JSON, ecc.
      (response). Il response può, o meno, confermare che lo stato della
      risorsa è stato modificato. Le operazioni più comuni, (metodi HTTP)
      sono GET, POST, PUT, DELETE, OPTIONS, ecc.


* Cosa si intende per servizio SOAP ?
    - Qui, in piena onestà intellettuale, non sono ferratisimo. So che a
      differenza del REST è un messaging protocol e quindi può essere
      utilizzato per comunicare tra server tramite XML.


* Cos'è un database relazionale ?
    - Un Relational Database (RDB) è un database costruito sulla base di un
      modello dati relazionale: il dato è presentato all'utente tramite
      relazioni rappresentate da tabelle formate da righe e colonne di dati.
      Ogni tabella ha un campo chiave univoco che identifica una data riga
      (Primary Key). Idealmente, ogni tabella rappresenta un'entità,
      ad es. 'cliente', e ogni colonna rappresenta un suo attributo. 
      La Foreign Key di una tabella relazionale definisce la relazione tra questa
      e un'altra. Alcuni esempi, nello scenario dello standard industriale,
      di un RDB sono Microsoft SQL Server, MySQL, MariaDB, SQLite.
      

* Cos'è un database NoSQL ?
    - Un database NoSQL è un database il cui data model non poggia sul modello 
      relazionale, ma su qualunque altra forma, come ad esempio 'documentale' 
      (MongoDB) o 'chiave-valore' (Redis).
      

* Cos'è un ORM ? Fai almeno un esempio.
    - L'Object–relational mapping (ORM) è una tecnica per convertire dati tra 
      sistemi incompatibili tramite l'uso di programmazione a oggetti (OOP). 
      Alcuni esempi di ORM sono SQLAlchemy (usato in questa repo), PyMongo 
      (che ho usato per altri progetti). 
      

* Cos'è la SQL Injection ?
    - La SQL Injection è una tecnica d'attacco che sfrutta l'ingestione di stringhe 
      SQL in campi che prevedono l'esecuzione di codice server-side.
      

* Cos'è l'autenticazione a 2 fattori? Descrivi brevemente un esempio.
    - L'autenticazione a 2 fattori è una tecnica pensata per irrobustire il 
      processo di autenticazione di un computer, aggiungendo un layer di sicurezza.
      Un esempio può essere rappresentato da una pagina web che concede l'accesso
      a risorse private solo dopo aver superato con successo due layer di autenticazione: 
      credenziali d'accesso (nome utente, password) e qualcosa di cui l'utente 
      essere effettivamente in possessso (notifica su app su altro dispositivo, codice SMS, ecc.)
      

* Descrivi brevemente un metodo sicuro per salvare le password degli utenti sul DB.
    - Uno dei metodi di crittografia password è il bcrypt, del quale esistono implementazioni
      per i maggiori linguaggi di programmazione. Non ne so tantissimo. So che usa 
      il tipico 'salt', cioé una serie di caratteri random generati a runtime che
      vengono aggiunti alla password in ingresso e del quale alla fine viene 
      creatoi l'hashing (SHA256).
      

* Cos'è una Sticky Session in un sistema con Load Balancing?
    - La sticky session è una caratteristica dei load balancer che mantiene l'oggetto
      sessione inalterato per tutte le interazioni client-server permettendo alle richieste 
      di essere indirizzate allo stesso server. 

## Esercizi

1. Scrivi una query che estragga il **numero di persone** con **meno di 30 anni** che guadagnano **più di 50.000 dollari l'anno**.
   ```sqlite
    SELECT COUNT(*) [Numero di persone]
    FROM records
    WHERE over_50k = 1
      AND age < 30;
   ```
    |Numero di persone|
    |-----------------|
    |746|


2. Scrivi una query che riporti il **guadagno di capitale medio** per ogni categoria lavorativa

    ```sqlite
    SELECT w.name            [Categoria lavorativa]
         , AVG(capital_gain) [Guadagno capitale medio]
    FROM records r
             JOIN workclasses w on r.workclass_id = w.id
    GROUP BY w.name
    ```
    
    |Categoria lavorativa|Guadagno capitale medio|
    |------------------------|---------------------|
    |?|502.94605216148625|
    |Federal-gov|923.2877094972067|
    |Local-gov|798.2286352040817|
    |Never-worked|0|
    |Private|896.1353742700408|
    |Self-emp-inc|5132.794100294986|
    |Self-emp-not-inc|1781.7446918694977|
    |State-gov|756.3361938414942|
    |Without-pay|325.23809523809524|


3. (a) Lista dei record denormalizzati, cioè ogni entità deve contenere anche tutte le informazioni derivanti dalle tabelle secondarie del DB. L'API deve essere realizzata in GET e avere una paginazione parametrica (cioè tramite l'url è possibile definire offset e count)


3. (b) Statistiche aggregate filtrate in base ad alcuni parametri significativi
    
    L'API, realizzabile in **GET** o in **POST**, deve soddisfare questa
    documentazione fornita dal cliente:
   
    **INPUT**:
   ```
    - aggregationType: "age", "education_level_id", "occupation_idb"
    - aggregationValue: int
   ```

    **OUTPUT** :
    ```
    {
        "aggregationType": "string",
        "aggregationFilter": int,
        "capital_gain_sum": float,
        "capital_gain_avg": float,
        "capital_loss_sum": float,
        "capital_loss_avg": float,
        "over_50k_count": int,
        "under_50k_count": int
    }
   ```

    **ESEMPIO**:
    Passando i parametri "aggregationType" = "age" e "aggregationValue" = 30 si ottengono
    le statistiche per tutti coloro che hanno 30 anni.


4. Esponi inoltre, tramite il medesimo servizio web, un endpoint che faccia il 
   download in formato **CSV** di tutti i dati **denormalizzati** 
   (cioè ogni riga deve contenere sia il record che tutti i dati relazionati dalle altre tabelle)
   