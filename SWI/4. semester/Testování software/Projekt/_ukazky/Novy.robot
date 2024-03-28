*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Resource  ObjektovyRepositar/Browsers.robot
Resource  ObjektovyRepositar/URLs.robot
Resource  ObjektovyRepositar/Buttons.robot
Resource  ObjektovyRepositar/Inputs.robot

*** Test Cases ***
Pre-conditions - Otevři hlavni stranku Google a odklikni Cookies
    Open Browser  ${URL_Google_MainPage_HTTPS}  ${Browser_Chrome}
    Wait Until Location Is  ${URL_Google_MainPage_HTTPS}
    Wait Until Element Is Visible  ${Button_PreConditions_OdmitnoutCookies_XPathCZ}
    Click Element  ${Button_PreConditions_OdmitnoutCookies_XPathCZ}
    Element Should Not Be Visible  ${Button_PreConditions_OdmitnoutCookies_XPathCZ}

TC_001 - Zkusíme vyhledat "Pepa"
    Wait Until Element Is Visible  ${Input_Google_MainPage_Vyhledani_XPathCZ}
    Input Text  ${Input_Google_MainPage_Vyhledani_XPathCZ}  Pepa
    #Press Keys  ${Input_Google_MainPage_Vyhledani_XPathCZ}  ENTER

    Wait Until Element Is Visible  ${Button_Google_MainPage_HledatGooglem_XPathCZ}
    Click Element  ${Button_Google_MainPage_HledatGooglem_XPathCZ}

    Wait Until Location Contains  ${URLPart_Google_Vyhledavani_Slovo-Pepa}

Post-conditions
    Close Browser

