# Pre-review Questionnaire

Eventually, it would be nice if a document like this was part of a specification
publishing process. See <http://lists.w3.org/Archives/Public/public-w3process/2014Nov/0026.html>
for some discussion around that notion.

Pull requests ever so welcome: <https://github.com/mikewest/spec-questionnaire>

1.  Does this specification deal in any way with [personally-identifiable
    information][pii]?

2.  Does this specification deal with high-value information like credentials or
    payment?

3.  Does this specification allow an origin access to a user's location?

4.  Does this specification allow an origin access to sensors on a user's
    device?

5.  Does this specification allow an origin access to aspects of a user's local
    computing environment (e.g. screen sizes, installed fonts, installed
    plugins)?

6.  Does this specification allow an origin some measure of control over a user
    agent's native UI (showing, hiding, or modifying certain details, especially
    if those details are relevant to security)?

7.  Does this specification expose origin-controlled data to an origin over
    HTTP (e.g. cookies, `ETag` and `Last Modified` headers)? Via an API (e.g.
    `localStorage`)?

8.  Does this specification expose temporary identifiers to the web (e.g. TLS
    features like Channel ID, session identifiers/tickets, etc)?

9.  Does this specification expose persistent details to the web (device-level,
    like GPU details, or otherwise)? Have steps been taken to reduce the entropy
    these details introduce?

10. Does this specification distinguish between behavior in first-party and
    third-party contexts (where "first-party" is simply defined as the top-level
    origin the user theoretically sees in the address bar)?

11. Does this specification expose any other data to an origin that it doesn't
    currently have access to (e.g. Content Security Policy's violation reports)?

12. Does this specification create a string-to-script mechanism (e.g. `eval()`
    or `setTimeout([string], ...)`)?

13. Does this specification enable a new script loading/execution mechanism
    (e.g. HTML Imports)? What about style?

14. Does this specification have a "Security Considerations" and "Privacy
    Considerations" section?

[pii]: http://en.wikipedia.org/wiki/Personally_identifiable_information
