# Oturum 5 - Belge Nesne Modeli, Olaylar ve Formlar

Önceki bölümde JavaScript dilini öğrendik; JavaScript ile tarayıcının aynı şey
olmadığını da gördük. Şimdi bu sınırı bilinçli biçimde geçeceğiz. Tarayıcı,
JavaScript'e sayfanın canlı bir temsilini sunar, kullanıcı ve sistem
etkileşimlerini olaylar aracılığıyla bildirir ve formların davranışını yönetir.
Bu özellikler birlikte Campus Hub belgesini etkileşimli bir uygulamaya
dönüştürür.

Bu bölüm, ekranda görünen tek bir paragraf ve düğmeyle başlar; ardından aynı
fikirleri aranabilir bir etkinlik listesine taşır. Öğrenci; kaynak HTML'den canlı
belgeye, olaydan duruma, durumdan ekrana ve form denetiminden doğrulanmış veriye
uzanan sınırları açıklayabilirse React gibi bir çerçevenin mantığını da ezber
yerine kavrayabilir.

## Bölümün yol haritası

Tablo 5.1, gözlemden sınanmış bir özelliğe uzanan öğrenme sırasını gösterir.
Öğrenciler her aşamada önce ne beklediklerini söyler, sonra tarayıcıdan kanıt
toplar.

**Tablo 5.1 - Oturum 5 öğrenme sırası ve gözlenebilir kanıtlar**

| Aşama | Temel soru | Kanıt |
|---|---|---|
| Gözlem | JavaScript gerçekte hangi sayfayla etkileşir? | Kaynak metin ile canlı Document Object Model karşılaştırılır. |
| Seçme ve değiştirme | Kod, amaçlanan öğeyi nasıl bulur ve günceller? | Seçici, null denetimi ve güvenli değişiklik görünür bir sonuç üretir. |
| Modelleme | Uygulamanın durumu nerede tutulmalıdır? | Tek bir durum nesnesi yinelenebilir bir ekrana dönüştürülür. |
| Tepki verme | Tarayıcı etkileşimi nasıl bildirir? | Olay özellikleri ve yayılma yolu incelenir. |
| Veri toplama | Form nasıl yapılandırılmış veriye dönüşür? | Adlandırılmış denetimler FormData içinde görülür. |
| Doğrulama | Yararlı ve erişilebilir hata nasıl bildirilir? | Yerel kısıtlar ve özel iletiler klavye ile sınanır. |
| Mühendislik | Daha büyük arayüzler nasıl öngörülebilir ve verimli kalır? | DOM çalışması gruplanır, gözlemlenir ve açık bileşen sınırları içinde tutulur. |
| Doğrulama | Davranışın çalıştığını nasıl anlarız? | Model testleri geçer ve tarayıcı çıktısı incelenir. |

## Ön koşullar

2-4. bölümleri tamamlayın veya anlamsal HyperText Markup Language (HTML), temel
Cascading Style Sheets (CSS) ve JavaScript fonksiyonlarını, dizilerini,
nesnelerini, modüllerini ve testlerini okuyabiliyor olun. Komutları,
`package.json` dosyasının bulunduğu depo kök klasöründe çalıştırın. Bölüm 0,
depo klasörünü bulmayı ve sunucu terminalini sıradan komut terminalinden ayırt
etmeyi açıklar.

## Öğrenme çıktıları

Bu bölümün sonunda:

1. HTML kaynak metnini tarayıcının canlı Belge Nesne Modelinden (Document Object
   Model, DOM) ayırabilecek;
2. `window`, `document`, düğüm, öğe ve metin düğümünün görevini açıklayabilecek;
3. CSS seçicileriyle öğe bulup bulunamayan sonucu güvenli biçimde ele alabilecek;
4. kırılgan sayfa düzenine bağımlı kalmadan yakın öğeler arasında gezinebilecek;
5. metni, öznitelikleri, özellikleri, sınıfları ve veri özniteliklerini amaca
   uygun güncelleyebilecek;
6. düğüm oluşturabilecek, kopyalayabilecek, ekleyebilecek, değiştirebilecek ve
   kaldırabilecek;
7. güvenilmeyen düz metin için `innerHTML` yerine `textContent` seçebilecek;
8. uygulama durumunu ekrandaki temsilden ayrı tutabilecek;
9. olayın dağıtılmasını, yakalama, hedef ve kabarcıklanma aşamalarını
   açıklayabilecek;
10. `event.target` ile `event.currentTarget` ayrımını yapabilecek;
11. varsayılan davranışı önleme ve yayılmayı durdurma yöntemlerini doğru amaçla
    kullanabilecek;
12. dinamik öğe listelerinde olay devrini uygulayabilecek;
13. ömrü biten olay dinleyicilerini kaldırabilecek;
14. form denetimlerini `FormData` ile okuyup başarılı denetim kurallarını
    yorumlayabilecek;
15. yerel kısıt doğrulamasını kullanıp özel doğrulamayı erişilebilir biçimde
    ekleyebilecek;
16. sunucu doğrulamasını son güven sınırı olarak koruyabilecek;
17. görünür, programatik ve odak davranışı düşünülmüş geri bildirim
    sağlayabilecek;
18. ekran güncellendiğinde klavye odağını koruyabilecek;
19. aşamalı iyileştirmeyi ve JavaScript kapalıyken oluşan farkı açıklayabilecek;
20. tarayıcı geliştirici araçlarıyla DOM ve olay davranışını hata ayıklayabilecek;
21. Campus Hub etkinlik gezginini oluşturup sınayabilecek;
22. yinelenen eşzamanlı yerleşim çalışmasını önlemek için DOM okumalarını yazmalardan ayırabilecek;
23. kendi durum modelinizin dışında yapılan değişiklikleri izlemek gerektiğinde `MutationObserver` kullanabilecek;
24. light DOM, shadow DOM, olay yeniden hedefleme ve özel öğelerin amacını açıklayabilecek;
25. yerel klavye, işaretçi, form ve yardımcı teknoloji davranışını koruyan olayı seçebilecek; ve
26. form sahipliği, sıfırlama, serileştirme kodlaması ve dosya girdisi sınırlarını açıklayabileceksiniz.

---

# 1. HTML kaynağından canlı belgeye

Şu kaynak satırını düşünün:

```html
<p id="status">Üç etkinlik var.</p>
```

Diskte bu satır karakterlerden oluşur. Tarayıcı, HyperText Markup Language
(HTML) karakterlerini ayrıştırır ve ağaç biçiminde bağlı nesneler oluşturur.
JavaScript dosyadaki baytlarla değil, bu nesnelerle etkileşir. Bu yapıya **Belge
Nesne Modeli (Document Object Model, DOM)** denir. “Belge”, yüklenmiş sayfayı;
“nesne modeli” ise sayfa parçalarının özellik ve yöntemleri olan nesnelerle
sunulmasını anlatır. Tarayıcı uygulama programlama arayüzü (Application
Programming Interface, API), tarayıcı nesnelerinin JavaScript'e sunduğu özellik
ve yöntemler bütünüdür.

Şekil 5.1, kaynak satırının canlı ağaç gösterimine ve oradan piksellere nasıl
dönüştüğünü izler. DOM değişikliği ekranda değişiklik yaratabilir; fakat diskteki
HTML dosyasını yeniden yazmaz.

**Şekil 5.1.** Kaynak HTML ayrıştırılarak canlı DOM ağacına, ardından ekranda
görülen piksellere dönüşür.

<!-- figure:dom-source-live-tree -->

## 1.1 Tarayıcı nesneleri

Tarayıcı birbiriyle ilişkili, ancak birbirinin yerine kullanılamayan nesneler
sunar. Tablo 5.2, her nesnenin neyi temsil ettiğini ve ne işe yaradığını gösterir.

**Tablo 5.2 - Tarayıcı nesneleri ve sorumlulukları**

| Ad | Anlamı | Örnek görevi |
|---|---|---|
| `window` | Tarama bağlamının genel nesnesi | Görünüm alanı, zamanlayıcılar, adres ve genel olaylar |
| `document` | Yüklenmiş HTML belgesi | Belge düğümlerini seçmek ve oluşturmak |
| `Node` | Ağaçtaki genel nesne arayüzü | Üst-alt ilişkileri ve kaldırma işlemi |
| `Element` | `<button>` gibi bir HTML öğesinin düğümü | Öznitelikler, sınıflar ve seçici eşleşmesi |
| `HTMLElement` | HTML öğelerine özgü davranış | `hidden`, `dataset` ve odak davranışı |
| `Text` | Bir öğenin içindeki karakter verisi | Paragrafta gösterilen sözcükler |

İlişkiyi şöyle okuyun: `HTMLElement`, `Element` türünden; `Element` ise `Node`
türündendir. `Text` de bir `Node` nesnesidir, ancak `Element` değildir. Her öğe
bir düğümdür; fakat her düğüm bir öğe değildir. Bu nedenle `childNodes` boşluk
karakterlerinden oluşan metin düğümlerini de içerebilirken `children` yalnızca
öğeleri içerir. Şekil 5.2 bu tür ilişkisini görselleştirir.

**Şekil 5.2.** `Node`, `Element` ve `HTMLElement` bir tür zinciri oluşturur;
`Text` ise öğe olmayan başka bir düğüm türüdür.

<!-- figure:dom-interface-map -->

## 1.2 Kaynak, DOM ve ekranda çizilen sayfa

Tarayıcı hatalı iç içe yerleşimleri onarabilir. Eklentiler düğüm ekleyebilir;
JavaScript de yüklemeden sonra ağacı değiştirebilir. Bu yüzden üç farklı kanıtı
ayırt edin:

- **Sayfa kaynağını görüntüle** alınan kaynak metni gösterir.
- **Elements** paneli o andaki canlı DOM'u gösterir.
- Tarayıcı penceresi o DOM'un ve biçimlendirme kurallarının çizilmiş sonucunu
  gösterir.

Bir hata ayıklarken önce hangi soruyu sorduğunuzu belirleyin. Sonradan JavaScript
tarafından eklenen bir düğüm, yalnızca kaynak görünümüne bakılarak bulunamaz.

## 1.3 Ayrıştırıcı ne yapar?

Tarayıcı HTML'i sırayla okur. Açılış etiketini görünce bir öğe nesnesi oluşturur,
ağaçta doğru yere bağlar ve okumaya devam eder. Etiketler arasındaki yazı metin
düğümüne dönüşür. Kapanış etiketi, yeni düğümlerin hangi üst öğeye bağlanacağını
değiştirir. Dolayısıyla kaynak dosya ekran görüntüsü değildir; yapılandırılmış
bir ağaç oluşturma sürecine verilen girdidir.

Ayrıştırıcı başka kaynaklarla da karşılaşır. Stil sayfası yararlı bir görüntünün
ne zaman çizileceğini etkileyebilir. Normal bir JavaScript dosyası alınırken ve
çalıştırılırken ayrıştırma durabilir. `defer` özniteliği bulunan klasik dosya,
ayrıştırma bitince çalışır. Modül dosyaları da varsayılan olarak ertelenir.
`DOMContentLoaded`, belge ayrıştırıldıktan sonra oluşur. `load` olayı ise resim
gibi başka kaynakları da beklediğinden daha geç gerçekleşir.

## 1.4 Kod belgeyi ne zaman seçebilir?

Bu kitap uygulama modüllerini belge başlığında yükler:

```html
<script type="module" src="app.js"></script>
```

Tarayıcı modülü, belgeyi ayrıştırdıktan sonra çalıştırır. Bu nedenle gövdede
yazılı öğeler `app.js` başladığında hazırdır. Başlıkta `defer` olmadan yüklenen
klasik bir dosya, gövdedeki öğeler oluşturulmadan çalışabilir. Dosya farklı
yerlerden yüklenebilecekse `DOMContentLoaded` dinleyicisi başka bir geçerli
seçenektir. Açık bir yükleme kuralınız varsa aynı amaçla gereksiz yere hem
ertelemeyi hem hazır olma dinleyicisini kullanmayın.

---

# 2. Öğeleri seçme ve ağaçta gezinme

`document.querySelector()` bir CSS seçicisi kabul eder ve ilk eşleşen öğeyi
döndürür. Eşleşme yoksa `null` döner.

```js
const status = document.querySelector("#status");

if (!status) {
  throw new Error("Belgede #status öğesi bulunmalı.");
}
```

Bu denetim gereksiz değildir. `id` değiştirilmiş, başka sayfa açılmış veya
betik yanlış yüklenmiş olabilir. Açık hata, HTML ile JavaScript arasındaki
sözleşmenin bozulduğunu nedenine yakın yerde gösterir. Bir öğenin bulunmaması
gerçekten kabul edilebilir değilse isteğe bağlı zincirleme kullanmayın.

`document.querySelectorAll()` o anda eşleşen öğelerden oluşan statik bir
`NodeList` döndürür. “Statik”, sonradan eklenen eşleşmelerin bu listenin içine
kendiliğinden girmediği anlamına gelir.

```js
const cards = [...document.querySelectorAll(".event-card")];
const fullCards = cards.filter((card) => card.dataset.remaining === "0");
```

`getElementById("status")` tek bir `id` için açık ve anlaşılırdır. Küçük bir
sayfada okunabilirlik, yapay performans tartışmalarından daha değerlidir.

Seçiciyi tüm belge yerine bir öğe içinde de arayabilirsiniz:

```js
const cards = eventList.querySelectorAll(".event-card");
```

Bu kod yalnızca `eventList` altındaki öğelere bakar. Böylece sayfanın başka bir
bölümündeki benzer sınıflar yanlışlıkla seçilmez. Seçici, HTML ile JavaScript
arasındaki bir sözleşmedir. HTML sınıfını değiştirirseniz seçiciyi de gözden
geçirin. Davranışla ilgili kararlı bir `id` veya `data-*` özniteliği, yalnızca
görsel amaçla adlandırılmış bir sınıftan daha uygun olabilir.

## 2.1 Yakın ilişkilerde gezinme

Seçiciler bir başlangıç noktasından öğe bulur. Gezinme yöntemleri, elinizdeki
öğeden devam eder:

- `closest(selector)`, öğenin kendisinde başlayıp üst öğelerde arar.
- `matches(selector)`, öğenin kendisinin seçiciyle eşleşip eşleşmediğini sorar.
- `parentElement`, `children`, `firstElementChild`, `nextElementSibling` ve
  `previousElementSibling` yapısal ilişkileri anlatır.

```js
const card = saveButton.closest("[data-event-id]");
```

`parentElement.parentElement.children[1]` gibi zincirler kırılgandır. HTML'e
bir kapsayıcı eklenmesi, “bu düğmeyi içeren etkinlik kartı” ilişkisini
değiştirmediği halde zinciri bozabilir.

Bir kerelik aramada statik `querySelectorAll()` listesi canlı listeden daha
öngörülebilir olabilir. Arayüz değiştikten sonra güncel öğeler gerekiyorsa
seçiciyi yeniden çalıştırın. Listeyi dolaşırken öğe ekleyip silmek önemlidir:
canlı liste döngü sırasında değişebilir; statik liste ise arama anındaki
eşleşmeleri korur.

---

# 3. DOM'u güvenli biçimde okuma ve değiştirme

Bir nesneyi bulmak tek başına ekranda bir şey değiştirmez. Programın doğru
özelliği okuması veya güncellemesi gerekir.

## 3.1 Metin, HTML ve güvenlik

Düz metin için `textContent` kullanın:

```js
status.textContent = "2 etkinlik gösteriliyor.";
```

Tarayıcı bu karakterleri metin olarak gösterir. `innerHTML` ise bir metni
işaretleme olarak ayrıştırır. Güvenilmeyen veri bu yolla atanırsa saldırgan
tehlikeli öğe veya öznitelik ekleyebilir. Bu, Belge Nesne Modeli tabanlı Siteler
Arası Komut Dosyası Çalıştırma (Document Object Model cross-site scripting,
DOM XSS) saldırısına ve daha genel Siteler Arası Komut Dosyası Çalıştırma
(cross-site scripting, XSS) sorununa yol açabilir. Şekil 5.3 iki veri yolunu
karşılaştırır.

**Şekil 5.3.** `textContent` veriyi yazı olarak korur; `innerHTML` veriyi HTML
ayrıştırıcısına gönderir ve güvenilir ya da doğru biçimde arındırılmış içerik
gerektirir.

<!-- figure:safe-dom-content -->

HTML ayrıştırması gerçekten gerekiyorsa yalnızca güvenilir veya gözden geçirilmiş
bir arındırıcıdan geçirilmiş işaretleme kullanın. Birkaç karakteri elle
değiştirmek genel amaçlı güvenli arındırma yöntemi değildir.

## 3.2 Öznitelikler ve özellikler aynı şey değildir

HTML öznitelikleri başlangıçtaki bildirimsel bilgiyi taşır. DOM özellikleri
nesnenin güncel durumunu sunar. Örneğin `getAttribute("checked")` onay
kutusunun kaynak işaretlemesinde başlangıçta bulunup bulunmadığını; `checked`
özelliği ise kullanıcının etkileşiminden sonraki güncel durumu gösterir.

```js
checkbox.checked = true;
button.setAttribute("aria-pressed", "true");
```

`aria-pressed`, Erişilebilir Zengin İnternet Uygulamaları (Accessible Rich
Internet Applications, ARIA)
öznitelik ailesinin bir parçasıdır. Yerel HTML kontrolünün tek başına
anlatamadığı erişilebilirlik anlamını sağlar. Durum için özel özellikler daha
uygunsa onları kullanın; özniteliğin kendisiyle çalışırken
`setAttribute`, `getAttribute`, `hasAttribute` ve `removeAttribute`
yöntemlerini kullanın.

## 3.3 Sınıflar, görünürlük ve veri öznitelikleri

`classList`, bütün sınıf metnini yeniden kurmadan adlandırılmış görünüm
durumlarını değiştirir:

```js
card.classList.toggle("event-card--saved", isSaved);
panel.hidden = !isOpen;
card.dataset.eventId = event.id;
```

`dataset.eventId`, `data-event-id` özniteliğine karşılık gelir. Veri
öznitelikleri kararlı kimlikler ve küçük bildirimsel bilgiler için kullanışlıdır.
Değerleri metindir, istemcide görünür ve güvenli gizli saklama alanı değildir.
Gizli bilgi veya sunucu için yetkili fiyat gibi değerleri burada tutmayın.

Çalışma anında hesaplanan bir değer gerçekten gerekiyorsa `style` atanabilir.
Adlandırılmış görünüm durumlarında sınıf kullanmak daha uygundur; böylece sunumun
sorumluluğu CSS'te kalır.

## 3.4 Düğüm oluşturma, kopyalama, ekleme ve kaldırma

Tarayıcı öğeleri tek tek oluşturabilir:

```js
const item = document.createElement("li");
item.textContent = "Robotik gecesi";
eventList.append(item);
```

Tekrarlanan ve anlamlı yapılar için `<template>` daha okunaklıdır. İçeriği,
kopyalanana kadar sayfada gösterilmez:

```js
const fragment = cardTemplate.content.cloneNode(true);
fragment.querySelector(".event-card__title").textContent = event.title;
eventList.append(fragment);
```

`append` sona ekler, `prepend` başa ekler; `before` ve `after` kardeş öğe
yerleştirir; `replaceChildren` kapsayıcı içeriğini bilinçli biçimde yeniler;
`remove` bir düğümü ayırır. `DocumentFragment`, istenmeyen bir kapsayıcı öğe
eklemeden birden fazla değişikliği gruplar.

Var olan bir öğeyi `append()` ile eklemek aynı nesneyi taşır; yeni bir kopya
oluşturmaz. Derin kopya için `cloneNode(true)` kullanın. Kopyalanan `id` değerleri
belgede yinelenen kimlikler yaratabilir. Şablon kopyasını doldururken beklenen alt
öğelerin var olduğunu denetleyin.

## 3.5 Öznitelik, özellik ve form denetimi durumu

Bir metin alanının `value` özelliği o andaki değerdir; kaynak özniteliği ilk
değeri sağlar. Kullanıcı yazı yazdıktan sonra özniteliği okumak eski metni
döndürebilir. Kullanıcının güncel verisi için özelliği okuyun.

`disabled` ile `readOnly` de birbirinin yerine kullanılamaz. Devre dışı denetim
kullanılamaz ve normalde form gönderimine katılmaz. Salt okunur metin alanı
klavyeyle odağı alabilir ve değeri gönderilebilir. Görsel görünüşe değil, gereken
etkileşime uygun duruma karar verin.

---

# 4. Önce durum, sonra çizim

Etkileşimli uygulama, yalnızca ekranda görülenlerden ibaret olmayan bilgileri
hatırlamalıdır: arama metni, seçilen kategori, uygunluk filtresi ve kaydedilmiş
etkinlik kimlikleri gibi. Bu bilgiler uygulama **durumunu** oluşturur.

```js
let state = {
  query: "",
  category: "all",
  availableOnly: false,
  savedIds: new Set(),
};
```

Sayfa bu durumun temsilidir. Yalnızca CSS sınıflarını veya ekrandaki sözcükleri
tek gerçek kaynak saymak davranışı öngörmeyi zorlaştırır. Olay yeni bir durum
oluşturur; `render()` DOM'u bu duruma uygun hale getirir. Şekil 5.4'teki oklar
birlikte çalışan aşamaları gösterir; alternatif yollar değildir.

**Şekil 5.4.** Kullanıcı eylemi olay üretir; olay işleyicisi durumu günceller;
çizim işlevi DOM'u bu duruma uygun hale getirir.

<!-- figure:state-render-loop -->

```js
function render() {
  const visible = deriveVisibleEvents(events, state);
  eventList.replaceChildren(...visible.map(createEventCard));
  savedCount.textContent = String(state.savedIds.size);
}
```

Aynı durum için yinelenen çizim, aynı gözlenebilir arayüzü üretmelidir. Kartları
tekrar tekrar eklememeli ve yeni durum yaratmamalıdır. `deriveVisibleEvents`
gibi saf fonksiyonlar tarayıcıya ihtiyaç duymadan sınanabilir.

Üç işi ayırın: olay işleyicisi ne olduğunu belirler; durum geçişi yeni gerçeği
kaydeder; çizim işlevi görünmesi gerekeni üretir. Etkinlik kaydetmek, kayıtlı
kimlikler kümesini değiştirir. Filtreleme, etkinliğin sonuçlara girip girmediğine
karar verir. Çizim de kart ve sayacı oluşturur. Böylece CSS sınıfı uygulama
verisinin tek kaynağına dönüşmez.

Kısa bir listeyi yeniden oluşturmak öğretirken açık ve kabul edilebilir bir
yöntemdir. Büyük arayüzlerde yalnızca değişen öğeyi güncellemek; odağı, seçimi ve
ortam durumunu korur. React gibi çerçeveler bu uzlaştırmanın bir bölümünü
otomatikleştirir, ancak durum ile çizim arasındaki ilişkiyi ortadan kaldırmaz.

---

# 5. Olaylar: tarayıcı etkileşimi nasıl bildirir?

**Olay**, fareyle etkinleştirme, tuşa basma, form değerinin değişmesi veya formun
gönderilmesi gibi bir durumu anlatan nesnedir. Program bu durumu sürekli sormak
yerine bir olay dinleyicisi kaydeder.

```js
saveButton.addEventListener("click", (event) => {
  console.log(event.type);
});
```

Tarayıcı, olay dağıtıldığında bu fonksiyonu çağırır ve olay nesnesini iletir.
Dinleyiciyi şimdi kaydedersiniz; olay gerçekleştiğinde çağrılır. Bu yaklaşım
olay güdümlü programlamadır.

## 5.1 Hedef, geçerli hedef ve yayılma

Kullanıcı kartın içindeki düğmeye bastığında olay bir yol boyunca ilerler.

- **Yakalama** aşamasında üst öğelerden hedefe doğru gider.
- **Hedef** aşamasında etkinleştirilen öğeye ulaşır.
- **Kabarcıklanma** aşamasında üst öğelere geri çıkar.

Şekil 5.5 tek tıklamanın yolunu gösterir. Üç aşama üç ayrı tıklama değildir.

**Şekil 5.5.** Tek bir tıklama yakalama, hedef ve kabarcıklanma aşamalarından
geçer.

<!-- figure:event-propagation -->

- `event.target`, olayın dağıtıldığı en iç nesnedir.
- `event.currentTarget`, o anda dinleyicisi çalışan nesnedir.

Üst öğe kabarcıklanan olayı dinlerken bu iki nesne farklı olabilir. Doğrudan bir
denetim üzerinde çalışan dinleyicide `currentTarget` çoğu zaman amaçlanan
öğedir. Olay devrinde ise `target` dikkatle incelenir.

Bazı olaylar aynı biçimde kabarcıklanmaz. `focus` ve `blur` için kabarcıklanan
karşılıklar `focusin` ve `focusout` olaylarıdır. Gölge DOM, olay hedefini yeniden
eşleştirebilir. İzin verilen yolun sınırlarını `event.composedPath()` ile
inceleyebilirsiniz.

## 5.2 Dinleyici seçenekleri ve ömrü

`addEventListener` üçüncü parametre olarak seçenek nesnesi kabul eder:

```js
const controller = new AbortController();

window.addEventListener("resize", updateLayout, {
  passive: true,
  signal: controller.signal,
});

controller.abort();
```

`capture: true` yakalama aşamasında dinler; `once: true` dinleyiciyi ilk
çağrısının ardından kaldırır; `passive: true` dinleyicinin
`preventDefault()` çağırmayacağını belirtir; `signal` ise dinleyici ömrünü bir
`AbortController` nesnesine bağlar.

Alternatif olarak `removeEventListener` çağrısına aynı olay türünü, fonksiyon
başvurusunu ve yakalama ayarını verin. Kullanılmayan dinleyicileri kaldırmak
yinelenen davranışları ve artık sayfada bulunmayan öğelerin gereksiz yere bellekte
tutulmasını önler.

## 5.3 Birbirinden farklı üç yöntem

`event.preventDefault()`, form gönderimi gibi iptal edilebilir varsayılan tarayıcı
davranışını önler. Kabarcıklanmayı durdurmaz. `event.stopPropagation()`, olayın
yayılma yolunda ilerlemesini keser. `event.stopImmediatePropagation()` aynı
öğedeki sonraki dinleyicileri de engeller. Yayılmayı gereksiz yere durdurmak
başka bileşenlerin veya analiz kodunun olay almasını engelleyebilir. Yalnızca
etkileşim sözleşmesi gerektiriyorsa kullanın.

## 5.4 Olay devri

Her çizimde kartlar yeniden oluşturulabilir. Her düğmeye ayrı dinleyici eklemek,
her yeniden çizimde yeniden kurulum gerektirir. Bunun yerine kararlı kapsayıcıya
tek dinleyici ekleyip yukarı kabarcıklanan olaydaki kontrolü bulun:

```js
eventList.addEventListener("click", (event) => {
  if (!(event.target instanceof Element)) return;
  const button = event.target.closest(".event-card__save");
  if (!button || !eventList.contains(button)) return;

  const card = button.closest("[data-event-id]");
  if (!card) return;
  save(card.dataset.eventId);
});
```

Şekil 5.6, olay devrinin özel bir olay türü değil; kabarcıklanma ve seçici
kullanımı olduğunu gösterir. Kapsayıcılık denetimi, iç içe başka bir bileşenden
gelen eşleşmeyi yanlışlıkla işlemeyi önler. Ortak davranışlı öğe listelerinde
olay devri kullanışlıdır; tek ve kararlı bir kontrol için doğrudan dinleyici daha
basit olabilir.

**Şekil 5.6.** Kararlı liste kapsayıcısı, bugünkü ve sonradan eklenen Save
düğmelerinin tıklamasını seçiciyle tanır.

<!-- figure:event-delegation -->

## 5.5 Kullanıcı amacını anlatan olayı seçme

`click`, fare veya klavyeyle etkinleştirilen yerel bir düğmenin amacını anlatır.
`<div>` öğesine düğme davranışını yeniden yazmayın. `input`, değer değiştikçe
oluşur; `change` genellikle değer onaylandığında oluşur. Form gönderimini
anlatan olay `submit` olup hem düğme etkinleştirmesini hem Enter tuşunu kapsar.
Koordinat veya hareket gerekiyorsa Pointer Events, fare, kalem ve dokunmayı ortak
bir modelde ele alır. Klavye dinleyicileri, klavyeye özgü komutlar içindir; anlamlı
HTML denetimlerinin yerine geçmez.

Metin alanlarında `input` genellikle değer değiştikçe çalışır. `change` metin
alanında daha geç, değer onaylandığında gerçekleşebilir. Girdi yöntemi
düzenleyicisi (Input Method Editor, IME), bir karakteri veya sözcüğü oluştururken
geçici metinleri olay olarak bildirebilir. Her ara değeri bitmiş arama saymak
kullanıcıyı rahatsız edebilir. Yazma sistemleri ve girdi araçlarıyla beklenen
davranışı sınayın.

JavaScript bileşenler arasında anlamlı bir **CustomEvent** de dağıtabilir. Özel
olay oluştururken kabarcıklanıp kabarcıklanmayacağına ve `detail` alanında hangi
verinin taşınacağına karar verin. Zaten kullanıcı eylemini anlatan yerel
`submit` veya `click` olayı varsa onu özel olayla değiştirmeyin. Olay adlarını ve
yük veri yapısını başka bir arayüz gibi belgeleyin.

---

# 6. Form denetimlerinden veri elde etme

Form yalnızca görsel bir grup değildir. Denetimleri, adları, değerleri, doğrulama
kısıtlarını ve gönderim sözleşmesini tanımlar. JavaScript bu yerel modeli
kullanmalıdır.

```html
<form id="event-filter">
  <label for="query">Etkinlik ara</label>
  <input id="query" name="query" type="search">

  <label>
    <input name="availableOnly" type="checkbox">
    Yalnızca yeri olan etkinlikleri göster
  </label>
  <button type="submit">Filtreleri uygula</button>
</form>
```

`id`, etiketi denetime bağlar. `name`, gönderilecek verinin alan adıdır. Ekranda
görünen ama `name` değeri olmayan denetim normalde gönderime katılmaz.

Etiket işlevsel bir ilişkidir; görünüşten ibaret değildir. Etikete tıklamak
çoğunlukla denetime odaklanır ve yardımcı teknoloji denetimin adını duyurabilir.
İlişkili seçenekleri `<fieldset>` ve `<legend>` ile gruplayın. Yer tutucu metin
görünür etiket yerine geçmez; kullanıcı yazmaya başlayınca kaybolabilir ve
kontrastı yetersiz olabilir.

## 6.1 Başarılı denetimleri FormData ile okuma

```js
const data = new FormData(filterForm);
const query = String(data.get("query") ?? "");
const availableOnly = data.get("availableOnly") === "on";
```

`FormData`, tarayıcının form kurallarını izler. Genel olarak etkin, adı olan
denetimler başarılı denetimdir. İşaretli olmayan onay kutusu veri üretmez.
Devre dışı bırakılmış alan kümesinin içindeki denetimler genellikle katılmaz.
Aynı adı taşıyan birden fazla öğe varsa `getAll()` ile hepsini alın. Dosya
denetimleri normal metin yerine `File` nesnesi verir.

**Tablo 5.3 - Yaygın form denetimleri ve oluşturdukları FormData girdileri**

| Kaynak ve güncel durum | Tipik FormData değeri | Açıklama |
|---|---|---|
| `<input name="query" value="robot">` | `query` -> `"robot"` | Metin değeri metin olarak aktarılır. |
| `availableOnly` adlı işaretli onay kutusu | Özel `value` yoksa `"on"` | Yalnızca işaretliyse katılır. |
| Aynı adla işaretli olmayan onay kutusu | Girdi oluşmaz | Yokluk boş metin değildir; anlamını kod belirlemelidir. |
| `topic` adlı iki işaretli onay kutusu | İki `topic` değeri | İkisini de almak için `getAll("topic")` kullanılır. |
| `<select name="category">` | Seçilen seçeneğin `value` değeri | Görünen etiketle aynı olmak zorunda değildir. |
| Devre dışı bırakılmış adlı denetim | Normalde girdi yoktur | Başarılı denetim değildir. |
| `<input type="file" name="poster">` | `File` nesnesi | Dosya sıradan metin değeri değildir. |

Bu tablo yaygın örnekleri gösterir; HTML Standardındaki bütün kuralları
kapsamaz. Formun `method` ve `action` öznitelikleri normal gönderim hedefini ve
istek yöntemini tanımlar. `GET`, değerleri paylaşılabilir arama ve filtrelere
uygun olan URL sorgusuna ekler. `POST`, değerleri istek gövdesinde gönderir ve
sunucu durumunu değiştiren işlemlerde yaygındır. `POST` kendi başına gizlilik veya
güvenlik sağlamaz; HTTPS ve sunucu denetimleri yine gereklidir. Parolaları,
belirteçleri ve özel verileri `GET` sorgusuna koymayın; geçmişte, günlüklerde ve
kopyalanan adreslerde görünebilir.

Gönderimi başlatan düğmenin adı ve değeri de veriye eklenebilir. Böyle bir ayrım
gerekiyorsa `new FormData(form, event.submitter)` kullanılabilir.

## 6.2 Gönderimi form sınırında ele alma

```js
filterForm.addEventListener("submit", (event) => {
  event.preventDefault();
  state = readFilterState();
  render();
});
```

Yalnızca düğmenin `click` olayını dinlemek bazı gönderimleri kaçırır. Gerçek
işlem formun `submit` olayıdır. `form.requestSubmit()` kullanıcı gönderimi gibi
doğrulamayı çalıştırır ve `submit` olayını dağıtır. `form.submit()` doğrudan
gönderim yapar ve bu adımları atlar; çoğu zaman istenen davranış bu değildir.

Bir form içindeki `<button>`, türü belirtilmezse gönder düğmesi gibi davranır.
Ana işlem için `type="submit"`, yerel bir işlem için `type="button"` yazın.
Böylece kaydetme veya genişletme düğmesi formu yanlışlıkla göndermez.

Şekil 5.7 form gönderiminin sınırını gösterir. Normal gönderimden önce yerel
tarayıcı doğrulaması yapılır. JavaScript yanıtı geliştirebilir; fakat istemci
değiştirilebildiği veya atlanabildiği için sunucu da doğrulama yapmalıdır.

**Şekil 5.7.** Form verisi adlandırılmış denetimlerden toplanır, kısıtlar
tarayıcıda denetlenir ve sunucu isteği yeniden doğrular.

<!-- figure:form-submit-validation -->

---

# 7. Kullanıcıya yardımcı olan doğrulama

HTML; `required`, uygun girdi türü, `min`, `max`, `minlength`, `maxlength`,
`step` ve `pattern` gibi kısıtlar sağlar. Gerçek kuralı açıklıyorsa bunları
kullanın.

```html
<label for="email">Üniversite e-posta adresi</label>
<input id="email" name="email" type="email" required
       aria-describedby="email-help email-error">
<p id="email-help">Onayın ulaşacağı adresi yazın.</p>
<p id="email-error"></p>
```

Kısıt Doğrulama API'si (Constraint Validation API) sonucu bildirir:

```js
if (!form.checkValidity()) {
  form.reportValidity();
}
```

`checkValidity()` denetler ve Boolean döndürür. `reportValidity()` ayrıca
tarayıcıdan geri bildirim göstermesini ister. Denetimin `validity` nesnesi
`valueMissing`, `typeMismatch`, `patternMismatch`, `tooShort` ve `rangeOverflow`
gibi durumlar ile yerelleştirilmiş `validationMessage` içerir.

## 7.1 Özel kurallar

Özniteliklerle anlatılamayan bir kural için `setCustomValidity(message)` kullanın.
Boş metin özel hatayı siler.

```js
function validateDateRange() {
  endDate.setCustomValidity("");
  if (startDate.value && endDate.value && endDate.value < startDate.value) {
    endDate.setCustomValidity("Bitiş tarihi başlangıçtan önce olamaz.");
  }
}
```

İki değerden biri değişince ve gönderimden önce yeniden doğrulayın. Kullanıcı
değeri düzelttikten sonra eski özel mesajı bırakmayın.

Yerel kısıtlar yaygın kuralları kodsuz anlatır. `required` değer girilip
girilmediğini denetler. `type="email"`, e-posta adresine benzeyen bir yazımı
denetler; adresin gerçekten var olduğunu veya kullanıcıya ait olduğunu kanıtlamaz.
`min` ve `max` sayısal ya da tarih aralığını, `step` ise artış miktarını sınırlar.
`pattern`, beklenen biçim için düzenli ifade kullanır. Tarayıcının bilemeyeceği
iş kurallarını ayrıca açıklayın.

Geçersiz bir denetimde ileti seçmeden önce `validity.valid` ve ilgili durum
bayraklarını inceleyin. `invalid` olayı geçersiz denetimde oluşur ve olağan
biçimde kabarcıklanmaz. Gönderim denenirken tarayıcı, formun `submit` olayı
oluşmadan önce geçersiz alana odaklanıp yerel uyarı gösterebilir. Yerel iletileri
değiştirirseniz anlaşılır hata metni ve öngörülebilir odak yönetimi artık
uygulamanın sorumluluğudur.

## 7.2 Erişilebilir hata ve durum bildirimi

Hatayı yalnızca renkle anlatmayın. Ne olduğunu ve nasıl düzeltileceğini belirten
metin verin. `aria-describedby` ile alana özgü yardım ve hata metnini denetime
bağlayın. Birden çok alan hatalıysa, ilgili alanlara bağlanan özet sunun. Odak,
öngörülebilir ve yararlı olduğunda özete veya ilk geçersiz alana taşınabilir.

Sayfa yenilenmeden değişen sonuçlar için kalıcı bir `role="status"` alanı kısa
sonucu duyurabilir:

```html
<p id="filter-status" role="status" aria-live="polite"></p>
```

Canlı alanı güncellemeden önce oluşturup metnini sonradan değiştirin. Her tuş
vuruşunda uzun bir ileti duyurmayın. Hata sonrasında kullanıcının yazdığı değerleri
koruyun. Canlı filtreleme sırasında odak arama alanında kalabilir. Gönderim
başarısız olduğunda özete odak taşımak yararlı olabilir; bunlar farklı
etkileşimlerdir ve farklı davranış gerektirir.

İstemci doğrulaması geri bildirimi iyileştirir, ancak güvenlik sınırı değildir.
Sunucu yetkilendirmeyi, türü, uzunluğu, aralığı, ilişkileri ve iş kurallarını
kendisine ulaşan verilerle yeniden denetlemelidir.

---

# 8. Aşamalı iyileştirme ve hata sınırları

**Aşamalı iyileştirme**, anlamlı HTML ile başlamayı ve temel işi gereksiz yere
CSS veya JavaScript'e bağımlı kılmamayı amaçlar. Gerçek bir arama formu,
JavaScript kapalıyken sunucuya gönderilebilir; JavaScript aynı gönderimi sayfayı
yenilemeden daha hızlı bir deneyime dönüştürebilir. Bunun çalışması için
sunucudaki `action` aramayı gerçekten uygulamalıdır. Statik öğretim sunucusundaki
boş `action`, sorgu parametreleriyle belgeyi yeniden yükler; verileri kendiliğinden
filtrelemez.

Campus Hub laboratuvarı örnek veriyi bellekte tutar; bu nedenle etkileşimli
filtreleme JavaScript gerektirir. Çözümde `<noscript>` açıklaması ve anlamlı
sayfa yapısı vardır; ancak bu, JavaScript olmadan çalışan bir arama değil,
kullanıcıya dürüst bir açıklamadır. Üretim sistemi ilk etkinlikleri sunucuda
oluşturup işlevsel bir form hedefi sağlayabilir ya da hangi özelliğin JavaScript
istediğini açıkça belirtebilir.

Şu sorunları ayrı hata sınırları olarak düşünün:

1. HTML veya JavaScript dosyası yüklenmeyebilir.
2. Seçici artık hiçbir öğeyle eşleşmeyebilir.
3. Verinin yapısı beklenenden farklı olabilir.
4. Dinleyici hiç çalışmayabilir veya iki kez çalışabilir.
5. Çizim odak öğesini kaldırabilir veya eski durum yeni veriyi ezebilir.
6. Doğrulama geçerli girdiyi reddedebilir ya da güvensiz girdiyi kabul edebilir.
7. Erişilebilir bildirim hiç duyurulmayabilir veya gereğinden fazla yinelenebilir.

Bu sınırları ayrı tutmak, doğru kanıt ve yararlı hata iletisi bulmayı kolaylaştırır.

---

# 9. Uygulamalı laboratuvar: Campus Hub etkinlik gezgini

Laboratuvar DOM seçimi, durum, çizim, olay devri, form, erişilebilirlik ve saf
model testlerini bir araya getirir. Şekil 5.8 tamamlanmış tarayıcı çıktısının
kanıt ekran görüntüsüdür; kavramsal çizim değildir.

**Şekil 5.8.** Campus Hub etkinlik gezgininin tarayıcıdaki başlangıç görünümü;
formu, üç etkinliği ve kayıt sayacını gösterir.

<!-- media:week-05-browser-output -->

## 9.1 Doğru klasörden başlayın

VS Code'da depo klasörünü açın. **Terminal > New Terminal** seçin. Windows
Komut İstemi'nde proje işaretçisini denetleyin:

```text
dir package.json
```

PowerShell karşılığı şöyledir:

```powershell
Get-Item package.json
```

Komut deponun `package.json` dosyasını göstermelidir. Göstermezse npm komutuna
geçmeyin; `cd` ile klonlanmış depo klasörüne girin.

## 9.2 Başlangıç uygulamasını çalıştırın

İlk terminalde şu komutu çalıştırın:

```text
npm run serve:week05:starter
```

Bu, sunucu terminalinizdir; özel bir uygulama değildir, yalnızca yerel sunucuyu
çalıştıran terminaldir. Açık bırakın ve tarayıcıda
`http://localhost:8000/` adresini açın. Test ve Git komutları için ikinci terminali
kullanın.

## 9.3 Dört dosyayı inceleyin

- `index.html` formu, durum alanını, sonuç kapsayıcısını ve şablonu tanımlar.
- `styles.css` arayüzü biçimlendirir.
- `model.js` örnek veriyi ve saf durum dönüşümlerini içerir.
- `app.js` tarayıcı olaylarını duruma ve çizime bağlar.

`app.js` içindeki aktarmaları `model.js` dosyasına kadar izleyin. Ardından
seçilen her `id` değerini `index.html` içinde bulun. Değişiklik yapmadan önce
sözleşmeyi görünür hale getirmiş olursunuz.

## 9.4 Veri modelini tamamlayın

`seatsRemaining`, `deriveVisibleEvents` ve `toggleSaved` fonksiyonlarını yazın.
Gelen `Set` nesnesini değiştirmeyin; değişiklik gözlenebilir olsun diye yeni bir
küme döndürün. İkinci terminalde:

```text
npm run test:week05
```

Beklenen son satır şöyledir: `Week 5 DOM, events, forms, and model checks passed.`
Bir test başarısızsa kodu değiştirmeden önce beklenen ve gerçekleşen değerleri
okuyun.

## 9.5 Tarayıcı çizimini tamamlayın

Gerekli beş öğeyi seçin ve biri eksikse anlaşılır hata verin. Her etkinlik için
şablonu kopyalayın. Metinleri `textContent` ile doldurun; etkinlik kimliğini
`data-event-id` içine, kayıtlı durumu `aria-pressed` içine yazın. Sonuç
kapsayıcısını bilinçli biçimde güncelleyin. Sonuç yoksa boş bir alan yerine
“Bu filtrelerle etkinlik bulunamadı” iletisi gösterin.

Çizim kart düğümlerini yenilediğinde klavye odağı kaldırılabilir. Kullanıcı
etkinliği klavyeyle kaydettiğinde aynı etkinliğin yeni Save düğmesine odağı geri
verin. Çözüm bu yöntemlerden birini uygular; yalnızca değişen kartı güncellemek de
geçerli bir tasarımdır.

## 9.6 Olayları bağlayın

Formun `input` olayında `FormData` oluşturun, filtre durumunu güncelleyin ve
çizim yapın. `submit` olayında gezinmenin varsayılan davranışını önleyip aynı
durumu güncelleyin. Sonuç kapsayıcısındaki tek `click` dinleyicisinde `closest()`
ile Save düğmesini ve kartını bulun.

## 9.7 Davranış, erişilebilirlik ve kanıtı doğrulayın

Şunların tümünü deneyin:

1. `robot` yazınca bir kart kalsın.
2. Arts seçilince orkestra görünsün.
3. “Show events with available seats only” seçilince dolu orkestra kaybolsun.
4. Save düğmesi metni ve `aria-pressed` değeri değişsin.
5. Kaydedilen etkinlik sayısı güncellensin.
6. Klavyeyle kaydettiğinizde odak güncellenmiş Save düğmesine dönsün.
7. Eşleşmeyen aramada açıklayıcı boş durum iletisi görünsün.
8. Tab ile her denetime mantıklı sırada ulaşılabilsin.
9. Enter ile gönderim sayfa gezinmesine yol açmasın.
10. Durum bölgesi sonuç sayısını bildirsin.

Developer Tools'u `F12` veya `Ctrl+Shift+I` ile açın. **Elements** panelinde
etkinlik kartını bulup `data-event-id` ile düğmenin `aria-pressed` değerini
doğrulayın. **Console** panelinde kırmızı hata olmadığını kontrol edin.
**Network** panelini açıp sayfayı yenileyin; `index.html`, `styles.css`,
`app.js` ve `model.js` başarılı durum kodu döndürmelidir.

## 9.8 Sınanmış çözümle karşılaştırın

Sunucuyu `Ctrl+C` ile durdurun ve şunu çalıştırın:

```text
npm run serve:week05:solution
```

Çözümü körü körüne kopyalamayın. Her farkın hangi sözleşmeyi karşıladığını
açıklayın. Sonunda çalışmalarınızı anlamlı bir Git iletisiyle kaydedip ders
ödevleri deponuza gönderin.

---

## 9.9 İleri inceleme: İyileştirmeden önce ölçün

Temel laboratuvar, kodun incelenmesi kolay olduğu için kısa listeyi bilinçli
olarak yeniden çizer. Şimdi performans hakkında tahmin yürütmek yerine bu
tasarımın kanıtını toplayın. **Performance** panelini açın, bir filtreleme
işlemini kaydedin ve betik çalışmasını izleyen stil, yerleşim ve boyama
aşamalarını bulun. İşlem görülemeyecek kadar kısaysa CPU yavaşlatma seçeneğiyle
tekrarlayın. Görünen kart sayısını, yaptığınız etkileşimi ve gözlediğiniz en uzun
görevi kaydedin. Bu karşılaştırma, uygulamanın her bilgisayarda aynı süreyle
çalışacağını kanıtlayan bir kıyaslama değildir.

Ardından iki denetimli inceleme yapın:

1. bir kartı kaydedip odağın yeni düğmeye geri döndüğünü doğrulayın;
2. `#event-list` öğesine geçici bir `MutationObserver` ekleyip bir kez kaydetme
   veya filtreleme yapın ve iletilen değişiklik kayıtlarını inceleyin.

Deney bitince gözlemciyi ayırın. Uygulama kendi `render()` fonksiyonunun listeyi
ne zaman değiştirdiğini zaten bilir; gözlemciyi kalıcı tutmak durum modelini
gereksiz yere yineleyecektir. Bu deney her arayüzde gözlemci kullanmayı önermek
için değil, sınırı görünür kılmak için vardır.

---

# 10. İleri DOM mühendisliği: Modeli kaybetmeden ölçekleme

Şimdiye kadar öğrendiğiniz API'ler gerçek bir arayüz oluşturmak için yeterlidir.
Daha büyük sayfalarda bir etkileşim daha fazla iş üretebilir ve birbirinden
bağımsız geliştirilen bileşenler aynı belgeyi paylaşabilir. Çözüm DOM'u terk
etmek değildir; sahipliği, zamanlamayı ve kanıtı açık hale getirmektir.

## 10.1 Önce okuyun, sonra karar verip yazın

Bir sınıfı değiştirmek veya düğüm eklemek her zaman anında boyama oluşturmaz.
Tarayıcı görsel işi erteleyip birleştirebilir. Ancak bazı DOM okumaları güncel
geometri ister. `getBoundingClientRect()` çağrısı yanıt vermeden önce tarayıcıyı
stil ve yerleşim bilgisini güncellemeye zorlayabilir. Geometri okumasıyla stil
yazmasını tekrar tekrar sırayla yapmak bu nedenle yinelenen yerleşim işi
oluşturabilir.

```js
// Tarayıcının gruplaması daha güçtür: oku, yaz, oku, yaz.
for (const card of cards) {
  const width = card.getBoundingClientRect().width;
  card.classList.toggle("event-card--compact", width < 320);
}
```

Tasarım gerçekten ölçüm gerektiriyorsa önce ölçümleri toplayın, kararı sıradan
JavaScript verisi üzerinde verin, ardından yazmaları yapın:

```js
const measurements = cards.map((card) => ({
  card,
  width: card.getBoundingClientRect().width,
}));

for (const { card, width } of measurements) {
  card.classList.toggle("event-card--compact", width < 320);
}
```

Şekil 5.9 bu üç aşamalı disiplini gösterir. Bu, her DOM yazmasının pahalı olduğu
iddiası değildir. Önbellek, kısmi çizim veya zamanlama mekanizması eklemeden önce
gerçek etkileşimi ölçün. Duyarlı sunum için JavaScript ile genişlik ölçmek yerine
CSS media ve container query kullanmak çoğu zaman daha uygundur.

<!-- figure:dom-read-decide-write -->

Bir `DocumentFragment` veya belgeden ayrık şablon kopyası, tek ekleme öncesinde
birden çok düğümü bir araya getirebilir. Bu yöntem ara belge değişikliklerini
azaltır ve oluşturma kodunu düzenli tutar. Verimsiz algoritmayı ortadan kaldırmaz;
gereksiz on bin kart oluşturmak yine gereksiz iştir.

## 10.2 Durum modelinizin dışındaki değişiklikleri gözlemleyin

`MutationObserver`, DOM değişikliklerini gerçekleştikten sonra toplu kayıtlar
halinde bildirir. Üçüncü taraf bir araç, düzenleyici veya atanmış içeriği izleyen
özel öğe gibi doğrudan başlatmadığınız değişikliklere tepki vermeniz gerektiğinde
kullanışlıdır.

```js
const observer = new MutationObserver((records) => {
  for (const record of records) {
    console.log(record.type, record.addedNodes.length);
  }
});

observer.observe(eventList, {
  childList: true,
  subtree: true,
});

// Gözlem sorumluluğu sona erdiğinde:
observer.disconnect();
```

Şekil 5.10 olay ile değişiklik kaydını ayırır. Olay, oluşumu bir yayılma yolu
üzerinden bildirir. Değişiklik gözlemcisi ise izlenen kapsamın ağaç, öznitelik
veya metin değişikliklerini daha sonra toplu olarak alır. Kullanıcının niyetini
açıklamaz ve uygulamanın kendi durum geçişinin yerine geçmemelidir. Yararlı en
dar kökü ve seçenekleri gözlemleyin; belgenin tamamını her değişiklik için
izlemek gürültü ve gereksiz iş oluşturur.

<!-- figure:mutation-observer-batch -->

Eski mutation event'ler kullanımdan kaldırılmıştır. Gerçek gereksinim değişiklik
gözlemi olduğunda `MutationObserver` kullanın. Değişikliği kendi fonksiyonunuz
yaptıysa sonraki uygulama adımını doğrudan çağırın; kendi işinizi gözlemciyle
yeniden keşfetmeyi beklemeyin.

## 10.3 Light DOM, shadow DOM ve özel öğeler

Bu kitaptaki öğelerin çoğu belgenin sıradan ağacındadır; bileşenin gölge ağacıyla
karşılaştırıldığında buna **light DOM** denir. **Shadow root**, bileşene stil ve
seçici kapsüllemesi olan dahili bir DOM alt ağacı verir. Sayfa, light DOM
çocuklarını adlandırılmış veya varsayılan `<slot>` konumlarına yerleştirebilir;
bileşen ise dahili uygulama sınırını korur.

Şekil 5.11 bu iki ağacın nasıl iş birliği yaptığını gösterir. Shadow DOM bir
güvenlik sınırı değildir: açık gölge kökleri incelenebilir, geliştirici araçları
yapıyı gösterir ve bileşen girdileri güvenilmeyen veri olmaya devam eder. Bu
sınır, bileşen yapısını ve stil sözleşmelerini kazara oluşan bağımlılıktan korur.

<!-- figure:shadow-dom-boundary -->

Olaylar, `composed` davranışları izin veriyorsa gölge sınırını aşabilir. Bileşen
dışında olay hedefi, dahili yapıyı korumak için **yeniden hedeflenebilir**;
`event.composedPath()` izin verilen dağıtım yolunu gösterir. Bu nedenle dış kod,
dahili düğmeye bağımlı olmak yerine bileşenin belgelenmiş genel olayını dinlemelidir.

**Özel öğe**, adı kısa çizgi içeren kayıtlı bir HTML öğesidir; örneğin
`<campus-event-card>`. Sınıfı yaşam döngüsü geri çağrılarını kullanabilir:

```js
class CampusEventCard extends HTMLElement {
  connectedCallback() {
    if (this.dataset.ready === "true") return;
    this.dataset.ready = "true";
    this.textContent = this.getAttribute("title") ?? "Adsız etkinlik";
  }
}

customElements.define("campus-event-card", CampusEventCard);
```

Öğe taşınıp yeniden bağlandığında `connectedCallback()` birden çok kez
çalışabilir. Bu yüzden kurulum yinelenebilir veya korumalı olmalı; uzun ömürlü
kaynakların temizliği yapılmalıdır. Gelişmiş bileşenler shadow DOM, gözlenen
öznitelikler, slotlar ve özel olaylar kullanabilir; ancak bunların hiçbiri özel
öğe için zorunlu değildir. Özerk ve formla ilişkili özel öğelerin ek sözleşmeleri
vardır. Bunlar, yerel `<button>`, `<input>` veya `<form>` davranışını değiştirmek
için gerekçe değildir.

## 10.4 Olayı anlamına ve girdi bağımsızlığına göre seçin

Tablo 5.4 yaygın seçimleri karşılaştırır. Görevi anlatan olayı seçin; tarayıcının
klavye ve erişilebilirlik davranışını sağlaması için anlamsal HTML kullanın.

**Tablo 5.4 - Kullanıcı niyetine ve kanıta göre olay seçimi**

| Niyet | Tercih edin | Tek mekanizma olarak kaçının | Gerekçe |
|---|---|---|---|
| Yerel düğmeyi etkinleştirme | `click` | `mousedown` veya `keydown` | yerel etkinleştirme işaretçi ve klavyeyi kapsar |
| Form değeri değişirken tepki verme | `input` | değeri sürekli sorgulama | olay, kullanıcı kaynaklı değer değişimini bildirir |
| Değer kesinleşince tepki verme | `change` | her tuşu son değer sayma | kesinleşme zamanı denetim türüne göre değişir |
| Form gönderme | form üzerinde `submit` | yalnızca düğmenin `click` olayı | Enter, yardımcı teknoloji ve `requestSubmit()` da gönderir |
| İşaretçi geometrisi veya hareketi | pointer event'ler | yalnızca mouse event'leri | mouse, dokunma ve kalemi ortak modelde anlatır |
| Klavyeye özgü komut | `event.key` ile `keydown` | sayısal tuş kodları | komut gerçekten klavyeye özgüdür |
| Bileşen içinde odak hareketi | `focusin` / `focusout` | `focus` olayının kabarcıklandığını varsayma | kabarcıklanan türler olay devrine uygundur |

Klavye komutlarını dikkatli tasarlayın. Tarayıcı, işletim sistemi veya yardımcı
teknoloji kısayollarını geçersiz kılmayın. Tuşu basılı tutmanın eylemi
yinelenmemesi gerekiyorsa `event.repeat` değerine bakın; tamamlanmamış Input
Method Editor (IME) bileşimini bitmiş komut saymayın. İşaretçi hareketlerinde
`pointercancel` gibi iptal yolu bulunmalıdır; kullanıcı yön değiştirebilir,
tarayıcı kaydırmayı devralabilir veya cihaz teması kaybedebilir.

`isTrusted`, kullanıcı aracının dağıttığı olay ile betiğin gönderdiği olayı
ayırt eder; yetkilendirme mekanizması değildir. Gerçek tıklama da güvenilmeyen
istemciden gelir. Güvenlik kararı sunucuda kalır.

## 10.5 Form sahipliği, sıfırlama, kodlama ve dosyalar

Denetim normalde en yakın üst `<form>` öğesine aittir. `form` özniteliği aynı
belgenin başka yerindeki bir formla ilişki kurabilir:

```html
<form id="event-search" action="/events" method="get"></form>

<label for="query">Etkinlik ara</label>
<input id="query" name="query" form="event-search">
<button type="submit" form="event-search">Ara</button>
```

Yerleşim gerçekten ayırmayı gerektiriyorsa bu özelliği kullanın; gerekmiyorsa
denetimleri form içinde tutmak daha kolay okunur. `form.elements` sahip olunan
denetimleri, `control.form` ise denetimin sahibini gösterir.

Sıfırlama da bir sözleşmedir. Reset, denetimleri başlangıç değerlerine yaklaştırır;
ayrı JavaScript durum nesnesini kendiliğinden sıfırlamaz. Uygulama durumu da
eşitlenecekse `reset` olayını dinleyin; tercihen tarayıcının varsayılan işlemini
tamamlamasına izin verip durumu son denetimlerden türetin. Etkisini açıklamadan
reset düğmesini genel bir “temizle” düğmesi gibi kullanmayın.

`formdata` olayı, form için `FormData` oluşturulduktan sonra girdileri incelemeyi
veya eklemeyi sağlar. Gerçekten gönderime ait türetilmiş değerlerde kullanışlıdır;
bildirimsel değerlerde gizli girdi daha açık olabilir. Yetkili fiyat, rol veya
izni istemcide ekleyip sunucunun güvenmesini beklemeyin.

Normal gezinmede yöntem ve kodlama, girdilerin ağı nasıl geçeceğini belirler:

- `GET`, değerleri Uniform Resource Locator (URL) sorgusunda gösterir;
- varsayılan `application/x-www-form-urlencoded` kodlamalı `POST`, ad-değer
  verisini istek gövdesinde gönderir; ve
- dosya yükleyen form normalde `multipart/form-data` kullanır.

Dosya girdisindeki `accept` özniteliği bir kullanıcı arayüzü ipucudur; dosyanın
içeriğini veya güvenliğini kanıtlamaz. Tarayıcı JavaScript'e keyfi yerel dosya
yolu göstermez. Seçilen dosyaları güvenilmeyen veri sayın; boyut, tür, yetki,
saklama ve kötü amaçlı yazılım politikasını sunucu uygulamalıdır. Bu bölüm form
sınırında durur. Bölüm 6 istekleri programatik gönderecek; sonraki sunucu
bölümleri alınan veriyi doğrulayıp saklayacaktır.

---

# 11. Hata ayıklama kliniği

Tablo 5.5, görünen belirtiyi incelenecek ilk kanıtla eşleştirir.

**Tablo 5.5 - Belirti, olası anlam ve ilk kanıt**

| Belirti | Olası anlam | İlk incelenecek kanıt |
|---|---|---|
| Beyaz sayfa | Betik hatası, gizlenmiş veya boş içerik | Console hatası ve Network yanıtı |
| `Cannot set properties of null` | Seçici öğe bulamadı | Seçici yazımı ve canlı Elements paneli |
| Tıklama iki kez çalışıyor | Yinelenen dinleyici veya iç içe etkinleştirme | Olay dinleyici kesme noktası ve çağrı yığını |
| Simgeye tıklayınca işlem olmuyor | Kod yalnızca `target` değerini düğmeyle karşılaştırdı | `target` değerini inceleyip `closest()` deneyin |
| Form sayfayı yeniliyor | Gönderim varsayılanı önlenmedi | `submit` dinleyicisi ve Console çıktısı |
| Onay kutusunun değeri eksik | İşaretli olmayan kutu başarılı denetim değildir | `FormData` girdilerini inceleyin |
| Değer düzeltildiği halde hata sürüyor | Özel doğrulama temizlenmedi | `validationMessage` ve doğrulama işleyicisi |
| Yeni kartlar tepki vermiyor | Yalnızca eski çocuklara dinleyici bağlandı | Olay devri kapsayıcısı ve kurulum kodu |
| Yazarken odak kayboluyor | Çizim odaktaki düğümü kaldırdı | Çizim öncesi ve sonrası etkin öğe |
| Kaydırma gecikiyor | Wheel veya touch dinleyicisi varsayılanı engelliyor olabilir | Dinleyici seçenekleri ve Performance kaydı |
| Gözlemci Console'u dolduruyor | Kapsam geniştir veya geri çağrı gözlediği yeri değiştiriyordur | Gözlemci kökü, seçenekleri ve geri çağrı yazmaları |
| Bileşen tıklamasının hedefi beklenmiyor | Gölge sınırı olayı yeniden hedefledi | `target`, `currentTarget` ve `composedPath()` |
| Reset denetimleri değiştiriyor, sonucu değiştirmiyor | JavaScript durumu form sıfırlamasını izlemedi | `reset` dinleyicisi ve sıfırlama sonrası durum |

Tahmin eklemek yerine kesme noktası kullanın. **Sources** panelinde `click` veya
`submit` için bir Event Listener Breakpoint oluşturun. Kod durduğunda çağrı
yığınını, `event.target`, `event.currentTarget`, durumu ve seçili öğeleri inceleyin.
**Elements** panelindeki Event Listeners görünümü kayıtlı dinleyicileri gösterir.
Amaç belirtiyi gizlemek değil, hangi sözleşmenin bozulduğunu bulmaktır.

---

# 12. Alıştırmalar

1. `<main><h1>Hub</h1><p>Open</p></main>` için metin düğümleri dahil DOM ağacını
   çizin.
2. `textContent` değişikliğinin `index.html` dosyasını neden değiştirmediğini
   açıklayın.
3. `#saved-count` için güvenli seçme ve hata denetimi yazın.
4. `children` ile `childNodes` arasındaki farkı açıklayın.
5. Daha önce saklanan `querySelectorAll(".card")` sonucu yeni kart eklenince
   büyür mü? Tahmin edin.
6. Güvensiz `panel.innerHTML = userName` atamasını uygun işlemle değiştirin.
7. `checked` özniteliği ile özelliği arasındaki farkı anlatın.
8. Yalnızca `remaining === 0` iken `event-card--full` sınıfı ekleyin.
9. `data-event-id` neden kullanışlıdır ama gizli bilgi saklayamaz?
10. “Web seminar” metinli bir `<li>` oluşturup `list` öğesine ekleyin.
11. Aynı durumla tekrarlanan çizimin sağlaması gereken koşulu belirtin.
12. Liste dinleyicisi varken düğme içindeki `<span>` tıklanırsa `target` ve
    `currentTarget` nedir?
13. Yakalama, hedef ve kabarcıklanma sırasını yazın.
14. `preventDefault()` neden kabarcıklanmayı durdurmaz?
15. Tek kullanımda kaldırılan dinleyici yazın.
16. Her çocuğa dinleyici yerine olay devri ne zaman uygundur?
17. `FormData` içinden `topic` adlı tüm değerleri alın.
18. İşaretli olmayan onay kutusu neden `FormData` içinde bulunmayabilir?
19. `requestSubmit()` ile `submit()` yöntemlerini karşılaştırın.
20. Bitiş tarihi başlangıçtan önceyse reddeden ve düzeltmede hatayı temizleyen
    özel kural yazın.
21. Üç geçersiz alan için erişilebilir hata geri bildirimi tasarlayın.
22. İstemci doğrulaması öğrenci kaydına neden izin veremez?
23. Etkinlik araması için aşamalı iyileştirilmiş bir seçenek belirtin.
24. Etkinlik kaydetme için bir saf birim testi ve bir tarayıcı etkileşim testi
    tasarlayın.
25. `name="availableOnly"`, `value="yes"` olan işaretli onay kutusunda
    `FormData.get("availableOnly")` ne döndürür? İşaret kaldırılırsa ne olur?
26. `type="email"` bir adresin var olduğunu neden kanıtlayamaz?
27. Değeri gönderilmesi ama değiştirilmemesi gereken denetim için `disabled` mı,
    `readOnly` mi seçersiniz? Klavye sonucunu açıklayın.
28. Çizim, klavyeyle odaklanmış Save düğmesini değiştiriyor. Sorunu ve güvenli
    onarımını açıklayın.
29. Statik sunucu, boş form hedefinden GET sorgusu alıyor. Bu neden arama
    uygulamaz ve üretim sürümünde ne gerekir?
30. Girdi yöntemi düzenleyicisi canlı filtrelemeyi nasıl etkileyebilir? Yazma
    sırasında etkileşimi bozmamak için bir yöntem belirtin.
31. Kabarcıklanan `CustomEvent` için uygun bir kullanım ve yerel `submit`
    olayını özel olayla değiştirmeme nedeni verin.
32. Bir döngü her kartta `getBoundingClientRect()` okuyup ardından sınıfı
    değiştiriyor. Geometri okumaları DOM yazmalarından önce olacak biçimde planı
    yeniden yazın ve hangi kanıtın bu değişikliği haklı çıkaracağını açıklayın.
33. `#event-list` içine eklenen kartları bildiren dar kapsamlı bir
    `MutationObserver` tasarlayın ve ne zaman ayrılması gerektiğini belirtin.
34. Kullanıcı olayıyla değişiklik kaydını karşılaştırın. “Bu etkinliği kaydet”
    niyetini hangisi temsil etmelidir? Neden?
35. Tek bir bileşen etkileşimi üzerinden light DOM, shadow DOM, olay yeniden
    hedefleme ve `composedPath()` görevini açıklayın.
36. Özel öğe `connectedCallback()` içinde dinleyici bağlıyor. Yeniden bağlanınca
    davranışın neden yinelenebileceğini ve bir güvenli tasarımı açıklayın.
37. Şu işler için olayı seçin: yerel düğme etkinleştirme, canlı metin filtreleme,
    kesinleşmiş seçim, form gönderimi ve kalemle çizim hareketi.
38. `event.isTrusted === true` değerinin üniversite kaydını silmeye neden yetki
    veremeyeceğini açıklayın.
39. Arama denetimi ve gönderim düğmesi `<form>` dışında bulunan, fakat ona ait
    olan bir form oluşturun. Bu yapının ne zaman gerekli olduğunu belirtin.
40. URL kodlu ve multipart form gönderimini karşılaştırın. Dosya girdisindeki
    `accept` değerinin yüklenen dosyayı neden doğrulamadığını açıklayın.

---

# 13. Gerekçeli yanıtlar

## Yanıt 1

`main`, parçanın kök öğesidir. Altında `h1` ve `p` öğeleri bulunur. `h1` içinde
`Hub`, `p` içinde `Open` metin düğümü vardır. Etiketler arasındaki girintiler de
metin düğümü oluşturabilir. Bu nedenle yalnızca öğe çocuklarıyla çalışırken
`children` daha açık olabilir.

## Yanıt 2

Tarayıcı dosyayı bellekteki nesnelere dönüştürmüştür. `textContent`, canlı
nesnenin değerini değiştirerek ekrandaki çizimi etkiler. Tarayıcı geliştiricinin
kaynak dosyasını kendiliğinden düzenlemez; yeniden yüklemede sunucudaki özgün
belge geri gelebilir.

## Yanıt 3

```js
const savedCount = document.querySelector("#saved-count");
if (!savedCount) throw new Error("index.html içinde #saved-count bulunmalı.");
```

Hata hem bozulmuş sözleşmeyi hem de incelenecek dosyayı belirtir.

## Yanıt 4

`children` yalnızca öğe çocuklarını; `childNodes` metin ve yorum düğümleri dahil
farklı düğüm türlerini içerir. Kaynak girintisi öğe yapısını değiştirmeden
`childNodes` sonucunu değiştirebilir.

## Yanıt 5

Büyümez. `querySelectorAll()` arama anındaki eşleşmeleri içeren statik bir
`NodeList` döndürür. Yeni kartı görmek için seçiciyi yeniden çalıştırın.

## Yanıt 6

```js
panel.textContent = userName;
```

Karakterleri olası işaretleme olarak ayrıştırmak yerine düz metin olarak gösterir.

## Yanıt 7

Öznitelik kaynak işaretlemesindeki ilk bildirimi; özellik kullanıcı etkileşimi
sonrasındaki güncel durumu anlatır. Etkileşim kodu çoğunlukla
`checkbox.checked` değerini okumalıdır.

## Yanıt 8

```js
card.classList.toggle("event-card--full", remaining === 0);
```

İkinci bağımsız değişken, sınıfın hangi koşulda bulunacağını açıkça belirtir.

## Yanıt 9

Kimliği kartın yanında tutar ve olay devrinde okumayı kolaylaştırır. Geliştirici
araçlarında görünür ve istemci tarafından değiştirilebilir. Sunucu bunu gizli veya
yetkili veri kabul etmemelidir.

## Yanıt 10

```js
const item = document.createElement("li");
item.textContent = "Web seminar";
list.append(item);
```

Öğe oluşturulur, güvenli metin eklenir ve listeye bağlanır.

## Yanıt 11

Aynı veri ve durumla tekrarlanan çizim aynı arayüzü üretmeli; yinelenen içerik
veya yeni durum oluşturmamalıdır.

## Yanıt 12

`target`, en içteki `span`; `currentTarget`, dinleyicisi çalışan üst listedir.
`closest("button")` ile tıklanan denetime geri çıkılabilir.

## Yanıt 13

Yakalama üst öğelerden hedefe ilerler; hedef aşaması denetimi işler; kabarcıklanma
üst öğelere geri çıkar.

## Yanıt 14

Varsayılan davranış ile olay yayılması ayrı mekanizmalardır.
`preventDefault()` iptal edilebilir tarayıcı davranışını önler. Yayılmayı ayrıca
durdurmaz.

## Yanıt 15

```js
button.addEventListener("click", initializeOnce, { once: true });
```

Tarayıcı ilk çağrıdan sonra bu dinleyiciyi kaldırır.

## Yanıt 16

Birçok mevcut veya sonradan eklenecek çocuk aynı davranışı paylaşıyorsa ve olay
kararlı kapsayıcıya kabarcıklanıyorsa olay devri kullanışlıdır. Tek ve kararlı
kontrolde doğrudan dinleyici daha basittir.

## Yanıt 17

```js
const topics = new FormData(form).getAll("topic").map(String);
```

`getAll()`, aynı adı taşıyan başarılı denetimlerin tüm değerlerini korur.

## Yanıt 18

Başarılı denetim kuralları işaretli olmayan kutuyu gönderimden çıkarır. Kod
yokluğu bilinçli biçimde, çoğu Boolean durumda `false` olarak yorumlamalıdır.

## Yanıt 19

`requestSubmit()`, doğrulamayı çalıştırıp `submit` olayını üretir. `submit()`
doğrudan gönderim başlatır ve bu adımları atlar.

## Yanıt 20

```js
function validateRange() {
  end.setCustomValidity("");
  if (start.value && end.value && end.value < start.value) {
    end.setCustomValidity("Bitiş tarihi başlangıçtan önce olamaz.");
  }
}
start.addEventListener("input", validateRange);
end.addEventListener("input", validateRange);
```

Önce eski hata temizlenir; böylece düzeltilmiş aralık geçerli olabilir.

## Yanıt 21

Form başlığının yanında kısa bir hata özeti oluşturun ve her maddeyi denetime
bağlayın. Alana özgü iletiyi `aria-describedby` ile bağlayın. Gerekliyse geçersiz
durumu işaretleyin, girilmiş değerleri koruyun ve gönderim başarısız olduğunda
odağı düzeltme noktasına öngörülebilir biçimde taşıyın. Yalnızca kırmızı çerçeveye
güvenmeyin.

## Yanıt 22

Tarayıcı kullanıcının denetimindedir; betikler ve istekler değiştirilebilir veya
atlatılabilir. Sunucu öğrenciyi tanımalı, yetkiyi ve kapasiteyi denetlemeli,
isteği doğrulamalı ve son kayıt kuralını uygulamalıdır.

## Yanıt 23

Forma gerçek sunucu `action` ve `method` değerleri verin. JavaScript olmadan
sunucu tarafı sonuç sayfasına gidebilir; JavaScript ile aynı istek anlamı korunup
sonuçlar mevcut sayfada güncellenebilir.

## Yanıt 24

Saf birim testi, `toggleSaved` fonksiyonuna bir `Set` ve kimlik verir; sonuçta
kimliğin bulunduğunu ve özgün kümenin değişmediğini doğrular. Tarayıcı testi,
Save düğmesini etkinleştirip metni, `aria-pressed` değerini, sınıfı ve sayacı
denetler. Bu testler farklı sınırları kapsar; birbirinin yerine geçmez.

## Yanıt 25

İşaretliyken `"yes"` döner; çünkü açık `value` değeri varsayılan `"on"`
değerinin yerini alır. İşaret kaldırılınca alan hiç oluşmaz. Kod bu yokluğu boş
metin sanmamalı, gerektiği biçimde `false` olarak yorumlamalıdır.

## Yanıt 26

Tarayıcı e-posta adresine benzeyen yazımı denetler. Posta sunucusuna bağlanıp
posta kutusunun var olduğunu veya kullanıcının erişebildiğini kanıtlamaz. Sahiplik
doğrulaması için onay bağlantısı göndermek gibi sunucu tarafı bir işlem gerekir.

## Yanıt 27

Değer odaklanabilir ve normal form gönderimine katılabilir kalsın istiyorsanız
`readOnly` seçin. `disabled`, klavye gezinmesinde genellikle atlanır ve form
verisine katılmaz. Sunucu yine de gelen değerin yetkili olup olmadığına karar
vermelidir.

## Yanıt 28

Listenin yeniden oluşturulması odaktaki düğümü belgeden çıkarır. Odak gövdeye
dönebilir; sonraki Tab beklenmedik yere gidebilir. Çizim öncesinde etkinlik
kimliğini saklayıp görünür kalıyorsa aynı kartın yeni düğmesine odak vermek bir
çözümdür. Büyük arayüzlerde yalnızca değişen kartı güncellemek daha uygundur.

## Yanıt 29

Boş form hedefi aynı URL'yi yeniden çağırır; statik dosya sunucusu sorgu
parametrelerini filtre olarak yorumlamaz. Adres değişebilir, ancak görünen
etkinlikler aynı kalır. Üretimde sorguyu okuyan, doğrulayan ve uygulayan bir
sunucu rotası ya da sunucuda oluşturulmuş sonuçlar gerekir. İstemci filtrelemesi
çalışan bu temeli geliştirebilir.

## Yanıt 30

Girdi yöntemi düzenleyicisi bir karakter oluşurken ara değerler bildirebilir.
Her ara değerde filtrelemek sonuçların tamamlanmadan sıçramasına neden olur.
Yazma tamamlanana kadar beklemek için kompozisyon olaylarını kullanın veya
`isComposing` durumunda ara güncellemeleri atlayın. Öğrencilerin kullandığı yazma
sistemleriyle sınayın.

## Yanıt 31

Tarih aralığı bileşeni, normalleştirilmiş başlangıç ve bitiş değerlerini
`detail` içinde taşıyan kabarcıklanan `date-range-change` olayı gönderebilir.
Böylece üst bileşen iç denetimleri bilmeden tepki verir. Form gönderiminin zaten
yerel olayı, varsayılan davranışı, doğrulaması ve klavye anlamı vardır. Özel olay,
bu sözleşmeleri yeniden kurmak zorunda bırakır.

## Yanıt 32

Önce gereken tüm dikdörtgenleri sıradan veriye alın, compact kararlarını bu
veri üzerinde üretin, son olarak sınıfları ikinci geçişte değiştirin. Böylece
yerleşim bilgisini tekrar tekrar güncelleyebilen yazma-sonrası-okuma örüntüsü
kaldırılır. Performance kaydı, temsilî içerik ve cihazda yerleşim işinin gerçek
etkileşim süresinde önemli olduğunu gösteriyorsa değişiklik haklıdır. Zaten hızlı
olan kısa liste karmaşık optimizasyona ihtiyaç duymaz; CSS container query ölçümü
JavaScript'ten tamamen kaldırabilir.

## Yanıt 33

```js
const list = document.querySelector("#event-list");
if (!list) throw new Error("#event-list bulunmalı.");

const observer = new MutationObserver((records) => {
  for (const record of records) {
    for (const node of record.addedNodes) {
      if (node instanceof Element && node.matches(".event-card")) {
        console.log("Kart eklendi:", node.dataset.eventId);
      }
    }
  }
});

observer.observe(list, { childList: true });
// Gözlem sorumluluğu bitince observer.disconnect().
```

Kök yalnızca etkinlik listesi, seçenek ise doğrudan çocuk değişimidir. Alt
soy değişiklikleri sözleşmenin parçasıysa `subtree: true` eklenir. Görünüm
kaldırıldığında, deney bittiğinde veya sahibi bildirime ihtiyaç duymadığında
gözlemci ayrılmalıdır.

## Yanıt 34

Tıklama veya belgelenmiş özel olay, bir oluşumu ya da niyeti olay yolu üzerinden
taşır. Değişiklik kaydı, DOM değişimini gerçekleştikten sonra anlatır ve toplu
iletilebilir. “Bu etkinliği kaydet” yerel düğme etkinleştirmesinden veya alan
düzeyi özel olaydan ele alınmalıdır; niyet o anda bilinir. Sonraki metin veya
sınıf değişimini gözlemek, çizilmiş sonucu onu doğuran eylemle karıştırır.

## Yanıt 35

Light DOM, bileşene sağlanan sıradan sayfa çocuklarıdır. Shadow root dahili alt
ağaca sahiptir ve sağlanan içeriği slotlarla yerleştirebilir. Composed olay gölge
sınırını aştığında dış kod, dahili yapıyı koruyan yeniden hedeflenmiş bir hedef
görebilir. `composedPath()` platformun izin verdiği yayılma yolunu gösterir. Dış
dinleyici, geliştirici araçlarında görünen dahili seçiciye değil bileşenin genel
olay sözleşmesine dayanmalıdır.

## Yanıt 36

Öğe belgeden çıkarılıp yeniden eklenebilir; bu yüzden `connectedCallback()` birden
çok kez çalışır. Her bağlantıda yeni anonim dinleyici eklemek yinelenen çağrı
oluşturabilir. Tek seferlik kurulumu bayrakla koruyun, her bağlantı için bir
`AbortController` kullanıp `disconnectedCallback()` içinde iptal edin veya uygun
dahili düğümler hazırsa kararlı dinleyiciyi bir kez kurun. Seçim kaynak ömrüyle
eşleşmelidir.

## Yanıt 37

Yerel düğme için `click`, canlı filtre için `input`, kesinleşmiş seçim için
`change`, form üzerinde gönderim için `submit`, kalem hareketi için pointer
event'leri kullanın. Seçim görevin anlamına dayanır. Düğme ve form olayları
klavye ile yardımcı teknoloji yollarını korur; pointer event'leri mouse'a bağımlı
olmadan basınç, temas ve iptal bilgisi verir.

## Yanıt 38

`isTrusted`, olayı sayfanın `dispatchEvent()` çağrısı yerine kullanıcı aracının
dağıttığını söyler. Kimliği, rolü, kaydın sahipliğini veya ağ isteğinin
bütünlüğünü kanıtlamaz. İstemci farklı bir HTTP isteği oluşturabilir. Sunucu
kullanıcıyı doğrulamalı ve belirli kayıt ile işlem için yetkiyi uygulamalıdır.

## Yanıt 39

```html
<form id="event-search" action="/events" method="get"></form>
<label for="query">Etkinlik ara</label>
<input id="query" name="query" form="event-search">
<button type="submit" form="event-search">Ara</button>
```

İki denetim de `form="event-search"` ile sahibini belirtir; alt öğe olmasalar da
gönderime katılır. Gerçek yerleşim veya bileşen sınırı iç içe yerleştirmeyi
engelliyorsa uygundur. Sıradan durumda formun alt öğesi olmak daha kolay anlaşılır.

## Yanıt 40

Varsayılan URL kodlu biçim, sıradan ad-değer çiftlerini istek gövdesinde kompakt
taşır. `multipart/form-data`, girdileri parçalara ayırır ve dosya içeriğiyle
üstverisini taşıyabilir. `accept`, dosya seçicinin uygun seçenekleri göstermesine
yardım eder; uzantı ve bildirilen medya türü yanıltılabilir, istemci kuralları
atlanabilir. Sunucu boyutu, tanınan içerik türünü, yetkiyi, saklama yerini ve
güvenlik taramasını uygulamalıdır.

---

# 14. Kısa sınav

1. DOM neyin kısaltmasıdır? **Document Object Model.**
2. DOM değişikliği kaynak dosyayı değiştirir mi? **Hayır; bellekteki canlı belgeyi değiştirir.**
3. `querySelector` eşleşme bulamazsa ne döndürür? **`null`.**
4. `querySelectorAll` sonucu canlı mıdır? **Hayır, statik `NodeList` döndürür.**
5. Güvenilmeyen düz metni hangi özellik gösterir? **`textContent`.**
6. `classList.toggle(name, condition)` ne yapar? **Koşul doğruysa ekler, yanlışsa kaldırır.**
7. `dataset.eventId` hangi özniteliğe karşılık gelir? **`data-event-id`.**
8. `<template>` neden kullanılır? **Kopyalanana kadar gösterilmeyen yinelenebilir yapı sağlar.**
9. Uygulama durumu nedir? **Davranış ve görünümü belirlemek için hatırlanan bilgiler.**
10. Olay aşamaları hangi sıradadır? **Yakalama, hedef, kabarcıklanma.**
11. `event.target` nedir? **Olayın en içteki hedefi.**
12. `event.currentTarget` nedir? **Dinleyicisi o anda çalışan nesne.**
13. `preventDefault` kabarcıklanmayı durdurur mu? **Hayır.**
14. İlk çağrıdan sonra hangi seçenek dinleyiciyi kaldırır? **`once: true`.**
15. Olay devri nedir? **Üst öğede, alt öğeden kabarcıklanan eşleşmeleri ele almak.**
16. Form gönderimini hangi olay anlatır? **Form üzerindeki `submit`.**
17. Form denetiminin `name` değeri ne işe yarar? **Gönderilen veri alanını tanımlar.**
18. Yinelenen değerleri hangi FormData yöntemi alır? **`getAll()`.**
19. `checkValidity()` ne döndürür? **Boolean doğrulama sonucu.**
20. Özel doğrulama hatası nasıl silinir? **`setCustomValidity("")` çağrılır.**
21. Sunucu neden yeniden doğrulama yapar? **İstemci değiştirilebilir veya atlatılabilir.**
22. Aşamalı iyileştirme nedir? **Anlamlı temel deneyimi gereksiz yere bozmadan yetenek eklemek.**
23. Canlı DOM hangi geliştirici araçları panelindedir? **Elements.**
24. Olay kesme noktası ne sağlar? **İşleyicide durup çağrı yığınını ve değerleri inceleme olanağı.**
25. İşaretli onay kutusu her zaman `"on"` mı gönderir? **Hayır; `value` verilmişse o gönderilir.**
26. `type="email"` posta kutusunun sahipliğini doğrular mı? **Hayır; yalnızca yazım biçimini denetler.**
27. Devre dışı alan `FormData` değerine katılır mı? **Normalde katılmaz.**
28. Çizim odağı neden kaydırabilir? **Odaktaki düğüm belgeden kaldırılmış olabilir.**
29. Statik sunucu GET sorgusunu uygulama filtresine dönüştürür mü? **Hayır; bunu sunucu rotası yapmalıdır.**
30. Canlı aramada kompozisyon olayları neden önemlidir? **IME karakter oluşurken geçici metin bildirebilir.**
31. `CustomEvent.detail` içinde ne bulunur? **Dinleyicilerin ihtiyaç duyduğu küçük ve belgelenmiş veri.**
32. Geometri okumaları neden DOM yazmalarından önce gruplanır? **Yinelenen yazma-sonrası-okuma örüntüsünün eşzamanlı yerleşim işini zorlamasını önlemek için.**
33. `MutationObserver` ne zaman ayrılmalıdır? **Gözlem sorumluluğu veya sahip bileşenin ömrü sona erdiğinde.**
34. Değişiklik kaydı kullanıcı niyetini bildirir mi? **Hayır; gerçekleştikten sonraki DOM değişimini anlatır.**
35. Shadow DOM güvenlik sınırı mıdır? **Hayır; kapsülleme sınırıdır.**
36. Bileşen sınırından geçen izinli olay yolunu hangi yöntem gösterir? **`event.composedPath()`.**
37. Yerel düğme etkinleştirmesini normalde hangi olay anlatır? **`click`.**
38. `event.isTrusted` sunucu yetkilendirmesinin yerini alabilir mi? **Hayır.**
39. Dışarıdaki denetimi form sahibine hangi öznitelik bağlar? **`form`.**
40. Dosya yüklemede normalde hangi form kodlaması kullanılır? **`multipart/form-data`.**

---

# 15. Özet ve sözlük

DOM, HTML dosyasının kendisi değil; tarayıcının canlı nesne ağacıdır. JavaScript
bu ağacı seçip güvenli biçimde değiştirir. Açık uygulama durumu, çizimin
yinelenebilir olmasını sağlar. Olaylar bir yayılma yolundan geçer; hedef ile
geçerli hedefi anlamak doğrudan dinlemeyi ve olay devrini öngörülebilir kılar.
Formlar ad, değer, gönderim ve kısıt doğrulama davranışını zaten sağlar.
Profesyonel JavaScript bu anlamları geliştirir, erişilebilir geri bildirim verir
ve son güven sınırı olarak sunucu doğrulamasını korur. Daha büyük ölçeklerde
oku-karar ver-yaz gruplaması gereksiz yerleşim tekrarını azaltır; değişiklik
gözlemcileri uygulamanın kendi durum yolu dışındaki değişimleri izler; shadow DOM
ve özel öğeler yerel anlamı değiştirmeden açık bileşen sözleşmeleri kurar.

Tablo 5.6, bölüm boyunca kullanılan terimleri bir araya getirir.

**Tablo 5.6 - Oturum 5 sözlüğü**

| Terim | Anlam |
|---|---|
| DOM | Yüklenmiş belgenin canlı nesne gösterimi |
| Düğüm | Belge ağacındaki genel nesne |
| Öğe | HTML öğesinden oluşan düğüm |
| Durum | Davranışı ve çıktıyı belirlemek için hatırlanan bilgiler |
| Çizim | Arayüzü güncel duruma uygun hale getirme |
| Olay | Tarayıcı veya kod tarafından dağıtılan etkileşim nesnesi |
| Yayılma | Olayın yakalama, hedef ve genellikle kabarcıklanma aşamalarında ilerlemesi |
| Olay devri | Üst öğenin eşleşen alt öğe olayını ele alması |
| Varsayılan davranış | Form gönderimi gibi olayla ilişkili tarayıcı davranışı |
| Başarılı denetim | Adı ve değeri form verisine katılan denetim |
| Kısıt doğrulaması | Bildirilen form koşullarını denetleyen tarayıcı modeli |
| Aşamalı iyileştirme | Anlamlı temel deneyime yetenek ekleme yaklaşımı |
| Değişiklik gözlemcisi | Gözlenen DOM kapsamındaki değişimleri toplu kayıtlarla bildiren API |
| Light DOM | Gölge ağacı dışında sağlanan sıradan belge çocukları |
| Shadow DOM | Shadow host'a bağlı kapsüllenmiş bileşen alt ağacı |
| Olay yeniden hedefleme | Bileşen sınırında dışarıya gösterilen olay hedefinin ayarlanması |
| Özel öğe | Kısa çizgili ad ve tanımlı yaşam döngüsüyle kayıtlı HTML öğesi |
| Form sahibi | Altlık ilişkisi veya `form` özniteliğiyle denetimin bağlandığı form |

## Öğretim notu

12-14 ders saati ve bağımsız laboratuvar zamanı ayırın. İlk derste kaynak-DOM
farkını ve güvenli değişikliği; ikincide durum, çizim ve olay yayılmasını;
üçüncüde form, doğrulama, erişilebilirlik ve bütünleşik laboratuvarı işleyin.
Öğrenciler kodu çalıştırmadan önce `target`, `currentTarget` ve `FormData`
sonuçlarını tahmin etsin. Laboratuvarı yalnızca ekran görüntüsüne göre değil,
tarayıcı davranışı, model testleri, klavye kanıtı ve sözleşmeleri açıklama
becerisine göre değerlendirin. Bölüm 10'u ileri bir başvuru atölyesi olarak
işleyin: optimizasyonu tartışmadan önce küçük uygulamayı ölçün, tek değişiklik
kaydını gösterin ve herkesten bileşen kütüphanesi istemeden bir shadow root olay
yolunu inceleyin.

## Standartlar ve ileri okuma

- WHATWG, [DOM Living Standard](https://dom.spec.whatwg.org/). Belge düğümleri,
  olay dağıtımı ve ilgili arayüzler için temel standart.
- WHATWG, [HTML Living Standard: Formlar ve form denetimleri](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html).
  Gönderim, başarılı denetimler ve kısıt doğrulamasının ayrıntılı kuralları.
- WHATWG, [HTML Living Standard: Özel öğeler](https://html.spec.whatwg.org/multipage/custom-elements.html)
  ve [Shadow trees](https://dom.spec.whatwg.org/#shadow-trees). Bileşen yaşam
  döngüsü, ağaç sınırı, olay yolu ve yeniden hedeflemenin normatif modeli.
- W3C, [Pointer Events](https://www.w3.org/TR/pointerevents3/). Mouse, kalem ve
  dokunma için iptal davranışı dahil birleşik işaretçi modeli.
- MDN, [Document Object Model olayları](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Events)
  ve [Olay kabarcıklanması](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling).
  Dinleyici, yayılma ve olay devri açıklamaları.
- MDN, [HTML form doğrulaması ve Kısıt Doğrulama API'si](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
  ve [İstemci tarafı form doğrulaması](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation).
- W3C Web Accessibility Initiative, [Form doğrulaması](https://www.w3.org/WAI/tutorials/forms/validation/)
  ve [Kullanıcı bildirimleri](https://www.w3.org/WAI/tutorials/forms/notifications/).
- Stanford CS142, [DOM ve olay dersleri](https://web.stanford.edu/class/cs142/lectures.html).
  DOM ile olayları ayrı öğretip uygulama geliştirmeye ilerleyen bir üniversite sırası.
- University of Washington CSE 154, [JavaScript ve DOM](https://courses.cs.washington.edu/courses/cse154/20su/lectures/lec06-dom-events/index.html),
  [Olaylar ve DOM değişikliği](https://courses.cs.washington.edu/courses/cse154/20sp/lectures/lec07-js-events-styles/index.html)
  ve [Form gönderimi ve doğrulama](https://courses.cs.washington.edu/courses/cse154/20sp/lectures/lec15-post-form/index.html).
  Ders ve laboratuvar sıralamasına örnekler.

Teknik inceleme tarihi: 25 Kasım 2026. Standartlar sürekli güncellenir; yeni
akademik yıl baskısından önce tarayıcı davranışını ve erişilebilirlik rehberini
yeniden inceleyin.
