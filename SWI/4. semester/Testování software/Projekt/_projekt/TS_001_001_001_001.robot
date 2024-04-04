*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  resources/variables/Inputs.robot
Resource  resources/variables/Buttons.robot

*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds
    Open Browser  ${URL_ZakladneUdajeAKontakty}  ${BROWSER_CHROME}

TC_001_001_001_001-001 - Kontrola interakcie pola "Komentár"
    Wait Until Element Is Visible  ${iKomentar}  2 seconds
    Input Text  ${iKomentar}  This is a test comment

TC_001_001_001_001-002 - Kontrola interakcie pola "Meno"
    Wait Until Element Is Visible  ${iMeno}  2 seconds
    Input Text  ${iMeno}  Test Name

TC_001_001_001_001-003 - Kontrola interakcie pola "E-mail"
    Wait Until Element Is Visible  ${iEmail}  2 seconds
    Input Text  ${iEmail}  test@vevja.sg

TC_001_001_001_001-004 - Kontrola interakcie pola "Adresa webu"
    Wait Until Element Is Visible  ${iAdresaWebu}  2 seconds
    Input Text  ${iAdresaWebu}  www.test.com

TC_001_001_001_001-005 - Kontrola interakcie tlačidla "Pridať komentár"
    Wait Until Element Is Visible  ${bPridatKomentar}  2 seconds
    #Click Element  ${bPridatKomentar}

post conditions
    Sleep  2 seconds
    Close Browser