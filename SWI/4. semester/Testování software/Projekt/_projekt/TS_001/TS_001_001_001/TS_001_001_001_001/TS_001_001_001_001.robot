*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  ../../../Resources/keywords.robot

Resource  ../../../Resources/variables/Browsers.robot
Resource  ../../../Resources/variables/URLs.robot
Resource  ../../../Resources/variables/Inputs.robot
Resource  ../../../Resources/variables/Buttons.robot
Resource  ../../../Resources/variables/Values.robot
Resource  ../../../Resources/variables/Fonts.robot


*** Test Cases ***
Pre-conditions
    Open  ${BROWSER_CHROME}  ${URL_Obec_ZakladneUdajeAKontakty}
    Wait Until Element Contains  ${FONT_Obec_Header}  ${VALUE_ZakladneUdajeaKontakty}


TC_001_001_001_001-001 - Kontrola interakcie pola "Komentár"
    Input interaction  ${INPUT_Komentar}  ${VALUE_Komentar}
    Element Should Be Focused  ${INPUT_Komentar}

TC_001_001_001_001-002 - Kontrola interakcie pola "Meno"
    Input interaction  ${INPUT_Meno}  ${VALUE_Meno}
    Element Should Be Focused  ${INPUT_Meno}

TC_001_001_001_001-003 - Kontrola interakcie pola "E-mail"
    Input interaction  ${INPUT_Email}  ${VALUE_Email}
    Element Should Be Focused  ${INPUT_Email}

TC_001_001_001_001-004 - Kontrola interakcie pola "Adresa webu"
    Input interaction  ${INPUT_AdresaWebu}  ${VALUE_AdresaWebu}
    Element Should Be Focused  ${INPUT_AdresaWebu}

TC_001_001_001_001-005 - Kontrola interakcie tlačidla "Pridať komentár"
    Wait Until Element Is Visible  ${BUTTON_PridatKomentar}  2 seconds
    #Click Element  ${bPridatKomentar}
    Wait Until Keyword Succeeds  2 seconds  1 seconds  Wait Until Element Contains  ${FONT_Obec_Header}  ${VALUE_ZakladneUdajeaKontakty}


Post-conditions
    Close