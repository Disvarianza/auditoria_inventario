-- Productos con precio superior al promedio
SELECT * FROM inventario WHERE precio > (SELECT AVG(precio) FROM inventario);

-- Productos con cantidad en cero
SELECT * FROM inventario WHERE cantidad = 0;

-- Categorías con más productos
SELECT categoria, COUNT(*) as total FROM inventario GROUP BY categoria ORDER BY total DESC;