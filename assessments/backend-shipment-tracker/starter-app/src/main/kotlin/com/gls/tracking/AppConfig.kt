package com.gls.tracking

import org.springframework.boot.context.properties.EnableConfigurationProperties
import org.springframework.context.annotation.Configuration

@Configuration
@EnableConfigurationProperties(UpstreamProperties::class)
class AppConfig
