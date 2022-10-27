import sqlite3
import pandas as pd

con = sqlite3.connect("autosalon.sqlite")
cursor = con.cursor()


def q1():  # Запрос 1.  Вывести список клиентов, оставивших заявку на тест драйв.
    # Сортировать по возрастанию id. Сортировать по возрастанию id.
    df = pd.read_sql('''
    SELECT DISTINCT idBuyer, buyerFio FROM Buyer
    JOIN Request USING (idBuyer)
    WHERE idType = 1 ORDER BY idBuyer
    ''', con)
    print(df)
    print()


def q2():  # Запрос 2. Вывести список автомобилей с объёмом двигателя меньше 1.3. Сортировать по убыванию id.
    df = pd.read_sql('''
    SELECT idProduct, modelName, engineVolume FROM Product
    JOIN TechnicalData USING (idBodyType)
    WHERE engineVolume < 1.3 ORDER BY idProduct DESC
    ''', con)
    print(df)
    print()


def q3():  # Запрос 3. Вывести всех менеджеров с количеством закрытых ими заказов. группировать по айди менеджера.
    df = pd.read_sql('''
    SELECT  COUNT (idRequest), managerFio FROM Manager
    JOIN Request USING (idManager)
    GROUP BY idManager
    ''', con)
    print(df)
    print()


def q4():  # Запрос 4. Вывести количество заявок на каждую дату. группиировать по дате.
    df = pd.read_sql('''
    SELECT  COUNT (idRequest), date FROM Request
    GROUP BY date
    ''', con)
    print(df)
    print()


def q5():  # Запрос 5. Вывести список менеджеров, у которых базовая ставка выше средней.
    df = pd.read_sql('''
    SELECT  idManager, managerFio, baseRate FROM Manager
    WHERE baseRate > (SELECT AVG(baseRate) FROM Manager)
    ''', con)
    print(df)
    print()


def q6():  # Запрос 6. Вывести список машин, объём двигателя которых больше минимального.
    df = pd.read_sql('''
    SELECT  modelName, engineVolume FROM Product
    JOIN TechnicalData USING (idBodyType)
    WHERE engineVolume > (SELECT MIN(engineVolume) FROM TechnicalData)
    ''', con)
    print(df)
    print()


def q7():  # Запрос 7. Повысить базовую ставку на 5000 тем менеджерам, которые сделали более 3 продажю
    cursor.execute('''
    UPDATE Manager
    SET baseRate = baseRate + 5000
    WHERE CountOfDeals > 3;
    ''')
    print()


def q8():  # Запрос 8. Удалить авто, которых нет в наличии.
    cursor.execute('''
    DELETE FROM Product
    WHERE avaliability = 0
    ''')
    print()


def get_managers():
    df = pd.read_sql('''
    SELECT idManager, managerFio, baseRate, CountOfDeals FROM Manager
    ''', con)
    print(df)
    print()


def get_products():
    df = pd.read_sql('''SELECT * FROM Product''', con)
    print(df)
    print()


# q1()
# q2()
# q3()
# q4()
# q5()
# q6()
#
# get_managers()
# q7()
# get_managers()

# get_products()
# q8()
# get_products()

con.close()
