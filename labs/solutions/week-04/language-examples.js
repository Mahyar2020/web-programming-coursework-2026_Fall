export const events = [
  { title: "Robotics night", capacity: 80, registered: 62, featured: true },
  { title: "Campus orchestra", capacity: 120, registered: 120, featured: false },
  { title: "Sustainable gardens", capacity: 40, registered: 18, featured: true },
];

export function loopEvidence(allEvents = events) {
  const titles = [];
  for (const event of allEvents) titles.push(event.title);

  const indexedTitles = [];
  for (let index = 0; index < allEvents.length; index += 1) {
    indexedTitles.push(`${index}: ${allEvents[index].title}`);
  }

  const countdown = [];
  let seconds = 3;
  while (seconds > 0) countdown.push(seconds--);

  const attempts = [];
  let attempt = 0;
  do {
    attempt += 1;
    attempts.push(`attempt ${attempt}`);
  } while (attempt < 1);

  return { titles, indexedTitles, countdown, attempts };
}

export function seatsRemaining(event) {
  return Math.max(0, event.capacity - event.registered);
}

export function describeEvent(event, label = "Campus event") {
  return `${label}: ${event.title} (${seatsRemaining(event)} seats remaining)`;
}

export function eventMetrics(event) {
  return {
    remaining: seatsRemaining(event),
    percentFull: Math.round((event.registered / event.capacity) * 100),
  };
}

export function sum(...values) {
  return values.reduce((total, value) => total + value, 0);
}

export function functionEvidence() {
  const directCall = describeEvent(events[0]);
  const eventReporter = { label: "Featured", report(event) { return describeEvent(event, this.label); } };
  const methodCall = eventReporter.report(events[2]);
  const callbackCall = events.map((event) => seatsRemaining(event));
  const { remaining, percentFull } = eventMetrics(events[0]);

  return {
    directCall,
    methodCall,
    callbackCall,
    objectReturn: { remaining, percentFull },
    restParameters: sum(4, 8, 15, 16),
  };
}

export function arrayEvidence() {
  const categories = ["technology", "arts", "community"];
  const mutated = [...categories];
  mutated.push("sports");
  const removed = mutated.pop();
  mutated.splice(1, 1, "culture");

  const copiedReplacement = categories.with(1, "culture");
  const featuredTitles = events
    .filter((event) => event.featured)
    .map((event) => event.title);
  const totalCapacity = events.reduce((total, event) => total + event.capacity, 0);

  return {
    source: categories,
    mutated,
    removed,
    copiedReplacement,
    featuredTitles,
    totalCapacity,
  };
}
