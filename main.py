from app import app

# with app.app.context(): # ����� ������� ������� ��� ������ ����� �������
#    db.create_all() # ����� ������� ������� ��� ������ ����� �������

if __name__ == "__main__":
    app.run(debug=True)

