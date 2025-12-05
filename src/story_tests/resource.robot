*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}    localhost:5001
${DELAY}     0.5 seconds
${HOME_URL}  http://127.0.0.1:5001/
${BROWSER}   chrome
${HEADLESS}  false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
        Call Method  ${options}  add_argument  --incognito
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
        Call Method  ${options}  add_argument  --private-window
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0.05 seconds
        Call Method  ${options}  add_argument  --headless
        Call Method  ${options}  add_argument  --no-sandbox
        Call Method  ${options}  add_argument  --disable-dev-shm-usage
        Call Method  ${options}  add_argument  --disable-gpu
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser    ${HOME_URL}    ${BROWSER}    options=${options}