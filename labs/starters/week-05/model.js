export const events = Object.freeze([
  Object.freeze({ id: "robotics-night", title: "Robotics night", category: "technology", capacity: 80, registered: 62 }),
  Object.freeze({ id: "campus-orchestra", title: "Campus orchestra", category: "arts", capacity: 120, registered: 120 }),
  Object.freeze({ id: "sustainable-gardens", title: "Sustainable gardens", category: "community", capacity: 40, registered: 18 }),
]);

export function createInitialState() {
  return { query: "", category: "all", availableOnly: false, savedIds: new Set() };
}

export function seatsRemaining(event) {
  return Math.max(0, event.capacity - event.registered);
}

export function deriveVisibleEvents(allEvents, state) {
  // TODO: combine the query, category, and availability predicates.
  return allEvents;
}

export function toggleSaved(savedIds, eventId) {
  // TODO: return a new Set with eventId toggled; do not mutate savedIds.
  return new Set(savedIds);
}
