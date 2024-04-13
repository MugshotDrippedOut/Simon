*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
*** Keywords ***
Open 
    [Arguments]  ${BROWSER}  ${URL}
    
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep   200ms


Open Incognito
    [Arguments]  ${BROWSER}  ${URL}
    
    Open Browser    ${URL}    ${BROWSER}    incognito=yes
    Maximize Browser Window
    Sleep   200ms


Close
    Sleep  200ms
    Close Browser


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


Kontrola funkcie Move
    [Arguments]  ${DIV}  ${KEY}  ${MATRIX}  ${VALUE}
    
    ${count}=  Convert To Integer  0
    WHILE  ${count} <= 5
        Press Keys  ${DIV}  ${KEY}
        ${count}=  Evaluate  ${count} + 1
    END
    ${matrix}=  Get Element Attribute  ${MATRIX}  style
    Log  ${matrix}
    Should Be Equal  ${matrix}  ${VALUE}
