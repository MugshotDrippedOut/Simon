- TS_001_006 - Mapa
    - TC_001_006-001 - Kontrola zobrazenia mapy
    - TC_001_006-002 - Kontrola tlačítka `Zoom in`
    - TC_001_006-003 - Kontrola tlačítka `Zoom out`
    - TC_001_006-004 - Kontrola funkcie `Move left`
    - TC_001_006-005 - Kontrola funkcie `Move right`
    - TC_001_006-006 - Kontrola funkcie `Move up`
    - TC_001_006-007 - Kontrola funkcie `Move down`
    - TC_001_006-008 - Kontrola tlačítka `Show satellite imagery`
    - TC_001_006-009 - Kontrola tlačítka `Show street map`
    - TC_001_006-010 - Kontrola tlačítka `View larger map`


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
${DIV_Map_matrix_prmary}  position: absolute; z-index: 986; transform: matrix(1, 0, 0, 1, -2, -79);
${DIV_Map_matrix_zoom_in}  position: absolute; z-index: 985; transform: matrix(1, 0, 0, 1, -4, -158);
${DIV_Map_matrix_zoom_out}  position: absolute; z-index: 987; transform: matrix(1, 0, 0, 1, -1, -167);
${DIV_Map_matrix_move_left}  position: absolute; z-index: 986; transform: matrix(1, 0, 0, 1, -252, -79);
${DIV_Map_matrix_move_right}  position: absolute; z-index: 986; transform: matrix(1, 0, 0, 1, -2, -79);
${DIV_Map_matrix_move_up}  position: absolute; z-index: 986; transform: matrix(1, 0, 0, 1, -2, -73);
${DIV_Map_matrix_move_down}  position: absolute; z-index: 986; transform: matrix(1, 0, 0, 1, -2, -79);
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
    Wait Until Element Is Visible  ${BUTTON_ZoomIn}  10s
    Set Selenium Speed  0.5
    Click Element  ${BUTTON_ZoomIn}
    ${matrix}=  Get Element Attribute  ${DIV_Map_matrix}  style
    Should Be Equal  ${matrix}  ${DIV_Map_matrix_zoom_in}
    Set Selenium Speed  0


TC_001_006-003 - Kontrola tlačítka `Zoom out`
    Wait Until Element Is Visible  ${BUTTON_ZoomOut}  10s
    Set Selenium Speed  0.5
    Click Element  ${BUTTON_ZoomOut}
    Click Element  ${BUTTON_ZoomOut}
    ${matrix}=  Get Element Attribute  ${DIV_Map_matrix}  style
    Should Be Equal  ${matrix}  ${DIV_Map_matrix_zoom_out}
    Click Element  ${BUTTON_ZoomIn}
    Set Selenium Speed  0


TC_001_006-004 - Kontrola funkcie `Move left`
    Press Keys  ${DIV_Map_frame}  ARROW_LEFT
    ${count}=  Convert To Integer  0
    WHILE  ${count} < 5
        Press Keys  ${DIV_Map_frame}  ARROW_LEFT
        ${count}=  Evaluate  ${count} + 1
    END
    ${matrix}=  Get Element Attribute  ${DIV_Map_matrix}  style
    Log  ${matrix}
    Should Be Equal  ${matrix}  ${DIV_Map_matrix_move_left}

TC_001_006-005 - Kontrola funkcie `Move right`
    Press Keys  ${DIV_Map_frame}  ARROW_RIGHT
    ${count}=  Convert To Integer  0
    WHILE  ${count} < 5
        Press Keys  ${DIV_Map_frame}  ARROW_RIGHT
        ${count}=  Evaluate  ${count} + 1
    END
    ${matrix}=  Get Element Attribute  ${DIV_Map_matrix}  style
    Log  ${matrix}
    Should Be Equal  ${matrix}  ${DIV_Map_matrix_move_right}


TC_001_006-006 - Kontrola funkcie `Move up`
    Press Keys  ${DIV_Map_frame}  ARROW_UP
    ${count}=  Convert To Integer  0
    WHILE  ${count} < 5
        Press Keys  ${DIV_Map_frame}  ARROW_UP
        ${count}=  Evaluate  ${count} + 1
    END
    ${matrix}=  Get Element Attribute  ${DIV_Map_matrix}  style
    Log  ${matrix}
    Should Be Equal  ${matrix}  ${DIV_Map_matrix_move_up}


TC_001_006-007 - Kontrola funkcie `Move down`
    Press Keys  ${DIV_Map_frame}  ARROW_DOWN
    ${count}=  Convert To Integer  0
    WHILE  ${count} < 5
        Press Keys  ${DIV_Map_frame}  ARROW_DOWN
        ${count}=  Evaluate  ${count} + 1
    END
    ${matrix}=  Get Element Attribute  ${DIV_Map_matrix}  style
    Log  ${matrix}
    Should Be Equal  ${matrix}  ${DIV_Map_matrix_move_down}


TC_001_006-008 - Kontrola tlačítka `Show satellite imagery`
    Wait Until Element Is Visible  ${BUTTON_Satellite}  10s
    Set Selenium Speed  0.2
    Click Element  ${BUTTON_Satellite}
    Set Selenium Speed  0


TC_001_006-009 - Kontrola tlačítka `Show street map`
    Wait Until Element Is Visible  ${BUTTON_Street}  10s
    Set Selenium Speed  0.2
    Click Element  ${BUTTON_Street}
    Set Selenium Speed  0


TC_001_006-010 - Kontrola tlačítka `View larger map`
    Wait Until Element Is Visible  ${BUTTON_LargerMap}  10s
    Click Element  ${BUTTON_LargerMap}
    ${windows}=  Get Window Handles
    Switch Window  ${windows}[-1]
    Wait Until Element Is Visible  ${BUTTON_AcceptGoogle}  10s
    Click Element  ${BUTTON_AcceptGoogle}
    ${windows}=  Get Window Handles
    Switch Window  ${windows}[-1]
    

post conditions
    Set Selenium Speed  0
    Sleep  2 seconds
    Close Browser