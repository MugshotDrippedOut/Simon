- TS_001_001_001 - Obec
    - TC_001_001_001-001 - Kontrola interakcie tláčítka Základné údaje a kontakty
    - TC_001_001_001-002 - Kontrola interakcie tláčítka Geografická poloha
    - TC_001_001_001-003 - Kontrola interakcie tláčítka História obce Krakovany
    - TC_001_001_001-004 - Kontrola interakcie tláčítka Monografia obce
    - TC_001_001_001-005 - Kontrola interakcie tláčítka Erb obce
    - TC_001_001_001-006 - Kontrola interakcie tláčítka Územný plán obce
    - TC_001_001_001-007 - Kontrola interakcie tláčítka Program rozvoja obce
    - TC_001_001_001-008 - Kontrola interakcie tláčítka Prevádzkový poriadok Zberného dvora
    - TC_001_001_001-009 - Kontrola interakcie tláčítka Starosta obce
    - TC_001_001_001-010 - Kontrola interakcie tláčítka Obecné zastupiteľstvo
    - TC_001_001_001-011 - Kontrola interakcie tláčítka Obecná knižnica
    - TC_001_001_001-012 - Kontrola interakcie tláčítka Fotogaléria
    - TC_001_001_001-013 - Kontrola interakcie tláčítka Podnikateľské subjekty
    - TC_001_001_001-014 - Kontrola interakcie tláčítka Červ. kríž
    - TC_001_001_001-015 - Kontrola interakcie tláčítka Mikroregión 

*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  resources/variables/Inputs.robot
Resource  resources/variables/Buttons.robot
Resource  Resources/variables/Texts.robot


*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds
    Open Browser  ${URL_MainPage}  ${BROWSER_CHROME}

TC_001_001_001-001 - Kontrola interakcie tláčítka Základné údaje a kontakty
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_ZakladneUdajeAkontakty}  10 seconds
    Click Element  ${BUTTON_ZakladneUdajeAkontakty}
    Sleep  20 milliseconds
    Location Should Be  ${URL_ZakladneUdajeAkontakty}

TC_001_001_001-002 - Kontrola interakcie tláčítka Geografická poloha
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_GeografickaPoloha}  10 seconds
    Click Element  ${BUTTON_GeografickaPoloha}
    Sleep  20 milliseconds
    Location Should Be  ${URL_GeografickaPoloha}

TC_001_001_001-003 - Kontrola interakcie tláčítka História obce Krakovany
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_HistoriaObce}  10 seconds
    Click Element  ${BUTTON_HistoriaObce}
    Sleep  20 milliseconds
    Location Should Be  ${URL_HistoriaObce}

TC_001_001_001-004 - Kontrola interakcie tláčítka Monografia obce
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_MonografiaObce}  10 seconds
    Click Element  ${BUTTON_MonografiaObce}
    Sleep  20 milliseconds
    Location Should Be  ${URL_MonografiaObce}

TC_001_001_001-005 - Kontrola interakcie tláčítka Erb obce
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_ErbObce}  10 seconds
    Click Element  ${BUTTON_ErbObce}
    Sleep  20 milliseconds
    Location Should Be  ${URL_ErbObce}

TC_001_001_001-006 - Kontrola interakcie tláčítka Územný plán obce
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_UzemnyPlanObce}  10 seconds
    Click Element  ${BUTTON_UzemnyPlanObce}
    Sleep  20 milliseconds
    Location Should Be  ${URL_UzemnyPlanObce}

TC_001_001_001-007 - Kontrola interakcie tláčítka Program rozvoja obce
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_ProgramRozvojaObce}  10 seconds
    Click Element  ${BUTTON_ProgramRozvojaObce}
    Sleep  20 milliseconds
    Location Should Be  ${URL_ProgramRozvojaObce}

TC_001_001_001-008 - Kontrola interakcie tláčítka Prevádzkový poriadok Zberného dvora
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_PrevadzkovyPoriadokZbernehoDvora}  10 seconds
    Click Element  ${BUTTON_PrevadzkovyPoriadokZbernehoDvora}
    Sleep  20 milliseconds
    Location Should Be  ${URL_PrevadzkovyPoriadokZbernehoDvora}

TC_001_001_001-009 - Kontrola interakcie tláčítka Starosta obce
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_StarostaObce}  10 seconds
    Click Element  ${BUTTON_StarostaObce}
    Sleep  20 milliseconds
    Location Should Be  ${URL_StarostaObce}

TC_001_001_001-010 - Kontrola interakcie tláčítka Obecné zastupiteľstvo
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_ObecneZastupitelstvo}  10 seconds
    Click Element  ${BUTTON_ObecneZastupitelstvo}
    Sleep  20 milliseconds
    Location Should Be  ${URL_ObecneZastupitelstvo}

TC_001_001_001-011 - Kontrola interakcie tláčítka Obecná knižnica
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_ObecnaKniznica}  10 seconds
    Click Element  ${BUTTON_ObecnaKniznica}
    Sleep  20 milliseconds
    Location Should Be  ${URL_ObecnaKniznica}

TC_001_001_001-012 - Kontrola interakcie tláčítka Fotogaléria
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_Fotogaleria}  10 seconds
    Click Element  ${BUTTON_Fotogaleria}
    Sleep  20 milliseconds
    Location Should Be  ${URL_Fotogaleria}

TC_001_001_001-013 - Kontrola interakcie tláčítka Podnikateľské subjekty
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_PodnikatelskeSubjekty}  10 seconds
    Click Element  ${BUTTON_PodnikatelskeSubjekty}
    Sleep  20 milliseconds
    Location Should Be  ${URL_PodnikatelskeSubjekty}

TC_001_001_001-014 - Kontrola interakcie tláčítka Červ. kríž
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_CervenyKriz}  10 seconds
    Scroll Element Into View  ${BUTTON_CervenyKriz}
    Click Element  ${BUTTON_CervenyKriz}
    Sleep  20 milliseconds
    Location Should Be  ${URL_CervenyKriz}

TC_001_001_001-015 - Kontrola interakcie tláčítka Mikroregión
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_Mikroregion}  10 seconds
    Scroll Element Into View  ${BUTTON_Mikroregion}
    Click Element  ${BUTTON_Mikroregion}
    Sleep  20 milliseconds
    Location Should Be  ${URL_Mikroregion}

Post-conditions
    Close Browser