*** Keywords ***
Pre-condition
    [Arguments]  ${BROWSER}  ${URL}
    Open Browser    ${URL}    ${BROWSER}
    Sleep   200s