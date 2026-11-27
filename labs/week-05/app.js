// model.js dosyasından hazır veri ve hesaplama fonksiyonlarını içe aktarıyoruz
import { createInitialState, deriveVisibleEvents, events, seatsRemaining, toggleSaved } from "./model.js";

// HTML'deki gerekli elementleri seçiyoruz
const filterForm = document.querySelector("#event-filter");
const eventList = document.querySelector("#event-list");
const cardTemplate = document.querySelector("#event-card-template");
const filterStatus = document.querySelector("#filter-status");
const savedCount = document.querySelector("#saved-count");

// Uygulamanın başlangıç durumunu (state) oluşturuyoruz
let state = createInitialState();
// 1. GÖREV: Tek bir etkinlik kartı oluşturan fonksiyon
// Formdaki güncel filtre değerlerini (arama, kategori, boş yer) okuyan yardımcı fonksiyon
function createEventCard(event) {
// HTML'deki şablonu (template) kopyalıyoruz
  // TODO: clone the template, fill text with textContent, and set button state.
  // Kopyalanan şablonun içindeki alt elementleri seçiyoruz
  const fragment = cardTemplate.context.cloneNode(true);
  const card = fragment.querySelector(".event-card");
  const title = fragment.querySelector(".event-card__title");
  const category = fragment.querySelector(".event-card__category");
  const availability = fragment.querySelector(".event-card__availability");
  const saveButton = fragment.querySelector(".event-card__save");
// Kalan koltuk sayısını ve etkinliğin daha önce kaydedilip kaydedilmediğini kontrol ediyoruz
  const remaining = seatsRemaining(event);
  const isSaved = state.savedIds.has(event.id);
  // Karta etkinliğin ID'sini ve metin bilgilerini yazdırıyoruz
  card.dataset.eventId = event.id;
  title.textContent = event.title;
  category.textContext = event.category;
  availability.textContent = remaining === 0 ? "Full" : '$(remaining) seats remaining';
  saveButton.textContent = isSaved ? "Remove from saved events" : "Save event";
  saveButton.setAttribute("aria-pressed", String(isSaved));
  card.classlist.toggle("event-card--saved", isSaved);
  return fragment;
  
}

function render() {
  const activeElement = document.activeElement;
  const focusedCard = activeElement instanceof Element
  ? activeElement.closest("[data-event-id]")
  : null;
  const restoreSaveButton = activeElement instanceof Element 
  && activeElement.matches(".event-card_save");
  const focuseEventId = restoreSaveButton ? focusedCard?.dataset.eventId : null;

  const visibleEvents = deriveVisibleEvents(events, state);
  eventlist.replaceChildren(...visibleEvents.map(createEventCard));
    if (visibleEvents.length === 0) {
    const emptyState = document.createElement("p");
    emptyState.className = "empty-state";
    emptyState.textContent = "No events match these filters. Change or clear a filter to see more events.";
    eventList.append(emptyState);
  }
  savedCount.textContent = String(state.savedIds.size);
  filterStatus.textContent = visibleEvents.length === 1
    ? "Showing 1 matching event."
    : `Showing ${visibleEvents.length} matching events.`;

function render() {
  // TODO: derive visible events and replace the rendered children.
  if (focusedEventId) {
    const replacementCard = [...eventList.querySelectorAll("[data-event-id]")]
      .find((card) => card.dataset.eventId === focusedEventId);
    replacementCard?.querySelector(".event-card__save")?.focus({ preventScroll: true });
  }
}

filterForm.addEventListener("input", () => {
  state = readFilterState();
  render();
});

filterForm.addEventListener("submit", (event) => {
  event.preventDefault();
  state = readFilterState();
  render();
});

eventList.addEventListener("click", (event) => {
  if (!(event.target instanceof Element)) return;
  const saveButton = event.target.closest(".event-card__save");
  if (!saveButton) return;
  const card = saveButton.closest("[data-event-id]");
  if (!card) return;
  state = { ...state, savedIds: toggleSaved(state.savedIds, card.dataset.eventId) };
  render();
});

render();
}

// TODO: add form input/submit listeners and one delegated click listener.
render();
