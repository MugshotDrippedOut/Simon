*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Resource  Browsers.robot
Resource  URLs.robot
Resource  Buttons.robot
Resource  Inputs.robot
Resource  Values.robot
Resource  HeadingsAndTitles.robot
Resource  Keywords.robot
Resource  KeyboardKeys.robot

*** Test Cases ***
Pre-conditions
    Otevri prohlizec a Zajdi na hlavni stranku a Zaloguje se a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage_Gmail}  ${Heading_GmailLoginPage_XPathCZ}  ${Input_GmailLoginPage_Login_XPath}  ${Input_GmailLoginPage_Password_XPath}  ${Value_ValidLogin}  ${Value_ValidPassword}  ${Button_GmailLoginPage_Dalsi_XPathCZ}  ${Value_Checking_Email_XPath}

TC - 001 -> Vyzkouset hledani na Googlu
    Zajdi na Google a vyhledej Text a Zkontroluj  ${URL_MainPage_Google}  ${Input_GoogleMainPage_Hledat_XPathCZ}  ${Input_GoogleMainPage_Hledat_XPathCZ}  ${Value_HledanyText}  ${Key_ENTER}  ${Value_HledanyText_Kontrola_XPathCZ}

Post-condtions
    Close Browser


