

'''
# Функция, которую будем тестировать
def add(a, b):
    return a + b

# Тесты
class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -3), -4)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)

'''


# def f(nums, target):

nums = [1, 6, -1]
target = 5

def two_sum(nums,target):
  # Проверяем является ли список значением класса NoneType
  if nums == None:
    return 'Список является NoneType'
  
  # Проверяем, что список является списком, а его значения - целые числа
  if type(nums) == list:
    if not all(type(x)==int for x in nums):
      return 'В списке присутсвуют не целые числовые значения'
  else:
    return 'На вход подан не список'
  
  # Проверяем, что список не пустой
  if nums == []:
    return 'На вход подан пустой список'
  
  
  
  # Сама функция
  for i in range(len(nums)):
      for j in range(i+1, len(nums)):
          if (nums[i]+nums[j]) == target:
            return [i,j] # возвращаем самые первые найденные индексы
          
print(two_sum(nums, target))