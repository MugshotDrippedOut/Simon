*** Keywords ***
Zajdi na hlavni stranku a zkontroluj
    [Arguments]  ${URL}  ${KontrolovanyElement}

    Go To  ${URL}
    Wait Until Element Is Visible  ${KontrolovanyElement}
    Location Should Be  ${URL}

Pockej nez bude element viditelny
    [Arguments]  ${Element}
    Wait Until Element Is Visible  ${Element}


Otevri Browser a Zajdi na hlavni stranku a Zkontroluj
    [Arguments]  ${Browser}  ${URL}  ${KontrolovanyElement}

    Create Webdriver  ${Browser}  executable_path=C:\\Users\\student\\Downloads\\chromedriver.exe
    Maximize Browser Window
    Sleep  20
    Go To  ${URL}
    Wait Until Element Is Visible  ${KontrolovanyElement}
    Location Should Be  ${URL}