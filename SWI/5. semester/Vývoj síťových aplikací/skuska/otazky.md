# TEST 1

- ### Je v kódu nějaká chyba?

  ```java
      Socket socket = new Socket();
      socket.connect(new InetSocketAddress("example.com", 23));
      BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getInputStream()));
      writer.write("Hello, server!");
      writer.flush();
      socket.close();
  ```

  - PRAVDA <!--vytvoření BufferedWriteru z InputStreamu, který je vytvořen z OutputStreamu-->

- ### Jaký je hlavní účel "Topic" v MQTT?
  - Slouží k organizaci zpráv v síti. Určuje kdo obdrží zprávu. V

<!-- 3 -->

- ### Seřaďte kroky pro implementaci serveru, který připojí jednoho klienta a následně vypisuje přijaté zprávy na terminál:

  - Krok 1: Vytvořit ServerSocket a nastavit port pro příchozí spojení.
  - Krok 2: Zavolat metodu accept().
  - Krok 3: Vytvořit InputStream nebo BufferedReader pro čtení zpráv od klienta.
  - Krok 4: Ve smyčce číst zprávy od klienta a vypisovat je na terminál.
  - Krok 5: Uzavřít Socket klienta a ServerSocket po ukončení komunikace.

- ### Jaká je architektura protokolu MQTT?

  - Publish-subscribe

- ### Která anotace se používá pro označení metody, která bude obsluhovat HTTP GET požadavky ve Springu?

  - Odpověď: @GetMapping

- ### Který z následujících příkazů SMTP je volitelný a slouží k autentizaci uživatele?

  - AUTH

- ### Jaký je účel QoS (Quality of Service) v MQTT?

  - QoS určuje úroveň spolehlivosti při doručování zpráv mezi klientem a brokerem.

- ### Zadejte příkaz SMTP, kterým se označuje začátek těla emailu.

  - DATA

- ### Které protokoly používají šifrovanou komunikaci?

  - HTTPS

- ### Která metoda třídy ServerSocket v Javě čeká na příchozí spojení a vrací nový Socket?

  - accept()

- ### Přiřaďte ke každému protokolu odpovídající popis jeho použití v aplikacích. Každý popis odpovídá právě jednomu protokolu.

  - SMTP: Používá se pro odesílání a přenos elektronické pošty mezi servery a klienty.
  - Telnet: Poskytuje jednoduché textové rozhraní pro komunikaci se serverem pomocí příkazů.
  - MQTT: Slouží k přenosu lehkých zpráv mezi zařízeními s využitím publisher-subscriber modelu.
  - HTTP: Používá se k přenosu dat mezi webovým klientem a serverem, například pro API nebo webové stránky.

- ### Jaký je účel metody client.publish() v protokolu MQTT?

  - Používá se k odeslaní zpravy do specifikovaného topicu na broker.

- ### Jaký je hlavní rozdíl mezi MQTT QoS 1 a QoS 2?

  - QoS 1 používá mechanismus "at least once", zatímco QoS 2 používá "exactly once", což eliminuje duplikace zpráv.

- ### Které z následujících tvrzení o Telnet klientovi jsou správné?

  - Telnet je protokol, který funguje na principu textové komunikace mezi klientem a serverem.
  - Telnet klient umožňuje připojení k vzdáleným serverům pro provádění příkazů v textovém režimu.

- ### Jakou příponu mají binární soubory, které vznikají překladem java zdrojových souborů?

  - .class

- ### Která z následujících anotací ve Springu se používá pro označení třídy, která by měla být zaregistrována jako komponenta pro práci s konkrétní kolekcí dat v databází?

  - @Repository
  <!-- 17 -->
- ### Jak správně vytvořit instanci Telnet serveru v Javě, pokud chcete, aby server naslouchal na portu 23 a přijímal klientská připojení?

  - ServerSocket serverSocket = new ServerSocket(23);

- ### Jaký je rozdíl mezi SOAP a REST při komunikaci se serverem?

  - SOAP je přísně definován a formátován pomocí XML, zatímco REST je flexibilnější a umožňuje více formátů dat.

- ### Které z následujících problémů mohou způsobit odmítnutí příjemce při odesílání emailu?

  - Nedostatek úložného prostoru na straně příjemce.

  - Nespravná formatovaná emailová adresa. 

  - Server příjemce odmítl email kvůli blacklistech.

<!-- 20 -->

- ### Jaký kód je použitelný pro čtení dat ze socketu v Javě? (pokud je otevřený)

  - BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

- ### Jakým způsobem je možné vytvořit ExecutorService s fixní velikostí, který obsahuje 4 vlákna?

  - ExecutorService executor = Executors.newFixedThreadPool(4);

- ### Jaká výjimka je vyvolána, pokud Socket v Javě nedokáže navázat spojení se serveru?

  - UnknownHostException

- ### Systém pro automatický překlad textových adres (URL) na numerické IP adresy se nazývá?

  - DNS

- ### Budou data na server správně odeslána?
  ```java
  Socket socket = new Socket("localhost", 23);
  OutputStream outputStream = socket.getOutputStream();
  outputStream.write("Hello".getBytes());
  socket.close();
  ```
  - NEPRAVDA
  <!-- chybí volání metody flush() pro odeslání dat. -->

<!-- 25 -->

- ### Který transportní protokol je využíván MQTT?

  - TCP

- ### Který HTTP stavový kód označuje úspěšně zpracovaný požadavek, při kterém server vytvořil nový zdroj?

  - 201 Created

- ### Co se stane, pokud dvě vlákna současně volají nesynchronizovanou a synchronizovanou metodu na stejné instanci objektu?

  - Synchronizovaná metoda se spustí jedna v jeden okamžik, ale nesynchronizovaná metoda může být spuštěna i vícenásobně v jeden stejný okamžik.

- ### Seřaďte kroky pro implementaci klienta, který přijímá zprávy od serveru a vypisuje je na terminál.

  - Krok 1: Vytvořit socket a připojit se k serveru na daném portu.
  - Krok 2: Vytvořit InputStream nebo BufferedReader pro čtení dat ze serveru.
  - Krok 3: Ve smyčce číst zprávy přicházející ze serveru.
  - Krok 4: Vypisovat přijaté zprávy na terminál.
  - Krok 5: Uzavřít socket a všechny streamy po ukončení komunikace.

- ### Který protokol využívá Telnet pro komunikaci?

  - TCP

- Co označuje anotace @RequestBody v Springu?
- - Označuje, že parametr metody má být naplněn daty z těla HTTP požadavku.

# TEST 2

- ### Co znamená příkaz SMTP RSET?

  - Resetuje aktuální relaci na začátek bez ukončení spojení.

- ### Je v kódu nějaká chyba?

  ```java
  Socket socket = new Socket("localhost", 23);
  BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
  String response = reader.readLine();
  System.out.println(response);
  socket.close();
  ```

  - NEPRAVDA

- ### Jaký status kód odpovědi SMTP indikuje, že server je připraven přijmout tělo emailu? „Odpověď na STMP command DATA“

  - 354

- ### Jaký je příkaz pro zahájení komunikace s SMTP serverem?

  - HELO

- ### Který HTTP status kód by měl být vrácen v případě, že požadavek nebyl zpracován, protože požadovaný zdroj nebyl nalezen?

  - 404

- ### Jaké číslo portu využívá MQTT protokol?

  - 1883

- ### Co se stane, když se pokusíte spustit server na portu, který je již obsazen jinou službou?

  - Server se nespustí a dojde k chybě při pokusu o připojení na tento port.

- ### Je v kódu nějaká chyba? <!-- DUPLICITNÁ -->

  ```java
  Socket socket = new Socket();
  socket.connect(new InetSocketAddress("example.com", 23));
  BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getInputStream()));
  writer.write("Hello, server!");
  writer.flush();
  socket.close();
  ```

  - PRAVDA
  <!--vytvoření BufferedWriteru z InputStreamu, který je vytvořen z OutputStreamu-->

- ### Jaký balíček v Javě poskytuje třídy pro práci se síťovými aplikacemi, včetně vytváření socketů a komunikace přes TCP/IP?

  - java.net

- ### Budou data na server správně odeslána? <!-- DUPLICITNÁ -->
  ```java
  Socket socket = new Socket("localhost", 23);
  OutputStream outputStream = socket.getOutputStream();
  outputStream.write("Hello".getBytes());
  socket.close();
  ```
  - NEPRAVDA
  <!-- chybí volání metody flush() pro odeslání dat. -->

<!-- 11 DUPLICIDNA -->
<!-- 12 DUPLICIDNA -->
<!-- 13 -->

- ### Seřaďte správně kroky pro implementaci telnet klienta s funkcionalitou přijímání a odesílání zpráv přes socket.

  - <!-- Nedáva zmysel aby záležalo na poradí tvorby streamov -->

  - Krok 1: Vytvořte Socket připojený k serveru na daném portu.
  - Krok 2: Vytvořte stream pro čtení zpráv přicházejících od serveru (např. BufferedReader).
  - Krok 3: Vytvořte stream pro příjem zpráv z terminálu (např. Scanner pro čtení vstupu).
  - Krok 4: Vytvořte stream pro odesílání zpráv na server (např. PrintWriter).
  - Krok 5: Spusťte vlákno pro příjem zpráv od serveru, které bude zprávy vypisovat do terminálu.
  - Krok 6: Použijte Scanner pro čtení zprávy z terminálu a odešlete ji na server pomocí PrintWriter.
  - Krok 7: Uzavřete všechny otevřené streamy a socket po ukončení komunikace.

- ### Jaký je účel klíčového slova synchronized v Javě?

  - Zajišťuje, že pouze jedno vlákno má přístup ke sdílenému zdroji v daný okamžik.

- ### Napište název třídy, která se v knihovně Paho MQTT používá pro zpracování přijatých zpráv (callback).

  - MqttCallback

- ### Je kód pro REST kontrolér napsán bez chyb?

  ```java
  @RestController
  @RequestMapping("/api")
  public class ProductController {

      private final ProductService productService;

      @Autowired
      public ProductController(ProductService productService) {
          this.productService = productService;
      }
      @GetMapping("/products")
      public ResponseEntity<List<Product>> getAllProducts() {
          List<Product> products = productService. findAll();
          return products.isEmpty() ? new ResponseEntity<>(HttpStatus.NO_CONTENT) : new ResponseEntity<>(products, HttpStatus.OK);
      }
      @PostMapping("/products")
      public ResponseEntity<Product> createProduct(@RequestBody Product product) {
          Product createdProduct = productService.save(product);
          return new ResponseEntity<>(createdProduct, HttpStatus.CREATED);
      }
  }
  ```

  - PRAVDA

- ### Jaká je standardní IP adresa pro localhost?

  - 127.0.0.1

- ### Jaký port je standardně používán pro HTTP komunikaci?
  - 80
- ### Systém pro automatický překlad textových adres (URL) na numerické IP adresy se nazývá?

  - DNS

- ### Ve které metodě implementujeme kód, který po spuštění nového vlákna poběží v tomto vlákně?

  - run()

- ### Jaké tvrzení platí o telnet protokolu?

  - Telnet standardně využívá port 23.
  - Telnet přenáší veškerou komunikaci v čistém textu, což může vést k bezpečnostním problémům, jako je odposlech.

- ### Které kroky jsou standardně prováděny během životního cyklu socketu na straně klienta v javě?

  - Otevřít socket na konkrétní IP adresu a port
  - Zavřít socket po ukončení komunikace
  - Číst a zapisovat data přes InputStream a OutputStream

- ### Které z následujících knihoven lze použít k implementaci Telnet klienta v Javě?

  - java.net.Socket

- ### Jaká je velikost IPv4 adresy?

  - 32 bitů

- ### Je v kódu nějaká chyba?

  ```java
  Socket socket = new Socket("localhost", 23);
  BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getInputStream()));
  writer.write("Hello, server!");
  writer.flush();
  BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getOutputStream()));
  String response = reader.readLine();
  System.out.println(response);
  socket.close();
  ```

  - Používá se getInputStream() pro zápis, místo getOutputStream().
  - Kód se pokouší číst data z výstupního streamu, místo z vstupního proudu.

- ### Jaký kód je použitelný pro čtení dat ze socketu v Javě? (pokud je otevřený)

  - BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

- ### Který port používá Telnet protokol ve výchozím nastavení?

  - 23

- ### Jak správně použít Runnable v ThreadPoolExecutoru pro spuštění úlohy?

  - executor.execute(new MyRunnable());
  - executor.submit(new MyRunnable());

- ### Jaké tvrzení o telnet protokolu je pravdivé?

  - Nemá šifrování.

- ### Jaký je účel metody shutdown() v ExecutorService?
  - Zastaví příjem nových tasků, ale umožní dokončení těch aktuálně spuštěných

# TEST 3

- ### Co způsobí zavolání metody Thread.sleep(1000) ve vlákné?

  - Vlakno bude pozastaveno na 1000 milisekund.

- ### Jaký je správný způsob, jak vytvořit instanci třídy URL pro URL adresu "https://www.google.com"?

  - URL url = new URL("https://www.google.com");
  - URL url = new URL("https://google.com");

- ### Jak byste nejlépe popsali PuTTY?

  - PuTTY je klientský nástroj umožňujíci připojeni k serveru pomoci různých protokolů.

- ### Jaký je účel metody run() v třídě Thread v Javě?

  - Obsahuje kód, který se bude vykonávat v novém vlákně.

- ### Jaký je hlavní rozdil mezi InputStream a Reader v Javě?

  - InputStream čte binární data (bajty), zatímco Reader čte textová data (znaky).

- ### Jaký je účel metody execute(Runnable task) v rámci třídy ExecutorService v Javě?

  - Spusti nový task v rámci Thread pool executoru.

- ### Který z následujících přikazů pomocí curl použijete pro odeslání POST požadavku s JSON daty na URL http://localhost:8080/api/data?

  - curl-X POST http://localhost:8080/api/data-d'{"name":"John"]'-H "Content-Type: application/json"

- ### Jaký je hlavní rozdil mezi SOAP a REST z hlediska jejich architektury a použiti?

  - SOAP je protokol, zatímco REST je architektonický styl. SOAP používá XML a WSDL, zatimco REST podporuje různé formáty, jako JSON, XML, YAML.

- ### Jak správně počkat na ukončení vlákna v Javě, aby hlavní vlákno počkalo na jeho dokončení?

  - thread.join();

- ### Co obvykle obsahuje element <Envelope> v SOAP zprávě?

  - Dva hlavni elementy: <Header> a <Body>, které obsahují metadata a data zprávyv

- ### Jakým způsobem se můžete připojit k webové aplikaci, která je spuštěná na vašem aktuálním počitači na portu 8080?
  - http://localhost:8080
  - http://127.0.0.1:8080

- ### Napište název anotace, která slouži pro označení třídy jako databazové entity v rámci Spring JPA?
    
    - @Entity 

- ### Které z následujících přikazů patří do základního SMTP protokolu?

  - HELO
  - MAIL FROM
  - DATA
  - AUTH

- ### Co se stane, když se pokusite spustit server na portu, který je již obsazen jinou službou?

    - Server se nespusti a dojde k chybě při pokusu o připojení na tento port. 


- ### Jaký kód použít pro zpracování/přijetí klientského připojení u serveru v Javě, pokud již máte otevřený ServerSocket?
    
    - Socket socket = serverSocket.accept();

- ### Pokud v Spring JPA použiváte anotaci @GeneratedValue, jaký atribut určujete pro výběr konkrétní strategie generování ID?
    
  - strategy

- ### Jaká je hlavni výhoda použití ThreadPoolExecutor misto vytváření samostatných vláken pro každý task?

    - Snížení režie spojené s vytvářením a ničením vláken, protože vlákna mohou být znovu využita pro další task.

- ### Jaká metoda se využívá pro načtení HTML obsah z URL pomocí knihovny Jsoup?

    - Jsoup.connect(url).get()


- ### Na jakém portu standardně bēži SMTP server?
    
  - 25


- ### Který HTTP stavový kód označuje úspěšně zpracovaný požadavek, při kterém server vytvořil nový zdroj?

    - 201 Created


- ### Napište název třídy, která se v knihovně Paho MQTT použivá pro vytvoření klienta v siti MQTT.

    - MqttClient

- ### Která z následujícich anotaci označuje primárni klič v entitní třídě, která je mapována na databázovou tabulku v Spring JPA?

    - @Id

