# Web Programlama: Platformdan Üretime

## Vize Mazeret Sınavı - Temeller Baskısı (v21)

**Adı ve soyadı:** ________________________________________  
**Öğrenci numarası:** ____________________________________  
**Tarih:** ____________________  
**Süre:** 80 dakika  
**Toplam:** 100 puan

### Yönergeler

- Bu sınav, her biri 2,5 puan olan 40 çoktan seçmeli sorudan oluşmaktadır.
- Her soruda en uygun tek cevabı seçiniz. Her sorunun beş seçeneği (A-E) ve yalnızca bir doğru cevabı vardır.
- Aksi belirtilmedikçe standartlara uygun güncel tarayıcıları ve 0-3. oturumlarda açıklanan ders ortamını varsayınız.

---

## Bölüm I - Çalışma Ortamı ve Geliştirme İş Akışı

### 1.

Bir öğrenci `index.html` dosyasını değiştirmiş, tarayıcıyı yenilemiş ancak hâlâ eski sayfayı görmüştür. İlk olarak hangi işlem dizisi en yararlı kanıtı sağlar?

A. Git'i yeniden kurup depoyu yeniden adlandırmak  
B. Bütün CSS bildirimlerine `!important` eklemek  
C. Dosyanın kaydedildiğini, sunucunun aynı klasörü sunduğunu ve Network panelinde yeni bir belge isteği bulunduğunu doğrulamak  
D. HTML dosyasının yanında boş bir `package.json` oluşturmak  
E. Doğrulanmamış değişikliği GitHub'a push etmek

### 2.

Yerel sunucu bir terminalde çalışmaya devam etmekte ve istek kayıtlarını yazdırmaktadır. Öğrenci sunucuyu durdurmadan `npm test` komutunu nerede çalıştırmalıdır?

A. Aynı depo kökünde açılan ikinci bir terminalde  
B. Tarayıcının adres çubuğunda  
C. CSS dosyasının içinde  
D. Projenin konumundan bağımsız olarak `C:\Users\Student` klasöründe açılan terminalde  
E. Yerel sunucu çalışırken testler çalıştırılamaz.

### 3.

Tamamlanan bir laboratuvar çalışmasını en sorumlu biçimde hangi Git iş akışı kaydeder?

A. Önce push etmek, ardından düzenleyip kaydetmek  
B. Bilgisayardaki bütün dosyaları incelemeden commit etmek  
C. `.git` klasörünü silmek, yeniden oluşturmak ve zorla push etmek  
D. Her değişiklikten sonra projeyi yeniden adlandırmak  
E. Değişiklikleri incelemek, amaçlanan dosyaları staging alanına eklemek, anlamlı bir birimi commit etmek ve commiti push etmek

### 4.

`npm run serve:week03:starter` komutu ilgili scriptin bulunmadığını bildirmektedir; ancak `package.json` geçerli dizinde görünmektedir. Bundan sonra en uygun kontrol hangisidir?

A. Monitörün bağlı olup olmadığı  
B. `package.json` dosyasını açıp `scripts` altında tam script adını doğrulamak  
C. HTML içinde bir `<npm>` öğesi bulunup bulunmadığı  
D. Tarayıcıyı yeniden kurmak  
E. Sayfa adresini bir GitHub adresiyle değiştirmek

---

## Bölüm II - Web Nasıl Çalışır

### 5.

`https://events.example.edu:443/calendar?week=4#labs` adresi için hangi ikili doğrudur?

A. Host `/calendar`, yol `events.example.edu` değeridir.  
B. Şema `events`, sorgu `#labs` değeridir.  
C. Port `4`, fragment `443` değeridir.  
D. Yol `/calendar`, fragment `labs` değeridir.  
E. Sorgu `https`, host `week=4` değeridir.

### 6.

DNS sorgusu bir IP adresi döndürmüş, fakat tarayıcı daha sonra bağlantı zaman aşımı bildirmiştir. Bu kanıt neyi destekler?

A. HTML ayrıştırma DNS'den önce başarısız olmuştur.  
B. Ad çözümleme başarılı olmuş; bağlantı veya erişilebilirlikle ilgili daha sonraki bir adım başarısız olmuştur.  
C. CSS cascade adresi reddetmiştir.  
D. URL fragmenti DNS zaman aşımına yol açmıştır.  
E. Git sunucuyu içermemektedir.

### 7.

Aşağıdakilerden hangisi sözdizimsel olarak geçerli bir İnternet Protokolü sürüm 4 (IPv4) adresidir?

A. `192.168.1.42`  
B. `192.168.1.300`  
C. `192.168.1`  
D. `192:168:1:42`  
E. `campus.192.1.42`

### 8.

`2001:db8::40` değerinde neden yan yana iki iki nokta bulunabilir?

A. Bir URL şemasını yolundan ayırırlar.  
B. Şifrelenmiş bir port numarasını gösterirler.  
C. Değeri IPv4'e dönüştürürler.  
D. Geçersiz boş bir alanı gösterirler.  
E. IPv6 gösteriminde bir adet `::`, art arda gelen bir veya daha fazla tamamen sıfır grubu kısaltabilir.

### 9.

Tarayıcı `/events` için istekte bulunmuş ve `Location: /calendar` başlığıyla birlikte `301` durum kodu almıştır. Bu yanıt nasıl yorumlanmalıdır?

A. Sunucu kendi DNS adını çözememiştir.  
B. Tarayıcı kalıcı olarak boş bir sayfa göstermelidir.  
C. Kaynak yönlendirilmektedir ve istemci `/calendar` için başka bir istek yapabilir.  
D. Yanıt, `/calendar` içeriğinin sonsuza kadar aynı kalacağını kanıtlar.  
E. CSS dosyası sayfayı taşımıştır.

### 10.

Sorumlulukları doğru katmanlara yerleştiren ifade hangisidir?

A. HTTP fiziksel Wi-Fi frekanslarını seçer; CSS paketleri yönlendirir.  
B. DNS HTML'yi oluşturur; TCP başlık seviyelerini seçer.  
C. HTML aktarımı şifreler; Git sertifikanın kimliğini doğrular.  
D. IP paketleri adresler ve yönlendirir; taşıma katmanı uçtan uca iletimi destekler; HTTP ise Web istek ve yanıtlarını ifade eder.  
E. JavaScript bütün ağ katmanlarının yerini almalıdır.

### 11.

Hangi iki URL normal olarak aynı origin'e sahiptir?

A. `https://hub.example.edu/events` ve `http://hub.example.edu/events`  
B. `https://hub.example.edu/events` ve `https://hub.example.edu:443/news`  
C. `https://hub.example.edu` ve `https://api.example.edu`  
D. `https://hub.example.edu:8443` ve `https://hub.example.edu`  
E. `https://hub.example.edu` ve `file:///hub.html`

### 12.

Network panelinde belge `200`, `styles.css` ise `404` olarak görünmektedir. En doğru sonuç hangisidir?

A. DNS bütün sayfa için başarısız olmuştur.  
B. Belge ve stil sayfası zorunlu olarak aynıdır.  
C. HTTPS, CSS kullanımını yasaklamıştır.  
D. HTML isteği başarılı olmuş; istenen stil sayfası kaynağı bulunamamıştır.  
E. Stil sayfası yüklenmiş ancak cascade'i kaybetmiştir.

### 13.

`localhost` hakkında hangi ifade doğrudur?

A. İsteğin yapıldığı aynı bilgisayarı gösterir; seçilen portta yine de bir yerel sunucunun dinliyor olması gerekir.  
B. Herkesin erişebildiği genel bir üniversite alan adıdır.  
C. Her zaman dersin GitHub deposuna karşılık gelir.  
D. Tarayıcının bir dosyayı HTTP olmadan açtığı anlamına gelir.  
E. 8000 numaralı portun çalıştığını garanti eder.

### 14.

Bir HTTP yanıt başlığı gövdeden neden farklıdır?

A. Başlıklar CSS, gövde DNS'dir.  
B. Başlıklar görünen pikseller, gövde bir Git commitidir.  
C. Başlıklar yanıt üst verisini ve kontrol bilgisini; gövde ise varsa kaynağın temsilini taşır.  
D. Başlıklar yalnızca hatalarda bulunur.  
E. Bir yanıtta ikisi birlikte bulunamaz.

### 15.

`https://hub.example.edu` adresindeki bir sayfa `https://api.example.edu` adresinden veri istemektedir. Tarayıcı neden originler arası denetimler uygulayabilir?

A. Yollar çok kısadır.  
B. Her iki adres de HTTPS kullanmaktadır.  
C. Yanıt JavaScript Nesne Gösterimi biçimindedir.  
D. Sayfada form bulunmaktadır.  
E. Şema aynı olsa da hostlar farklıdır; dolayısıyla originler farklıdır.

### 16.

Adlandırılmış bir HTTPS sitesine yapılan ilk gezinmeyi en doğru hangi sıralama açıklar?

A. Pikselleri oluşturmak, Git commit etmek, ardından DNS çözmek  
B. Adı çözmek, gerekli bağlantı/güvenliği kurmak, HTTP iletilerini paylaşmak, kaynakları ayrıştırmak ve sayfayı oluşturmak  
C. CSS'i çalıştırmak, IPv4 adresi atamak, ardından URL oluşturmak  
D. Fragmenti DNS'ye göndermek, ardından tarayıcıyı indirmek  
E. Herhangi bir sunucuyla bağlantı kurmadan önce veritabanını açmak

---

## Bölüm III - Semantik HTML ve Erişilebilir Formlar

### 17.

Tek ana başlığı ve eş düzey iki bölümü olan bir sayfa için hangi belge başlık yapısı en tutarlıdır?

A. `<h3>Campus Hub</h3><h1>Etkinlikler</h1><h5>Haberler</h5>`  
B. `<div>Campus Hub</div><b>Etkinlikler</b><b>Haberler</b>`  
C. `<h1>Campus Hub</h1><h2>Etkinlikler</h2><h2>Haberler</h2>`  
D. `<h1>Etkinlikler</h1><h1>Haberler</h1><h4>Campus Hub</h4>`  
E. Başlık seviyeleri yalnızca varsayılan punto büyüklüklerine göre seçilmelidir.

### 18.

Bir kontrol, başka bir kaynağa gitmeden “Etkinliği kaydet” işlemini gerçekleştirmektedir. En uygun yerel semantiği hangi öğe sağlar?

A. `href` içermeyen `<a>Etkinliği kaydet</a>`  
B. `<input type="text" value="Etkinliği kaydet">`  
C. `<span onclick="save()">Etkinliği kaydet</span>`  
D. `<div role="presentation">Etkinliği kaydet</div>`  
E. `<button type="button">Etkinliği kaydet</button>`

### 19.

Hangi işaretleme bir metin girişine görünür ve programatik olarak ilişkilendirilmiş bir etiket kazandırır?

A. `<span>E-posta</span><input placeholder="E-posta">`  
B. `<input name="email"><p>E-posta</p>`  
C. `<label>E-posta</label><div contenteditable>`  
D. `<input id="email"><label for="mail">E-posta</label>`  
E. `<label for="email">E-posta</label><input id="email" name="email" type="email">`

### 20.

Campus Hub ana sayfasına dönen bağlantılı Campus Hub logosu için en uygun alternatif metin hangisidir?

A. `alt="Campus Hub ana sayfası"`  
B. `alt="mavi ve turuncu dikdörtgen resim"`  
C. `alt="logo.png"`  
D. `alt` niteliğini kullanmamak  
E. `alt="resim bağlantı grafiği"`

### 21.

Tekrarlanan site gezintisi ve footer içeriği dışında sayfanın baskın içeriği için hangi öğe tasarlanmıştır?

A. `<aside>`  
B. `<nav>`  
C. `<header>`  
D. `<main>`  
E. `<small>`

### 22.

Bir tablo etkinlik, tarih ve mekân bilgilerini listelemektedir. Başlık hücreleri için en doğru uygulama hangisidir?

A. Sıradan `<td>` hücrelerini kullanıp yalnızca CSS ile kalınlaştırmak  
B. Ekran okuyucuların etiketleri tahmin etmesi için hücreleri boş bırakmak  
C. Gerektiğinde kapsam ilişkileriyle birlikte uygun `<th>` hücrelerini kullanmak  
D. Tabloyu boşluklar ve satır sonlarıyla değiştirmek  
E. Tablonun tamamını bir resim içine yerleştirmek

### 23.

Bir form genel etkinlik araması için `method="get"` kullanmaktadır. Başarılı kontroller normal olarak nerede temsil edilir?

A. Yalnızca tarayıcı belleğinde  
B. URL'nin sorgu bölümünde ad-değer çiftleri olarak  
C. `#` işaretinden sonraki fragmentte  
D. CSS stil sayfasında  
E. Git commit mesajında

### 24.

Birbirini dışlayan üç katılım seçeneği için hangi alan gruplaması en uygundur?

A. Birbirinden bağımsız üç metin girişi  
B. Bir başlık ve ardından üç bağlantı  
C. Anlamı yalnızca renkle verilen bir `<div>`  
D. Üç değere sahip bir checkbox  
E. Bir `<legend>` içeren `<fieldset>` ve aynı `name` değerini paylaşan radio düğmeleri

### 25.

Belge dili hakkında hangi ifade doğrudur?

A. `lang` yalnızca CSS renk kullandığında gereklidir.  
B. Tarayıcı dili dosya adından her zaman kusursuz biçimde çıkarır.  
C. Belgenin ana dili belirtilmeli, metin içindeki dil değişiklikleri de yerel olarak işaretlenebilmelidir.  
D. `lang`, karakter kodlamasının yerini alır.  
E. Sayfa yalnızca başlıklarda dil belirtebilir.

### 26.

Öğretici bir diyagram, metinde başka yerde açıklanmayan bir ağ yolunu göstermektedir. En güçlü erişilebilirlik yaklaşımı hangisidir?

A. Diyagramı tanımlayan kısa bir `alt` ve anlamlı ilişkileri açıklayan bitişik ayrıntılı bir açıklama sağlamak  
B. `alt="diyagram"` kullanıp başka bilgi vermemek  
C. Diyagramı bütün kullanıcılardan gizlemek  
D. Bütün açıklamayı dosya adına yazmak  
E. Her yolu yalnızca renk ile ayırt etmek

### 27.

Yerel form türleriyle ilgili hangi ifade doğrudur?

A. `type="email"`, adresin gerçekten var olduğunu kanıtlar.  
B. `type="date"`, bütün tarayıcılarda aynı görünümü garanti eder.  
C. `type="number"`, rakamlardan oluşan her değer için idealdir.  
D. Uygun türler giriş kolaylıkları ve kısıt denetimleri sağlayabilir; ancak sunucu anlamı ve yetkiyi yine de doğrulamalıdır.  
E. Yerel türler etiket gereksinimini ortadan kaldırır.

### 28.

Geçersiz bir form gönderiminden sonra hangi yanıt en az yararlı ve en az erişilebilirdir?

A. Geçerli değerleri koruyup her düzeltmeyi belirtmek  
B. Formun tamamını temizleyip sayfanın altında yalnızca kırmızı “Hata” yazısı göstermek  
C. Bağlantılı bir hata özeti ve alan düzeyinde mesajlar sağlamak  
D. Görsel biçimlendirmeye ek olarak metin kullanmak  
E. Uygun olduğunda odağı öngörülebilir biçimde yararlı hata bilgisine taşımak

---

## Bölüm IV - CSS, Yerleşim ve Duyarlı Tasarım

### 29.

Aynı katman ve origin içinde `.card { color: navy; }` ve `main .card { color: teal; }` kurallarının ikisi de aynı öğeyle eşleşmektedir. Normalde hangi renk kazanır?

A. Daha kısa selector hızlı olduğu için lacivert  
B. `main .card` daha yüksek specificity değerine sahip olduğu için teal  
C. İki rengin ortalaması  
D. Daha az karakter içeren bildirim  
E. İki bildirim de geçersizdir.

### 30.

Bir alt paragrafta `color` bildirimi yoktur; üst öğesinde ise `color: #12355b` vardır. Normalde ne olur?

A. Paragraf saydam olur.  
B. Üst öğedeki bütün özellikler kopyalanır.  
C. Paragraf zorunlu olarak siyah olur.  
D. `color` miras alındığı için paragraf normalde `#12355b` kullanır.  
E. Paragraf normal akıştan çıkarılır.

### 31.

Sınırlı inline boyuta ve kullanılabilir yatay boşluğa sahip bir blokta `margin-inline: auto` genellikle ne sağlar?

A. Bloğu inline yönde ortalar.  
B. Bloğu Grid container yapar.  
C. Metni dikey hizalar.  
D. Bloğun padding değerini kaldırır.  
E. Sağdan sola yazımı zorunlu kılar.

### 32.

Uzun ve bölünemeyen bir dize içeren flex item üzerinde `min-width: 0` neden gerekli olabilir?

A. Yazı boyutunu otomatik büyütür.  
B. Flex eksenini değiştirir.  
C. Öğenin otomatik minimumundan daha küçük olabilmesine izin vererek amaçlanan satır kaydırma veya taşma yönetimini mümkün kılar.  
D. Cascade'i devre dışı bırakır.  
E. Dizeyi resme dönüştürür.

### 33.

En az `16rem` genişliğinde kalan ve fazladan alanı paylaşan duyarlı Grid sütunlarını hangi bildirim oluşturur?

A. `grid-template-columns: 16rem 16rem 16rem;`  
B. `display: flex-column;`  
C. `columns: auto;`  
D. `position: grid;`  
E. `grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));`

### 34.

Bir öğe `position: absolute` değerine sahiptir. Normalde neye göre konumlandırılır?

A. Genellikle en yakın konumlandırılmış üst öğenin oluşturduğu containing block'a göre  
B. Her zaman fiziksel ekrana göre  
C. Dosyadaki son CSS kuralına göre  
D. Git deposunun köküne göre  
E. Tarayıcının Network paneline göre

### 35.

`@media (prefers-reduced-motion: reduce)` kullanımının temel erişilebilirlik amacı nedir?

A. Bütün kullanıcılar için animasyon hızını artırmak  
B. Semantik HTML'yi kaldırmak  
C. Klavye girişini devre dışı bırakmak  
D. Bu tercihi bildiren kullanıcılar için azaltılmış hareket deneyimi sağlamak  
E. Sayfayı gri tonlamalı yazdırmak

### 36.

Bir bileşen bütün viewport'a değil, içinde bulunduğu makale sütununun genişliğine göre uyarlanmalıdır. Bu bağımlılığı hangi araç en doğru ifade eder?

A. Yalnızca viewport media query  
B. Sabit piksel genişliği  
C. Container query  
D. HTML tablosu  
E. Tarayıcı markası selectorı

### 37.

`height: 100vh` içerik sayfası için neden bazen kırılgandır?

A. Kaydırmayı her zaman devre dışı bırakır.  
B. Bütün uzunlukları piksele dönüştürür.  
C. Yalnızca baskıda çalışır.  
D. Miras alınan rengi engeller.  
E. İçerik veya hareketli tarayıcı kontrolleri katı yüksekliğin kırpma ya da taşmaya yol açmasına neden olabilir; minimum yükseklik veya dinamik viewport birimi gereksinime daha uygun olabilir.

### 38.

Odağı özellikle klavye benzeri odak etkileşiminde göstermek için en uygun selector hangisidir?

A. `:focus-visible`  
B. `:hover-only`  
C. `:visited-focus`  
D. `::keyboard`  
E. `[focus=mouse]`

### 39.

Kök yazı boyutu `18px` ise `2rem` uzunluğunun hesaplanan değeri nedir?

A. `2px`  
B. `18px`  
C. `20px`  
D. `36px`  
E. Yalnızca öğenin kendi yazı boyutuna bağlıdır.

### 40.

`320px` genişlikte sayfada yatay kaydırma oluşmaktadır. En disiplinli hata ayıklama işlemi hangisidir?

A. Bütün taşmayı hemen gizlemek  
B. Hangi öğenin viewport'u aştığını incelemek, buna yol açan hesaplanmış boyutu veya bölünemeyen içeriği belirlemek, ilgili kısıtı düzeltmek ve yeniden test etmek  
C. İkinci bir viewport meta öğesi eklemek  
D. Sayfanın tamamını yüzde 50 ölçeklemek  
E. Bütün semantik öğeleri kaldırmak

---

## Cevap Kâğıdı

| Soru | Cevap | Soru | Cevap | Soru | Cevap | Soru | Cevap |
|---:|:---:|---:|:---:|---:|:---:|---:|:---:|
| 1 |  | 11 |  | 21 |  | 31 |  |
| 2 |  | 12 |  | 22 |  | 32 |  |
| 3 |  | 13 |  | 23 |  | 33 |  |
| 4 |  | 14 |  | 24 |  | 34 |  |
| 5 |  | 15 |  | 25 |  | 35 |  |
| 6 |  | 16 |  | 26 |  | 36 |  |
| 7 |  | 17 |  | 27 |  | 37 |  |
| 8 |  | 18 |  | 28 |  | 38 |  |
| 9 |  | 19 |  | 29 |  | 39 |  |
| 10 |  | 20 |  | 30 |  | 40 |  |
