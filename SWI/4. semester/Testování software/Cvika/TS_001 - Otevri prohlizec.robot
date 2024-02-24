*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

*** Variables ***
${ProhlizecChrome}  Chrome
${URL}  https://www.google.com

*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds

TC_001 - Otevři browser chrome a jdi na adresu
    Open Browser  ${URL}  ${ProhlizecChrome}
    Sleep  2 seconds

Post-conditions
    Close Browser