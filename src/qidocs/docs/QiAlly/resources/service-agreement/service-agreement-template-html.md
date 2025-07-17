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

  <details>
    <summary>2. Scope of Services & Support Responsibilities</summary>
    <div class="section-content">
      <p>QiAlly offers a wide range of services customized to align with each Client’s needs.</p>
      <h4>2.1 These include, but are not limited to:</h4>
      <ul>
        <li>Business Strategy, Planning & Organizational Consulting</li>
        <li>Tax Filing, Compliance & Strategic Tax Planning</li>
        <li>Full-Spectrum Bookkeeping, Payroll & Cash Flow Forecasting</li>
        <li>Human Resources, Workers' Comp & Personnel Systems</li>
        <li>Legal Support (document preparation, not legal representation)</li>
        <li>Certified Translations & USCIS/Immigration Form Assistance</li>
        <li>Web Design, App Development, Automation & AI Tools</li>
        <li>Content Creation, Branding & Digital Marketing Solutions</li>
      </ul>

      <h4>Engagements</h4>
      <p>Each engagement includes a custom service plan, mutually approved in writing.</p>

      <h4>2.2 Delivery</h4>
      <p>Specific timelines, deliverables, and client action items may be documented via proposal, invoice, project workspace (e.g., Notion), or other formal record.</p>

      <h4>2.3 Payment of Compensation</h4>
      <p>(See sections 2.4–2.6 below for details.)</p>

      <h4>2.4 Invoice Delivery</h4>
      <p><strong>#PARTY A#</strong> shall invoice <strong>#PARTY B#</strong>.</p>

      <h4>2.5 Payment</h4>
      <ol>
        <li><strong>#PARTY B#</strong> shall pay each invoice to <strong>#PARTY A#</strong> within <strong>#PAYMENT DEADLINE#</strong> Business Days after receipt, in immediately available funds, to the account/method specified by <strong>#PARTY A#</strong>.</li>
      </ol>

      <h4>2.6 Invoice Procedure and Requirements</h4>
      <ol>
        <li>Make each invoice to <strong>#PARTY B#</strong> in writing, including:
          <ul>
            <li>An invoice number</li>
            <li>The total amount due</li>
            <li>A summary of the work invoiced</li>
          </ul>
        </li>
        <li>Send each invoice to:
          <ul>
            <li>Name: #PARTY B PAYABLES#</li>
            <li>Title: #PARTY B PAYABLES TITLE#</li>
            <li>Mailing Address: #PARTY B PAYABLES ADDRESS#</li>
            <li>Email: #PARTY B PAYABLES EMAIL#</li>
          </ul>
        </li>
      </ol>

      <h4>Additional Terms</h4>
      <ul>
        <li>Deposits required before project initiation (unless waived).</li>
        <li>Payments due upon receipt (unless stated otherwise).</li>
        <li>$20 late fee after 5 days + 2% monthly interest on outstanding balances.</li>
        <li>Accounts 30+ days overdue may incur a $100 fee and be sent to collections.</li>
        <li>Until full payment, QiAlly retains ownership of deliverables, credentials, and IP; client access may be restricted if past due.</li>
        <li>Recurring services billed monthly/quarterly as agreed; third-party software/subscriptions may be billed separately.</li>
      </ul>
    </div>
  </details>

  <details>
    <summary>3. Client Responsibilities</summary>
    <div class="section-content">
      <ul>
        <li>Provide accurate, timely data and documentation</li>
        <li>Respond to communication within 48 business hours</li>
        <li>Submit necessary files (e.g., receipts) by the 5th of each month when applicable</li>
        <li>Communicate material changes in operations or expectations</li>
        <li>Follow onboarding instructions and agreed communication channels</li>
      </ul>
      <p>Delays or missed deliverables due to client inaction may incur additional fees or rescheduling.</p>
    </div>
  </details>

  <!-- Continue adding other sections as needed -->

</div>
```
