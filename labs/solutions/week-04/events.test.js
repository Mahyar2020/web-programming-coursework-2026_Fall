import test from "node:test";
import assert from "node:assert/strict";
import {
  createEventRegistry,
  eventStatus,
  filterEvents,
  groupEventsByCategory,
  seatsRemaining,
  summarizeEvents,
} from "./events.js";

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

test("groupEventsByCategory builds a Map without changing the source array", () => {
  const arts = { ...sample, title: "Concert", category: "arts" };
  const source = [sample, arts];
  const groups = groupEventsByCategory(source);

  assert.equal(groups instanceof Map, true);
  assert.deepEqual(groups.get("technology"), [sample]);
  assert.deepEqual(groups.get("arts"), [arts]);
  groups.get("arts").push({ ...arts, title: "Gallery" });
  assert.equal(source.length, 2);
});

test("createEventRegistry keeps its Map private and returns defensive list arrays", () => {
  const registry = createEventRegistry([sample]);
  const firstList = registry.list();
  firstList.length = 0;

  assert.equal(registry.findByTitle("Robotics night"), sample);
  assert.equal(registry.list().length, 1);

  const concert = { ...sample, title: "Concert", category: "arts" };
  registry.add(concert);
  assert.deepEqual(registry.list(), [sample, concert]);
});

test("createEventRegistry rejects invalid initial data and blank titles", () => {
  assert.throws(() => createEventRegistry("not an array"), TypeError);
  assert.throws(
    () => createEventRegistry([{ ...sample, title: "" }]),
    /non-empty title/,
  );
});
