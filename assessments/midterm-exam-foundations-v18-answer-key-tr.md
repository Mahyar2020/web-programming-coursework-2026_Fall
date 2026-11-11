# Ara Sınav - Öğretim Elemanı Cevap Anahtarı

**Kaynak kapsamı:** *Web Programlama: Platformdan Üretime - Temeller Baskısı, Gözden Geçirilmiş v18*  
**Soru sayısı:** 40  
**Puanlama:** Her soru 2,5 puan; toplam 100 puan

## Değerlendirme Planı

| İçerik alanı | Sorular | Sayı |
|---|---:|---:|
| Çalışma ortamı ve geliştirme iş akışı | 1-4 | 4 |
| Web nasıl çalışır | 5-16 | 12 |
| Semantik HTML ve erişilebilir formlar | 17-28 | 12 |
| CSS, yerleşim ve duyarlı tasarım | 29-40 | 12 |

| Bilişsel düzey | Sorular | Sayı |
|---|---|---:|
| Temel kavrayış | 1, 3, 5, 6, 8, 17, 19, 22, 29, 33 | 10 |
| Uygulamalı kavrayış | 2, 4, 7, 9, 11, 13, 14, 18, 20, 21, 23, 24, 26, 27, 30, 31, 32, 35, 36, 38 | 20 |
| Analiz ve tanılama | 10, 12, 15, 16, 25, 28, 34, 37, 39, 40 | 10 |

Zorluk dağılımı %25 temel, %50 uygulama ve %25 analiz/tanılama düzeyindedir. Doğru cevap konumları dengelidir: A, B, C, D ve E seçeneklerinin her biri sekiz kez doğru cevaptır.

## Cevaplar ve Gerekçeler

| Soru | Cevap | Gerekçe |
|---:|:---:|---|
| 1 | B | Hazır olma durumu, çalıştırılabilir sürüm kanıtı ve gerçek ders iş akışının başarıyla tamamlanmasını gerektirir; kurulum dosyası veya kısayol yeterli kanıt değildir. |
| 2 | D | Hata yolu, npm'in dosyayı nerede aradığını gösterir. Proje komutları `package.json` içeren depo kökünde çalıştırılmalıdır. |
| 3 | A | Kaydetme çalışma dosyasını yazar; commit seçilen içeriği yerel geçmişe kaydeder; push commitleri uzak depoya aktarır. |
| 4 | E | Network kaydı istek tamamlandıktan sonra başlamış olabilir. Panel açıkken sayfayı yenilemek alışverişi kaydeder. |
| 5 | C | İnternet ağların altyapısıdır; Web bu altyapıyı kullanan bir uygulamadır. |
| 6 | A | Fragment istemci tarafından yorumlanır ve normal olarak HTTP istek hedefine eklenmez. |
| 7 | D | Origin; scheme, host ve etkin port üçlüsüdür. Path, query ve fragment origin'i belirlemez. |
| 8 | B | DNS, host adı için adres bilgisi sağlar; sayfayı almaz, oluşturmaz, şifrelemez veya doğruluğunu onaylamaz. |
| 9 | E | Görünür hata gövdesi ve `404` durum kodu birlikte sunucu yanıtının parçalarıdır. |
| 10 | C | HTTPS aktarım hâlindeki veriyi ve sertifikalı uç noktanın kimliğini korur; uygulamanın doğru ya da kusursuz olduğunu kanıtlamaz. |
| 11 | A | İlk HTML belgesi, her biri ayrı istek gerektirebilen birden çok kaynağa başvurabilir. |
| 12 | D | `200 OK` tek bir isteğe ilişkin protokol kanıtıdır; semantik, erişilebilirlik, veri veya arayüz doğruluğunu kanıtlamaz. |
| 13 | B | HTTP bağımsız istekler arasında konuşma durumunu kendiliğinden korumaz; uygulamalar cookie veya token gibi mekanizmalarla süreklilik ekler. |
| 14 | E | HTTP URL'si ile yöntem, durum ve yanıt alanlarını içeren Network kaydı, HTTP sunumunu doğrudan `file:` yüklemesinden ayırır. |
| 15 | C | DOM, ayrıştırma sonucunda üretilen canlı ağaçtır; kaynak metinde bulunmayan düzeltmeleri ve betik değişikliklerini içerebilir. |
| 16 | A | `<h1>` istenen birinci düzey başlığı, `<a href="events.html">` ise kaynağa çalışan yerel bağlantıyı oluşturur. |
| 17 | D | Semantik HTML, görsel stillemeden bağımsız olarak rolleri ve ilişkileri iletir. |
| 18 | B | Başlık düzeyleri yapısal hiyerarşiyi, CSS ise görsel boyut ve aralığı belirler. |
| 19 | E | `article`, bağımsız olarak anlamlı veya yeniden kullanılabilir bir bileşim için uygundur. |
| 20 | C | Bağlantı bir kaynağa gider; düğme bir eylem gerçekleştirir. Görünüm semantiği belirlemez. |
| 21 | A | Placeholder kaybolur ve güvenilir bir kalıcı etiket ya da erişilebilir ad değildir. |
| 22 | D | Başarılı ve adlandırılmış bir denetim, gönderilen form verisine anahtar-değer çifti ekler; anahtarı `name` sağlar. |
| 23 | B | İstemci sunucunun güven sınırının dışındadır ve istemci tarafı denetimleri atlanabilir veya değiştirilebilir. |
| 24 | E | Boş alternatif, dekoratif veya gereksiz görselin erişilebilirlik deneyimine gürültü eklemesini bilinçli olarak önler. |
| 25 | C | `required` bir Boolean niteliktir: yazılı değeri `false` dizesi olsa bile varlığı true anlamına gelir. |
| 26 | A | Öğrenci numaraları ve posta kodları tanımlayıcıdır; nicelik semantiği ve sayısal normalleştirme geçerli biçimi bozabilir. |
| 27 | D | Devre dışı denetimler normalde gönderime katılmaz; adlandırılmış salt okunur metin denetimi ise normalde gönderilir. |
| 28 | B | Erişilebilir düzeltme; hataya özgü başlık, gezilebilir özet, alan ilişkileri, durum/odak yönetimi ve güvenli geçerli girdilerin korunmasını birleştirir. |
| 29 | E | Cascade; origin, importance, layer, specificity ve source order etkenlerini içeren sıralı bir karar süreci kullanır. |
| 30 | C | `content-box` altında dış boyut 300 + 40 padding + 4 border = 344 pikseldir. |
| 31 | A | `border-box`, padding ve border değerlerini bildirilen boyutlara dâhil eder; öngörülebilirliği artırır ancak her taşmayı engellemez. |
| 32 | D | Flexbox tek bir temel ekseni modeller; `flex-wrap` gezinme öğelerinin dayanıklı biçimde sarmalanmasını sağlar. |
| 33 | B | Grid, satır ve sütunları koordine ettiği için iki boyutlu kart yerleşimlerine uygundur. |
| 34 | E | Container query, genel viewport yerine bileşene container tarafından ayrılan alana yanıt verir. |
| 35 | C | İçerik odaklı breakpoint, geçici cihaz listesine değil gerçek yerleşim ilişkisinin gerektirdiği alana göre belirlenir. |
| 36 | A | Görsel yeniden sıralama, DOM tabanlı okuma ve klavye odak sırasını zorunlu olarak değiştirmez. |
| 37 | D | `opacity: 0` pikselleri gizler ancak öğeyi yerleşimde ve potansiyel olarak odaklanabilir ya da etkileşimli bırakabilir. |
| 38 | B | Odak görünür biçimde belirtilmeli ve gerçek klavye kullanımı ile duyarlı koşullarda başka içerik tarafından kapatılmamalıdır. |
| 39 | E | `min(100%, 20rem)`, hedeflenen üst sınırı korurken kartın daha dar container'a sığmasını sağlar. |
| 40 | C | Kanıta dayalı sıra, kodu değiştirmeden önce yükleme, eşleşme, cascade/hesaplama ve yerleşim varsayımlarını denetler. |

## Kısa Cevap Anahtarı

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| B | D | A | E | C | A | D | B | E | C |

| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | D | B | E | C | A | D | B | E | C |

| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | D | B | E | C | A | D | B | E | C |

| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| A | D | B | E | C | A | D | B | E | C |

## Öğretim Elemanı Notları

- 10, 12, 15, 25, 28, 34, 37 ve 40. sorular ezberlenmiş terimleri işlemsel kavrayıştan ayırmak için özellikle kullanışlıdır.
- Kurumun standart sınav politikası farklı bir hüküm içermedikçe her soru için yalnızca bir cevap kabul ediniz.
- Cevap anahtarı dosyasını öğrencilere açık dağıtım kanallarından uzak tutunuz.
- İşlenen kapsam çalışma ortamı hazırlığını içermediyse 1-4. sorular çıkarılabilir ve kalan 36 soru yeniden puanlanabilir. Mevcut sürüm, gözden geçirilmiş v18'in tüm içeriğini bilinçli olarak değerlendirir.
