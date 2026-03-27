package com.gls.tracking

import org.slf4j.LoggerFactory
import org.springframework.stereotype.Component
import org.springframework.web.reactive.function.client.WebClient
import reactor.core.publisher.Mono

@Component
class ShipmentApiClient(
    properties: UpstreamProperties,
    builder: WebClient.Builder
) {
    private val log = LoggerFactory.getLogger(javaClass)

    private val webClient: WebClient = builder
        .baseUrl(properties.shipmentApiBaseUrl)
        .build()

    fun getShipment(shipmentId: String): Mono<ShipmentMetadataResponse> {
        log.info("Fetching shipment metadata for {}", shipmentId)
        return webClient.get()
            .uri("/external/shipments/{shipmentId}", shipmentId)
            .retrieve()
            .bodyToMono(ShipmentMetadataResponse::class.java)
    }
}