*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/Keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  Resources/variables/Images.robot

*** Test Cases ***
Pre-conditions
    Open   ${BROWSER_CHROME}  ${URL_MainPage}

TC_001_004-001 - Kontrola obsahu cookies
    Wait Until Element Is Visible  ${IMAGE_Plus}  10s
    Click Element  ${IMAGE_Plus}
    Reload Page
    ${cookies_before} =  Get Cookie  name=fontSize
    Reload Page
    ${cookies_after} =  Get Cookie  name=fontSize
    Should Be Equal  ${cookies_before.value}  ${cookies_after.value}

post conditions
    Sleep  2 seconds
    Close Browser