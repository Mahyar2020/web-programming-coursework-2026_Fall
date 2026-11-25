import { arrayEvidence, functionEvidence, loopEvidence } from "./language-examples.js";

const format = (value) => JSON.stringify(value, null, 2);
document.querySelector("#loop-output").textContent = format(loopEvidence());
document.querySelector("#function-output").textContent = format(functionEvidence());
document.querySelector("#array-output").textContent = format(arrayEvidence());
