*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Resource  Browsers.robot
Resource  URLs.robot
Resource  Inputs.robot
Resource  Keywords.robot

*** Test Cases ***
Pre-conditions
    Otevri Browser a Zajdi na hlavni stranku a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Input_MainPage_SearchInput_XPath}

Post-conditions
    Close Browser

