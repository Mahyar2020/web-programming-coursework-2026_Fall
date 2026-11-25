import test from "node:test";
import assert from "node:assert/strict";
import {
  createInitialState,
  deriveVisibleEvents,
  events,
  seatsRemaining,
  toggleSaved,
} from "./model.js";

test("initial state shows every event", () => {
  assert.deepEqual(deriveVisibleEvents(events, createInitialState()), events);
});

test("query matching is trimmed and case-insensitive", () => {
  const state = { ...createInitialState(), query: "  ROBOTICS " };
  assert.deepEqual(deriveVisibleEvents(events, state).map((event) => event.id), ["robotics-night"]);
});

test("category and availability filters cooperate", () => {
  const state = { ...createInitialState(), category: "arts", availableOnly: true };
  assert.deepEqual(deriveVisibleEvents(events, state), []);
});

test("available-only filtering excludes full events", () => {
  const state = { ...createInitialState(), availableOnly: true };
  assert.deepEqual(deriveVisibleEvents(events, state).map((event) => event.id), [
    "robotics-night",
    "sustainable-gardens",
  ]);
});

test("filtering does not mutate the event collection or state", () => {
  const state = { ...createInitialState(), query: "robot" };
  const originalQuery = state.query;
  const originalIds = events.map((event) => event.id);
  deriveVisibleEvents(events, state);
  assert.equal(state.query, originalQuery);
  assert.deepEqual(events.map((event) => event.id), originalIds);
});

test("seatsRemaining clamps over-registration to zero", () => {
  assert.equal(seatsRemaining({ capacity: 20, registered: 25 }), 0);
});

test("toggleSaved returns a new Set and toggles membership", () => {
  const original = new Set(["robotics-night"]);
  const removed = toggleSaved(original, "robotics-night");
  const added = toggleSaved(removed, "campus-orchestra");
  assert.notEqual(original, removed);
  assert.deepEqual([...original], ["robotics-night"]);
  assert.deepEqual([...added], ["campus-orchestra"]);
});

test("toggleSaved safely adds a previously unsaved identifier", () => {
  const original = new Set();
  const next = toggleSaved(original, "robotics-night");
  assert.notEqual(next, original);
  assert.equal(next.has("robotics-night"), true);
  assert.equal(original.size, 0);
});
