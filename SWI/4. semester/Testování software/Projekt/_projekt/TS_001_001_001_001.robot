*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Resource  resources/keywords.robot
Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  resources/variables/Inputs.robot

*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds

TC_001_001_001_001-001 - Kontrola interakcie pola "Komentár"
    Open Browser  ${URL_ZakladneUdajeAKontakty} ${BROWSER_CHROME}
    Sleep  5 seconds

post conditions
    Close Browser