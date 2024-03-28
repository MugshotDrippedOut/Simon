*** Variables ***
${Value_ValidLogin}  ap4ts.utb@gmail.com
${Value_ValidPassword}  tQb6kqdnQB4R5h8

${Value_Checking_Email_XPath}  //span[contains(text(), ${Value_ValidLogin})]

${Value_HledanyText}  Text
${Value_HledanyText_Kontrola_XPathCZ}  (//*[contains(text(),"Text - Wikipedie")])[1]