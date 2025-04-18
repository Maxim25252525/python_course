import random
from datetime import datetime

import pytest

from hw14.tasks import task1


@pytest.fixture
def get_card():
    random.seed(1984)
    return task1.Card("Волков Д.А.", "МИР", 1234)


class TestHw14Task1:

    @pytest.mark.parametrize(
        "pin_code",
        [12345, 123, "123A", "hello"],
    )
    def test_init_card_raise(self, pin_code):
        with pytest.raises(ValueError) as ex:
            task1.Card("Иванов И.И.", "МИР", pin_code),
        assert "Ошибка установки пин-кода" == str(ex.value)

    def test_card_attributes(self, get_card):
        assert get_card.__dict__ == {
            "user": "Волков Д.А.",
            "_payment_system": "МИР",
            "_Card__number": 54110951971074007,
            "_validity_period": datetime.now()
            .replace(year=datetime.now().year + 3)
            .date(),
            "_Card__code_cv": 321,
            "_Card__pin_code": 1234,
            "is_blocked": False,
            "_balance": 0,
        }

    def test_get_payment_system(self, get_card):
        assert get_card.get_payment_system() == "МИР"

    def test_get_number(self, get_card):
        assert get_card.get_number() == "***4007"

    def test_get_validity_period(self, get_card):
        assert get_card.get_validity_period() == "04/28"

    def test_get_cv(self):
        assert task1.Card.get_cv() == "***"

    def test_block(self, get_card):
        assert get_card.is_blocked == False  # noqa
        get_card.block()
        assert get_card.is_blocked == True  # noqa

    def test_print(self, get_card):
        assert str(get_card) == "Данная карта принадлежит: Волков Д.А."

    def test_get_info(self):
        assert task1.Card.get_info() == (
            "Правила пользования карточкой:\n"
            "1. Запомнить ПИН-код и нигде его не сохранять.\n"
            "2. Не передавать карту другим людям.\n"
            "3. Подключить push-уведомления или СМС-оповещения.\n"
            "4. Бережно относиться к карточке.\n"
            "5. Если карта потеряна, сразу же связаться с банком.\n"
            "6. Не хранить крупную сумму."
        )

    def test_balance(self, get_card):
        assert get_card.get_balance() == 0
        get_card.put_money(100, 1234)
        assert get_card.get_balance() == 100
        get_card.get_money(19.98, 1234)
        assert get_card.get_balance() == 80.02

    def test_get_money_raise_code_error(self, get_card):
        with pytest.raises(PermissionError) as ex:
            get_card.get_money(123, 4321)
        assert "Неверный пин-код" == str(ex.value)

    def test_get_money_raise_low_balance(self, get_card):
        with pytest.raises(ValueError) as ex:
            get_card.put_money(122, 1234)
            get_card.get_money(123, 1234)
        assert "Недостаточное количество средств" == str(ex.value)

    def test_put_money_raise_code_error(self, get_card):
        with pytest.raises(PermissionError) as ex:
            get_card.put_money(123, 4321)
        assert "Неверный пин-код" == str(ex.value)

    def test_put_money_raise_balance_error(self, get_card):
        with pytest.raises(ValueError) as ex:
            get_card.put_money(-1, 1234)
        assert "Количество средств для внесения должно быть больше 0" == str(
            ex.value
        )
