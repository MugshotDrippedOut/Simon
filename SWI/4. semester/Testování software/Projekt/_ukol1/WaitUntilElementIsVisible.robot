*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing


*** Variables ***
${BROWSER}  Chrome
${URL}  https://www.krakovany.sk
${HEADER_XPATH}  //*[@id="header"]


*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds


TC_001 - Wait Until Header Is Visible
    Open Browser  ${URL}  ${BROWSER}
    Wait Until Element Is Visible  ${HEADER_XPATH}  5s


Post-conditions
    Close Browser