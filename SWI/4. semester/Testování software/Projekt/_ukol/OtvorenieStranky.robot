*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

*** Variables ***
${BROWSER}  Chrome
${URL}  https://www.krakovany.sk

*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds

TC_001 - Otevři browser chrome a jdi na adresu
    Open Browser  ${URL}  ${BROWSER}
    Sleep  5 seconds

Post-conditions
    Close Browser