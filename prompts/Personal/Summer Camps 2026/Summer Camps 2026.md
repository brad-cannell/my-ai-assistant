---
title: Summer Camps 2026
task: planning
audience: personal
interface: browser
author: "Brad Cannell"
created: 2026-03-28
last_updated: 2026-03-28
project: null
domain: personal
tags:
  - personal
  - planning
  - family
  - girls
  - camp
  - activities
  - summer
---

# Overview (optional)
- Planning summer camps 2026
- I think I want help creating a spreadsheet

# SYSTEM PROMPT

None

---

# USER MESSAGE

## Attachments
- Key People.md (included below as context)
- 2026ProgramGuideasof030626.pdf
- TCC Course Catalog.pdf
- XPLORESummeratTVS202616.pdf

<context>
Tracy and I are planning 2026 summer camps for Olivia, Lindsey, and Lauren ("the girls").

We have custody of all three girls during the possession windows listed in <possession_dates> below.
Each window runs from a Friday pickup through the following Friday dropoff (i.e., the end date is
the last full day we have them — they return to their other parent on the morning of the day after).
In general, the girls are with their other parent during weeks not listed. There may be some weeks
that we trade possession with Brooke, George, or both. Some camp start and end dates may fall
outside of our possession windows, and that is okay.
</context>

<possession_dates>
  <window start="2026-05-29" end="2026-06-05"/>
  <window start="2026-06-12" end="2026-06-19"/>
  <window start="2026-06-26" end="2026-07-03"/>
  <window start="2026-07-10" end="2026-07-17"/>
  <window start="2026-07-24" end="2026-07-31"/>
  <window start="2026-08-07" end="2026-08-14"/>
</possession_dates>

<girls>
  See "Key People.md"
</girls>

<preferences>
  Here is a text message the girls sent me with some of their preferences: "ld do Musical Theater Camp (12:30pm-3:30) Together and lauren could do A Week at the Spa (12:30pm-3:30) It’s at TVS. In the morning I could do Young Artists (9am-12pm) and Olivia said in the morning she would like to do Crochet Studio (9am-12pm)

June 29-July 3: Crafted from Nature (9am-12pm) sounds fun in the morning. Olivia wants to do Day in Court: Mock Trial with Epic Edu in partnership with Black Rocket Productions (9am-12pm). Olivia and I want to do Savor the World (12:30pm-3:30pm) has some cooking and eating and it’s at all saints 

July 13-17: Olivia and mwah wants to do Money $mart with Little Scholars, LLC (9am-12pm) could be fun and educational in the morning and Make Your First Video Game with Black Rocket Production (12:30pm-3:30pm) 
If we finish our game early, family can play it too

July 27-31: We think we want to do a TCC camp but our backup is Movement  climbing gymmmmmmmm"
</preferences>

<scheduling_priorities>
  <priority>All three girls should be at the same camp simultaneously whenever possible.</priority>
  <priority>Tracy and I will both be working full-time for most of the summer, with occasional days off. Ideally, every possession week is filled with activities.</priority>
  <priority>Camp Balcones Springs will be the only overnight camp this summer. All other camps will be day camps.</priority>
  <priority>Many camps are half-day. Where possible, pair complementary half-day camps to create full-day coverage on working days.</priority>
  <priority>All camps listed are within budget and geographic range — no need to filter on those criteria.</priority>
</scheduling_priorities>

<camps>

  <camp id="balcones">
    <name>Camp Balcones Springs</name>
    <url>https://campiscool.com/</url>
    <terms>
      <term>
        <term_name>Term 2</term_name>
        <start_date>2026-06-14</start_date>
        <end_date>2026-06-27</end_date>
        <price>$3890</price>
        <note>Olivia and Lindsey are already registered for this term.</note>
      </term>
      <term>
        <term_name>One Week 2A</term_name>
        <start_date>2026-06-14</start_date>
        <end_date>2026-06-21</end_date>
        <price>$2185</price>
        <note>Lauren is already registered for this term.</note>
      </term>
    </terms>
  </camp>

  <camp id="tvs">
    <name>Xplore Summer at TVS</name>
    <url>https://www.tvs.org/quicklinks/xplore-summer-at-tvs</url>
    <note>See attached PDF for session dates, descriptions, and prices.</note>
  </camp>

  <camp id="all_saints">
    <name>Summer You at All Saints</name>
    <url>https://www.summeryou.org/2026-camps</url>
    <note>See attached PDF for session dates, descriptions, and prices.</note>
  </camp>

  <camp id="movement">
    <name>Movement Climbing Gym</name>
    <url>https://app.rockgympro.com/b/widget/?a=offering&offering_guid=16e5ffc527284ca48c9101685674b872&widget_guid=5383ae103084490790c05a841357d9f0&random=69c876f8560bb&iframeid=&mode=p</url>
    <url>https://app.rockgympro.com/b/widget/?a=offering&offering_guid=4a5324efc1b74209a0f49321a122af26&widget_guid=5383ae103084490790c05a841357d9f0&random=69c8772695f9e&iframeid=&mode=p</url>
  </camp>

  <camp id="tcc">
    <name>Tarrant County College</name>
    <url>https://selfservice.tccd.edu/Student/InstantEnrollment/SearchResult</url>
    <note>See attached PDF for course offerings, dates, and prices.</note>
  </camp>

  <camp id="camp_carter">
    <name>YMCA Camp Carter Day Camp</name>
    <url>https://ymcafw.org/camp-carter/traditional/</url>
  </camp>

  <camp id="zoo">
    <name>Fort Worth Zoo Camp</name>
    <url>https://www.fortworthzoo.org/summer-zoo-camp</url>
  </camp>

  <camp id="tcu_tennis">
    <name>TCU Tennis Camp</name>
    <url>https://www.wilsontenniscamps.com/texas-christian-university-tennis-camp-fort-worth/</url>
  </camp>

</camps>

<task>
  <step order="1">
    Create a spreadsheet to help us plan and track summer camps. The spreadsheet should include
    columns for: girl's name, camp name, session/term name, start date, end date, days of week,
    half-day or full-day, price, registration status (registered / considering / not registered),
    and any notes. Pre-populate it with the camps and sessions we have already confirmed
    (Camp Balcones Springs terms listed above), and add rows for each camp and session that
    appears in the attached PDFs or camp list above. Leave registration status as "considering"
    for unconfirmed camps.
  </step>
  <step order="2">
    After creating the spreadsheet, summarize which possession weeks currently have full-day
    coverage for all three girls, which weeks are only partially covered, and which weeks have
    no coverage at all. Flag any scheduling conflicts (e.g., overlapping camps for the same girl).
  </step>
  <step order="3">
    Based on the gaps identified, suggest specific camps from our list that could fill those
    gaps, keeping the scheduling priorities above in mind.
  </step>
</task>