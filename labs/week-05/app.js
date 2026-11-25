import { createInitialState, deriveVisibleEvents, events, seatsRemaining, toggleSaved } from "./model.js";

const filterForm = document.querySelector("#event-filter");
const eventList = document.querySelector("#event-list");
const cardTemplate = document.querySelector("#event-card-template");
const filterStatus = document.querySelector("#filter-status");
const savedCount = document.querySelector("#saved-count");
let state = createInitialState();

function createEventCard(event) {
  // TODO: clone the template, fill text with textContent, and set button state.
}

function render() {
  // TODO: derive visible events and replace the rendered children.
}

// TODO: add form input/submit listeners and one delegated click listener.
render();
