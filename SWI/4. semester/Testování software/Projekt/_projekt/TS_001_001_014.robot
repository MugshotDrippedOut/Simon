- TS_001_001_014 - TV KRAKOVANY
    - TC_001_001_014-001 - Kontrola interakcie videa
    - TC_001_001_014-002 - Kontrola tlačítka `Play`
    - TC_001_001_014-003 - Kontrola funkcie posunutia vpred o 5 sekúnd
    - TC_001_001_014-004 - Kontrola funkcie posunutia vzad o 5 sekúnd
    - TC_001_001_014-005 - Kontrola tlačítka `Mute`
    - TC_001_001_014-006 - Kontrola funkcie `Play-back speed` a nastavenie rýchlosti prehrávania na 0.70 pomocou možnosti `Custom`
    - TC_001_001_014-007 - Kontrola funkcie `Full-screen` 
    - TC_001_001_014-008 - Kontrola tlačítka `Quality` a zmena kvality na 144p
    - TC_001_001_014-009 - Kontrola funkcie `Watch on YouTube` 
*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  Resources/variables/Inputs.robot
Resource  Resources/variables/Values.robot
Resource  Resources/variables/KeyboardKeys.robot
Resource  Resources/variables/Headings.robot
Resource  Resources/variables/Videos.robot
Resource  Resources/variables/Iframes.robot
Resource  Resources/variables/Buttons.robot
Resource  Resources/variables/Spans.robot
Resource  Resources/variables/Divs.robot


*** Test Cases ***
Pre-conditions
    Open EN Incognito Chrome Webdriver  ${URL_TvKrakovany}


TC_001_001_014-001 - Kontrola interakcie videa
    Wait Until Element Is Visible  ${IFRAME_Video}  10s
    Scroll Element Into View  ${IFRAME_Video}
    Select Frame  ${IFRAME_Video}
    Button interaction  ${BUTTON_Video_PlayBig}


TC_001_001_014-006 - Kontrola funkcie `Play-back speed` a nastavenie rýchlosti prehrávania na 0.70 pomocou možnosti `Custom`
    Button interaction  ${BUTTON_Video_Settings}
    Set Selenium Speed  1
    Click Element  ${DIV_Video_PlayBackSpeed}
    Click Element  ${DIV_Video_PlayBackSpeed_Custom}
    Drag And Drop By Offset  ${DIV_Video_PlayBackSpeed_Custom}  50  0
    Set Selenium Speed  0

TC_001_001_014-002 - Kontrola tlačítka `Play`
    Button interaction  ${BUTTON_Video_Play}
    Element Attribute Value Should Be  ${BUTTON_Video_Play}  data-title-no-tooltip  Play
    Button interaction  ${BUTTON_Video_Play}
    Element Attribute Value Should Be  ${BUTTON_Video_Play}  data-title-no-tooltip  Pause


TC_001_001_014-003 - Kontrola funkcie posunutia vpred o 5 sekúnd
    Button interaction  ${BUTTON_Video_Play}
    Button interaction  ${BUTTON_Video_ClosePopUp}
    ${time_before} =  Get time from span YT video  ${SPAN_TimeCurrent}
    Press Keys  ${VIDEO_TvKrakovany}  ${KEY_Right}
    ${time_after} =  Get time from span YT video  ${SPAN_TimeCurrent}
    ${time_diff} =  Subtract  ${time_after}  ${time_before}
    Log  ${time_diff}
    Should Be Equal As Numbers  ${time_diff}  5


TC_001_001_014-004 - Kontrola funkcie posunutia vzad o 5 sekúnd
    Button interaction  ${BUTTON_Video_Play}
    ${time_before} =  Get time from span YT video  ${SPAN_TimeCurrent}
    Press Keys  ${VIDEO_TvKrakovany}  ${KEY_Left}
    ${time_after} =  Get time from span YT video  ${SPAN_TimeCurrent}
    ${time_diff} =  Subtract  ${time_before}  ${time_after}
    Log  ${time_diff}
    Should Be Equal As Numbers  ${time_diff}  5


TC_001_001_014-005 - Kontrola tlačítka `Mute`
    Button interaction  ${BUTTON_Video_Mute}
    Element Attribute Value Should Be  ${BUTTON_Video_Mute}  data-title-no-tooltip  Unmute
    Button interaction  ${BUTTON_Video_Mute}
    Element Attribute Value Should Be  ${BUTTON_Video_Mute}  data-title-no-tooltip  Mute 


Post-conditions
    Close