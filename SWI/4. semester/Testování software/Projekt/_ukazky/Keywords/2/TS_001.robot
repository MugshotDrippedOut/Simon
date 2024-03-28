*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Resource  Browsers.robot
Resource  URLs.robot
Resource  Buttons.robot
Resource  Inputs.robot
Resource  Values.robot
Resource  HeadingsAndTitles.robot
Resource  Keywords.robot

*** Test Cases ***
Pre-conditions
    Otevri prohlizec a Zajdi na hlavni stranku a Zaloguje se a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage_Gmail}  ${Heading_GmailLoginPage_XPathCZ}  ${Input_GmailLoginPage_Login_XPath}  ${Input_GmailLoginPage_Password_XPath}  ${Value_ValidLogin}  ${Value_ValidPassword}  ${Button_GmailLoginPage_Dalsi_XPathCZ}  ${Value_Checking_Email_XPath}

Post-condtions
    Close Browser


