*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Page Should Open Successfully
    Open Browser    ${HOME_URL}  Chrome
    Wait Until Page Contains    Sourcemanager - Lähdeviitearkisto     timeout=5s
    [Teardown]    Close Browser