package com.gls.tracking

data class ShipmentMetadataResponse(
    val shipmentId: String,
    val recipientCountry: String,
    val createdAt: String,
    val promisedDeliveryDate: String
)

data class TrackingEventMessage(
    val eventId: String,
    val shipmentId: String,
    val status: String,
    val timestamp: String,
    val hubCode: String
)
