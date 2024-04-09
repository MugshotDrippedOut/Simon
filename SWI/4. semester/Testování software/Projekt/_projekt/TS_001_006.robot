- TS_001_006 - Mapa
    - TC_001_006-001 - Kontrola zobrazenia mapy
    - TC_001_006-002 - Kontrola tlačítka `Zoom in`
    - TC_001_006-003 - Kontrola tlačítka `Zoom out`
    - TC_001_006-004 - Kontrola funkcie `Scroll in`
    - TC_001_006-005 - Kontrola funkcie `Scroll out`
    - TC_001_006-006 - Kontrola funkcie `Move left`
    - TC_001_006-007 - Kontrola funkcie `Move right`
    - TC_001_006-008 - Kontrola funkcie `Move up`
    - TC_001_006-009 - Kontrola funkcie `Move down`
    - TC_001_006-010 - Kontrola tlačítka `Show satellite imagery`
    - TC_001_006-011 - Kontrola tlačítka `Show street map`
    - TC_001_006-011 - Kontrola tlačítka `View larger map`

*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  Resources/variables/Images.robot
Resource  Resources/variables/Iframes.robot
Resource  Resources/variables/Buttons.robot
Resource  Resources/variables/Divs.robot

*** Variables ***
${DIV_Map_matrix}  

*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds
    Open Browser  ${URL_MainPage}  ${BROWSER_CHROME}

TC_001_006-001 - Kontrola zobrazenia mapy
    Wait Until Element Is Visible  ${IMAGE_Map}  10s
    Scroll Element Into View  ${IMAGE_Map}
    Set Selenium Speed  0.5
    Click Element  ${IMAGE_Map}
    Wait Until Element Is Visible  ${IFRAME_Map}  10s
    Scroll Element Into View  ${IFRAME_Map}
    Select Frame  ${IFRAME_Map}
    Set Selenium Speed  0

TC_001_006-002 - Kontrola tlačítka `Zoom in`
    ${MAP_matrix_before}=  Get Element Attribute  ${DIV_Map_matrix}  style
    Wait Until Element Is Visible  ${BUTTON_ZoomIn}  10s
    Click Element  ${BUTTON_ZoomIn}

TC_001_006-003 - Kontrola tlačítka `Zoom out`
    Wait Until Element Is Visible  ${BUTTON_ZoomOut}  10s
    Click Element  ${BUTTON_ZoomOut}

TC_001_006-004 - Kontrola funkcie `Scroll in`
    Press Keys  None  CTRL
    Execute JavaScript  window.scrollBy(0,500);

TC_001_006-005 - Kontrola funkcie `Scroll out`
    Press Keys  None  CTRL
    Execute JavaScript  window.scrollBy(0,-500);



post conditions
    Sleep  2 seconds
    Close Browser