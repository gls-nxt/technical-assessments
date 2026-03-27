# Spring Boot + Kotlin Starter App

See [`PROBLEM.md`](./PROBLEM.md) for the assignment brief.

## Tech stack

- Spring Boot 3.5 + Kotlin 2.1
- Spring WebFlux (WebSocket client, REST client)
- Java 21

## Run

Start the mock upstream first:

```bash
docker compose up --build
```

Then run the app:

```bash
./gradlew bootRun
```

The app starts on port `8080`. The mock upstream runs on `8081`.
