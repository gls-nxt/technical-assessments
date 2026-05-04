package com.gls.tracking

import org.springframework.boot.context.properties.ConfigurationProperties

@ConfigurationProperties(prefix = "upstream")
data class UpstreamProperties(
    val websocketUrl: String,
    val shipmentApiBaseUrl: String
)
