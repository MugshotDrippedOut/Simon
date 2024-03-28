*** Keywords ***

NazevKeywordy
    [Arguments]  ${PrvniLokalniPromenna}  ${DruhaLokalniPromenna}  ${TretiLokalniPromenna}

    Open Browse ....


Open Browser And Decline Cookies
    [Arguments]  ${Browser_local_variable}  ${URL_local_variable}  ${AcceptCookiesButton_local_variable}

    Open Browser  ${URL_local_variable}  ${Browser_local_variable}
    Wait Until Location Is  ${URL_local_variable}

    Wait Until Element Is Visible  ${AcceptCookiesButton_local_variable}
    Click Element  ${AcceptCookiesButton_local_variable}
    Element Should Not Be Visible  ${AcceptCookiesButton_local_variable}

Spat
    [Arguments]  ${PocetSekund}

    Sleep  ${PocetSekund}

Zadat Text Do Pole
    [Arguments]  ${InputField}  ${VkladanaHodnota}

    Wait Until Element Is Visible  ${InputField}
    Input Text  ${InputField}  ${VkladanaHodnota}

Kliknout A Zkontrolovat URL A Element
    [Arguments]  ${Tlacitko}  ${KontrolovanaURL}  ${KontrolovanyElement}
    Wait Until Element Is Visible  ${Tlacitko}
    Click Element  ${Tlacitko}
    Wait Until Location Contains  ${KontrolovanaURL}
    Element Should Be Visible  ${KontrolovanyElement}

