from sqlalchemy import create_engine, text, inspect


class CompanyTable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_inspector(self):
        """Возвращает инспектор для анализа БД"""
        return inspect(self.db)

    def get_subjects(self):
        connection = self.db.connect()
        result = connection.execute(text("SELECT * FROM subject"))
        return result.fetchall()

    def add_subject(self, subject_id, subject_title):
        connection = self.db.connect()
        query = text("INSERT INTO subject (subject_id, subject_title) "
                     "VALUES (:id, :title)")
        connection.execute(query, {"id": subject_id, "title": subject_title})
        connection.commit()
        return subject_id

    def update_subject(self, subject_id, subject_title):
        connection = self.db.connect()
        query = text("UPDATE subject "
                     "SET subject_title = :title WHERE subject_id = :id")
        connection.execute(query, {"title": subject_title, "id": subject_id})
        connection.commit()
        return subject_title

    def delete_subject(self, subject_id):
        connection = self.db.connect()
        query = text("DELETE FROM subject WHERE subject_id = :id")
        result = connection.execute(query, {"id": subject_id})
        connection.commit()
        return result.rowcount
