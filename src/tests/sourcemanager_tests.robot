*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Page Should Open Successfully
    Wait Until Page Contains    Sourcemanager - Lähdeviitearkisto     timeout=5s

Add Reference Link Should Work
    Click Link    Lisää viite
    Wait Until Page Contains    Valitse viitteen tyyppi:    timeout=5s
    Go Back

Reference List Link Should Work
    Click Link    Listaa kaikki viitteet
    Wait Until Page Contains    Kaikki viitteet    timeout=5s
    Go Back

Search Link Should Work
    Click Link    Hae arkistosta
    Wait Until Page Contains    Haku    timeout=5s
