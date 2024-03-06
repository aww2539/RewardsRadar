from flask_restful import Resource
from ..database.connect import connect_to_db


class ChaseApi(Resource):
    def get(self, id):
        with connect_to_db() as db_conn:
            with db_conn.cursor() as cursor:
                sql = """
                    SELECT * 
                    FROM chase_cards
                    WHERE id = %s
                """

                cursor.execute(sql, id)
                results = cursor.fetchall()
        
        return results

class ChaseListApi(Resource):
    def get(self):
        with connect_to_db() as db_conn:
            with db_conn.cursor() as cursor:
                sql = """
                    SELECT * 
                    FROM chase_cards
                """
                cursor.execute(sql)
                results = cursor.fetchall()

        return results

