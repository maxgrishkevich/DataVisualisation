import matplotlib.pyplot as plt
import numpy as np


# 1. Протягом наступних 10 років прогнозується зменшення кількості навчальних закладів
years = np.arange(2024, 2034)
initial_schools = 1000
decrease_per_year = 0.02

number_of_schools = [initial_schools * (1 - decrease_per_year) ** (year - years[0]) for year in years]

plt.figure(figsize=(10, 6))
plt.plot(years, number_of_schools, marker='o', linestyle='-', color='blue')
plt.title('Прогноз зменшення кількості навчальних закладів на наступні 10 років')
plt.xlabel('Рік')
plt.ylabel('Кількість навчальних закладів')
plt.grid(True)
plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()


# 2. Більшість співробітників отримує зарплату від 10 до 15 тис. гривень
np.random.seed(42)
salaries = np.concatenate((
    np.random.uniform(10, 15, 700),
    np.random.uniform(5, 10, 200),
    np.random.uniform(15, 20, 100)
))

plt.figure(figsize=(10, 6))
plt.hist(salaries, bins=15, color='skyblue', edgecolor='black')
plt.title('Розподіл зарплат серед співробітників')
plt.xlabel('Зарплата (тис. гривень)')
plt.ylabel('Кількість співробітників')
plt.axvline(salaries.mean(), color='red', linestyle='dashed', linewidth=1)
plt.text(salaries.mean()*1.03, plt.ylim()[1]*0.9, f'Середнє: {salaries.mean():.2f} тис. грн', color='red')

plt.tight_layout()
plt.show()


# 3. Підвищення ціни на окремі сорти бензину не означає підвищення їх якості
time_periods = ['Сьогодні', 'Через місяць', 'Через 6 місяців', 'Через рік']
prices_regular = [2.5, 2.8, 3.2, 3.6]  # Ціни на звичайний бензин у доларах за галон
prices_premium = [3, 3.2, 3.5, 3.8]    # Ціни на преміум бензин у доларах за галон
qualities_regular = [4, 4.1, 4.2, 4.4]  # Якість звичайного бензину (від 1 до 5)
qualities_premium = [4.5, 4.5, 4.5, 4.5] # Якість преміум бензину (від 1 до 5)

plt.figure(figsize=(10, 6))
plt.plot(time_periods, prices_regular, marker='o', linestyle='-', color='blue', label='Ціна (звичайний)')
plt.plot(time_periods, prices_premium, marker='s', linestyle='-', color='green', label='Ціна (преміум)')
plt.plot(time_periods, qualities_regular, marker='o', linestyle='--', color='red', label='Якість (звичайний)')
plt.plot(time_periods, qualities_premium, marker='s', linestyle='--', color='orange', label='Якість (преміум)')
plt.title('Зміна ціни та якості бензину з плином часу')
plt.xlabel('Часовий період')
plt.ylabel('Ціна / Оцінка якості')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

# 4. У вересні рівень плинності кадрів по 6 підрозділам був приблизно однаковий
departments = ['Підрозділ 1', 'Підрозділ 2', 'Підрозділ 3', 'Підрозділ 4', 'Підрозділ 5', 'Підрозділ 6']
fluency_levels = [80, 85, 82, 83, 81, 84]

plt.figure(figsize=(10, 6))
plt.barh(departments, fluency_levels, color='skyblue')
plt.title('Рівень плинності кадрів у вересні за підрозділами')
plt.xlabel('Рівень плинності')
plt.ylabel('Підрозділ')
plt.xlim(75, 90)
plt.grid(axis='x')

plt.show()


# 5. Продавець магазину проводить з клієнтами лише 15% свого часу
labels = ['З клієнтами', 'На касі', 'Організація товару', 'Інші обов’язки']
sizes = [15, 30, 25, 30]

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon'])
plt.title('Розподіл часу продавця магазину')
plt.axis('equal')

plt.show()


# 6. Розмір надбавки до зарплати не залежить від трудового стажу
np.random.seed(42)
trud_stazh = np.random.randint(0, 40, 100)
nadbavka = np.random.normal(200, 50, 100)

avg_nadbavka = []
unique_trud_stazh = np.unique(trud_stazh)
for stazh in unique_trud_stazh:
    avg = np.mean(nadbavka[trud_stazh == stazh])
    if not np.isnan(avg):
        avg_nadbavka.append(avg)
    else:
        avg_nadbavka.append(0)

plt.figure(figsize=(10, 6))
plt.plot(unique_trud_stazh, avg_nadbavka, marker='o', linestyle='-', color='skyblue')
plt.title('Залежність розміру надбавки до зарплати від трудового стажу')
plt.xlabel('Трудовий стаж (роки)')
plt.ylabel('Середній розмір надбавки (грн)')
plt.grid(True)
plt.tight_layout()

plt.show()


# 7. Торік найбільша плинність кадрів спостерігалася у віковій групі від 30 до 35 років
age_groups = ['20-25', '25-30', '30-35', '35-40', '40-45']
turnover_rates = [15, 20, 25, 22, 18]

plt.figure(figsize=(10, 6))
plt.bar(age_groups, turnover_rates, color='skyblue')
plt.title('Рівень плинності кадрів у різних вікових групах')
plt.xlabel('Вікова група')
plt.ylabel('Рівень плинності кадрів (%)')
plt.grid(axis='y')
plt.tight_layout()

plt.show()


# 8. Центральний регіон займає останнє місце з народжуваності
regions = ['Західний', 'Східний', 'Північний', 'Південний', 'Центральний']
birth_rates = [12, 14, 11, 13, 9]

plt.figure(figsize=(10, 6))
plt.barh(regions, birth_rates, color='skyblue')
plt.title('Рівень народжуваності у різних регіонах')
plt.xlabel('Рівень народжуваності (на 1000 осіб)')
plt.ylabel('Регіон')
plt.grid(axis='x')
plt.tight_layout()

plt.show()


# 9. Прибутковість акцій нашої компанії скорочується
periods = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024']
profitability = [100, 98, 90, 85, 70, 69]

plt.figure(figsize=(10, 6))
plt.plot(periods, profitability, marker='o', linestyle='-', color='skyblue')
plt.title('Зміна прибутковості акцій компанії в часі')
plt.xlabel('Період часу')
plt.ylabel('Прибутковість акцій')
plt.grid(True)
plt.tight_layout()

plt.show()


# 10. Найбільша частка фондів задіяна у виробництві
sectors = ['Виробництво', 'Торгівля', 'Сфера послуг', 'Фінанси', 'Інші']
fund_share = [40, 25, 20, 10, 5]

plt.figure(figsize=(8, 8))
plt.pie(fund_share, labels=sectors, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightgray'])
plt.title('Розподіл частки фондів між різними секторами')
plt.axis('equal')

plt.show()


# 11. Спостерігається звʼязок між доходами і зарплатою
incomes = [30000, 35000, 50000, 40000, 55000, 70000]
salaries = [20000, 25000, 30000, 28000, 37000, 40000]

plt.figure(figsize=(8, 6))
plt.scatter(incomes, salaries, color='skyblue')
plt.title('Звʼязок між доходами та зарплатою')
plt.xlabel('Дохід')
plt.ylabel('Зарплата')
plt.grid(True)
plt.tight_layout()

plt.show()


# 12. У серпні 2 студента обігнали за успішність шість інших
students = ['Студент 1', 'Студент 2', 'Студент 3', 'Студент 4', 'Студент 5', 'Студент 6', 'Студент 7', 'Студент 8']
grades = [95, 90, 85, 80, 75, 70, 65, 60]

plt.figure(figsize=(10, 6))
plt.bar(students, grades, color='skyblue')
plt.title('Успішність студентів у серпні')
plt.xlabel('Студенти')
plt.ylabel('Успішність (%)')
plt.grid(axis='y')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()