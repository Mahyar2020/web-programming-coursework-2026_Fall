import test from "node:test";
import assert from "node:assert/strict";
import { arrayEvidence, functionEvidence, loopEvidence } from "./language-examples.js";

test("loop evidence distinguishes value, index, condition, and post-test loops", () => {
  const result = loopEvidence();
  assert.deepEqual(result.indexedTitles, [
    "0: Robotics night",
    "1: Campus orchestra",
    "2: Sustainable gardens",
  ]);
  assert.deepEqual(result.countdown, [3, 2, 1]);
  assert.deepEqual(result.attempts, ["attempt 1"]);
});

test("function evidence preserves direct, method, callback, object, and rest results", () => {
  const result = functionEvidence();
  assert.match(result.directCall, /Robotics night/);
  assert.match(result.methodCall, /^Featured:/);
  assert.deepEqual(result.callbackCall, [18, 0, 22]);
  assert.deepEqual(result.objectReturn, { remaining: 18, percentFull: 78 });
  assert.equal(result.restParameters, 43);
});

test("array evidence distinguishes mutation from copying operations", () => {
  const result = arrayEvidence();
  assert.deepEqual(result.source, ["technology", "arts", "community"]);
  assert.deepEqual(result.mutated, ["technology", "culture", "community"]);
  assert.equal(result.removed, "sports");
  assert.deepEqual(result.copiedReplacement, ["technology", "culture", "community"]);
  assert.deepEqual(result.featuredTitles, ["Robotics night", "Sustainable gardens"]);
  assert.equal(result.totalCapacity, 240);
});
