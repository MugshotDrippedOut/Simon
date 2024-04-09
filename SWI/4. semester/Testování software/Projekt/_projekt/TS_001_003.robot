# TS_001_003 - Testovanie zmeny zobrazenie
#    - TC_001_003-001 - Kontorla interakcie s tlačítkom "+"
#    - TC_001_003-002 - Kontorla interakcie s tlačítkom "-"
#    - TC_001_003-003 - Kontorla interakcie s tlačítkom "100%"


*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  Resources/variables/Texts.robot
Resource  Resources/variables/Images.robot



*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds
    Open Browser  ${URL_MainPage}  ${BROWSER_CHROME}
    Wait Until Element Is Visible  ${TEXT_Vitam}  10s
    

TC_001_003-001 - Kontorla interakcie s tlačítkom "+"
    Click Element  ${IMAGE_Plus}
    ${font_size}=  Get Element Attribute  ${TEXT_Vitam}  style
    Should Be Equal  ${font_size}  font-size: 110%;

TC_001_003-002 - Kontorla interakcie s tlačítkom "-"
    Click Element  ${IMAGE_Minus}
    Click Element  ${IMAGE_Minus}
    ${font_size}=  Get Element Attribute  ${TEXT_Vitam}  style
    Should Be Equal  ${font_size}  font-size: 90%;

TC_001_003-003 - Kontorla interakcie s tlačítkom "100%"
    Click Element  ${IMAGE_100}
    ${font_size}=  Get Element Attribute  ${TEXT_Vitam}  style
    Should Be Equal  ${font_size}  font-size: 100%;

post conditions
    Sleep  2 seconds
    Close Browser