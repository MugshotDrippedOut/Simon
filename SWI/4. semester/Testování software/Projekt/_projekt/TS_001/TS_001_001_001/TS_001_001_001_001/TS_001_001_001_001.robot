*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  ../../../Resources/keywords.robot

Resource  ../../../Resources/variables/Browsers.robot
Resource  ../../../Resources/variables/URLs.robot
Resource  ../../../Resources/variables/Inputs.robot
Resource  ../../../Resources/variables/Buttons.robot
Resource  ../../../Resources/variables/Values.robot


*** Test Cases ***
Pre-conditions
    Open  ${BROWSER_CHROME}  ${URL_Obec_ZakladneUdajeAKontakty}  

TC_001_001_001_001-001 - Kontrola interakcie pola "Komentár"
    Input interaction  ${INPUT_Komentar}  ${VALUE_Komentar}

TC_001_001_001_001-002 - Kontrola interakcie pola "Meno"
    Input interaction  ${INPUT_Meno}  ${VALUE_Meno}

TC_001_001_001_001-003 - Kontrola interakcie pola "E-mail"
    Input interaction  ${INPUT_Email}  ${VALUE_Email}

TC_001_001_001_001-004 - Kontrola interakcie pola "Adresa webu"
    Input interaction  ${INPUT_AdresaWebu}  ${VALUE_AdresaWebu}

TC_001_001_001_001-005 - Kontrola interakcie tlačidla "Pridať komentár"
    Wait Until Element Is Visible  ${BUTTON_PridatKomentar}  2 seconds
    #Click Element  ${bPridatKomentar}

Post-conditions
    Close