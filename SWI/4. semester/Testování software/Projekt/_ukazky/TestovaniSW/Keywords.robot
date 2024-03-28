*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj  #Název
    [Arguments]  ${Browser}  ${URL}  ${KontrolovanyElement}

    Create Webdriver  ${Browser}  executable_path=C:\\Users\\student\\Downloads\\chromedriver.exe
    Maximize Browser Window
    Go To  ${URL}

    Wait Until Element Is Visible  ${KontrolovanyElement}

Zaloguj a Zkontroluj
    [Arguments]  ${LoginInput}
    ...  ${LoginValue}  ${HesloInput}  ${HesloValue}  ${Tlacitko}  ${KontrolovanyElement}  ${Kontrolovane}

    Element Should Be Visible  ${LoginInput}
    Element Should Be Visible  ${HesloInput}
    Element Should Be Visible  ${Tlacitko}

    Input Text  ${LoginInput}  ${LoginValue}
    Input Text  ${HesloInput}  ${HesloValue}

    Click Element  ${Tlacitko}

    Wait Until Element Is Visible  ${KontrolovanyElement}
    Location Should Contain  ${Kontrolovane}


