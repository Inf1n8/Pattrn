## 💡Inspiration
- 2020 US Census survey showed that adults were 3x more likely to screen positive for depression or anxiety in 2020 vs 2019
- A 2019 review of 18 papers summarized that wearable data could help identify depression, and coupled with behavioral therapy can help improve mental health
- 1 in 5 americans owns wearables now, and this adoption is projected to grow 18% every year
- Pattrn aims to turning activity and mood data into actionable insights for better mental health.

## 🤔 What it does
- Digests activity monitor data and produces bullet point actionable summary on health status
- Allows users to set goals on health metrics, and provide daily, weekly, month review against goals
- Based on user mood rating and memo entry, deduce activities that correlates with good and bad days
[Screen-Shot-2022-10-16-at-1-09-40-PM.jpg](https://postimg.cc/bd9JvX3V)

## 🦾 How we built it
- Frontend: ReactJS
- Backend: Flask, Google Cloud App Engine, Intersystems FHIR, Cockroach Labs DB, Cohere

## 👨🏻‍🤝‍👨🏽 Challenges / Accomplishments 
- Ideating and validating took up a big chunk of this 24 hour hack
- Continuous integration and deployment, and Github collaboration for 4 developers in this short hack
- Each team member pushing ourselves to try something we have never tried before

## 🛠 Hack for Health
- Pattrn currently is able to summarize actionable steps for users to take towards a healthy lifestyle
- Apart from health goal setting and reviewing, pattrn also analyses what activities have historically correlated with "good" and "bad" days

## 🛠 Intersystems Tech Prize
- We paginated a GET and POST request
- Generated synthetic data and pushed it in 2 different time resolution (Date, Minutes)
- Endpoints used: Patient, Observation, Goals, Allergy Intolerance
- Optimized API calls in pushing payloads through bundle request

## 🛠 Cockroach Labs Tech Prize
- Spawned a serverless Cockroach Lab instance
- Saved user credentials
- Stored key mapping for FHIR user base
- Stored sentiment data from user daily text input  

## 🛠 Most Creative Use of GitHub
- Implemented CICD, protected master branch, pull request checks
- Version control, package build
- Deployed using Netlify

## 🛠 Cohere Prize
- Used sentiment analysis toolkit to parse user text input, model human languages and classify sentiments with timestamp related to user text input
- Framework designed to implement a continuous learning pipeline for the future

## 🛠 Google Cloud Prize
- App Engine to host the React app and Flask observer and linked to Compute Engine
- Hosted Cockroach Lab virtual machine

## What's next for Pattrn
- Continue working on improving sentiment analysis on user’s health journal entry
- Better understand pattern between user health metrics and daily activities and events
- Provide personalized recommendations on steps to improve mental health
- Provide real time feedback eg. haptic when stressful episode are predicted
