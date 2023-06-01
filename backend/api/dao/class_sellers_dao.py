class ClassSellers:
    def __init__(self, connection):
        self.nombre = "QualiificationDao"
        self.connection = connection

    def topSellers(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            select r.k_representante, count(k_pedido) from pedido p
            join cliente c on p.k_cliente = c.k_cliente
            join representante r on c.k_representante = r.k_representante
            group by r.k_representante
            order by count(k_pedido) desc
            """)
            top = []
            for row in cursor:
                k_representante, quantity = row
                top.append({
                    'k_representante': k_representante,
                    'quantity': quantity
                })
            print(top)
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, top]
        
    def monthlySells(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            SELECT TRUNC(PEDIDO.F_CREACION, 'MM') AS PERIODO,
            SUM(PEDI_ITEM.N_CANTIDAD * PEDI_ITEM.N_PRECIOU) AS TOTAL_VENTAS FROM PEDIDO
            INNER JOIN PEDI_ITEM ON PEDIDO.K_PEDIDO = PEDI_ITEM.K_PEDIDO GROUP BY 
            TRUNC(PEDIDO.F_CREACION, 'MM') ORDER BY PERIODO
            """)
            monthly = []
            for row in cursor:
                periodo, total = row
                monthly.append({
                    'periodo': periodo,
                    'total': total
                }) 
            print(monthly)
        except Exception as e:
            return [False, str(e)]
        finally:
            cursor.close()
        return [True, monthly]