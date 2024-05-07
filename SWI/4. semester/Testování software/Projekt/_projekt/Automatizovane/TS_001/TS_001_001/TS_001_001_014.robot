*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  ../../Resources/Keywords.robot

Resource  ../../Resources/variables/Browsers.robot
Resource  ../../Resources/variables/URLs.robot
Resource  ../../Resources/variables/Inputs.robot
Resource  ../../Resources/variables/Values.robot
Resource  ../../Resources/variables/KeyboardKeys.robot
Resource  ../../Resources/variables/Headings.robot
Resource  ../../Resources/variables/Videos.robot
Resource  ../../Resources/variables/Iframes.robot
Resource  ../../Resources/variables/Buttons.robot
Resource  ../../Resources/variables/Spans.robot
Resource  ../../Resources/variables/Divs.robot
Resource  ../../Resources/variables/Anchors.robot


*** Test Cases ***
Pre-conditions
    Open EN Incognito Chrome Webdriver  ${URL_TvKrakovany}


TC_001_001_014-001 - Kontrola interakcie videa
    Wait Until Element Is Visible  ${IFRAME_Video}  10s
    Scroll Element Into View  ${IFRAME_Video}
    Element Attribute Value Should Be  ${IFRAME_Video}  ${VALUE_Src}  ${URL_Video_EmbededYT}
    Select Frame  ${IFRAME_Video}
    Button interaction  ${BUTTON_Video_PlayBig}
    Take Screenshot  TC_001_001_014-001


TC_001_001_014-002 - Kontrola tlačítka `Play`
    Button interaction  ${BUTTON_Video_Play}
    Element Attribute Value Should Be  ${BUTTON_Video_Play}  ${VALUE_AttributeDTNT}  ${VALUE_Play}
    Button interaction  ${BUTTON_Video_Play}
    Element Attribute Value Should Be  ${BUTTON_Video_Play}  ${VALUE_AttributeDTNT}  ${VALUE_Pause}


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
    Element Attribute Value Should Be  ${BUTTON_Video_Mute}  ${VALUE_AttributeDTNT}  ${VALUE_Unmute}
    Button interaction  ${BUTTON_Video_Mute}
    Element Attribute Value Should Be  ${BUTTON_Video_Mute}  ${VALUE_AttributeDTNT}  ${VALUE_Mute}


TC_001_001_014-006 - Kontrola funkcie `Play-back speed` a nastavenie rýchlosti prehrávania na 0.5
    Button interaction  ${BUTTON_Video_Settings}
    Set Selenium Speed  1
    Click Element  ${DIV_Video_PlayBackSpeed}
    Click Element  ${DIV_Video_PlayBackSpeed_05}
    Set Selenium Speed  0
    ${time_before} =  Get time from span YT video  ${SPAN_TimeCurrent}
    Sleep  4s
    ${time_after} =  Get time from span YT video  ${SPAN_TimeCurrent}
    ${time_diff} =  Subtract  ${time_after}  ${time_before}
    Log  ${time_diff}
    Should Be Equal As Numbers  ${time_diff}  2


TC_001_001_014-007 - Kontrola funkcie `Full-screen` a minimalizoavanie
    Button interaction  ${BUTTON_Video_FullScreen}
    Element Attribute Value Should Be  ${BUTTON_Video_FullScreen}  ${VALUE_AttributeTitle}  ${VALUE_ExitFullscreen}
    Take Screenshot  TC_001_001_014-007-FullScreen
    Button interaction  ${BUTTON_Video_FullScreen}
    Element Attribute Value Should Be  ${BUTTON_Video_FullScreen}  ${VALUE_AttributeTitle}  ${VALUE_FullScreen}
    Take Screenshot  TC_001_001_014-007-ExitFullScreen


TC_001_001_014-008 - Kontrola tlačítka `Quality` a zmena kvality na 144p
    Set Selenium Speed  0.5
    Mouse Over  ${VIDEO_TvKrakovany}
    Button interaction  ${BUTTON_Video_Play}
    Button interaction  ${DIV_MoviePlayer}
    Button interaction  ${DIV_Video_Quality} 
    Button interaction  ${DIV_Video_Quality_144}
    Button interaction  ${DIV_MoviePlayer}
    Wait Until Element Is Visible  ${SPAN_Quality}  30s
    ${text}=  Get Text  ${SPAN_Quality}
    Set Selenium Speed  0
    log  ${text}
    Should Be Equal  ${text}  ${VALUE_144p}
    Take Screenshot  TC_001_001_014-008


Post-conditions
    Close