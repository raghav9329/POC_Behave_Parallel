Feature:Fail with incorrect certificates

Scenario:check if website have incorrect or untrusted certificates
Given Open browser visit application
When the page is loaded check that it is loaded with secure certificates or not
