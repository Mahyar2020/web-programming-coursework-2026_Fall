export const events = [
  { title: "Robotics night", category: "technology", capacity: 80, registered: 62, featured: true },
  { title: "Campus orchestra", category: "arts", capacity: 120, registered: 120, featured: false },
  { title: "Sustainable gardens", category: "community", capacity: 40, registered: 18, featured: true },
];

export function seatsRemaining(event) {
  if (!event || !Number.isFinite(event.capacity) || !Number.isFinite(event.registered)) {
    throw new TypeError("An event must contain numeric capacity and registered values.");
  }
  return Math.max(0, event.capacity - event.registered);
}

export function eventStatus(event) {
  const remaining = seatsRemaining(event);
  if (remaining === 0) return "full";
  if (remaining <= 10) return "almost full";
  return "open";
}

export function filterEvents(allEvents, category = "all") {
  if (!Array.isArray(allEvents)) throw new TypeError("allEvents must be an array.");
  return category === "all"
    ? [...allEvents]
    : allEvents.filter((event) => event.category === category);
}

export function summarizeEvents(allEvents) {
  return allEvents.map((event) => ({
    title: event.title,
    remaining: seatsRemaining(event),
    status: eventStatus(event),
  }));
}

export function groupEventsByCategory(allEvents) {
  if (!Array.isArray(allEvents)) throw new TypeError("allEvents must be an array.");

  const groups = new Map();
  for (const event of allEvents) {
    seatsRemaining(event);
    const group = groups.get(event.category) ?? [];
    groups.set(event.category, [...group, event]);
  }
  return groups;
}

export function createEventRegistry(initialEvents = []) {
  if (!Array.isArray(initialEvents)) throw new TypeError("initialEvents must be an array.");
  const byTitle = new Map();

  function add(event) {
    seatsRemaining(event);
    if (typeof event.title !== "string" || event.title.trim() === "") {
      throw new TypeError("An event must contain a non-empty title.");
    }
    byTitle.set(event.title, event);
  }

  for (const event of initialEvents) add(event);

  return Object.freeze({
    add,
    findByTitle(title) {
      return byTitle.get(title);
    },
    list() {
      return [...byTitle.values()];
    },
  });
}

const summary = summarizeEvents(events);
console.table(summary);

const output = typeof document === "undefined" ? null : document.querySelector("#program-output");
if (output) {
  output.textContent = summary
    .map(({ title, remaining, status }) => `${title}: ${status} (${remaining} seats remaining)`)
    .join("\n");
}
