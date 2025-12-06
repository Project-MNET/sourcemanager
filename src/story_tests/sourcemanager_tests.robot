*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Variables ***
${BASE_URL}    http://localhost:5001


*** Test Cases ***
Page Should Open Successfully
    Open And Configure Browser
    [Documentation]    Testaa etusivun aukeamisen
    Wait Until Page Contains    Sourcemanager - Lähdeviitearkisto     timeout=5s

Add Reference Link Should Work
    Open And Configure Browser
    [Documentation]     Testaa viitten lisäys linkin toiminnan
    Click Link    Lisää viite
    Wait Until Page Contains    Valitse viitteen tyyppi:    timeout=5s
    Go Back

Reference List Link Should Work
    Open And Configure Browser
    [Documentation]     Testaa viitelistasivun toiminnan
    Click Link    Listaa kaikki viitteet
    Wait Until Page Contains    Kaikki viitteet    timeout=5s
    Go Back

Search Link Should Work
    Open And Configure Browser
    [Documentation]     Testaa Hakulinkin toiminnan
    Click Link    Hae arkistosta
    Wait Until Page Contains    Haku    timeout=5s
    Go Back

Add Book Reference
    Open And Configure Browser
    [Documentation]    Testaa kirja-viitteen lisääminen
    Go To      ${BASE_URL}/add_reference      
    Wait Until Page Contains Element    id=reference_type
    Select From List By Value           id=reference_type    Book
    Input Text       id=key        TEST_BOOK_2
    Input Text       id=author     Test Author
    Input Text       id=title      Test Book
    Input Text       id=year       2025
    Input Text       id=publisher  Test Publisher
    Click Button     Lisää viite
    Page Should Contain           Sourcemanager - Lähdeviitearkisto
    
Add Article Reference
    Open And Configure Browser
    [Documentation]    Testaa artikkeli-viitteen lisääminen
    Go To      ${BASE_URL}/add_reference      
    Wait Until Page Contains Element    id=reference_type
    Select From List By Value           id=reference_type    Article
    Input Text       id=key        TEST_ARTICLE
    Input Text       id=author     Test Author
    Input Text       id=title      Test Article
    Input Text       id=year       2025
    Input Text       id=doi  Test doi_Article
    Input Text       id=journal  Test Journal
    Input Text       id=volume  Volume_test
    Input Text       id=pages  Pages_test
    Click Button     Lisää viite
    Page Should Contain           Sourcemanager - Lähdeviitearkisto

Add Inproceedings Reference
    Open And Configure Browser
    [Documentation]    Testaa konferenssijulkaisun lisääminen
    Go To      ${BASE_URL}/add_reference      
    Wait Until Page Contains Element    id=reference_type
    Select From List By Value           id=reference_type    Inproceedings
    Input Text       id=key        TEST_INPROCEEDINGS
    Input Text       id=author     Test Author
    Input Text       id=title      Test Inproceedings
    Input Text       id=year       2025
    Input Text       id=booktitle  Test BookTitle
    Click Button     Lisää viite
    Page Should Contain           Sourcemanager - Lähdeviitearkisto


Check Book Reference In List
    Open And Configure Browser
    [Documentation]    Tarkistaa, että lisätty kirja löytyy listasta
    Go To      ${BASE_URL}/reference_list    
    Wait Until Page Contains           Test Book
    Page Should Contain                Test Author
    Page Should Contain                Test Book

Check Book search
    Open And Configure Browser
    [Documentation]    Tarkistaa, että lisätty kirja löytyy viite tyypillä
    Go To      ${BASE_URL}/search     

    Wait Until Page Contains Element  xpath=//input[@type='checkbox' and @value='kaikki']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='kaikki']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='artikkeli']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='konferenssi']

    Select Checkbox      xpath=//input[@type='checkbox' and @value='kirja']
    Click Button    Lähetä

    Wait Until Page Contains           Test Book
    Page Should Contain                Test Author
    Page Should Contain                Test Book

Check Article Reference search
    Open And Configure Browser
    [Documentation]    Tarkistaa, että lisätty artikkeli löytyy viite tyypillä
    Go To      ${BASE_URL}/search    
    Wait Until Page Contains Element  xpath=//input[@type='checkbox' and @value='kaikki']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='kaikki']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='kirja']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='konferenssi']

    Select Checkbox      xpath=//input[@type='checkbox' and @value='artikkeli']
    Click Button    Lähetä

    Wait Until Page Contains           Test Article
    Page Should Contain                Test Author
    Page Should Contain                Test Article

Check Conference Reference search
    Open And Configure Browser
    [Documentation]    Tarkistaa, että lisätty artikkeli löytyy viite tyypillä
    Go To      ${BASE_URL}/search    
    Wait Until Page Contains Element  xpath=//input[@type='checkbox' and @value='kaikki']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='kaikki']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='kirja']
    Unselect Checkbox    xpath=//input[@type='checkbox' and @value='artikkeli']

    Select Checkbox      xpath=//input[@type='checkbox' and @value='konferenssi']
    Click Button    Lähetä

    Wait Until Page Contains           Test Inproceedings
    Page Should Contain                Test Author
    Page Should Contain                Test Inproceedings



Search Field Should Work
    Open And Configure Browser
    [Documentation]      Testaa Hakukentän, Sovelluksessa on hakutoiminto, jolla voi hakea viitteitä hakusanalla.
    Go To      ${BASE_URL}/search
    Wait Until Page Contains Element    name=query    timeout=5s
    Input Text    name=query    Test Book
    Click Button     Lähetä
    Wait Until Page Contains    Test Book    timeout=5s
    Page Should Contain    Test Author
    Page Should Contain    2025
    Close Browser
    
Check Deletion From Reference search
    Open And Configure Browser
    [Documentation]    Tarkistaa, että artikkeleita voi poistaa
    Go To      ${BASE_URL}/search  
    Click Button    Lähetä
    Wait Until Page Contains  Test Book
    Wait Until Page Contains  Test Article
    Wait Until Page Contains  Test Inproceedings

    Click Element    xpath=//form[contains(@action, '/delete/TEST_BOOK_2/')]//button
    Handle Alert    action=ACCEPT

    Click Element    xpath=//form[contains(@action, '/delete/TEST_ARTICLE/')]//button
    Handle Alert    action=ACCEPT

    Click Element    xpath=//form[contains(@action, '/delete/TEST_INPROCEEDINGS/')]//button
    Handle Alert    action=ACCEPT


    
    Page Should Not Contain    Test Book
    Page Should Not Contain    Test Article
    Page Should Not Contain    Test Inproceedings
