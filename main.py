import sqlite3
# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("autosalon.sqlite")
cursor = con.cursor()
cursor.execute('''
SELECT DISTINCT idBuyer, buyerFio FROM Buyer
JOIN Request USING (idBuyer)
WHERE idType = 1 ORDER BY idBuyer
''')

print(cursor.fetchall())
cursor.execute('''
SELECT idProduct, modelName, engineVolume FROM Product
JOIN TechnicalData USING (idBodyType)
WHERE engineVolume < 1.3 ORDER BY idProduct DESC
''')

print(cursor.fetchall())
cursor.execute('''
SELECT  COUNT (idRequest), managerFio FROM Manager
JOIN Request USING (idManager)
GROUP BY idManager
''')

print(cursor.fetchall())
cursor.execute('''
SELECT  COUNT (idRequest), date FROM Request
GROUP BY date
''')

print(cursor.fetchall())
cursor.execute('''
SELECT  idManager, managerFio, baseRate FROM Manager
WHERE baseRate > (SELECT AVG(baseRate) FROM Manager)
''')
print(cursor.fetchall())

cursor.execute('''
SELECT  modelName, engineVolume FROM Product
JOIN TechnicalData USING (idBodyType)
WHERE engineVolume > (SELECT MIN(engineVolume) FROM TechnicalData)
''')
print(cursor.fetchall())

cursor.execute('''
UPDATE Manager
SET baseRate = baseRate + 5000
WHERE CountOfDeals > 3;
''')
print(cursor.fetchall())

# cursor.execute('''
# SELECT * FROM Product
# ''')
# print(cursor.fetchall())

cursor.execute('''
DELETE FROM Product
WHERE avaliability = 0
''')
print(cursor.fetchall())

# cursor.execute('''
# SELECT * FROM Product
# ''')
print(cursor.fetchall())
con.close()