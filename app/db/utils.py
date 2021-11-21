from datetime import datetime as dt


def unpack_user(row):
    return {
        "login_name": row[1],
        "full_name": row[2],
        "address_name": row[3],
        "phone_number": row[4],
    }


def unpack_category(row):
    return {
        "category_name": row[1],
        "avg_calories": row[2],
    }


def unpack_order(row):
    return {
        "id": row[0],
        "owner_id": row[1],
        "food_name": row[2],
        "category_id": row[3],
        "price": float(row[4]),
        "due_date": row[5],
        "comment": row[6],
        "is_anonymus": bool(row[7]),
        "is_completed": bool(row[8]),
        "is_trashed": bool(row[9]),
    }
