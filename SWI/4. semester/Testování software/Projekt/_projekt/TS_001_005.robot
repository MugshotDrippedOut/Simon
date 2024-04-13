- TS_001_005 - Kontrola Generovania Elementov
    - TC_001_005-001 - Kontrola, či sú všetky očakávané `div` elementy prítomné
    - TC_001_005-002 - Kontrola, či sú všetky očakávané `img` elementy prítomné a či majú správne nastavené `src` a `alt` atribúty
    - TC_001_005-003 - Kontrola, či sú všetky očakávané `a` elementy prítomné 
    - TC_001_005-004 - Kontrola, či sú všetky očakávané `input` elementy prítomné a či majú správne nastavené `type` a `name` atribúty

*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  resources/keywords.robot

Resource  resources/variables/Browsers.robot
Resource  resources/variables/URLs.robot
Resource  resources/variables/Inputs.robot
Resource  Resources/variables/Images.robot


*** Test Cases ***
Pre-conditions
    Sleep  200 milliseconds
    Open Browser  ${URL_MainPage}  ${BROWSER_CHROME}

TC_001_005-001 - Kontrola, či sú všetky očakávané `div` elementy prítomné
    ${divs} =  Get Element Count  locator=//div
    Should Be Equal As Numbers  ${divs}  259

TC_001_005-002 - Kontrola, či sú všetky očakávané `img` elementy prítomné a či majú správne nastavené `src` a `alt` atribúty
    ${images_count}=  Get Element Count  locator=//img
    Should Be Equal As Numbers  ${images_count}  24
    ${images}=  Create List  ${IMAGE_ObecKrakovany}  ${IMAGE_Print}  ${IMAGE_Starosta}  ${IMAGE_Map}  ${IMAGE_Plus}  ${IMAGE_Minus}  ${IMAGE_100}  ${IMAGE_Dcom}  ${IMAGE_Mobec}  ${IMAGE_Lsvr}  ${IMAGE_Zmaos}  ${IMAGE_Zmo}  ${IMAGE_Mnh}
    ${srcs}=  Create List  ${IMAGE_ObecKrakovany_src}  ${IMAGE_Print_src}  ${IMAGE_Starosta_src}  ${IMAGE_Map_src}  ${IMAGE_Plus_src}  ${IMAGE_Minus_src}  ${IMAGE_100_src}  ${IMAGE_Dcom_src}  ${IMAGE_Mobec_src}  ${IMAGE_Lsvr_src}  ${IMAGE_Zmaos_src}  ${IMAGE_Zmo_src}  ${IMAGE_Mnh_src}
    ${alts}=  Create List  ${IMAGE_ObecKrakovany_alt}  ${IMAGE_Print_alt}  ${IMAGE_Starosta_alt}  ${IMAGE_Map_alt}  ${IMAGE_Plus_alt}  ${IMAGE_Minus_alt}  ${IMAGE_100_alt}  ${IMAGE_Dcom_alt}  ${IMAGE_Mobec_alt}  ${IMAGE_Lsvr_alt}  ${IMAGE_Zmaos_alt}  ${IMAGE_Zmo_alt}  ${IMAGE_Mnh_alt}
    ${count}=  Convert To Integer  0
    FOR  ${image}  IN  @{images}
        ${src}=  Get Element Attribute  ${image}  src
        ${alt}=  Get Element Attribute  ${image}  alt
        Should Be Equal As Strings  ${src}  ${srcs}[${count}]
        Should Be Equal As Strings  ${alt}  ${alts}[${count}]
        ${count}=  Convert To Integer  ${count+1}
    END

TC_001_005-003 - Kontrola, či sú všetky očakávané `a` elementy prítomné 
    ${a}=  Get Element Count  locator=//a
    Should Be Equal As Numbers  ${a}  350

TC_001_005-004 - Kontrola, či sú všetky očakávané `input` elementy prítomné a či majú správne nastavené `type` a `name` atribúty    
    ${inputs_count}=  Get Element Count  locator=//input
    Should Be Equal As Numbers  ${inputs_count}  1
    ${type}=  Get Element Attribute  ${INPUT_Vyhladavanie}  type
    ${name}=  Get Element Attribute  ${INPUT_Vyhladavanie}  name
    Should Be Equal As Strings  ${type}  ${INPUT_Vyhladavanie_type}
    Should Be Equal As Strings  ${name}  ${INPUT_Vyhladavanie_name}

Post-conditions
    Close