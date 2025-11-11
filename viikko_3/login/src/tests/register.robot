*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Milla
    Set Password  password123
    Set Password Confirmation  password123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    set Username   Mi
    Set Password  password123
    Set Password confirmation  password123
    Submit Registration
    Registration Should Fail  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  Milla
    Set Password  12
    Set Password confirmation  12
    Submit Registration
    Registration Should Fail  Password must be at least 8 characters long and

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  Milla
    Set Password  password
    Set Password confirmation  password
    Submit Registration
    Registration Should Fail  Password cannot consist of letters only

Register With Nonmatching Password And Password Confirmation
    Set Username  Milla
    Set Password  password123
    Set Password confirmation  password111
    Submit Registration
    Registration Should Fail  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  password123
    Set Password confirmation  password123
    Submit Registration
    Registration Should Fail  Username is already taken


*** Keywords ***
Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Go To Starting Page
    Go To  ${HOME_URL}

Go To Welcome Page
    Go To  ${WELCOME_URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Registration Should Fail
    [Arguments]  ${error_message}
    Registration Page Should Be Open
    Page Should Contain  ${error_message}

Registration Page Should Be Open
    Title Should Be  Register

Registration Should Succeed
    Title Should Be  Welcome to Ohtu Application!

