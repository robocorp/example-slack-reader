*** Settings ***
Library  RPA.Robocorp.Vault
Library  slack_reader.py

*** Tasks ***
Log History from General Channel
    ${slack}=     Get Secret  slack
    ${channels}=  List Channels  ${slack}[token]
    ${messages}=  Retrieve Messages  ${slack}[token]  ${channels}[general][id]  limit=10

    FOR  ${msg}  IN  @{messages}
        Log  ${msg}[text]
    END
