package com.gls.tracking

import jakarta.annotation.PostConstruct
import org.slf4j.LoggerFactory
import org.springframework.stereotype.Component
import org.springframework.web.reactive.socket.client.ReactorNettyWebSocketClient

@Component
class TrackingWebSocketClient(
    private val properties: UpstreamProperties
) {
    private val log = LoggerFactory.getLogger(javaClass)
    private val client = ReactorNettyWebSocketClient()

    @PostConstruct
    fun start() {
        client.execute(java.net.URI.create(properties.websocketUrl)) { session ->
            log.info("Connected to tracking stream at {}", properties.websocketUrl)
            session.receive()
                .map { it.payloadAsText }
                .doOnNext { rawEvent -> log.info("Received event: {}", rawEvent) }
                .then()
        }
            .doOnError { error -> log.error("Tracking stream connection failed", error) }
            .subscribe()
    }
}
