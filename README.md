# Repetika

A monorepo for a learning platform employing spaced repetition to make learning fun and effective.

## Highlights

* Multi-service backend (authentication, courses, decks, planning, sessions, quiz, main gateway)
* React Native app built with Expo for web and mobile
* Local orchestration with Docker Compose and an NGINX dev proxy
* Continuous Integration with GitHub Actions, including testing and static analysis

## Getting started

### Prerequisites

* Docker Desktop (or Docker Engine) installed
* Node.js LTS and npm installed
* If testing on a mobile device, install the **Expo Go** app (App Store / Google Play)

### 0) Configure environment

Create a `.env` file at the repository root with the following variables (setting the values as needed). Replace `SECRET_KEY` and `POSTGRES_PASSWORD` with secure values for use in production.

```
MONGO_DB=repetika
MONGO_URL=mongodb://mongodb:27017/repetika
MONGO_URI=mongodb://mongodb:27017/
SECRET_KEY=placeholder_secret_key
POSTGRES_DB=authdb
POSTGRES_USER=authuser
POSTGRES_PASSWORD=authpass
```

Docker Compose reads this file automatically when you run the stack.

### 1) Start the backend stack

```bash
git clone https://github.com/Romain-Ryckebusch/Repetika.git
cd Repetika

docker compose up --build -d
```

### 2) Launch the app (Expo)

```bash
cd apps/mobile/RepetikaApp

npm install

npx expo install # Press 'Y' when prompted to install ngrok

npx expo start --tunnel
```

### 3) Use the app

* **Web preview**: open the URL printed by the Expo CLI (or press `w` in the terminal).
* **Mobile**: open **Expo Go** on your phone and scan the QR code shown by the CLI.

### 4) Stop services

```bash
# from the repository root
docker compose down
```

## Troubleshooting

* **Expo tunnel issues**: if the tunnel is unstable on your network, try `npx expo start` and select **LAN** as the connection type, or restart the Expo server.
* **Ports in use**: stop stale containers or processes that bind the same ports, then re-run `docker compose up --build -d`.
* **Cold start**: the first `compose up` includes image builds and may take several minutes depending on your machine.

## Why this repo may interest you

* Demonstrates a modular service architecture packaged for fast local onboarding.
* Shows a single codebase running both a mobile app and a web preview through Expo.
* Uses Docker to keep developer machines clean and environments reproducible.

## License

See `LICENSE` in the repository root.
