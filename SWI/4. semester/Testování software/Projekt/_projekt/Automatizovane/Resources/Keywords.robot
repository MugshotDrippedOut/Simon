*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

*** Keywords ***
Open 
    [Arguments]  ${BROWSER}  ${URL}
    
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep   200ms


Open Incognito
    [Arguments]  ${BROWSER}  ${URL}
    
    Open Browser    ${URL}    ${BROWSER}    incognito=yes
    Maximize Browser Window
    Sleep   200ms

Open EN Incognito Chrome Webdriver
    [Arguments]  ${URL}
    [Documentation]  Open Chrome browser in incognito mode with English language
    ${chrome_options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    ${prefs}=  Create Dictionary  intl.accept_languages  en
    Call Method  ${chrome_options}  add_experimental_option  prefs  ${prefs}
    Call Method  ${chrome_options}  add_argument  --incognito
    Create WebDriver  Chrome  options=${chrome_options}
    Go To  ${URL}
    Maximize Browser Window


Close
    Sleep  200ms
    Close Browser

Take Screenshot
    [Arguments]  ${NAME}
    [Documentation]  take screenshot of the page and save it in the Screenshots folder
    Capture Page Screenshot  Screenshots/${NAME}.png


Button interaction main menu 
    [Arguments]  ${BUTTON_MAIN}  ${BUTTON_SUB}  ${URL_TO_CHECK}  ${HEADER_LOCATOR}  ${HEADER_TEXT}  ${LIST_LOCATOR}  ${LIST_TEXT}

    Wait Until Element Is Visible  ${BUTTON_MAIN}  10 seconds
    Mouse Over  ${BUTTON_MAIN}
    Wait Until Element Is Visible  ${BUTTON_SUB}  10 seconds
    Scroll Element Into View  ${BUTTON_SUB}
    Click Element  ${BUTTON_SUB}
    Location Should Be  ${URL_TO_CHECK}
    Page Should Contain Element  ${HEADER_LOCATOR}
    Element Should Contain  ${HEADER_LOCATOR}  ${HEADER_TEXT}
    Page Should Contain Element  ${LIST_LOCATOR}
    Element Should Contain  ${LIST_LOCATOR}  ${LIST_TEXT}

Button interaction 
    [Arguments]  ${BUTTON}

    Wait Until Element Is Visible  ${BUTTON}  15 seconds
    Set Selenium Speed  0.2
    Click Element  ${BUTTON}
    Set Selenium Speed  0


Input interaction
    [Arguments]  ${INPUT}  ${VALUE}
    [Documentation]  Input text into input field
    Wait Until Element Is Visible  ${INPUT}  10 seconds
    Input Text  ${INPUT}  ${VALUE}


Move functionality
    [Arguments]  ${DIV}  ${KEY}  ${MATRIX}  ${VALUE}

    ${count}=  Convert To Integer  0
    WHILE  ${count} <= 5
        Press Keys  ${DIV}  ${KEY}
        ${count}=  Evaluate  ${count} + 1
    END
    ${matrix}=  Get Element Attribute  ${MATRIX}  style
    Log  ${matrix}
    Should Be Equal  ${matrix}  ${VALUE}


Convert To Lowercase
    [Arguments]  ${TEXT}
    [Documentation]  Convert text to lowercase
    ${lowercase_text}=  Execute Javascript  return arguments[0].toLowerCase();  ARGUMENTS  ${TEXT}
    Log  ${lowercase_text}
    RETURN  ${lowercase_text}


Get Last Two Characters
    [Arguments]  ${TEXT}
    [Documentation]  Get last two characters from string
    ${first_two_characters}=  Execute Javascript  return arguments[0].slice(-2);  ARGUMENTS  ${TEXT}
    Log  ${first_two_characters}
    RETURN  ${first_two_characters}


Subtract
    [Arguments]  ${VALUE1}  ${VALUE2}
    [Documentation]  Subtract two values
    ${result}=  Evaluate  ${VALUE1} - ${VALUE2}
    Log  ${result}
    RETURN  ${result}


Get time from span YT video
    [Arguments]  ${SPAN}
    [Documentation]  Get time from span element
    ${time}=  Get Text  ${SPAN}
    ${time}=  Get Last Two Characters  ${time}
    ${time}=  Convert To Integer  ${time}
    Log  ${time}
    RETURN  ${time}


Should Be Equal or Heigher
    [Arguments]  ${VALUE1}  ${VALUE2}
    [Documentation]  Check if value1 is heigher or equal to value2
    Should Be True  ${VALUE1} >= ${VALUE2}


Should Be In Range
    [Arguments]  ${VALUE}  ${MIN}  ${MAX}
    [Documentation]  Check if value is in range
    Should Be True  ${VALUE} >= ${MIN}
    Should Be True  ${VALUE} <= ${MAX}