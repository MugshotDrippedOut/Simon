*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing

Resource  ../Resources/keywords.robot

Resource  ../Resources/variables/Browsers.robot
Resource  ../Resources/variables/URLs.robot
Resource  ../Resources/variables/Inputs.robot
Resource  ../Resources/variables/Images.robot
Resource  ../Resources/variables/Values.robot


*** Test Cases ***
Pre-conditions
    Open EN Incognito Chrome Webdriver  ${URL_MainPage}


TC_001_005-001 - Kontrola, či sú všetky očakávané `div` elementy prítomné
    ${div} =  Get Element Count  locator=//div
    Log  ${div}
    Should Be In Range  ${div}  ${VALUE_NumberOfDivsMin}  ${VALUE_NumberOfDivsMax}


TC_001_005-002 - Kontrola, či sú všetky očakávané `img` elementy prítomné a či majú správne nastavené `src` a `alt` atribúty
    ${images_count}=  Get Element Count  locator=//img
    Should Be Equal As Numbers  ${images_count}  ${VALUE_NumberOfImages}
    ${images}=  Create List  ${IMAGE_ObecKrakovany}  ${IMAGE_Print}  ${IMAGE_Starosta}  ${IMAGE_Map}  ${IMAGE_Plus}  ${IMAGE_Minus}  ${IMAGE_100}  ${IMAGE_Dcom}  ${IMAGE_Mobec}  ${IMAGE_Lsvr}  ${IMAGE_Zmaos}  ${IMAGE_Zmo}  ${IMAGE_Mnh}
    ${srcs}=  Create List  ${IMAGE_ObecKrakovany_src}  ${IMAGE_Print_src}  ${IMAGE_Starosta_src}  ${IMAGE_Map_src}  ${IMAGE_Plus_src}  ${IMAGE_Minus_src}  ${IMAGE_100_src}  ${IMAGE_Dcom_src}  ${IMAGE_Mobec_src}  ${IMAGE_Lsvr_src}  ${IMAGE_Zmaos_src}  ${IMAGE_Zmo_src}  ${IMAGE_Mnh_src}
    ${alts}=  Create List  ${IMAGE_ObecKrakovany_alt}  ${IMAGE_Print_alt}  ${IMAGE_Starosta_alt}  ${IMAGE_Map_alt}  ${IMAGE_Plus_alt}  ${IMAGE_Minus_alt}  ${IMAGE_100_alt}  ${IMAGE_Dcom_alt}  ${IMAGE_Mobec_alt}  ${IMAGE_Lsvr_alt}  ${IMAGE_Zmaos_alt}  ${IMAGE_Zmo_alt}  ${IMAGE_Mnh_alt}
    ${count}=  Convert To Integer  0
    FOR  ${image}  IN  @{images}
        ${src}=  Get Element Attribute  ${image}  ${VALUE_ImgSrc}
        ${alt}=  Get Element Attribute  ${image}  ${VALUE_ImgAlt}
        Should Be Equal As Strings  ${src}  ${srcs}[${count}]
        Should Be Equal As Strings  ${alt}  ${alts}[${count}]
        ${count}=  Convert To Integer  ${count+1}
    END

TC_001_005-003 - Kontrola, či sú všetky očakávané `a` elementy prítomné 
    ${a}=  Get Element Count  locator=//a
    Log  ${a}
    Should Be In Range  ${a}  ${VALUE_NumberOfAnchorsMin}  ${VALUE_NumberOfAnchorsMax}

TC_001_005-004 - Kontrola, či sú všetky očakávané `input` elementy prítomné a či majú správne nastavené `type` a `name` atribúty    
    ${inputs_count}=  Get Element Count  locator=//input
    Should Be Equal As Numbers  ${inputs_count}  ${VALUE_NumberOfInputs}
    ${type}=  Get Element Attribute  ${INPUT_Vyhladavanie}  ${VALUE_AttributeType}
    ${name}=  Get Element Attribute  ${INPUT_Vyhladavanie}  ${VALUE_AttributeName}
    Should Be Equal As Strings  ${type}  ${INPUT_Vyhladavanie_type}
    Should Be Equal As Strings  ${name}  ${INPUT_Vyhladavanie_name}

Post-conditions
    Close