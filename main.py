from app import app

# with app.app.context(): # ѕосле первого запуска эту строку можно удалить
#    db.create_all() # ѕосле первого запуска эту строку можно удалить

if __name__ == "__main__":
    app.run(debug=True)

