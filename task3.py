class Tomato:

    # Стадии созревания томата
    states = {0: 'росток', 1: 'зелёный помидор', 2: 'красный помидор'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход следующую стадию созревания
    def grow(self):
        if self._state < 2:
            self._state += 1


    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Работа садовника
    def work(self):
        self._plant.grow_all()
        print('Садовник работает')

    # Собираем урожай
    def harvest(self):
        print('Садовник проверяет, все ли плоды созрели')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Садовник собрал урожай')
        else:
            print('Помидоры ещё не созрели')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''отрасль растениеводства, занимающаяся возделыванием многолетних плодовых или 
        ягодных культур для получения фруктов, ягод и орехов (плодоводство); и выращиванием декоративных
        растений (декоративное садоводство). Садоводство может быть очень специализированным,
        с выращиванием только одного вида растений или с участием множества растений в смешанных посадках.
        Оно предполагает активное участие в выращивании растений и, как правило, является трудоёмким, что 
        отличает его от сельского или лесного хозяйства.''')

if __name__ == '__main__':
    Gardener.knowledge_base()
    first_tomato_bush = TomatoBush(4)
    gardener = Gardener('Григорий', first_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()


