# mesaj-botu
Bu kod, pyautogui ve time modüllerini kullanarak, belirli bir aralıkta bir dosyadan okunan metinleri yazdırmak için tasarlanmıştır. İlk olarak, kullanıcıdan kaç saniyede bir mesajın yazılmasını istediği sorulur ve bu değer "süre" değişkenine atanır. Daha sonra "mesaj.txt" adlı dosya açılır ve dosyadaki her bir satır için belirtilen süre kadar beklenir. Ardından pyautogui ile satır yazılır ve enter tuşuna basılır. Bu işlem sonsuz bir döngü içerisinde devam eder ve her döngü sonunda dosya kapatılır ve kullanıcının belirlediği süre sonra saniye beklenir.
