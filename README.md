# BaoTangSo — CSE703073 Nhom16

He thong bao tang ao va tour tham quan 360 do tren nen web, ho tro hai che do tham quan tu do va co dan dat theo tour chu de, tich hop lop tri thuc hien vat, thuyet minh am thanh da ngu, so luu but va bo suu tap ca nhan.

## Ngăn xếp công nghệ
PHP 8.3 / Laravel 11 · MySQL 8.0 · Vue 3 + Vite · Python 3.12 (FastAPI, pandas,scikit-learn) · Nginx · Docker Compose

## Yêu cầu môi trường
| Thanh phan | Phien ban toi thieu |
|------------|---------------------|
| PHP        | 8.2                 |
| Composer   | 2.7                 |
| Node.js    | 20                  |
| MySQL      | 8.0                 |
| Python     | 3.11                |

## Cài đặt nhanh bằng Docker
cd C:\du-lich-so\backend

Copy-Item .env.example .env

docker compose up -d --build

## Cai dat trực tiếp
cd C:\du-lich-so\backend

composer install

npm ci

npm run build

Copy-Item .env.example .env

php artisan key:generate

php artisan migrate --seed

php artisan serve

## Cấu trúc thư mục
app/            Tang nghiep vu va dieu khien
resources/      Khung nhin, tai nguyen giao dien, thanh phan Vue
database/       Di tru, seeder, tep SQL
python-service/ Mo-dun xu ly du lieu
tests/          Kiem thu don vi, tinh nang, e2e
docker/         Dockerfile va cau hinh Nginx
scripts/        backup.sh, deploy.sh, dong-goi.sh

## Kiểm thử
php artisan test
npx playwright test

## Thành viên
Thanh vien
Ho va ten	MSSV	Vai tro
<Ho ten>	<MSSV>	Truong nhom — Quan tri du an
<Ho ten>	<MSSV>	Lap trinh vien Back-end
<Ho ten>	<MSSV>	Lap trinh vien Front-end
<Ho ten>	<MSSV>	Chuyen vien kiem thu
<Ho ten>	<MSSV>	Nghiep vu va tai lieu

## Giấy phép
San pham hoc thuat phuc vu muc dich dao tao, hoc phan CSE703073,
Truong Cong nghe thong tin, Dai hoc Phenikaa.