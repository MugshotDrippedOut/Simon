# TS_001_003 - Testovanie zmeny zobrazenie
#    - TC_001_003-001 - Kontorla interakcie s tlačítkom "+"
#    - TC_001_003-002 - Kontorla interakcie s tlačítkom "-"
#    - TC_001_003-003 - Kontorla interakcie s tlačítkom "100%"


*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  resources/variables/Inputs.robot
Resource  resources/variables/Buttons.robot
Resource  Resources/variables/Texts.robot

*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds
    Open Browser  ${URL_MainPage}  ${BROWSER_CHROME}

TC_001_003-001 - Kontorla interakcie s tlačítkom "+"
    Wait Until Element Is Visible  ${tVitam}  10s
    ${element}=  Get Webelement  ${tVitam}
    ${style_before}=  Execute JavaScript  return window.getComputedStyle(arguments[0]).fontSize;  ARGUMENTS  ${element}
    ${font_size_before}=  Convert To Number  ${style_before.split('px')[0]}  # Extract font size from style attribute
    Log  Font size before clicking is: ${font_size_before}
    Click Element  ${bPlus}
    Wait Until Element Is Visible  ${tVitam}  10s
    ${style_after}=  Execute JavaScript  return window.getComputedStyle(arguments[0]).fontSize;  ARGUMENTS  ${element}
    ${font_size_after}=  Convert To Number  ${style_after.split('px')[0]}  # Extract font size from style attribute
    Log  Font size after clicking is: ${font_size_after}
    Should Be True  ${font_size_after} > ${font_size_before}

post conditions
    Sleep  2 seconds
    Close Browser