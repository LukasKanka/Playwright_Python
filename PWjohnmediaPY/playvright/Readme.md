Video 2 nastavuji
doporučuji zde se podívat jak stopnout některy browsey https://youtu.be/IDrTacdVNRM?t=838
 @pytest.mark.skip_browser("firefox")
 @pytest.mark.only_browser("chrome")

 pytest --tracing on  --> tento pžíkaz na spuštění testu vytvoří složky kde je v zip výsledek testu
     zip mohu otevřít zde a podívat se na výsledek testu https://trace.playwright.dev/
     další možnosti jak využít trace.zip https://youtu.be/IDrTacdVNRM?t=1148

     na inportovaném pytest.ini mužu nastavit default URL a další parametry
Video 3 codegen a Inspektor 
 v codegen vygeneruji v mém případě zatím code v pytest
https://playwright.dev/python/docs/codegen#recording-a-test
https://playwright.dev/python/docs/debug

 video jakým vše možným způsobem se dá použít playwright codegen je zde: https://youtu.be/IRTeqUXkPbA
 třeba je mémožné ho použít na nacvakání jako na iPhone, nebo daným rozlišení stránky
 velikost textu se zobrazí v nastavení parametrů přímo v testu
 navíc můžeme importovat tmavé schéma, geolokační data (od kud přistupuji na net), vše je v dokumentaci

 