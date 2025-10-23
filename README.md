# Dự án Django — Preskool (nhóm)

README ngắn bằng tiếng Việt để giúp bạn thiết lập và khởi chạy dự án.

## Yêu cầu
- Python 3.11+ (hệ thống sử dụng 3.13 trong môi trường của bạn — tương thích với virtualenv)
- pip
- virtualenv (khuyến nghị)

## Cài đặt (môi trường phát triển)
1. Tạo và kích hoạt virtualenv (nếu chưa có):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Cài đặt phụ thuộc (nếu có requirements.txt):

```bash
pip install -r requirements.txt
```

> Nếu không có `requirements.txt`, cài Django bằng tay (phiên bản dùng trong repo là 5.x):

```bash
pip install "django>=5.1,<6"
```

3. Thiết lập database và migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Tạo superuser (nếu cần):

```bash
python manage.py createsuperuser
```

5. Chạy server phát triển:

```bash
python manage.py runserver
```

Truy cập http://127.0.0.1:8000/ để xem trang.

## Cấu trúc cơ bản của repo
- `Home/` — project Django (cấu hình, urls, wsgi/asgi)
- `school/` — app chính (đã có sẵn)
- `student/` — app sinh viên (nếu bạn muốn dùng root route cho student, file `student/urls.py` nên tồn tại)
- `templates/` — template chung, bao gồm `Home/base.html`
- `static/` — file tĩnh (CSS/JS/images)

## Vấn đề phổ biến & cách khắc phục
- Lỗi `ModuleNotFoundError: No module named 'student.urls'`:
  - Nguyên nhân: Django cố gắng include `student.urls` nhưng không tìm thấy package `student` hoặc `student/urls.py`.
  - Kiểm tra:
    - `student/` tồn tại ở thư mục gốc (nơi `manage.py` nằm).
    - `student/urls.py` tồn tại và export `urlpatterns`.
    - `student` có trong `INSTALLED_APPS` (nếu cần migrations hoặc models).
  - Cách fix nhanh:

```bash
# ở thư mục project (chứa manage.py)
ls -la student
# Nếu không tồn tại, tạo folder và file urls.py
```

- Lỗi template `"'block' tag with name 'body' appears more than once"`:
  - Nguyên nhân: `base.html` bị nhân đôi phần tài liệu HTML hoặc có nhiều `{% block body %}`.
  - Cách fix: mở `templates/Home/base.html`, đảm bảo chỉ có một cặp `{% block body %}...{% endblock %}` và file HTML chỉ xuất hiện một lần.

## Gợi ý phát triển
- Khi thêm app mới:
  - Tạo app folder, `__init__.py`, `apps.py`, `urls.py`, `views.py`, `models.py`.
  - Đăng ký app trong `INSTALLED_APPS` nếu cần migrations.
- Khi thay đổi `urls.py`, chạy `python manage.py check` để bắt lỗi sớm.

## Liên hệ
Nếu muốn tôi khởi server, chạy migrate, hoặc sửa trực tiếp file `templates/Home/base.html`, nói cho tôi biết hành động bạn muốn tôi thực hiện và tôi sẽ chạy các lệnh cần thiết trong terminal.
