*** Settings ***
Library	     SeleniumLibrary
Library	     Collections
Library          String

*** Variables ***
${URL}	      http://127.0.0.1:5000/
${BROWSER}    Chrome

*** Test Cases ***
General Greeting
	[Setup]	Open Main Page
	Check Greeting
	Reset State
	[Teardown]	Close Browser

Greeting With A Specific Name
	 [Setup]   Open Main Page
	 Submit Name
	 Check Named Greeting
	 Reset State
	 [Teardown]  Close Browser
Remember A Name
       [Setup]   Open Main Page
	 Submit Name
       Check Named Greeting
       Reload Page
       Check Named Greeting
       Reset State
	 [Teardown]  Close Browser

Greeting With A Random Name Senario Four
       [Setup]   Open Main Page
       Click Hello Button
       Check Random Name Greeting
       Reset State
       [Teardown]  Close Browser

Greeting With A Random Name Senario Five
       [Setup]   Open Main Page
       Click Hello Button
       Check Random Name Greeting
       Check Random Name Not Repeated Five Times
       Reset State
       [Teardown]  Close Browser
      
Greeting With A Random Name Senario Six
       [Setup]   Open Main Page
       Submit Name
       Check Named Greeting
       Check Random Name Not Repeated Five Times
       Reset State
       [Teardown]  Close Browser

*** Keywords ***
Open Main Page
     Open Browser     ${URL}	${BROWSER}
     Maximize Browser Window

Reset State
      Go To	${URL}/reset

Check Greeting
      Element Text Should Be	xpath=//*[@id='greeting']	Hello, Web!

Submit Name
      Input Text	xpath=//*[@id='name']	Robot
      Click Button	xpath=//*[@id='hello']

Check Named Greeting
      Element Text Should Be	xpath=//*[@id='greeting']	Hello, Robot!


Click Hello Button
      Click Button	xpath=//*[@id='hello']

Check Random Name Greeting
      Element Text Should Not Be 	xpath=//*[@id='greeting']	Hello, Web!
	Element Text Should Not Be 	xpath=//*[@id='greeting']	Hello!
      Element Should Contain  xpath=//*[@id='greeting']   Hello,

Check Random Name Not Repeated Five Times
      @{names}=   Create List
      FOR    ${i}    IN RANGE    5
            Click Hello Button
            ${name}=    Get Text    xpath=//*[@id='greeting']
            Append To List    ${names}  ${name}
            Log    Name value is ${name}
      END
      ${occurance}=   Get Count    ${names}    ${names}[0]
      Should Be True  ${occurance} < 5
