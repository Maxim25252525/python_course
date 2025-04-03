import pytest

from hw9.tasks import task1, task2, task3


class TestHw9Task1:

    def test_get_info(self):
        human = task1.Human("Иван", "Иванов", "Иванович", "м")
        assert (
            human.get_info()
            == "Фамилия: Иванов\nИмя: Иван\nОтчество: Иванович\nВозраст: 0\n"
            "Пол: м\nВес: 3.3 кг\nРост: 50 см"
        )

    def test_age(self):
        human = task1.Human("Анастасия", "Полякова", "Дмитриевна", "ж")
        human.age = 4
        assert (
            human.get_info()
            == "Фамилия: Полякова\nИмя: Анастасия\nОтчество: Дмитриевна\n"
            "Возраст: 4\nПол: ж\nВес: 3.3 кг\nРост: 50 см"
        )

    def test_weight(self):
        human = task1.Human("Роман", "Кирилов", "Михайлович", "м")
        human.age = 7
        human.weight = 30
        assert (
            human.get_info()
            == "Фамилия: Кирилов\nИмя: Роман\nОтчество: Михайлович\n"
            "Возраст: 7\nПол: м\nВес: 30 кг\nРост: 50 см"
        )

    def test_height(self):
        human = task1.Human("Рада", "Белякова", "Алексеевна", "ж")
        human.age = 16
        human.weight = 53.67
        human.height = 165
        assert (
            human.get_info()
            == "Фамилия: Белякова\nИмя: Рада\nОтчество: Алексеевна\n"
            "Возраст: 16\nПол: ж\nВес: 53.67 кг\nРост: 165 см"
        )


class TestHw9Task2:

    def test_mage(self):
        mage = task2.Mage("Oris")
        assert mage.name == "Oris"
        assert mage.life == 100
        assert mage.damage == 20
        assert mage.energy == 100

    def test_get(self):
        mage = task2.Mage("Viking")
        assert mage.get_name() == "My name is Viking"
        assert mage.get_life() == "Life: 100"
        assert mage.get_damage() == "Damage: 20"
        assert mage.get_energy() == "Energy: 100"

    def test_life(self):
        mage = task2.Mage("Leader")
        mage.reduce_life()
        mage.reduce_life()
        mage.reduce_life()
        mage.increase_life()
        assert mage.life == 60

    def test_life_empty(self):
        with pytest.raises(ValueError) as ex:
            mage = task2.Mage("Kamikaze")
            for _ in range(6):
                mage.reduce_life()
        assert "Показатель жизни на нуле" == str(ex.value)

    def test_damage(self):
        mage = task2.Mage("Mark")
        mage.increase_damage()
        mage.increase_damage()
        mage.increase_damage()
        mage.reduce_damage()
        assert mage.damage == 60

    def test_damage_empty(self):
        with pytest.raises(ValueError) as ex:
            mage = task2.Mage("Kamikaze")
            mage.reduce_damage()
            mage.reduce_damage()
        assert "Показатель урона на нуле" == str(ex.value)

    def test_energy(self):
        mage = task2.Mage("Olov")
        mage.increase_energy()
        mage.reduce_energy()
        assert mage.energy == 70

    def test_damage_energy(self):
        with pytest.raises(ValueError) as ex:
            mage = task2.Mage("Kamikaze")
            mage.increase_energy()
            for _ in range(4):
                mage.reduce_energy()
        assert "Показатель энергии на нуле" == str(ex.value)

    def test_update_attributes(self):
        mage = task2.Mage("Oris")
        mage.increase_energy()
        mage.reduce_life()
        mage.increase_damage()
        for _ in range(3):
            mage.reduce_energy()
        assert mage.name == "Oris"
        assert mage.life == 80
        assert mage.damage == 40
        assert mage.energy == 0

    def test_update_attributes_fire_mage(self):
        mage = task2.FireMage("FireOris")
        mage.increase_energy()
        mage.reduce_life()
        mage.increase_damage()
        for _ in range(3):
            mage.reduce_energy()
        assert mage.name == "FireOris"
        assert mage.life == 80
        assert mage.damage == 40
        assert mage.energy == 0

    def test_apply_ability(self):
        mage = task2.FireMage("FIreViking")
        assert mage.apply_ability() == "FIRE....."
        mage.increase_energy()
        mage.apply_ability()
        assert mage.apply_ability() == "Phhh..."


class TestHw9Task3:

    def test_gun(self):
        gun = task3.Gun()
        assert gun.shoot_count == 0
        assert gun.max_shoot_number == 5

    def test_shoot(self):
        gun = task3.Gun()
        result = [gun.shoot() for _ in range(7)]
        assert result == ["пиу", "пау", "пиу", "пау", "пиу", "чик", "чик"]

    def test_shoot_count(self):
        gun = task3.Gun()
        for _ in range(3):
            gun.shoot()
        assert gun.shoot_count == 3

    def test_reload(self):
        gun = task3.Gun()
        for _ in range(3):
            gun.shoot()
        gun.reload()
        assert gun.shoot_count == 0

    def test_update_magazine_capacity(self):
        gun = task3.Gun()
        gun.update_magazine_capacity(10)
        result = [gun.shoot() for _ in range(11)]
        assert gun.max_shoot_number == 10
        assert result == [
            "пиу",
            "пау",
            "пиу",
            "пау",
            "пиу",
            "пау",
            "пиу",
            "пау",
            "пиу",
            "пау",
            "чик",
        ]
