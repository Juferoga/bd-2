---
title: Sobre el proyecto
author: Juferoga
date: 2023-01-31
category: Jekyll
layout: post
---

# CASO DE ESTUDIO: VENTAS MULTINIVEL1
## Objetivo
Implementar una aplicación, preferiblemente con una interfaz web, soportada en una base de datos relacional, que permita gestionar los requerimientos funcionales y no funcionales de una empresa de ventas multinivel.

## Descripción del problema

Basándonos en las necesidades de la empresa NatAmE, podemos esquematizar una base de datos con las siguientes tablas (Ideas):

- **Tabla de Representantes de ventas:** incluirá campos como ID, nombre, identificación, correo electrónico, género, fecha de nacimiento, fecha de contrato, teléfono de contacto, dirección, regional a la cual está inscrito y el ID del representante que lo introdujo.
- **Tabla de Clientes:** incluirá campos como ID, nombre, identificación, dirección, ciudad, teléfono, correo electrónico y el ID del representante que lo captó.
- **Tabla de Productos:** incluirá campos como ID, nombre, descripción, categoría y subcategoría.
- **Tabla de Pedidos:** incluirá campos como ID, fecha, cliente, representante de ventas, estado del pedido, total y método de pago.
- **Tabla de Detalles de Pedido:** incluirá campos como ID del pedido, producto, cantidad y precio unitario.
- **Tabla de Calificaciones:** incluirá campos como ID del representante de ventas, ID del cliente, calificación y comentario.
- **Tabla de Clasificación de Representantes de ventas:** incluirá campos como ID del representante de ventas, valor vendido, promedio de calificaciones, categoría y comisión.
- **Tabla de Cambios de Representante de ventas:** incluirá campos como ID del cliente, ID del representante de ventas anterior, ID del representante de ventas nuevo y fecha.

Con estas tablas, se pueden realizar consultas y generar informes que permitan a la empresa NatAmE realizar un seguimiento efectivo de su operación básica, como por ejemplo:

- Consultar la información de un representante de ventas, incluyendo su valor vendido y su categoría actual.
- Consultar el historial de pedidos de un cliente, así como las calificaciones y comentarios asociados a cada pedido.
- Generar informes de las ventas por regional, categoría de producto y subcategoría de producto.
- Generar informes de los representantes de ventas con mayor valor vendido y mayor promedio de calificaciones.
- Calcular el valor de las comisiones de ventas de cada representante y generar los reportes correspondientes.