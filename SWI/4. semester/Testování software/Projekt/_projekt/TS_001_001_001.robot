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
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_ZakladneUdajeAkontakty}  ${URL_ZakladneUdajeAkontakty}


TC_001_001_001-002 - Kontrola interakcie tláčítka Geografická poloha
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_GeografickaPoloha}  ${URL_GeografickaPoloha}


TC_001_001_001-003 - Kontrola interakcie tláčítka História obce Krakovany
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_HistoriaObce}  ${URL_HistoriaObce}


TC_001_001_001-004 - Kontrola interakcie tláčítka Monografia obce
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_MonografiaObce}  ${URL_MonografiaObce}


TC_001_001_001-005 - Kontrola interakcie tláčítka Erb obce
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_ErbObce}  ${URL_ErbObce}


TC_001_001_001-006 - Kontrola interakBUTTON_Obec_ZakladneUdajeAkontakty
    Main menu button BUTTON_Obec_ZakladneUdajeAkontaktybec}  ${BUTTON_Obec_UzemnyPlanObce}  ${URL_UzemnyPlanObce}    


TC_001_001_001-007 - Kontrola interakcie tláčítka Program rozvoja obce
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_ProgramRozvojaObce}  ${URL_ProgramRozvojaObce}


TC_001_001_001-008 - Kontrola interakcie tláčítka Prevádzkový poriadok Zberného dvora
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_PrevadzkovyPoriadokZbernehoDvora}  ${URL_PrevadzkovyPoriadokZbernehoDvora}


TC_001_001_001-009 - Kontrola interakcie tláčítka Starosta obce
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_StarostaObce}  ${URL_StarostaObce}


TC_001_001_001-010 - Kontrola interakcie tláčítka Obecné zastupiteľstvo
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_ObecneZastupitelstvo}  ${URL_ObecneZastupitelstvo}


TC_001_001_001-011 - Kontrola interakcie tláčítka Obecná knižnica
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_ObecnaKniznica}  ${URL_ObecnaKniznica}


TC_001_001_001-012 - Kontrola interakcie tláčítka Fotogaléria
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_Fotogaleria}  ${URL_Fotogaleria}


TC_001_001_001-013 - Kontrola interakcie tláčítka Podnikateľské subjekty
    Main menu button interaction check  ${BUTTON_Obec}  ${BUTTON_Obec_PodnikatelskeSubjekty}  ${URL_PodnikatelskeSubjekty}


TC_001_001_001-014 - Kontrola interakcie tláčítka Červ. kríž
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_Obec_CervenyKriz}  10 seconds
    Scroll Element Into View  ${BUTTON_Obec_CervenyKriz}
    Click Element  ${BUTTON_Obec_CervenyKriz}
    Sleep  20 milliseconds
    Location Should Be  ${URL_CervenyKriz}


TC_001_001_001-015 - Kontrola interakcie tláčítka Mikroregión
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_Obec_Mikroregion}  10 seconds
    Scroll Element Into View  ${BUTTON_Obec_Mikroregion}
    Click Element  ${BUTTON_Obec_Mikroregion}
    Sleep  20 milliseconds
    Location Should Be  ${URL_Mikroregion}


Post-conditions
    Close Browser