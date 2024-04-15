*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  Resources/variables/P.robot
Resource  Resources/variables/Images.robot
Resource  Resources/variables/Values.robot



*** Test Cases ***
Pre-conditions
    Open EN Incognito Chrome Webdriver  ${URL_MainPage}
    Wait Until Element Is Visible  ${P_Vitam}  10s
    

TC_001_003-001 - Kontorla interakcie s tlačítkom "+"
    Click Element  ${IMAGE_Plus}
    ${font_size}=  Get Element Attribute  ${P_Vitam}  ${VALUE_AttributeStyle}
    Should Be Equal  ${font_size}  ${VALUE_FontSizeLarge} 

TC_001_003-002 - Kontorla interakcie s tlačítkom "-"
    Click Element  ${IMAGE_Minus}
    Click Element  ${IMAGE_Minus}
    ${font_size}=  Get Element Attribute  ${P_Vitam}  ${VALUE_AttributeStyle}
    Should Be Equal  ${font_size}  ${VALUE_FontSizeSmall} 

TC_001_003-003 - Kontorla interakcie s tlačítkom "100%"
    Click Element  ${IMAGE_100}
    ${font_size}=  Get Element Attribute  ${P_Vitam}  ${VALUE_AttributeStyle}
    Should Be Equal  ${font_size}  ${VALUE_FontSizeNormal}

Post-conditions
    Close