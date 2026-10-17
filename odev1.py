# Introduction to Python, Ödev 1
# IEEE Hacettepe University Student Branch, Güz 2026
#
# Bu ödevin sonunda error message'ı okuyup hatayı düzeltebilecek,
# aritmetik operator'lar ve variable'larla küçük hesaplar yapabileceksiniz.
#
# Son teslim: 25 Ekim 2026 Pazar 23.59
# Teslim formu: https://forms.gle/61hSuP7zyptmGsedA
# Ödev reposu: https://github.com/natozenbilek/a-million-seconds-python-hw
#
# Ödevi nasıl yapacaksınız
# 1. Bu dosyayı python-kurs klasörünüze kaydedin ve PyCharm'da açın.
# 2. Her görevde "# TODO" satırının yerine kodunuzu yazın.
# 3. Dosyayı Run ile çalıştırın. Her görevin başlık satırından sonraki
#    çıktısı, o görevin "Beklenen çıktı" kısmıyla birebir aynı olmalı.
# 4. Bitince formda "İsim" alanına isminizi yazın, odev1.py'yi "Ödev dosyası"
#    alanına yükleyin ve onay kutusunu işaretleyin. Söylemek istediğiniz bir
#    şey varsa isteğe bağlı "Açıklama" alanına yazın.
#
# Dosya bu haliyle de hatasız çalışır ve yalnızca görev başlıklarını yazar.
# Yalnızca Ders 1'de gördüğümüz yapıları kullanın.


print("=== 1. Not kartı ===")
# Aşağıdaki kartı dört print() ile yazdırın.
# Son satırdaki 9'u kendiniz yazmayın: 4 + 3 + 2 expression'ı hesaplasın.
# TODO
#
# Beklenen çıktı:
# Hacettepe Üniversitesi
# Not Döküm Belgesi (örnek)
# Dersler: MAT123, FIZ127, TKD103
# Toplam kredi: 9


print("=== 2. Hatalı satırlar ===")
# Aşağıdaki üç satırın her birinde bir hata var.
# Her satır için:
# - satırı TODO'nun yerine "# " olmadan kopyalayın, dosyayı çalıştırın ve
#   error message'ın son satırını okuyun;
# - satırı düzeltin ve sonuna, bir comment olarak, hatanın adını yazın.
#   Örnek: print("Selam")  # NameError
# Derste gördüğümüz gibi, dosyada SyntaxError varken hiçbir satır çalışmaz;
# görev başlıkları da yazılmaz. Satırı düzeltince hepsi geri gelir.
#
# print("Ders 1 bitti)
# Print("IEEE Hacettepe")
# print("Ankara'da", 2026
#
# TODO
#
# Beklenen çıktı:
# Ders 1 bitti
# IEEE Hacettepe
# Ankara'da 2026


print("=== 3. Bir milyon saniye ===")
total_seconds = 1000000
# Bir günde 24 * 60 * 60 saniye vardır.
# a) total_seconds'ın kaç gün ettiğini / ile yazdırın.
# b) Aynı süreyi // ve % ile tam gün, saat, dakika ve saniyeye ayırın.
#    days = total_seconds // (24 * 60 * 60) ile başlayın. Günlerden artan
#    saniyeleri % ile rest_after_days'e koyun; hours, minutes ve seconds'ı
#    da aynı yolla bulun.
#    Her ara sonuca yeni bir isim verin, tur süresi slaytındaki rest_ms
#    gibi. Bir ismin value'sunu sonradan değiştirmeyi Ders 2'de göreceğiz.
# TODO
#
# Beklenen çıktı:
# Gün: 11.574074074074074
# 11 gün 13 saat 46 dakika 40 saniye


print("=== 4. AGNO'ya bir ders eklemek ===")
# Üç ders:  MAT123  4 kredi  C1 (2.50)
#           FIZ127  3 kredi  B2 (3.00)
#           TKD103  2 kredi  A2 (3.75)
# a) total_credits ve total_points variable'larını hesaplayın.
#    total_points, her dersin kredisiyle katsayısının çarpımlarının
#    toplamıdır. AGNO, total_points / total_credits'tir. İlk iki satırı
#    yazdırın.
# b) BBM101 dersini (3 kredi, A3, 3.50) ekleyin: yeni toplamlar için
#    new_credits ve new_points adlı variable'lar kullanın, örneğin
#    new_credits = total_credits + 3. Önce "BBM101 eklendi", sonra yeni
#    toplam kredi ve AGNO satırlarını yazdırın.
# c) Son satırda new_credits ile new_points'in type'ını yazdırın.
# TODO
#
# Beklenen çıktı:
# Toplam kredi: 9
# AGNO: 2.9444444444444446
# BBM101 eklendi
# Toplam kredi: 12
# AGNO: 3.0833333333333335
# <class 'int'> <class 'float'>


print("=== 5. Dört tane 4 ===")
# Her satırda tam dört tane 4 ve arithmetic operators kullanarak 1, 5, 6 ve
# 7 sayılarını yazdırın. Parantez kullanabilirsiniz.
# Çıktıda ".0" olmamalı: / yerine // kullanın.
# Örnek: print((4 + 4 + 4) // 4) 3 yazar.
# TODO
#
# Beklenen çıktı:
# 1
# 5
# 6
# 7


print("=== Meraklısına ===")
# Zorunlu değil.
# Sayı tutma hilesi: bir sayı tutun, iki katını alın, 10 ekleyin, yarıya
# bölün ve tuttuğunuz sayıyı çıkarın. Sonuç hep 5'tir.
# a) Hileyi number ve result adlı iki variable ile yazın: result'ı tek
#    bir expression olarak hesaplayın, number = 42 ile çalıştırın.
# b) Aynı hesabı big_number = 10 ** 17 ve big_result ile yapın: sonuç 5
#    çıkmaz. Nedenini bir comment ile yazın, sonra / yerine // kullanan
#    düzeltilmiş halini (fixed_result) altına ekleyin.
# TODO
#
# Beklenen çıktı (a, b ve düzeltilmiş b):
# Sonuç: 5.0
# Sonuç: 0.0
# Sonuç: 5
