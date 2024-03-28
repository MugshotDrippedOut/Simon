*** Keywords ***
Otevri prohlizec a Zajdi na hlavni stranku a Zaloguje se a Zkontroluj
    [Arguments]  ${Browser}  ${URL}  ${Kontrola1}  ${InputLogin}  ${InputHeslo}  ${Login}  ${Heslo}  ${Tlacitko}  ${Kontrola2}

    #Incognito verze
    ${options}=    Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    Call Method    ${options}    add_argument    incognito
    Create Webdriver  ${Browser}  executable_path=C:\\Users\\student\\Downloads\\chromedriver.exe  chrome_options=${options}
    Maximize Browser Window
    Go To  ${URL}

    Wait Until Element Is Visible  ${Kontrola1}
    Element Should Be Visible  ${InputLogin}

    Input Text  ${InputLogin}  ${Login}
    Click Element  ${Tlacitko}


    #Nefunguje s tímto Gmail účtem
    Sleep  10
    Wait Until Element Is Visible  ${InputHeslo}
    Input Text  ${InputHeslo}  ${Heslo}
    Click Element  ${Tlacitko}

    Wait Until Element Is Visible  ${Kontrola2}
