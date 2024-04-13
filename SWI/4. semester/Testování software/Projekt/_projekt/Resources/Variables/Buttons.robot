//buttons
*** Variables ***
# TS_001_001_001 - Obec
${BUTTON_Obec}  //*[@id="menu-hlavne-1"]/li[2]/a
${BUTTON_Obec_ZakladneUdajeAkontakty}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[1]/a
${BUTTON_Obec_GeografickaPoloha}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[2]/a
${BUTTON_Obec_HistoriaObce}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[3]/a
${BUTTON_Obec_MonografiaObce}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[4]/a
${BUTTON_Obec_ErbObce}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[5]/a
${BUTTON_Obec_UzemnyPlanObce}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[6]/a
${BUTTON_Obec_ProgramRozvojaObce}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[7]/a
${BUTTON_Obec_PrevadzkovyPoriadokZbernehoDvora}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[8]/a
${BUTTON_Obec_StarostaObce}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[9]/a
${BUTTON_Obec_ObecneZastupitelstvo}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[10]/a
${BUTTON_Obec_ObecnaKniznica}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[11]/a
${BUTTON_Obec_Fotogaleria}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[12]/a
${BUTTON_Obec_PodnikatelskeSubjekty}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[13]/a
${BUTTON_Obec_CervenyKriz}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[14]/a
${BUTTON_Obec_Mikroregion}  //*[@id="menu-hlavne-1"]/li[2]/ul/li[15]


# TS_001_001_001_001 - Základné údaje a kontakty
${BUTTON_PridatKomentar}  //input[@id='submit'] 

# Map
${BUTTON_ZoomIn}  //button[@title='Zoom in']
${BUTTON_ZoomOut}  //*[@id="mapDiv"]/div/div[3]/div[12]/div/div/div/button[2]
${BUTTON_Satellite}  //*[@id="mapDiv"]/div/div[3]/div[13]/div/div/button/div[1]
${BUTTON_Street}  //*[@id="mapDiv"]/div/div[3]/div[13]/div/div/button/div[1]
${BUTTON_LargerMap}  //*[@id="mapDiv"]/div/div[3]/div[3]/div/div/div/div/a
    # accept google thing
${BUTTON_AcceptGoogle}  //*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button