*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Resource  resources/keywords.robot
Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  resources/variables/Inputs.robot

*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds
    Open Browser  ${URL_ZakladneUdajeAKontakty}  ${BROWSER_CHROME}

TC_001_001_001_001-001 - Kontrola interakcie pola "Komentár"
    Sleep  5 seconds

post conditions
    Close Browser