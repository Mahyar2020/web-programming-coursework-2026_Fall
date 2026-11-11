# Web Programlama Platformdan Üretime

## Ara Sınav - Temeller Baskısı (Gözden Geçirilmiş v18)

**Adı ve soyadı:** ________________________________________  
**Öğrenci numarası:** ____________________________________  
**Tarih:** ____________________  
**Süre:** 80 dakika  
**Toplam:** 100 puan

### Yönergeler

- Bu sınav 40 çoktan seçmeli sorudan oluşmaktadır.
- Her soru 2,5 puandır.
- Her soru için en uygun tek seçeneği işaretleyiniz.
- Her sorunun beş seçeneği (A-E) ve yalnızca bir doğru cevabı vardır.
- Aksi belirtilmedikçe standartlara uygun güncel tarayıcıları ve kitapta açıklanan ders ortamını varsayınız.

---

## Bölüm I - Çalışma Ortamı ve Geliştirme İş Akışı

### 1.

Bir öğrenci Node.js'i kurmuş ancak henüz herhangi bir ders komutu çalıştırmamıştır. Kurulumun ders iş akışına hazır olduğunu en iyi hangi kanıt gösterir?

A. Kurulum dosyasının İndirilenler klasöründe bulunması  
B. `node --version` komutunun gerekli sürümü göstermesi ve deponun doğrulama betiğinin başarıyla tamamlanması  
C. Node.js web sitesinin tarayıcıda açılması  
D. Masaüstünde bir Node.js kısayolunun bulunması  
E. Öğrencinin bir HTML dosyasını çift tıklayarak açabilmesi

### 2.

`npm test` komutu çalıştırıldığında yolu `C:\Users\Student\package.json` ile biten bir `ENOENT` hatası oluşmaktadır. Gerçek depo `C:\Users\Student\Documents\GitHub\coursework` içindedir. İlk olarak yapılması gereken en uygun işlem hangisidir?

A. npm'i global olarak yeniden kurmak  
B. `C:\Users\Student` içinde yeni ve boş bir `package.json` oluşturmak  
C. Depoyu silip yeniden klonlamak  
D. Deponun kök dizinine geçmek, `package.json` dosyasının bulunduğunu doğrulamak ve komutu yeniden çalıştırmak  
E. Sayfayı bir `file:` URL'siyle açmak

### 3.

Kaydetme, commit oluşturma ve push işlemleri arasındaki farkı hangi ifade doğru açıklar?

A. Kaydetme dosya değişikliklerini yazar; commit seçilen içeriği yerel Git geçmişine kaydeder; push ise commitleri uzak depoya aktarır.  
B. Kaydetme ve commit değişiklikleri karşıya yükler; push ise bir web sitesi yayımlar.  
C. Kaydetme dosyaları staging alanına ekler; commit testleri çalıştırır; push bir branch oluşturur.  
D. Kaydetme yalnızca tarayıcı depolamasına, commit diske, push ise Git'e yazar.  
E. Kaydetme yerel anlık görüntü oluşturur; commit bunu GitHub'a gönderir; push ise `main` ile birleştirir.

### 4.

Campus Hub sayfası görünmektedir ancak Network paneli boştur. Projeyi değiştirmeden doğrudan yararlı kanıt elde etmek için hangi işlem yapılmalıdır?

A. Trafiği kaydeden bir tarayıcı eklentisi kurmak  
B. Bilgisayarı yeniden başlatıp tarayıcıyı yeniden kurmak  
C. Sayfaya yeni bir `<script>` öğesi eklemek  
D. Devam etmeden önce mevcut dosyaları commit etmek  
E. Network panelini açık tutup isteğin kaydedilmesi için sayfayı yenilemek

---

## Bölüm II - Web Nasıl Çalışır

### 5.

İnternet ile Web arasındaki ilişkiyi en doğru hangi ifade açıklar?

A. Bunlar aynı protokolün iki farklı adıdır.  
B. İnternet, Web tarafından gerçekleştirilen bir tarayıcı özelliğidir.  
C. İnternet ağ altyapısıdır; Web ise bağlantılı kaynakları paylaşmak için bu altyapıyı kullanan bir uygulamadır.  
D. Web fiziksel ağdır; İnternet ise onun HTML içeriğidir.  
E. İnternet yalnızca e-postayı, Web ise yalnızca web sitelerini yönetir.

### 6.

`https://hub.campus.example:8443/events?day=monday#details` adresinde hangi bileşen normal olarak HTTP istek hedefinin bir parçası olarak gönderilmez, istemcide tutulur ve istemci tarafından yorumlanır?

A. `#details`  
B. `day=monday`  
C. `/events`  
D. `8443`  
E. `hub.campus.example`

### 7.

Bir Web origin değerini hangi üç bileşen belirler?

A. Host, path ve query  
B. Scheme, path ve fragment  
C. Scheme, query ve port  
D. Scheme, host ve etkin port  
E. Host, query ve fragment

### 8.

Adı belirtilmiş bir web sitesine yapılan sıradan gezinme sırasında DNS'in temel katkısı nedir?

A. HTTP yanıt gövdesini şifrelemek  
B. Host adını, hizmete ulaşmak için kullanılacak adres bilgisine çözümlemek  
C. HTML'yi DOM'a dönüştürmek  
D. Sitedeki bilgilerin doğru olduğunu doğrulamak  
E. Cascade içinde hangi CSS kurallarının kazanacağını seçmek

### 9.

Tarayıcı, biçimlendirilmiş bir HTML hata sayfasını HTTP `404` durum koduyla birlikte alıyor. Hangi sonuç doğrudur?

A. Sunucular yalnızca `200` yanıtı verdiği için hiçbir sunucuyla iletişim kurulmamıştır.  
B. Tarayıcı istek göndermeden önce DNS kesinlikle başarısız olmuştur.  
C. Tarayıcı HTML'yi yanıt almadan kendisi üretmiştir.  
D. HTTPS başarılı bir yanıtı hataya dönüştürmüştür.  
E. Sunucu yanıt vermiş ve yanıt, istenen kaynağın bulunamadığını bildirmiştir.

### 10.

HTTPS hakkında hangi ifade doğrudur?

A. Sitede sunulan tüm bilgilerin doğru olduğunu kanıtlar.  
B. Uygulamada hiçbir güvenlik kusuru bulunmadığını garanti eder.  
C. Bağlantıyı korur ve sertifikalı sunucu kimliğini doğrular; ancak uygulamanın dürüst veya hatasız olduğunu garanti etmez.  
D. Sunucunun `4xx` veya `5xx` yanıtları döndürmesini engeller.  
E. Tüm kaynakların aynı origin'i paylaşmasını sağlar.

### 11.

Tek bir Web sayfasının görüntülenmesi neden çok sayıda HTTP isteği oluşturabilir?

A. Belgenin ayrıştırılması; ayrıca alınması gereken stil sayfalarını, betikleri, görselleri, yazı tiplerini ve verileri ortaya çıkarabilir.  
B. HTTP, her HTML öğesinin ayrı ayrı istenmesini zorunlu kılar.  
C. DNS, her öğe için sayfa isteğinin tamamını tekrarlar.  
D. Git, commit edilmiş her dosya için bir istek oluşturur.  
E. Tarayıcı her CSS bildirimi için farklı bir sunucuyla iletişim kurmalıdır.

### 12.

Network paneli bir belge isteği için `200 OK` göstermektedir. Yalnızca bu kanıttan hangi sonuca varılabilir?

A. Sayfa her kullanıcı için erişilebilirdir.  
B. HTML geçerlidir ve görüntülenen bilgiler doğrudur.  
C. Tüm alt kaynaklar da başarıyla yüklenmiştir.  
D. Sunucu, ilgili HTTP isteğini yönteminin anlamına uygun biçimde başarıyla işlemiştir; ancak uygulamanın doğruluğu için başka kanıtlar gerekir.  
E. Yanıt, sayfadaki her betikle aynı origin'den gelmiştir.

### 13.

HTTP'nin stateless olarak tanımlanmasını en iyi hangi ifade açıklar?

A. Sunucuların uygulama verisi saklaması yasaktır.  
B. HTTP, bağımsız istekler arasındaki konuşmayı kendiliğinden hatırlamaz; uygulamalar sürekliliği açık mekanizmalarla ekler.  
C. Tarayıcılar cookie veya yetkilendirme bilgisi gönderemez.  
D. Her yanıtın gövdesi boş olmalıdır.  
E. Bir istemci her bağlantıda yalnızca bir istek gönderebilir.

### 14.

HTTP üzerinden sunulan bir sayfayı doğrudan açılmış yerel bir dosyadan en açık biçimde hangi gözlem ayırır?

A. Belgenin bir `<html>` öğesi içermesi  
B. Sayfanın bir tarayıcı penceresinde görüntülenmesi  
C. Kaynak dosyanın `.html` uzantısına sahip olması  
D. Sayfanın göreli bir bağlantı içermesi  
E. Adresin `http:` veya `https:` kullanması ve Network panelinde yöntem ile durum içeren bir belge alışverişinin görünmesi

### 15.

HTML kaynağı ile DOM arasındaki farkı hangi ifade doğru açıklar?

A. DOM özgün dosyadır; HTML ise onun ekran görüntüsüdür.  
B. HTML yalnızca JavaScript çalıştıktan sonra oluşur; DOM ise ayrıştırmadan önce vardır.  
C. HTML kaynak işaretleme dilidir; DOM tarayıcının canlı ayrıştırılmış ağacıdır ve ayrıştırıcı düzeltmelerini veya sonraki betik değişikliklerini içerebilir.  
D. HTML stilleri, DOM ise yalnızca ağ başlıklarını saklar.  
E. İkisi her zaman karakter karakter aynı olmak zorundadır.

### 16.

Hangi HTML parçası birinci düzey başlığı ve ardından `events.html` adresine çalışan bir bağlantıyı doğru biçimde oluşturur?

A. `<h1>Kampüs Etkinlikleri</h1><a href="events.html">Etkinlikleri görüntüle</a>`  
B. `<h1>Kampüs Etkinlikleri</h1><a>Etkinlikleri görüntüle</a>`  
C. `<h2>Kampüs Etkinlikleri</h2><a href="events.html">Etkinlikleri görüntüle</a>`  
D. `<h1>Kampüs Etkinlikleri</h1><button href="events.html">Etkinlikleri görüntüle</button>`  
E. `<heading>Kampüs Etkinlikleri</heading><a src="events.html">Etkinlikleri görüntüle</a>`

---

## Bölüm III - Semantik HTML ve Erişilebilir Formlar

### 17.

Semantik HTML'nin temel amacı nedir?

A. Her öğenin tam renklerini ve aralıklarını tanımlamak  
B. Hiçbir CSS'e gerek kalmayacağını garanti etmek  
C. Her belgenin tüm tarayıcılarda aynı görünmesini sağlamak  
D. İçerik ve denetimlerin rollerini ve aralarındaki ilişkileri iletmek  
E. Tüm erişilebilirlik testlerinin yerini almak

### 18.

Bir tasarımcı, bir alt bölüm başlığının daha küçük görünmesini istiyor. En iyi uygulama hangisidir?

A. Hiyerarşiden bağımsız olarak varsayılan yazı tipi daha küçük olduğu için `<h5>` seçmek  
B. Belge hiyerarşisini temsil eden başlık düzeyini koruyup görünümünü CSS ile değiştirmek  
C. Başlığı bir `<div>` ve kalın metinle değiştirmek  
D. Başlık yerine placeholder kullanmak  
E. Görsel önemini azaltmak için alt bölümü `<footer>` içine yerleştirmek

### 19.

`<article>` hangi durumda genellikle `<section>` öğesinden daha uygundur?

A. İçeriğin kenarlığa ihtiyaç duyduğu her durumda  
B. Öğe, `<main>` öğesinin ilk çocuğu olduğunda  
C. İçerik bir başlık içerdiğinde  
D. JavaScript içeriği güncelleyeceğinde  
E. Bileşim, haber yazısı veya etkinlik kartı gibi bağımsız olarak anlamlı ya da yeniden kullanılabilir olduğunda

### 20.

Mavi dikdörtgen biçiminde stillendirilmiş bir denetim ayrıntılar sayfasını açmaktadır. Davranışla en iyi eşleşen yerel öğe hangisidir?

A. Tüm mavi denetimler düğme olduğu için `<button type="button">`  
B. Stilleme semantiği belirlediği için `<div tabindex="0">`  
C. Denetim bir kaynağa gittiği için `<a href="details.html">`  
D. Tüm kullanıcı eylemleri form gönderdiği için `<input type="submit">`  
E. Gezinme yalnızca görsel olduğu için `<span role="presentation">`

### 21.

Placeholder metni neden görünür ve programatik olarak ilişkilendirilmiş bir form etiketinin yeterli bir alternatifi değildir?

A. Veri girişi sırasında kaybolur ve kullanıcının gereksinim duyduğu kalıcı erişilebilir adı ve yönergeyi güvenilir biçimde sağlamaz.  
B. Her zaman denetimin değeri olarak gönderilir.  
C. Klavye odağını engeller.  
D. Tarayıcı doğrulamasını otomatik olarak devre dışı bırakır.  
E. Yalnızca `<textarea>` ile kullanılabilir.

### 22.

Bir denetimin `name` niteliğinin formla ilgili amacı nedir?

A. Sayfa başlığında gösterilen metni ayarlar.  
B. Denetimin CSS specificity değerini belirler.  
C. Denetimin görünür etiketini sağlar.  
D. Denetimin gönderilen değeriyle ilişkilendirilen anahtarı sağlar.  
E. Denetim `disabled` olsa bile gönderime katılmasını zorunlu kılar.

### 23.

Sunucu, tarayıcının zaten gerçekleştirdiği doğrulamayı neden tekrarlamalıdır?

A. Tarayıcı doğrulaması ancak sunucu veriyi kabul ettikten sonra çalışır.  
B. İstemci tarafı denetimleri atlanabilir veya değiştirilebilir; bu nedenle sunucu işlemi kendi güven sınırında korumalıdır.  
C. HTML denetimleri gerekli değerleri hiçbir zaman doğrulamaz.  
D. Sunucu doğrulaması yalnızca CSS stillemesini iyileştirmek için gereklidir.  
E. Doğrulamayı tekrarlamak gönderimi otomatik olarak şifreler.

### 24.

Bir görsel tamamen dekoratiftir ve sayfayı anlamak ya da kullanmak için gerekli hiçbir bilgiyi tekrar etmemektedir. Genellikle hangi işaretleme uygundur?

A. Tarayıcının açıklama oluşturması için `alt` niteliğini yazmamak  
B. Dosya adını alternatif metin olarak kullanmak  
C. Görseli bir başlığın içine yerleştirmek  
D. `alt="dekoratif görsel"` yazmak  
E. Gereksiz görseli erişilebilirlik deneyiminden çıkarmak için `alt=""` kullanmak

### 25.

Bir formda `<input required="false">` bulunmaktadır. Standartlara uygun bir tarayıcı `required` niteliğini nasıl yorumlar?

A. Dize değeri `false` olduğu için denetim isteğe bağlıdır.  
B. Geçersiz bir değere sahip olduğu için nitelik yok sayılır.  
C. Boolean nitelikler mevcut olduklarında true sayıldıkları için denetim zorunludur.  
D. Denetim salt okunur hâle gelir.  
E. Form yalnızca JavaScript ile gönderilebilir.

### 26.

`type="number"` bir öğrenci numarası veya posta kodu için neden genellikle kötü bir seçimdir?

A. Bunlar nicelik değil tanımlayıcıdır; number denetimleri aritmetik davranış izlenimi verebilir ve baştaki sıfırlar gibi biçimleri hatalı işleyebilir.  
B. Number denetimlerinin etiketi olamaz.  
C. Number denetimleri hiçbir zaman klavyeyle erişilebilir değildir.  
D. Bu tanımlayıcılar kullanıcılardan her zaman gizlenmelidir.  
E. Number denetimi sunucuya hiçbir değer göndermez.

### 27.

Olağan form davranışında `disabled` ve `readonly` metin denetimlerini hangi ifade doğru karşılaştırır?

A. Her ikisi de gönderimden daima çıkarılır.  
B. Her ikisi de düzenlenebilir kalır ancak odak alamaz.  
C. `disabled` değerler gönderilir, `readonly` değerler gönderilmez.  
D. Devre dışı bırakılmış bir denetim normalde gönderime katılmaz; `name` niteliği bulunan salt okunur metin denetimi normalde gönderilir.  
E. `readonly`, değeri sunucu için otomatik olarak güvenilir hâle getirir.

### 28.

Sunucu, iki alan geçersiz olduğu için gönderilen formu reddediyor. Hangi yanıt en güçlü erişilebilir düzeltme deneyimini sağlar?

A. Tüm alanları temizlemek ve formun çevresinde yalnızca kırmızı bir kenarlık göstermek  
B. Hataya özgü sayfa başlığı, bağlantılı hata özeti, denetimlerle ilişkilendirilmiş alan mesajları, uygun geçersiz durum/odak yönetimi sunmak ve güvenli geçerli değerleri korumak  
C. Yalnızca “Geçersiz giriş.” diyen bir uyarı göstermek  
D. Tüm denetimleri devre dışı bırakıp kullanıcıdan sayfayı yenilemesini istemek  
E. Görünür bir açıklama olmadan `200 OK` döndürmek

---

## Bölüm IV - CSS Yerleşim ve Duyarlı Tasarım

### 29.

Cascade'i en iyi hangi ifade açıklar?

A. Stil sayfasında yazılmış ilk bildirimi seçer.  
B. Yalnızca kalıtılan özelliklere uygulanır.  
C. Satır içi stillere her olası bildirime karşı daima öncelik verir.  
D. Kuralları yalnızca seçici uzunluğuna göre sıralar.  
E. Çakışan bildirimleri origin, importance, layer, specificity ve source order gibi etkenlerle çözümler.

### 30.

Varsayılan `content-box` modelinde bir öğenin `width: 300px`, iki yandaki `padding` değeri `20px` ve iki yandaki kenarlığı `2px`'tir. Margin değerleri hariç dış inline boyutu nedir?

A. `300px`  
B. `322px`  
C. `344px`  
D. `340px`  
E. `384px`

### 31.

Aşağıdaki kural neden bir projenin temel CSS'inde yaygın olarak kullanılır?

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

A. Bildirilen width ve height değerlerine öğenin padding ve border değerlerini dâhil ederek kutu boyutlandırmasını daha öngörülebilir hâle getirir.  
B. Tüm öğeleri eşit boyutlara zorlar.  
C. Tarayıcının tüm varsayılan stillerini kaldırır.  
D. Her öğeyi bir flex container'a dönüştürür.  
E. İçeriğin taşmasını her koşulda engeller.

### 32.

Alan daraldığında öğeleri alt satıra geçmesi gereken tek boyutlu bir gezinme listesine en uygun yerleşim seçeneği hangisidir?

A. Mutlak konumlandırma  
B. Çok sütunlu yerleşim  
C. Tek satırlı bir tablo  
D. Sarmalama etkinleştirilmiş Flexbox  
E. Sabit genişlikli float öğeleri

### 33.

Satırları ve sütunları iki boyutta koordine etmesi gereken kart koleksiyonu için en uygun yerleşim seçeneği hangisidir?

A. Yalnızca normal inline akış  
B. CSS Grid  
C. Metin hizalama  
D. Her kartta göreli konumlandırma  
E. Bir dizi `<br>` öğesi

### 34.

Bir etkinlik kartı, içinde bulunduğu kenar çubuğu viewport genişliğinden bağımsız olarak `20rem` değerinden daha geniş olduğunda iç yerleşimini değiştirmelidir. Bu gereksinimi en iyi hangi mekanizma ifade eder?

A. Cihaz modeline dayalı bir `screen` media query  
B. İşletim sistemi adını denetleyen JavaScript  
C. Yazdırma stil sayfası  
D. Kart üzerinde sabit genişlik  
E. Kartın container inline boyutuna dayalı bir container query

### 35.

Duyarlı tasarım breakpoint'i seçmek için en iyi ilke hangisidir?

A. Yalnızca en yeni telefonun boyutlarını kullanmak  
B. Her 100 pikselde bir breakpoint eklemek  
C. İçerik ve yerleşimin anlamlı bir geliştirme için yeterli alana gereksinim duyduğu noktada eklemek  
D. Her projede aynı breakpoint'i kullanmak  
E. Kullanıcının tarayıcı markasına göre belirlemek

### 36.

Yanlış HTML kaynak sırasını düzeltmek için CSS `order` kullanmak neden erişilebilirlik sorunu oluşturabilir?

A. Görsel sıra değişirken okuma ve klavye odak sırası DOM'u izlemeye devam edebilir.  
B. Bu özellik tüm öğeleri erişilebilirlik ağacından çıkarır.  
C. Bu özellik yalnızca yazdırma ortamında çalışır.  
D. Grid ve Flexbox öğelerinin sarmalanmasını engeller.  
E. Bağlantıları otomatik olarak düğmelere dönüştürür.

### 37.

Hangi gizleme tekniği bir öğeyi görünmez yaparken öğenin olağan yerleşim kutusunu korumasına ve öğeye bağlı olarak etkileşim ya da odak için kullanılabilir kalmasına neden olabilir?

A. `display: none`  
B. HTML `hidden` niteliği  
C. Öğeyi DOM'dan kaldırmak  
D. `opacity: 0`  
E. Metnini boş dize yapmak

### 38.

Klavye erişilebilirliği için en uygun odak uygulaması hangisidir?

A. Odak bağlamdan anlaşılabildiği için tüm outline göstergelerini kaldırmak  
B. Açıkça görülebilen bir `:focus-visible` göstergesi sağlamak ve sabit ya da sticky içeriğin bunu kapatmadığını test etmek  
C. Odağı yalnızca işaretçi denetimin üzerine geldiğinde göstermek  
D. Odağı yalnızca renkle ve sadece geniş ekranlarda belirtmek  
E. Odaklanan öğeleri DOM'un başına taşımak

### 39.

Bir kart, tipik `16px` kök yazı tipi boyutunda `280px` genişliğindeki container içinde `width: 20rem` kullanmaktadır. Tercih edilen `20rem` üst sınırını korurken yatay taşmayı önleme olasılığı en yüksek değişiklik hangisidir?

A. `width: 20rem !important;`  
B. `min-width: 20rem;`  
C. `width: 280rem;`  
D. `position: absolute;`  
E. `width: min(100%, 20rem);`

### 40.

Geliştirici araçlarında bir CSS bildiriminin üzeri çizilmiş görünmekte ve beklenen yerleşim oluşmamaktadır. En disiplinli inceleme sırası hangisidir?

A. Birkaç `!important` bildirimi eklemek ve sayfa doğru görünene kadar yenilemek  
B. Stil sayfasının yüklenip yüklenmediğini denetlemeden HTML'yi yeniden yazmak  
C. Stil sayfasının yüklendiğini, seçicinin amaçlanan öğeyle eşleştiğini, bildirimin cascade'i kazanıp geçerli bir değere hesaplandığını ve yerleşimin beklenen alan ile içerik varsayımlarına sahip olduğunu doğrulamak  
D. Tarayıcıyı değiştirmek ve özgün tarayıcının hatalı olduğunu varsaymak  
E. Cascade'i kaldırmak için diğer tüm stil sayfalarını silmek

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
