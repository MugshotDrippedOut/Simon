*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  ../../Resources/keywords.robot

Resource  ../../Resources/variables/Browsers.robot
Resource  ../../Resources/variables/URLs.robot
Resource  ../../Resources/variables/Images.robot
Resource  ../../Resources/variables/Iframes.robot
Resource  ../../Resources/variables/Buttons.robot
Resource  ../../Resources/variables/Divs.robot
Resource  ../../Resources/variables/Values.robot
Resource  ../../Resources/variables/KeyboardKeys.robot

*** Test Cases ***
Pre-conditions
    Open EN Incognito Chrome Webdriver  ${URL_MainPage}


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
    Should Be Equal  ${matrix}  ${VALUE_Map_matrix_zoom_in}
    Set Selenium Speed  0


TC_001_006-003 - Kontrola tlačítka `Zoom out`
    Wait Until Element Is Visible  ${BUTTON_ZoomOut}  10s
    Set Selenium Speed  0.5
    Click Element  ${BUTTON_ZoomOut}
    Click Element  ${BUTTON_ZoomOut}
    ${matrix}=  Get Element Attribute  ${DIV_Map_matrix}  style
    Should Be Equal  ${matrix}  ${VALUE_Map_matrix_zoom_out}
    Click Element  ${BUTTON_ZoomIn}
    Set Selenium Speed  0


TC_001_006-004 - Kontrola funkcie `Move left`
    Move functionality  ${DIV_Map_frame}  ${KEY_Left}  ${DIV_Map_matrix}  ${VALUE_Map_matrix_move_left}


TC_001_006-005 - Kontrola funkcie `Move right`
    Move functionality  ${DIV_Map_frame}  ${KEY_Right}  ${DIV_Map_matrix}  ${VALUE_Map_matrix_move_right}


TC_001_006-006 - Kontrola funkcie `Move up`
    Move functionality  ${DIV_Map_frame}  ${KEY_Up}  ${DIV_Map_matrix}  ${VALUE_Map_matrix_move_up}


TC_001_006-007 - Kontrola funkcie `Move down`
    Move functionality  ${DIV_Map_frame}  ${KEY_Down}  ${DIV_Map_matrix}  ${VALUE_Map_matrix_move_down}


TC_001_006-008 - Kontrola tlačítka `Show satellite imagery`
    Button interaction   ${BUTTON_Satellite}


TC_001_006-009 - Kontrola tlačítka `Show street map`
    Button interaction   ${BUTTON_Street}


TC_001_006-010 - Kontrola tlačítka `View larger map`
    Wait Until Element Is Visible  ${BUTTON_LargerMap}  10s
    Click Element  ${BUTTON_LargerMap}
    Switch Window  NEW
    Wait Until Element Is Visible  ${BUTTON_AcceptGoogle}  10s
    Scroll Element Into View  ${BUTTON_AcceptGoogle}
    Click Element  ${BUTTON_AcceptGoogle}
    Location Should Be  ${URL_GoogleMap}


Post-conditions
    Close