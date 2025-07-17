```html
<!--
QiAlly LLC – Master Service Agreement (MSA)
Version: Draft for Web Embedding

This HTML snippet includes collapsible toggles for each main section using native <details> and <summary> tags. The content is styled for readability and mobile responsiveness.

Replace all #PLACEHOLDERS# (e.g. #PARTY A NAME#) with appropriate content before publishing.
-->

<style>
  #msa-container {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 2rem auto;
    color: #333;
    line-height: 1.5;
  }
  details {
    margin-bottom: 1.25rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    background: #fafafa;
  }
  summary {
    cursor: pointer;
    padding: 0.75rem 1rem;
    font-size: 1.15rem;
    font-weight: bold;
    background: #ececec;
    border-radius: 4px 4px 0 0;
    user-select: none;
  }
  summary::-webkit-details-marker { display: none; }
  summary:after {
    content: " ▶";
    float: right;
    transition: transform 0.2s ease;
  }
  details[open] summary:after {
    transform: rotate(90deg);
  }
  .section-content {
    padding: 1rem 1.5rem;
  }
  .section-content h4 {
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    font-size: 1rem;
  }
  .section-content ul,
  .section-content ol {
    margin: 0.5rem 0 1rem 1.5rem;
  }
</style>

<div id="msa-container">

  <details>
    <summary>QiAlly LLC – Master Service Agreement Intro</summary>
    <div class="section-content">
      <p>This agreement is entered into as of the last date signed by the parties (the "Effective Date") between <strong>#PARTY A NAME#</strong>, [whose principal place of residence is at / a #PARTY A JURISDICTION# corporation with its principal place of business at #PARTY A ADDRESS#] ("#PARTY A#") and <strong>#PARTY B NAME#</strong>, [whose principal place of residence is at / a #PARTY B JURISDICTION# corporation with its principal place of business at #PARTY B ADDRESS#] ("#PARTY B#").</p>
      <p>(The capitalized terms used in this agreement, in addition to those above, are defined in section "DEFINITIONS".)</p>
      <p>This agreement is written in legal language (binding) to protect both parties and clearly define expectations, rights, and responsibilities. QiAlly values transparency and respectful communication. For each key section, a plain‑language “Keeping it Real” version is available at <a href="https://www.qially.me/legal" target="_blank" rel="noopener">https://www.qially.me/legal</a>. These summaries are not substitutes for the legal terms but are meant to foster shared understanding and trust.</p>
    </div>
  </details>

  <details>
    <summary>1. Term</summary>
    <div class="section-content">
      <p>This Service Agreement ("Agreement") is made and entered into by and between QiAlly LLC ("the Company") and the undersigned client ("Client") as of the effective date indicated below. It defines the terms from the moment of engagement through the conclusion or termination of the services. This Agreement remains in effect unless terminated under the conditions listed herein.</p>

      <h4>1.1 Initial Term</h4>
      <p>The initial term of this agreement will begin on the Effective Date and continue for <strong>#TERM PERIOD#</strong> months/years, unless terminated earlier (the "Initial Term").</p>

      <h4>1.2 Automatic Renewal</h4>
      <p>Subject to paragraph "ELECTION NOT TO RENEW", at the end of each Term this agreement will automatically renew for a renewal term of <strong>#RENEWAL TERM PERIOD#</strong> months/years, unless terminated earlier ("Renewal Term").</p>

      <h4>1.3 Election Not to Renew</h4>
      <p>Either party may elect not to renew this agreement by providing notice to the other party at least <strong>#NON-RENEWAL NOTICE PERIOD#</strong> Business Days before the end of the Term.</p>

      <h4>1.4 Term Definition</h4>
      <p>"Term" means either the Initial Term or the then-current Renewal Term.</p>

      <h4>1.5 Assignment</h4>
      <p>Neither party may assign this agreement or any of their rights or obligations under this agreement without the prior written consent of the other party.</p>

      <h4>1.6 Successors</h4>
      <p>This agreement benefits and binds the parties and their respective heirs, successors, and permitted assigns.</p>

      <h4>1.7 Amendments</h4>
      <p>This agreement can be amended only by a writing signed by both parties.</p>
    </div>
  </details>

  <!-- Continue other <details> sections below as needed -->

</div>
```
