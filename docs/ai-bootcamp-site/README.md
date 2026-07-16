# AI Project & Competition Starter Hub

This folder contains a static prototype for the student self-learning website.

Open this file in a browser:

```text
index.html
```

## Purpose

The website is organized as a two-track starter hub:

```text
Track A: Project Track
Build a real AI application based on an education-management demo scenario.

Track B: Competition Skill Track
Build the Python, data, ML, LLM, and competition skills students need next.
```

The project track follows this learning flow:

```text
Real School Operation
-> Data Collection
-> Structured Database
-> Python Analysis
-> AI Summary
-> Student Learning Profile
-> Human Review
```

## API Decision

The first version uses mock API files, not the real CSAA system API.

This lets students learn API concepts safely:

- endpoint
- request
- response
- JSON
- status
- error handling

No production data is exposed.
No admin API is exposed.
No real student privacy data is used.

## Included Demo Data

```text
data/students.csv
data/attendance.csv
data/teacher_comments.csv
```

## Included Mock API Responses

```text
mock-api/search-student-emma.json
mock-api/sign-in-emma.json
mock-api/sign-out-emma.json
mock-api/attendance-summary.json
```

## Included Templates

```text
templates/attendance_analysis_starter.py
templates/openai_comment_summary_prompt.md
```

## Website vs Dashboard

Website:

- The full learning and project guide
- Weekly lessons
- Templates
- Checklists
- Final project instructions

Dashboard:

- One final student project output
- Displays Student Learning Profile
- Shows attendance analysis
- Shows AI comment summary
- Shows next-step suggestions

## Current Features

- Project Track and Skill Track overview
- Competition skill roadmap
- 4-week learning path
- 12 lesson cards
- Interactive lesson navigation
- Per-lesson checklist
- Local progress saving through browser localStorage
- Final project checklist
- Resources section
- Demo CSV files
- Mock API JSON examples
- Python and prompt starter templates

## Suggested Next Steps

- Move lesson content into content/lessons.json
- Add content/resources.json for competition resources
- Add Python notebook template
- Add Streamlit dashboard template
- Add bilingual lesson pages
- Add instructor guide
- Add final presentation template
