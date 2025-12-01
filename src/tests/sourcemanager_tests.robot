*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Variables ***
${BASE_URL}    http://localhost:5001


*** Test Cases ***
Page Should Open Successfully
    Open And Configure Browser
    Wait Until Page Contains    Sourcemanager - Lähdeviitearkisto     timeout=5s

Add Reference Link Should Work
    Open And Configure Browser
    Click Link    Lisää viite
    Wait Until Page Contains    Valitse viitteen tyyppi:    timeout=5s
    Go Back

Reference List Link Should Work
    Open And Configure Browser
    Click Link    Listaa kaikki viitteet
    Wait Until Page Contains    Kaikki viitteet    timeout=5s
    Go Back

Search Link Should Work
    Open And Configure Browser
    Click Link    Hae arkistosta
    Wait Until Page Contains    Haku    timeout=5s
    Go Back

Add Book Reference
    Open And Configure Browser
    [Documentation]    Testaa kirja-viitteen lisääminen
    Go To      ${BASE_URL}/add_reference    chrome     
    Wait Until Page Contains Element    id=reference_type
    Select From List By Value           id=reference_type    Book
    Input Text       id=key        TEST_BOOK_2
    Input Text       id=author     Test Author
    Input Text       id=title      Test Title
    Input Text       id=year       2025
    Input Text       id=publisher  Test Publisher
    Click Button     Lisää viite
    Page Should Contain           Sourcemanager - Lähdeviitearkisto
    

Check Book Reference In List
    Open And Configure Browser
    [Documentation]    Tarkistaa, että lisätty kirja löytyy listasta
    Go To      ${BASE_URL}/reference_list    chrome     
    Wait Until Page Contains           Test Title
    Page Should Contain                Test Author
    Page Should Contain                Test Title
    