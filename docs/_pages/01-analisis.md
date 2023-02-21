---
title: Fase de análisis
author: Juferoga
date: 2023-02-01
category: Jekyll
layout: post
---

Una de las etapas fundamentales y más importante para el desarrollo de software. Es la etapa en la cual se analiza el proyecto, es en la cual podemos obtener los fundamentos en los que se basara el proyecto que se cree.

## Problemáticas empresariales
--- 

- Una empresa de venta directa necesita un sistema de software que permita la gestión de pedidos, el registro de representantes y clientes, y la generación de informes de ventas.
- Una empresa de venta por catálogo necesita un sistema que le permita gestionar el inventario de productos, la colocación de pedidos, el seguimiento de entregas y el pago de comisiones a sus vendedores.
- Una empresa de marketing multinivel necesita una plataforma que facilite la gestión de ventas, el seguimiento de los clientes, la formación de equipos de vendedores y el cálculo de comisiones.
- Una empresa de venta de productos por internet necesita un sistema que permita la gestión de pedidos, el seguimiento de entregas y el pago de comisiones a sus vendedores.
- Una empresa que se dedica a la venta de productos en ferias y eventos necesita un software que facilite la gestión de ventas, el control de inventario y la asignación de comisiones a sus vendedores.
- Una empresa que se dedica a la venta de productos en tiendas departamentales necesita un sistema que facilite la gestión de inventarios, el seguimiento de ventas y la asignación de comisiones a sus vendedores.
- Una empresa que ofrece servicios de consultoría necesita un software que permita la gestión de proyectos, la asignación de tareas y la facturación de servicios.

## Situación problema
--- 

La empresa de ventas multinivel "NatAmE" necesita un sistema de software para gestionar su operación básica. La empresa tiene presencia en diferentes países y dentro de ellos en varias regiones. Cada región maneja su propio inventario de productos organizados en categorías y subcategorías. Las ventas son realizadas por representantes de ventas adscritos a una regional particular. Los clientes pueden convertirse en representantes de ventas y cada venta que se hace se acumula al valor vendido del representante que lo introdujo. Los representantes de ventas se clasifican en cuatro categorías con distintas comisiones de ventas, según el valor vendido y el promedio de calificaciones recibidas en un periodo. El sistema debe permitir registrar representantes y clientes, gestionar pedidos, contabilizar el valor vendido y calificar al representante de ventas con cada pedido, clasificar periódicamente a los representantes, calcular las comisiones de ventas, permitir el cambio de representante por parte del cliente y generar estadísticas por periodo.

## Definición de objetivos
--- 

Draft

## Requerimientos funcionales y no funcionales
--- 

### Requerimientos Funcionales:

- Registrar representantes de ventas.
- Registrar clientes.
- Gestionar pedidos: adicionar o quitar productos, pagar el pedido, cancelar el pedido.
- Calificar representante de ventas con cada pedido.
- Clasificar periódicamente los representantes de ventas.
- Calcular comisiones de ventas para cada representante.
- Permitir el cambio de representante de ventas por parte del cliente.
- Generar estadísticas por periodo: top n de representantes, regionales con más ventas, producto más vendido.

### Requerimientos No Funcionales:

- **Escalabilidad:** capacidad de manejar el crecimiento de la empresa y el número de usuarios del sistema.
- **Seguridad:** garantizar la confidencialidad de la información de los usuarios y el acceso seguro al sistema.
- **Usabilidad:** facilidad de uso del sistema tanto para representantes de ventas como para clientes.
- **Disponibilidad:** garantizar que el sistema esté disponible en todo momento para los usuarios.
- **Performance:** capacidad de procesamiento y respuesta rápida en la gestión de las operaciones del sistema.

## Definición de actores y privilegios por actor
--- 

En el sistema descrito en el problema previo, los siguientes actores estarían involucrados con diferentes privilegios:

- **Administrador del sistema:** tendría acceso a todas las funcionalidades del sistema, incluyendo la creación de cuentas de usuario y la configuración del sistema.
- **Vendedor:** tendría acceso a las funcionalidades de gestión de ventas y clientes, incluyendo el registro de nuevos clientes, la gestión de pedidos y la calificación de los representantes de ventas.
- **Representante de ventas:** tendría acceso a las mismas funcionalidades que un vendedor, pero además tendría la capacidad de registrar nuevos representantes de ventas y asignar clientes a otros representantes.
- **Cliente:** tendría acceso a las funcionalidades de registro de cuenta, gestión de pedidos y calificación de representantes de ventas.