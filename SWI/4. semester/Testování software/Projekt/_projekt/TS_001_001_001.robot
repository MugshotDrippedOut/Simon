*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  resources/variables/Inputs.robot
Resource  resources/variables/Buttons.robot


*** Test Cases ***
Pre-conditions
    Open   ${BROWSER_Chrome}  ${URL_MainPage}


TC_001_001_001-001 - Kontrola interakcie tláčítka Základné údaje a kontakty
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ZakladneUdajeAkontakty}  ${URL_Obec_ZakladneUdajeAKontakty}


TC_001_001_001-002 - Kontrola interakcie tláčítka Geografická poloha
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_GeografickaPoloha}  ${URL_Obec_GeografickaPoloha}


TC_001_001_001-003 - Kontrola interakcie tláčítka História obce Krakovany
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_HistoriaObce}  ${URL_Obec_HistoriaObce}


TC_001_001_001-004 - Kontrola interakcie tláčítka Monografia obce
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_MonografiaObce}  ${URL_Obec_MonografiaObce}


TC_001_001_001-005 - Kontrola interakcie tláčítka Erb obce
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ErbObce}  ${URL_Obec_ErbObce}


TC_001_001_001-006 - Kontrola interakBUTTON_Obec_ZakladneUdajeAkontakty
    Button interaction main menu  ${BUTTON_Obec}  ${BUTTON_Obec_UzemnyPlanObce}  ${URL_Obec_UzemnyPlanObce}    


TC_001_001_001-007 - Kontrola interakcie tláčítka Program rozvoja obce
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ProgramRozvojaObce}  ${URL_Obec_ProgramRozvojaObce}


TC_001_001_001-008 - Kontrola interakcie tláčítka Prevádzkový poriadok Zberného dvora
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_PrevadzkovyPoriadokZbernehoDvora}  ${URL_Obec_PrevadzkovyPoriadokZbernehoDvora}


TC_001_001_001-009 - Kontrola interakcie tláčítka Starosta obce
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_StarostaObce}  ${URL_Obec_StarostaObce}


TC_001_001_001-010 - Kontrola interakcie tláčítka Obecné zastupiteľstvo
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ObecneZastupitelstvo}  ${URL_Obec_ObecneZastupitelstvo}


TC_001_001_001-011 - Kontrola interakcie tláčítka Obecná knižnica
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ObecnaKniznica}  ${URL_Obec_ObecnaKniznica}


TC_001_001_001-012 - Kontrola interakcie tláčítka Fotogaléria
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_Fotogaleria}  ${URL_Obec_Fotogaleria}


TC_001_001_001-013 - Kontrola interakcie tláčítka Podnikateľské subjekty
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_PodnikatelskeSubjekty}  ${URL_Obec_PodnikatelskeSubjekty}


TC_001_001_001-014 - Kontrola interakcie tláčítka Červ. kríž
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_Obec_CervenyKriz}  10 seconds
    Scroll Element Into View  ${BUTTON_Obec_CervenyKriz}
    Click Element  ${BUTTON_Obec_CervenyKriz}
    Sleep  20 milliseconds
    Location Should Be  ${URL_Obec_CervenyKriz}


TC_001_001_001-015 - Kontrola interakcie tláčítka Mikroregión
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_Obec_Mikroregion}  10 seconds
    Scroll Element Into View  ${BUTTON_Obec_Mikroregion}
    Click Element  ${BUTTON_Obec_Mikroregion}
    Sleep  20 milliseconds
    Location Should Be  ${URL_Obec_Mikroregion}


Post-conditions
    Close Browser