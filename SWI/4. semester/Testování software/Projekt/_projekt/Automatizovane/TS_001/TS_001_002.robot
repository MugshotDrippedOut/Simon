*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  ../resources/Keywords.robot

Resource  ../resources/variables/Browsers.robot
Resource  ../resources/variables/URLs.robot
Resource  ../Resources/variables/Inputs.robot
Resource  ../Resources/variables/Values.robot
Resource  ../Resources/variables/KeyboardKeys.robot
Resource  ../Resources/variables/Headings.robot


*** Test Cases ***
Pre-conditions
    Open Incognito   ${BROWSER_CHROME}  ${URL_MainPage}

TC_001_002-001 - Kontrola interakcie vstupu `Vyhľadávanie`
    Wait Until Element Is Visible  ${INPUT_Search}  10s
    Input Text  ${INPUT_Search}  ${VALUE_Search}
    Press Keys  ${INPUT_Search}  ${KEY_Enter}
    Wait Until Element Is Visible  ${HEADING_SearchResults1}  10s
    @{HEADING_SearchResults}=  Create List  ${HEADING_SearchResults1}  ${HEADING_SearchResults2}  ${HEADING_SearchResults3}  ${HEADING_SearchResults4}  ${HEADING_SearchResults5}  ${HEADING_SearchResults6}  ${HEADING_SearchResults7}
    FOR  ${element}  IN  @{HEADING_SearchResults}
        ${TEXT}=  Get Text  ${element}
        ${TEXT}=  Convert To Lowercase  ${TEXT}
        Should Contain  ${TEXT}  ${VALUE_SearchResults}
    END
    Take Screenshot  TC_001_002-001
    

Post-conditions
    Close