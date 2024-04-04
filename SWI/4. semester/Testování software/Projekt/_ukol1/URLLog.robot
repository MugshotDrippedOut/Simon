*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

*** Variables ***
${BROWSER}  Chrome
${URL}  https://www.krakovany.sk
${LINK_XPATH}  //*[@id="menu-hlavne-1"]/li[12]/a

*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds

TC_001 - Click Link and Log URL
    Open Browser  ${URL}  ${BROWSER}
    Click Link  ${LINK_XPATH}
    ${current_url}=  Get Location
    Log  Current URL is: ${current_url}

Post-conditions
    Close Browser