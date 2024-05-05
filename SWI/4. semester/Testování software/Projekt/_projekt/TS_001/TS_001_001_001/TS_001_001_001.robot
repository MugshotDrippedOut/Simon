*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  ../../Resources/keywords.robot

Resource  ../../Resources/variables/Browsers.robot
Resource  ../../Resources/variables/URLs.robot
Resource  ../../Resources/variables/Inputs.robot
Resource  ../../Resources/variables/Buttons.robot
Resource  ../../Resources/variables/Values.robot
Resource  ../../Resources/variables/Lists.robot
Resource  ../../Resources/variables/Fonts.robot
Resource  ../../Resources/variables/Headings.robot


*** Test Cases ***
Pre-conditions
    Open EN Incognito Chrome Webdriver  ${URL_MainPage}


TC_001_001_001-001 - Kontrola interakcie tláčítka Základné údaje a kontakty
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ZakladneUdajeAkontakty}  ${URL_Obec_ZakladneUdajeAKontakty}  ${FONT_Obec_Heading}  ${VALUE_ZakladneUdajeaKontakty}  ${LIST_ThirdElement}  ${VALUE_ZakladneUdajeaKontakty} 


TC_001_001_001-002 - Kontrola interakcie tláčítka Geografická poloha
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_GeografickaPoloha}  ${URL_Obec_GeografickaPoloha}  ${FONT_Obec_Heading}  ${VALUE_GeografickaPoloha}  ${LIST_ThirdElement}  ${VALUE_GeografickaPoloha}


TC_001_001_001-003 - Kontrola interakcie tláčítka História obce Krakovany
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_HistoriaObce}  ${URL_Obec_HistoriaObce}  ${FONT_Obec_Heading}  ${VALUE_HistoriaObce}  ${LIST_ThirdElement}  ${VALUE_HistoriaObce}


TC_001_001_001-004 - Kontrola interakcie tláčítka Monografia obce
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_MonografiaObce}  ${URL_Obec_MonografiaObce}  ${FONT_Obec_Heading}  ${VALUE_MonografiaObce}  ${LIST_ThirdElement}  ${VALUE_MonografiaObce}


TC_001_001_001-005 - Kontrola interakcie tláčítka Erb obce
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ErbObce}  ${URL_Obec_ErbObce}  ${FONT_Obec_Heading}  ${VALUE_ErbObce}  ${LIST_ThirdElement}  ${VALUE_ErbObce}


TC_001_001_001-006 - Kontrola interakcie tláčítka Územný plán obce
    Button interaction main menu  ${BUTTON_Obec}  ${BUTTON_Obec_UzemnyPlanObce}  ${URL_Obec_UzemnyPlanObce}  ${FONT_Obec_Heading}  ${VALUE_UzemnyPlanObce}  ${LIST_ThirdElement}  ${VALUE_UzemnyPlanObce}


TC_001_001_001-007 - Kontrola interakcie tláčítka Program rozvoja obce
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ProgramRozvojaObce}  ${URL_Obec_ProgramRozvojaObce}  ${FONT_Obec_Heading}  ${VALUE_ProgramRozvojaObce}  ${LIST_ThirdElement}  ${VALUE_ProgramRozvojaObce}


TC_001_001_001-008 - Kontrola interakcie tláčítka Prevádzkový poriadok Zberného dvora
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_PrevadzkovyPoriadokZbernehoDvora}  ${URL_Obec_PrevadzkovyPoriadokZbernehoDvora}  ${FONT_Obec_Heading}  ${VALUE_PrevadzkovyPoriadokZbernehoDvora}  ${LIST_ThirdElement}  ${VALUE_PrevadzkovyPoriadokZbernehoDvora}


TC_001_001_001-009 - Kontrola interakcie tláčítka Starosta obce
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_StarostaObce}  ${URL_Obec_StarostaObce}  ${FONT_Obec_Heading}  ${VALUE_StarostaObce}  ${LIST_ThirdElement}  ${VALUE_StarostaObce}


TC_001_001_001-010 - Kontrola interakcie tláčítka Obecné zastupiteľstvo
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ObecneZastupitelstvo}  ${URL_Obec_ObecneZastupitelstvo}  ${FONT_Obec_Heading}  ${VALUE_ObecneZastupitelstvo}  ${LIST_ThirdElement}  ${VALUE_ObecneZastupitelstvo}


TC_001_001_001-011 - Kontrola interakcie tláčítka Obecná knižnica
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_ObecnaKniznica}  ${URL_Obec_ObecnaKniznica}  ${FONT_Obec_Heading}  ${VALUE_ObecnaKniznica}  ${LIST_FourthElement}  ${VALUE_ObecnaKniznica}


TC_001_001_001-012 - Kontrola interakcie tláčítka Fotogaléria
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_Fotogaleria}  ${URL_Obec_Fotogaleria}  ${FONT_Obec_Heading}  ${VALUE_Fotogaleria}  ${LIST_FourthElement}  ${VALUE_Fotogaleria}


TC_001_001_001-013 - Kontrola interakcie tláčítka Podnikateľské subjekty
    Button interaction main menu   ${BUTTON_Obec}  ${BUTTON_Obec_PodnikatelskeSubjekty}  ${URL_Obec_PodnikatelskeSubjekty}  ${FONT_Obec_Heading}  ${VALUE_PodnikateleSubjekty}  ${LIST_ThirdElement}  ${VALUE_PodnikateleSubjekty}


TC_001_001_001-014 - Kontrola interakcie tláčítka Červ. kríž
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_Obec_CervenyKriz}  10 seconds
    Scroll Element Into View  ${BUTTON_Obec_CervenyKriz}
    Click Element  ${BUTTON_Obec_CervenyKriz}
    Sleep  20 milliseconds
    Location Should Be  ${URL_Obec_CervenyKriz}
    Page Should Contain Element  ${FONT_Obec_Heading}
    Page Should Contain  ${VALUE_CervenyKriz}
    Page Should Contain Element  ${LIST_ThirdElement}
    Page Should Contain  ${VALUE_CervenyKriz}


TC_001_001_001-015 - Kontrola interakcie tláčítka Mikroregión
    Wait Until Element Is Visible  ${BUTTON_Obec}  10 seconds
    Mouse Over  ${BUTTON_Obec}
    Wait Until Element Is Visible  ${BUTTON_Obec_Mikroregion}  10 seconds
    Scroll Element Into View  ${BUTTON_Obec_Mikroregion}
    Click Element  ${BUTTON_Obec_Mikroregion}
    Sleep  20 milliseconds
    Location Should Be  ${URL_Obec_Mikroregion}
    Page Should Contain Element  ${HEADING_MikroregionNadHoleskou}
    Element Should Contain  ${HEADING_MikroregionNadHoleskou}  ${VALUE_MikroregionNadHoleskou}


Post-conditions
    Close Browser