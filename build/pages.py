#!/usr/bin/env python3
"""
Generates the interior pages for Work in Progress Wellness.

index.html is hand-written and NOT touched by this script.
Run:  python3 build/pages.py
Output: site/*.html
"""
import os, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOMAIN = "https://wip-wellness.com"

TEL = "971.415.0024"
TEL_HREF = "+19714150024"
EMAIL = "wiprelationshipcounseling@gmail.com"

NAV = [
    ("index.html", "Home"),
    ("team.html", "Our Team"),
    ("individual-therapy.html", "Individual Therapy"),
    ("mindfulness-coaching.html", "Mindfulness Coaching"),
    ("parenting-guidance.html", "Parenting Guidance"),
    ("retreats.html", "Retreats"),
    ("testimonials.html", "Testimonials"),
    ("contact.html", "Contact"),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Karla:wght@400;500;600;700'
         '&amp;family=Newsreader:ital,opsz,wght@0,6..72,200..400;1,6..72,200..400&amp;display=swap" rel="stylesheet">')


def nav_html(current):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'      <a href="{href}"{cur}>{label}</a>')
    return "\n".join(out)


def head(slug, title, desc, jsonld=""):
    ld = f'\n<script type="application/ld+json">\n{jsonld}\n</script>' if jsonld else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}/{slug}">
<meta name="theme-color" content="#F5F2EB">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}/assets/img/hero-water.jpg">
<meta property="og:url" content="{DOMAIN}/{slug}">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html">
      <span class="b1">Work in Progress</span>
      <span class="b2">Wellness</span>
    </a>

    <nav class="nav" aria-label="Main">
{nav_html(slug)}
    </nav>

    <a class="header-tel" href="tel:{TEL_HREF}">{TEL}</a>

    <button class="burger" type="button" aria-label="Menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<main id="main">
"""


FOOTER = f"""
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html">
          <span class="b1">Work in Progress</span>
          <span class="b2">Wellness</span>
        </a>
        <p class="footer-blurb">
          Relationship counseling, mindfulness and retreats with Grae Rose,
          Professional Counselor Associate. In person in Portland, Oregon and
          by telehealth across the state.
        </p>
      </div>

      <div>
        <h4>Explore</h4>
        <ul>
{chr(10).join(f'          <li><a href="{h}">{l}</a></li>' for h, l in NAV)}
        </ul>
      </div>

      <div>
        <h4>Get in touch</h4>
        <ul>
          <li><a href="tel:{TEL_HREF}">{TEL}</a></li>
          <li><a href="mailto:{EMAIL}">Email the practice</a></li>
          <li style="margin-top:.5rem; line-height:1.7">
            Mindful Therapy Group<br>
            11740 SW 68th Parkway, Suite 200<br>
            Portland, OR 97223
          </li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Work in Progress Relationship Counseling. All rights reserved.</span>
      <span>If you are in crisis, call or text 988 (Suicide &amp; Crisis Lifeline) or dial 911.</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""


def phero(eyebrow, h1, lede=""):
    l = f'\n      <p class="lede" data-reveal style="--d:180ms">{lede}</p>' if lede else ""
    return f"""
  <section class="phero">
    <div class="wrap">
      <p class="eyebrow" data-reveal>{eyebrow}</p>
      <h1 class="h-xl" data-reveal style="--d:90ms">{h1}</h1>{l}
    </div>
  </section>
"""


CTA_BAND = f"""
  <section class="band">
    <img src="assets/img/calm-pond.jpg" alt="Reeds and still water under a pale morning sky" loading="lazy" width="1920" height="1280">
    <div>
      <p class="eyebrow" data-reveal>Next step</p>
      <h2 class="h-lg" data-reveal style="--d:120ms">Let's start with a conversation.</h2>
      <p data-reveal style="--d:220ms">
        A free 15-minute call, no cost and no obligation &mdash; just a chance to work out
        whether we're a good fit for one another.
      </p>
      <div data-reveal style="--d:320ms">
        <a class="btn btn--light" href="contact.html">Get in touch <span class="arw">&rarr;</span></a>
      </div>
    </div>
  </section>
"""


def soon(title, body, note="Grae is writing this page now. In the meantime, call or text "
                          f"<a class=\"tlink\" href=\"tel:{TEL_HREF}\">{TEL}</a> with any questions."):
    return f"""
  <section class="section">
    <div class="wrap wrap--narrow">
      <div class="soon" data-reveal>
        <div class="ripple" aria-hidden="true" style="margin-bottom:1.5rem"><span></span><span></span><span></span></div>
        <p class="eyebrow eyebrow--center">{title}</p>
        <p class="lede" style="margin-inline:auto">{body}</p>
        <p style="margin-top:1.5rem; font-size:.9375rem; color:var(--ink-faint)">{note}</p>
      </div>
    </div>
  </section>
"""


PAGES = {}

# ---------------------------------------------------------------- Our Team
PAGES["team.html"] = dict(
    title="Our Team | Grae Rose, Professional Counselor Associate | Work in Progress Wellness",
    desc="Meet Grae Rose, Professional Counselor Associate at Work in Progress Wellness in Portland, Oregon. Holistic, person-centred therapy for adults. LGBTQ+ affirming.",
    jsonld="""{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Grae Rose",
  "jobTitle": "Professional Counselor Associate",
  "worksFor": { "@type": "ProfessionalService", "name": "Work in Progress Wellness" },
  "alumniOf": { "@type": "CollegeOrUniversity", "name": "Golden Gate University" },
  "telephone": "+1-971-415-0024",
  "image": "%s/assets/img/grae-rose.jpg"
}""" % DOMAIN,
    body=phero("Our team", "The person you'll actually be sitting with.",
               "Work in Progress Wellness is a one-therapist practice, which means you get "
               "one consistent person who knows your story &mdash; not a rotating roster. "
               "More practitioners will join as the retreat programme opens up.")
    + """
  <section class="section">
    <div class="wrap">
      <div class="split split--even">
        <figure style="margin:0" data-reveal>
          <div class="portrait">
            <img src="assets/img/grae-rose.jpg" alt="Grae Rose, Professional Counselor Associate" width="800" height="861">
          </div>
        </figure>
        <div data-reveal style="--d:140ms">
          <p class="eyebrow">Founder &amp; therapist</p>
          <h2 class="h-lg">Grae Rose</h2>
          <p class="credential">Professional Counselor Associate</p>
          <p class="lede" style="margin-top:1.6rem">
            I approach therapy from a holistic perspective, taking into account all the
            thoughts, beliefs and experiences that have shaped and influenced your life.
          </p>
          <p>
            We will work together to recognise and understand patterns in your life with the
            goal of strengthening relationships, identifying support systems and harvesting
            your innate strengths and resources, allowing you to make the changes you desire.
          </p>
          <p>
            I hold a Master's Degree in Psychology, Marriage &amp; Family Therapy from Golden
            Gate University in San Francisco and am trained in a variety of therapeutic models,
            including person-centred therapy, narrative therapy, mindfulness work, cognitive
            behavioural therapy and motivational interviewing. We'll work together to determine
            the approach that best fits your needs.
          </p>
          <p><strong style="color:var(--ink); font-weight:600">I am a staunch LGBTQ+ ally.</strong></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="background:var(--paper-2); border-block:1px solid var(--paper-3)">
    <div class="wrap">
      <div class="split">
        <div data-reveal>
          <p class="eyebrow">Approach</p>
          <h2 class="h-md" style="max-width:18ch">Trained in several models, wedded to none.</h2>
        </div>
        <div data-reveal style="--d:140ms">
          <ul class="taglist">
            <li>Person-centred therapy</li>
            <li>Narrative therapy</li>
            <li>Mindfulness work</li>
            <li>Cognitive behavioural therapy</li>
            <li>Motivational interviewing</li>
            <li>Holistic perspective</li>
          </ul>
          <p style="margin-top:1.8rem">
            No single model fits every person. We start where you are and adjust as we
            learn what actually helps.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Help with</p>
      <h2 class="h-md" data-reveal style="--d:90ms; max-width:22ch; margin-bottom:2.2rem">
        Some of what people bring into the room.
      </h2>
      <ul class="taglist" data-reveal style="--d:180ms">
        <li>Anxiety</li>
        <li>Depression</li>
        <li>Stress &amp; burnout</li>
        <li>Life transitions</li>
        <li>Relationship with self and others</li>
        <li>Spirituality &amp; religion</li>
        <li>Codependency</li>
        <li>Family issues</li>
        <li>Emotion regulation &amp; coping skills</li>
        <li>Other issues</li>
      </ul>
    </div>
  </section>
""" + CTA_BAND)

# -------------------------------------------------------- Individual Therapy
PAGES["individual-therapy.html"] = dict(
    title="Individual Therapy in Portland, OR | Work in Progress Wellness",
    desc="Individual talk therapy for adults 18+ in Portland, Oregon and by telehealth statewide. 50-minute sessions, $100 cash pay, in-network with many major insurance plans.",
    jsonld="""{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Individual Therapy",
  "provider": { "@type": "ProfessionalService", "name": "Work in Progress Wellness", "telephone": "+1-971-415-0024" },
  "areaServed": { "@type": "State", "name": "Oregon" },
  "offers": { "@type": "Offer", "price": "100", "priceCurrency": "USD",
              "description": "Individual therapy, 50-minute session" }
}""",
    body=phero("Individual therapy", "Individual therapy with Grae.",
               "Caring, non-judgmental support for adults (ages 18 and up) who wish to "
               "strengthen relationships and explore emotional health through compassionate "
               "talk therapy.")
    + """
  <section class="section">
    <div class="wrap">
      <div class="split">
        <div class="sticky" data-reveal>
          <p class="eyebrow">Fees</p>
          <h2 class="h-lg">Straightforward, and said out loud.</h2>
        </div>
        <div data-reveal style="--d:140ms">
          <dl class="contact-rows" style="margin:0">
            <div class="crow">
              <dt>Individual therapy</dt>
              <dd>
                <span class="big">$100</span>
                <p style="margin:.4rem 0 0; font-size:.9375rem; color:var(--ink-faint)">50-minute session</p>
              </dd>
            </div>
            <div class="crow">
              <dt>Insurance</dt>
              <dd>
                <p style="margin:0">
                  I am in-network with many major insurance plans and also offer a cash pay
                  option for those who are uninsured or prefer not to use insurance.
                </p>
                <p style="margin:.7rem 0 0; font-size:.9375rem; color:var(--ink-faint)">
                  Not sure whether your plan is covered? Ask me on the consultation call and
                  I'll check.
                </p>
              </dd>
            </div>
            <div class="crow">
              <dt>Consultation</dt>
              <dd>
                <span class="big">Free &middot; 15 minutes</span>
                <p style="margin:.4rem 0 0; font-size:.9375rem; color:var(--ink-faint)">
                  No cost, no obligation, no pressure.
                </p>
              </dd>
            </div>
          </dl>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="background:var(--paper-2); border-block:1px solid var(--paper-3)">
    <div class="wrap">
      <p class="eyebrow" data-reveal>Sessions</p>
      <h2 class="h-lg" data-reveal style="--d:90ms; max-width:16ch; margin-bottom:clamp(2.5rem,5vw,3.5rem)">
        Two ways to meet.
      </h2>

      <div class="split split--even">
        <div data-reveal>
          <h3 class="h-sm" style="margin-bottom:1rem">In-person sessions</h3>
          <p>
            In-person sessions are conducted at:
          </p>
          <p style="color:var(--ink); line-height:1.8">
            Mindful Therapy Group<br>
            11740 SW 68th Parkway, Suite 200<br>
            Portland, OR 97223
          </p>
        </div>
        <div data-reveal style="--d:140ms">
          <h3 class="h-sm" style="margin-bottom:1rem">Telehealth sessions</h3>
          <p>
            Prefer not to come to the office? Online sessions are available for anyone
            desiring more flexibility &mdash; anywhere in Oregon.
          </p>
          <p>
            All you need is a private space, a decent connection and 50 minutes with the
            door shut.
          </p>
        </div>
      </div>

      <div class="divider" aria-hidden="true"><span class="line"></span></div>

      <p class="lede" data-reveal style="max-width:60ch">
        Whether in-person or online, you will be in a safe and accepting therapeutic
        environment that facilitates growth, insight and change.
      </p>
    </div>
  </section>

  <section class="section quote">
    <div class="wrap wrap--narrow">
      <div class="ripple" data-reveal aria-hidden="true"><span></span><span></span><span></span></div>
      <blockquote data-reveal style="--d:140ms">
        <q>Change is possible. You know yourself better than anyone. If you desire change
        and are ready to take an active part in your treatment, I am here to help.</q>
        <cite>Grae Rose, PCA</cite>
      </blockquote>
    </div>
  </section>
""" + CTA_BAND)

# ------------------------------------------------------ Mindfulness Coaching
PAGES["mindfulness-coaching.html"] = dict(
    title="Mindfulness Coaching | Work in Progress Wellness, Portland OR",
    desc="Mindfulness coaching and training with Grae Rose at Work in Progress Wellness, Portland, Oregon. Coming soon — call 971.415.0024 to register your interest.",
    body=phero("Mindfulness coaching", "Mindfulness training.",
               "Attention is a skill, and like any skill it can be practised. Mindfulness "
               "coaching is about building that practice into a life you actually live "
               "&mdash; not a retreat you visit twice a year.")
    + """
  <section class="section">
    <div class="wrap">
      <div class="split split--even">
        <div data-reveal>
          <div class="breathe" aria-hidden="true">
            <span class="breathe__ring"></span>
            <span class="breathe__orb"></span>
            <span class="breathe__label">Breathe with it</span>
          </div>
        </div>
        <div data-reveal style="--d:140ms">
          <p class="eyebrow">What it looks like</p>
          <h2 class="h-md" style="margin-bottom:1.4rem">Small practices, used where it's hard.</h2>
          <p>
            Sitting quietly in a calm room is the easy part. The work is being able to find
            your feet in traffic, in a difficult conversation, in the middle of a night when
            your brain won't switch off.
          </p>
          <p>
            Mindfulness coaching draws on the same training that informs my therapy work,
            but it's skills-led rather than history-led: we pick the practices that suit
            how your mind actually behaves, and then we make them stick.
          </p>
        </div>
      </div>
    </div>
  </section>
""" + soon("Full details coming soon",
           "Grae is putting the finishing touches to the mindfulness coaching programme "
           "&mdash; formats, session lengths and pricing will be published here shortly.")
    + CTA_BAND)

# ------------------------------------------------------- Parenting Guidance
PAGES["parenting-guidance.html"] = dict(
    title="Parenting Guidance | Work in Progress Wellness, Portland OR",
    desc="Parenting guidance and support with Grae Rose at Work in Progress Wellness, Portland, Oregon. Coming soon — call 971.415.0024 to register your interest.",
    body=phero("Parenting guidance", "Parenting guidance.",
               "A hard job, done mostly without feedback, usually while exhausted. "
               "Having a thoughtful second opinion in your corner is not a sign that "
               "anything has gone wrong.")
    + soon("Coming soon",
           "This service is still being shaped. If parenting support is what brought you "
           "here, say so when you get in touch &mdash; it genuinely helps Grae work out what "
           "to build first.")
    + CTA_BAND)

# ----------------------------------------------------------------- Retreats
PAGES["retreats.html"] = dict(
    title="Personal & Group Retreats | Work in Progress Wellness, Portland OR",
    desc="Personal and small-group wellness retreats with Work in Progress Wellness, Portland, Oregon. Coming soon — call 971.415.0024 to join the interest list.",
    body=phero("Retreats", "Personal and group retreats.",
               "Time away from the noise &mdash; space to reset, reflect and come back to "
               "yourself, on your own or in a small group.")
    + """
  <section class="band" style="min-height:clamp(320px,44vw,520px)">
    <img src="assets/img/calm-lake.jpg" alt="Still water at dawn with mist over the far shore" loading="lazy" width="1920" height="1280">
    <div>
      <p class="eyebrow" data-reveal>The idea</p>
      <h2 class="h-lg" data-reveal style="--d:120ms">Somewhere quiet enough to hear yourself think.</h2>
    </div>
  </section>
"""
    + soon("Dates and details coming soon",
           "Retreat formats, locations and dates are being finalised. Register your interest "
           "now and you'll be first to hear when the first dates open.")
    + CTA_BAND)

# ------------------------------------------------------------- Testimonials
PAGES["testimonials.html"] = dict(
    title="Testimonials | Work in Progress Wellness, Portland OR",
    desc="What clients say about working with Grae Rose at Work in Progress Wellness, Portland, Oregon.",
    body=phero("Testimonials", "In their words.",
               "Therapy is private work. Anything shared here is shared anonymously, "
               "voluntarily, and only with permission.")
    + soon("Gathering these now",
           "Grae is in the middle of asking clients whether they'd like to contribute a few "
           "words. Rather than fill this page with invented quotes, it's staying honest and "
           "empty until there are real ones to put here.",
           "Been helped by the work and want to say so? Mention it next time you speak, or "
           f"call / text <a class=\"tlink\" href=\"tel:{TEL_HREF}\">{TEL}</a>. Entirely optional, "
           "and never expected.")
    + CTA_BAND)

# Reference markup for when real testimonials arrive — kept out of the live page
# on purpose. Drop this block in place of the `soon(...)` call above and fill in
# the quotes. Oregon licensing and the ACA code restrict SOLICITING testimonials
# from current clients, so only publish unsolicited, anonymised, written-consent
# quotes.
TESTIMONIAL_MARKUP_WHEN_READY = """
  <section class="section">
    <div class="wrap">
      <div class="tgrid">
        <blockquote class="tcard" data-reveal>
          <q>Real client quote here.</q>
          <footer>Client initials &middot; Year</footer>
        </blockquote>
      </div>
    </div>
  </section>
"""

# ------------------------------------------------------------------ Contact
PAGES["contact.html"] = dict(
    title="Contact | Work in Progress Wellness, Portland OR | 971.415.0024",
    desc="Call or text 971.415.0024, or send a message to book a free 15-minute consultation with Grae Rose at Work in Progress Wellness in Portland, Oregon.",
    jsonld="""{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "mainEntity": {
    "@type": "ProfessionalService",
    "name": "Work in Progress Wellness",
    "telephone": "+1-971-415-0024",
    "email": "%s",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "11740 SW 68th Parkway, Suite 200",
      "addressLocality": "Portland",
      "addressRegion": "OR",
      "postalCode": "97223",
      "addressCountry": "US"
    }
  }
}""" % EMAIL,
    body=phero("Contact", "For questions, or a free 15&#8209;minute consultation.",
               "The quickest way to reach me is a call or a text. I like to speak with "
               "people before anything is booked &mdash; it's the best way for both of us to "
               "tell whether we're a good fit.")
    + f"""
  <section class="section">
    <div class="wrap">
      <div class="split split--even">
        <div data-reveal>
          <dl class="contact-rows" style="margin:0">
            <div class="crow">
              <dt>Call or text</dt>
              <dd><a class="big" href="tel:{TEL_HREF}">{TEL}</a></dd>
            </div>
            <div class="crow">
              <dt>Email</dt>
              <dd><a class="big big--email" href="mailto:{EMAIL}">{EMAIL}</a></dd>
            </div>
            <div class="crow">
              <dt>Office</dt>
              <dd>
                <span class="big" style="font-size:clamp(1.0625rem,1rem + .45vw,1.25rem)">
                  Mindful Therapy Group<br>
                  11740 SW 68th Parkway, Suite 200<br>
                  Portland, OR 97223
                </span>
              </dd>
            </div>
            <div class="crow">
              <dt>Telehealth</dt>
              <dd><p style="margin:0">Available anywhere in Oregon.</p></dd>
            </div>
          </dl>

          <div class="callout" style="margin-top:2.5rem">
            <h3 class="h-sm">Please note</h3>
            <p style="margin:0">
              This practice does not offer online self-booking. Every new client starts with a
              short conversation first &mdash; that way we can both be sure the fit is right
              before any appointment is made.
            </p>
          </div>
        </div>

        <div data-reveal style="--d:140ms">
          <h2 class="h-md" style="margin-bottom:1.6rem">Send a message</h2>
          <form class="form" data-mailto-form="{EMAIL}" novalidate>
            <div class="field--row">
              <div class="field">
                <label for="f-name">Your name</label>
                <input id="f-name" name="name" type="text" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="f-phone">Phone</label>
                <input id="f-phone" name="phone" type="tel" autocomplete="tel">
              </div>
            </div>

            <div class="field">
              <label for="f-email">Email</label>
              <input id="f-email" name="email" type="email" autocomplete="email" required>
            </div>

            <div class="field--row">
              <div class="field">
                <label for="f-pref">Best way to reach you</label>
                <select id="f-pref" name="contact_pref">
                  <option>Phone call</option>
                  <option>Text message</option>
                  <option>Email</option>
                </select>
              </div>
              <div class="field">
                <label for="f-topic">I'm interested in</label>
                <select id="f-topic" name="topic">
                  <option>Individual therapy</option>
                  <option>Mindfulness coaching</option>
                  <option>Parenting guidance</option>
                  <option>Retreats</option>
                  <option>Something else</option>
                </select>
              </div>
            </div>

            <div class="field">
              <label for="f-msg">What would you like me to know?</label>
              <textarea id="f-msg" name="message" rows="5"></textarea>
            </div>

            <div class="hp" aria-hidden="true">
              <label>Leave this empty<input type="text" name="company" tabindex="-1" autocomplete="off"></label>
            </div>

            <div>
              <button class="btn" type="submit">Send message <span class="arw">&rarr;</span></button>
            </div>

            <p class="note" data-form-status role="status">
              Please don't include sensitive clinical details in this form &mdash; it isn't a
              secure or HIPAA-compliant channel. A name and the best way to reach you is plenty.
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="background:var(--paper-2); border-top:1px solid var(--paper-3)">
    <div class="wrap wrap--narrow" style="text-align:center">
      <p class="eyebrow eyebrow--center" data-reveal>In a crisis?</p>
      <p class="lede" data-reveal style="--d:100ms; margin-inline:auto">
        This website is not monitored for emergencies. If you are in crisis or thinking about
        harming yourself, call or text <strong style="color:var(--ink)">988</strong> (Suicide &amp;
        Crisis Lifeline), or dial <strong style="color:var(--ink)">911</strong>.
      </p>
    </div>
  </section>
""")


def build():
    SITE.mkdir(parents=True, exist_ok=True)
    for slug, p in PAGES.items():
        html = head(slug, p["title"], p["desc"], p.get("jsonld", "")) + p["body"] + FOOTER
        (SITE / slug).write_text(html, encoding="utf-8")
        print("wrote", slug, len(html) // 1024, "KB")

    # sitemap
    urls = "".join(
        f"  <url><loc>{DOMAIN}/{'' if s == 'index.html' else s}</loc>"
        f"<changefreq>monthly</changefreq>"
        f"<priority>{'1.0' if s == 'index.html' else '0.8'}</priority></url>\n"
        for s, _ in NAV)
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls + "</urlset>\n", encoding="utf-8")
    (SITE / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    print("wrote sitemap.xml, robots.txt")


if __name__ == "__main__":
    build()
