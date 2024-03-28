*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Resource  Browsers.robot
Resource  URLs.robot
Resource  Buttons.robot
Resource  Values.robot
Resource  Inputs.robot
Resource  Keywords.robot

*** Test Cases ***
Pre-conditions
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_MainPage_Login_XPath}

Kontrola prihlaseni - Nevalidni login + heslo
    Zaloguj a Zkontroluj  ${Input_MainPage_Login_XPath}  ${Value_NevalidniLogin}  ${Input_MainPage_Password_XPath}  ${Value_NevalidniHeslo}  ${Button_MainPage_Login_XPath}  ${Button_BadCredentialsPage_Login_XPath}  ${URL_BadCredentials_Part}

Post-conditions
    Close Browser

