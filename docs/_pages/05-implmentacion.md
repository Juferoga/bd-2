---
title: Fase de implementación
author: Juferoga
date: 2023-02-05
category: Jekyll
layout: post
---

## Arquitectura
--- 

![Infraestructura del proyecto con aws](/fis/assets/images/pages/implementacion/infra_fis.svg "Infraestructura del proyecto con aws")

### Costos de la arquitectura
<div class="table-wrapper" markdown="block">


  | category   | type | region    | count | unitPrice | cost  | instanceType | instanceSize | platform | role       | engine            | dataGb |
  |------------|------|-----------|-------|-----------|-------|--------------|--------------|----------|------------|-------------------|--------|
  | compute    | ec2  | us-east-1 | 1     | 15.18     | 15.18 | t3           | small        | Linux    |            |                   |        |
  | networking | elb  | us-east-1 | 1     | 22.27     | 22.27 |              |              |          |            |                   | 10     |
  | storage    | s3   | us-east-1 | 1     | 3.95      | 3.95  |              |              |          |            |                   | 0.25   |
  | database   | rds  | us-east-1 | 1     | 43.8      | 43.8  | serverless   | serverless   |          | serverless | aurora-postgresql |        |


</div>

![Precios infraestructura del proyecto con aws](/fis/assets/images/pages/implementacion/infra_fis_prices.png "Precios infraestructura del proyecto con aws")

[Tool for diagram for cloud implementation.][1]

## Instalación
--- 

Instalación del sistema.

## Soporte técnico post-instalación
--- 

Errores post-instalación? obvio si 😆.


[1]:https://www.cloudcraft.co/