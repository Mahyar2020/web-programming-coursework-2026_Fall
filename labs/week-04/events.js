const events = [
  { title: "Robotics night", category: "technology", capacity: 80, registered: 62, featured: true },
  { title: "Campus orchestra", category: "arts", capacity: 120, registered: 120, featured: false },
  { title: "Sustainable gardens", category: "community", capacity: 40, registered: 18, featured: true },
];

function seatsRemaining(event) {
  return event.capacity - event.registered;
}

function eventStatus(event) {
  const remaining = seatsRemaining(event);

  if (remaining === 0) return "full";
  if (remaining <= 10) return "almost full";
  return "open";
}
function filterEvents(allEvents, category) {
  return allEvents.filter((event) => event.category === category);
}
function summarizeEvents(allEvents) {
  return allEvents.map((event) => ({
    title: event.title,
    remaining: seatsRemaining(event),
    status: eventStatus(event),
  }));
}

const summary = summarizeEvents(events);
console.table(summary);

const output = typeof document === "undefined" ? null : document.querySelector("#program-output");
if (output) {
  output.textContent = summary
    .map(({ title, remaining, status }) => `${title}: ${status} (${remaining} seats remaining)`)
    .join("\n");
}
