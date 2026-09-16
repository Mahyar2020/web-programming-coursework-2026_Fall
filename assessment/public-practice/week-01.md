# Week 1 Public Practice Bank

These are formative variants. They are not secure summative questions.

## Variant A — URL and request boundary

Given:

```text
https://api.example.edu:8443/v1/events?limit=5#today
```

1. Label the scheme, host, port, path, query, and fragment.
2. Write the request target normally sent in an HTTP request.
3. Identify the portion retained by the client.

### Answer

The components are `https`, `api.example.edu`, `8443`, `/v1/events`, `limit=5`,
and `today`. The request target is normally `/v1/events?limit=5`. The browser
retains `#today`.

## Variant B — Status reasoning

A page looks like an error and the Network panel reports `404`. A student claims
the server never responded. Evaluate the claim.

### Answer

It is incorrect. `404` is an HTTP response status. The visible error page can be
the response content. A lack of response would appear as a network-level failure,
not a completed HTTP response with status `404`.

## Variant C — Local environments

Compare `file:///home/student/site/index.html` with
`http://localhost:8000/index.html` using two observable differences.

### Answer

The schemes differ (`file` vs `http`), and only the latter requires a local server
and produces an HTTP exchange with a method, response status, and HTTP fields.

## Variant D — Commit quality

Rewrite these messages to communicate intent: `stuff`, `more`, `done`.

### Example answer

`Create the Campus Hub document`, `Add event and community navigation`, and
`Record successful and missing-resource HTTP observations`.
