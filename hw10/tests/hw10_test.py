import pytest

from hw10.tasks import task1, task2, task3


class TestHw6Task1:

    @pytest.mark.parametrize(
        ("obj_filter", "result"),
        [
            (task1.Filter([]), []),
            (task1.Filter([1, 2, 3]), [1, 2, 3]),
            (task1.Filter([0]), [0]),
            (
                task1.Filter([1.2, "1.2", 1, [1.2], {1.2: 1.2}, (1.2, 1.3)]),
                [1.2, "1.2", 1, [1.2], {1.2: 1.2}, (1.2, 1.3)],
            ),
            (
                task1.Filter(
                    [1, 2, 2.3, "2,3", [1, 2, 3], {1: "str", 2: "int"}, -1]
                ),
                [1, 2, 2.3, "2,3", [1, 2, 3], {1: "str", 2: "int"}, -1],
            ),
        ],
    )
    def test_data(self, obj_filter, result):
        assert obj_filter.data == result

    @pytest.mark.parametrize(
        ("obj_filter", "result"),
        [
            (task1.Filter([]), []),
            (task1.Filter([1, 2, 3]), [1, 2, 3]),
            (task1.Filter([0]), [0]),
            (
                task1.Filter([1.2, "1.2", 1, [1.2], {1.2: 1.2}, (1.2, 1.3)]),
                [1.2, 1],
            ),
            (
                task1.Filter(
                    [1, 2, 2.3, "2,3", [1, 2, 3], {1: "str", 2: "int"}, -1]
                ),
                [1, 2, 2.3, -1],
            ),
        ],
    )
    def test_filter_by_numbers(self, obj_filter, result):
        assert obj_filter.filter_by_numbers() == result

    @pytest.mark.parametrize(
        ("obj_filter", "result"),
        [
            (task1.Filter([]), []),
            (task1.Filter([1, 2, 3]), []),
            (task1.Filter([0]), []),
            (task1.Filter(["0", 1, 2, "1"]), ["0", "1"]),
            (
                task1.Filter([1.2, "1.2", 1, [1.2], {1.2: 1.2}, (1.2, 1.3)]),
                ["1.2"],
            ),
            (
                task1.Filter(
                    [1, 2, 2.3, "2,3", [1, 2, 3], {1: "str", 2: "int"}, -1]
                ),
                ["2,3"],
            ),
        ],
    )
    def test_filter_by_string(self, obj_filter, result):
        assert obj_filter.filter_by_string() == result

    @pytest.mark.parametrize(
        ("obj_filter", "result"),
        [
            (task1.Filter([]), []),
            (task1.Filter([1, 2, 3]), [1, 2, 3]),
            (task1.Filter([0]), [0]),
            (
                task1.Filter([1.2, "1.2", 1, [1.2], {1.2: 1.2}, (1.2, 1.3)]),
                [1.2, 1],
            ),
            (
                task1.Filter(
                    [1, 2, 2.3, "2,3", [1, 2, 3], {1: "str", 2: "int"}, -1]
                ),
                [1, 2, 2.3],
            ),
        ],
    )
    def test_filter_by_slice_numbers(self, obj_filter, result):
        assert obj_filter.filter_by_slice_numbers() == result

    @pytest.mark.parametrize(
        ("obj_filter", "result"),
        [
            (task1.Filter([]), []),
            (task1.Filter([1, 2, 3]), [1, 2]),
            (task1.Filter([0]), []),
            (
                task1.Filter([1.2, "1.2", 1, [1.2], {1.2: 1.2}, (1.2, 1.3)]),
                [1.2, 1],
            ),
            (
                task1.Filter(
                    [1, 2, 2.3, "2,3", [1, 2, 3], {1: "str", 2: "int"}, -1]
                ),
                [1, 2],
            ),
        ],
    )
    def test_filter_by_slice_numbers_with_attributes(self, obj_filter, result):
        assert obj_filter.filter_by_slice_numbers(1, 2) == result


class TestHw6Task2:
    @pytest.mark.parametrize(
        ("degrees", "start", "end"),
        [
            (task2.Degree(2, 3), 2, 3),
            (task2.Degree(5, 7), 5, 7),
        ],
    )
    def test_degree(self, degrees, start, end):
        assert degrees.start == start
        assert degrees.end == end

    @pytest.mark.parametrize(
        ("degrees", "result"),
        [
            (
                task2.Degree(2, 3),
                {
                    2: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
                    3: [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049],
                },
            ),
            (
                task2.Degree(5, 5),
                {
                    5: [
                        1,
                        5,
                        25,
                        125,
                        625,
                        3125,
                        15625,
                        78125,
                        390625,
                        1953125,
                        9765625,
                    ]
                },
            ),
        ],
    )
    def test_get_degrees(self, degrees, result):
        assert degrees.get_degrees() == result


@pytest.fixture
def get_class_journal():
    return task3.ClassJournal(
        ["Математика", "Физкультура"],
        ["Родионова Дарья Артёмовна", "Макаров Никита Мирославович"],
    )


class TestHw6Task3:

    @staticmethod
    def set_marks(class_journal):
        class_journal.set_mark("Макаров Никита Мирославович", "Математика", 4)
        class_journal.set_mark("Макаров Никита Мирославович", "Математика", 5)
        class_journal.set_mark("Макаров Никита Мирославович", "Физкультура", 4)
        class_journal.set_mark("Родионова Дарья Артёмовна", "Физкультура", 5)
        class_journal.set_mark("Родионова Дарья Артёмовна", "Математика", 4)

    def test_get_degrees(self, get_class_journal):
        assert get_class_journal.class_journal == {
            "Родионова Дарья Артёмовна": {"Математика": [], "Физкультура": []},
            "Макаров Никита Мирославович": {
                "Математика": [],
                "Физкультура": [],
            },
        }

    def test_set_mark(self, get_class_journal):
        self.set_marks(get_class_journal)
        assert get_class_journal.class_journal == {
            "Родионова Дарья Артёмовна": {
                "Математика": [4],
                "Физкультура": [5],
            },
            "Макаров Никита Мирославович": {
                "Математика": [4, 5],
                "Физкультура": [4],
            },
        }

    def test_set_mark_without_student(self, get_class_journal):
        with pytest.raises(KeyError) as ex:
            get_class_journal.set_mark(
                "Макаров Олег Мирославович", "Математика", 4
            )
        assert "'Данного ученика или предмета нет в журнале'" == str(ex.value)

    def test_set_mark_without_subject(self, get_class_journal):
        with pytest.raises(KeyError) as ex:
            get_class_journal.set_mark(
                "Макаров Никита Мирославович", "Музыка", 4
            )
        assert "'Данного ученика или предмета нет в журнале'" == str(ex.value)

    def test_get_student_info(self, get_class_journal):
        self.set_marks(get_class_journal)

        assert get_class_journal.get_student_info(
            "Родионова Дарья Артёмовна"
        ) == {"Математика": [4], "Физкультура": [5]}
        assert get_class_journal.get_student_info(
            "Макаров Никита Мирославович"
        ) == {"Математика": [4, 5], "Физкультура": [4]}

    def test_get_student_info_raise(self, get_class_journal):
        with pytest.raises(KeyError) as ex:
            get_class_journal.get_student_info("Родионова Анастасия Артёмовна")
        assert "'Данного ученика нет в журнале'" == str(ex.value)

    def test_get_all_info(self, get_class_journal):
        self.set_marks(get_class_journal)

        assert get_class_journal.get_all_info() == {
            "Макаров Никита Мирославович": {
                "Математика": [4, 5],
                "Физкультура": [4],
            },
            "Родионова Дарья Артёмовна": {
                "Математика": [4],
                "Физкультура": [5],
            },
        }

    def test_get_student_info_deepcopy(self, get_class_journal):
        student = get_class_journal.get_student_info(
            "Родионова Дарья Артёмовна"
        )
        student["Математика"].append(5)

        assert (
            student["Математика"]
            != get_class_journal.get_student_info("Родионова Дарья Артёмовна")[
                "Математика"
            ]
        )

    def test_get_all_info_deepcopy(self, get_class_journal):
        info = get_class_journal.get_all_info()
        info["Родионова Дарья Артёмовна"]["Математика"].append(5)
        info["Родионова Дарья Артёмовна"]["Физкультура"].append(5)
        info["Макаров Никита Мирославович"]["Математика"].append(4)
        info["Макаров Никита Мирославович"]["Физкультура"].append(5)

        assert info != get_class_journal.get_all_info()
