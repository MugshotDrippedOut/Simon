*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  Resources/variables/Inputs.robot
Resource  Resources/variables/Values.robot
Resource  Resources/variables/KeyboardKeys.robot
Resource  Resources/variables/Headings.robot


*** Test Cases ***
Pre-conditions
    Open Incognito   ${BROWSER_CHROME}  ${URL_TvKrakovany}