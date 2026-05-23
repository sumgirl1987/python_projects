from companyTable import CompanyTable

db = CompanyTable("postgresql://postgres:sumgirl1987@localhost:5432/QA")


def test_db_connection():
    inspector = db.get_inspector()  # ✅ Красивое решение
    names = inspector.get_table_names()
    print("\n" + "=" * 40)
    print("Таблицы в базе данных:")
    print("=" * 40)
    for table in names:
        print(f"  📊 {table}")
    print("=" * 40)
    print(f"Всего таблиц: {len(names)}")


def test_get_subjects():
    subjects = db.get_subjects()
    print("\n" + "=" * 40)
    print("Предметы в таблице Subject:")
    print("=" * 40)
    for sub in subjects:
        print(f"  📊 {sub}")
    print("=" * 40)
    print(f"Всего предметов: {len(subjects)}")

    assert len(subjects) == 15
    print("✅ Тест пройден успешно!")


def test_add_subject():
    new_subject = "Music"
    new_id = 16
    result = db.add_subject(new_id, new_subject)
    print("\n" + "=" * 40)
    print(f"В таблицу Subject добавился новый предмет: "
          f"{new_subject} с id = {new_id}")
    print("=" * 40)

    assert result == new_id
    print("✅ Тест пройден успешно!")


def test_update_subject():
    subject_id = 16
    current_subject = "Music"
    updated_subject = "Painting"
    result = db.update_subject(subject_id, updated_subject)
    print("\n" + "=" * 40)
    print(f"В таблице Subject предмет '{current_subject}' "
          f"изменен на '{updated_subject}'")
    print("=" * 40)

    assert result == updated_subject
    print("✅ Тест пройден успешно!")


def test_delete_subject():
    subject_id = 16
    subjects_before = db.get_subjects()
    print(f"\nДо удаления: {len(subjects_before)} записей")

    deleted_count = db.delete_subject(subject_id)
    subjects_after = db.get_subjects()
    print(f"После удаления: {len(subjects_after)} записей")
    print("=" * 40)
    if deleted_count > 0:
        print(f"Предмет с id = {subject_id} успешно удален!")
        print(f"Удалено записей: {deleted_count}")
    else:
        print(f"❌ Предмет с id={subject_id} не найден")
    print("=" * 40)

    assert len(subjects_after) == len(subjects_before) - 1
    print("✅ Тест пройден успешно!")
