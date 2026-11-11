import test from "node:test";
import assert from "node:assert/strict";
import { eventStatus, filterEvents, seatsRemaining, summarizeEvents } from "./events.js";

globalThis.document = { querySelector: () => null };

const sample = { title: "Robotics night", category: "technology", capacity: 80, registered: 62 };

test("seatsRemaining subtracts registrations without returning a negative value", () => {
  assert.equal(seatsRemaining(sample), 18);
  assert.equal(seatsRemaining({ ...sample, registered: 90 }), 0);
});

test("eventStatus applies the documented boundaries", () => {
  assert.equal(eventStatus(sample), "open");
  assert.equal(eventStatus({ ...sample, registered: 72 }), "almost full");
  assert.equal(eventStatus({ ...sample, registered: 80 }), "full");
});

test("filterEvents returns a new array and respects the category", () => {
  const source = [sample, { ...sample, title: "Concert", category: "arts" }];
  assert.deepEqual(filterEvents(source, "technology"), [sample]);
  assert.notEqual(filterEvents(source), source);
});

test("summarizeEvents returns the public summary shape", () => {
  assert.deepEqual(summarizeEvents([sample]), [
    { title: "Robotics night", remaining: 18, status: "open" },
  ]);
});

test("invalid event data produces a useful TypeError", () => {
  assert.throws(() => seatsRemaining({ capacity: "80", registered: 10 }), TypeError);
});
