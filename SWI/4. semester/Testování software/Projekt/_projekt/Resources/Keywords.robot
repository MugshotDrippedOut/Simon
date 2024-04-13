*** Keywords ***
Pre-condition
    [Arguments]  ${BROWSER}  ${URL}
    
    Open Browser    ${URL}    ${BROWSER}
    Sleep   200ms


Main menu button interaction check
    [Arguments]  ${BUTTON_MAIN}  ${BUTTON_SUB}  ${URL_TO_CHECK}
    
    Wait Until Element Is Visible  ${BUTTON_MAIN}  10 seconds
    Mouse Over  ${BUTTON_MAIN}
    Wait Until Element Is Visible  ${BUTTON_SUB}  10 seconds
    Scroll Element Into View  ${BUTTON_SUB}
    Click Element  ${BUTTON_SUB}
    Location Should Be  ${URL_TO_CHECK}

Button interaction check
    [Arguments]  ${BUTTON}
    
    Wait Until Element Is Visible  ${BUTTON}  10 seconds
    Set Selenium Speed  0.2
    Click Element  ${BUTTON}
    Set Selenium Speed  0