# -*- coding: utf-8 -*-
"""
database/seed_data.py — Sinh dữ liệu mẫu cho Bảo tàng ảo (ĐT-16)
GHI FILE TRỰC TIẾP VỚI UTF-8 — không qua stdout.

Chạy:  python seed_data.py
Kết quả: file seed.sql (UTF-8) cùng thư mục
Nạp:  mysql -u root -pRoot@123 --default-character-set=utf8mb4 baotangso -e "source seed.sql"
"""
import random
import datetime as dt
import hashlib
import os
import sys

# Ép Python dùng UTF-8 cho mọi thao tác I/O
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

random.seed(703073)  # Cố định seed để tái lập kết quả
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seed.sql")

print("=" * 60)
print("  SINH SEED DATA CHO BAO TANG AO (DT-16)")
print("=" * 60)

# ============ DỮ LIỆU GỐC ============

MUSEUMS = [
    ("Bảo tàng Lịch sử Quốc gia", "bao-tang-lich-su-quoc-gia",
     "Số 1 Tràng Tiền, Hoàn Kiếm, Hà Nội", 21.0245, 105.8573,
     "Bảo tàng trưng bày hiện vật lịch sử Việt Nam từ thời tiền sử đến hiện đại"),
    ("Bảo tàng Mỹ thuật Việt Nam", "bao-tang-my-thuat-viet-nam",
     "Số 66 Nguyễn Thái Học, Ba Đình, Hà Nội", 21.0306, 105.8372,
     "Bảo tàng trưng bày tác phẩm mỹ thuật của các nghệ sĩ Việt Nam"),
    ("Bảo tàng Dân tộc học Việt Nam", "bao-tang-dan-toc-hoc",
     "Số 1 Nguyễn Văn Huyên, Cầu Giấy, Hà Nội", 21.0383, 105.8006,
     "Bảo tàng giới thiệu văn hóa 54 dân tộc Việt Nam"),
    ("Bảo tàng Chứng tích Chiến tranh", "bao-tang-chung-tich-chien-tranh",
     "Số 28 Võ Văn Tần, Quận 3, TP Hồ Chí Minh", 10.7796, 106.6923,
     "Bảo tàng trưng bày chứng tích chiến tranh Việt Nam"),
    ("Bảo tàng Hồ Chí Minh", "bao-tang-ho-chi-minh",
     "Số 19 Ngọc Hà, Ba Đình, Hà Nội", 21.0358, 105.8328,
     "Bảo tàng về cuộc đời và sự nghiệp của Chủ tịch Hồ Chí Minh"),
]

SCENE_TITLES = [
    "Khu vực trưng bày chính",
    "Phòng khảo cổ",
    "Không gian văn hóa Đông Sơn",
    "Phòng trưng bày gốm sứ",
    "Khu vực chiến tranh",
    "Phòng tưởng niệm",
    "Không gian dân tộc học",
    "Phòng tranh nghệ thuật",
    "Khu vực tái hiện lịch sử",
    "Phòng chiếu phim tư liệu",
]

ARTIFACT_TEMPLATES = [
    ("Trống đồng Đông Sơn", "Văn hóa Đông Sơn, ~700 TCN", "Đồng", "80cm x 80cm"),
    ("Bình gốm hoa lam", "Thời Lê sơ, thế kỷ XV", "Gốm sứ", "30cm x 40cm"),
    ("Tượng Phật bằng đá", "Thời Lý, thế kỷ XI", "Đá", "50cm x 120cm"),
    ("Áo dài truyền thống", "Thế kỷ XIX", "Vải lụa", "150cm x 60cm"),
    ("Bản đồ cổ Đại Việt", "Thời Nguyễn, thế kỷ XIX", "Giấy", "120cm x 80cm"),
    ("Gươm báu", "Thời Lê, thế kỷ XV", "Sắt", "90cm x 10cm"),
    ("Mũ quan triều Nguyễn", "Thời Nguyễn, thế kỷ XIX", "Kim loại", "30cm x 30cm"),
    ("Bút tích chữ Nôm", "Thế kỷ XVIII", "Giấy", "40cm x 30cm"),
    ("Đồng tiền cổ", "Thời Đinh, thế kỷ X", "Đồng", "3cm x 3cm"),
    ("Trang phục dân tộc Thái", "Thế kỷ XX", "Vải thổ cẩm", "160cm x 80cm"),
    ("Nhạc cụ đàn bầu", "Thế kỷ XX", "Gỗ và dây", "100cm x 20cm"),
    ("Tranh sơn mài Hạ Long", "Thế kỷ XX", "Sơn mài", "100cm x 60cm"),
    ("Máy ảnh cổ", "Đầu thế kỷ XX", "Kim loại", "15cm x 10cm"),
    ("Bức thư cách mạng", "Thế kỷ XX", "Giấy", "25cm x 20cm"),
    ("Bi đá cổ", "Thời tiền sử", "Đá", "40cm x 30cm"),
]

# ============ HÀM TIỆN ÍCH ============

def sql_escape(s):
    """Escape chuỗi cho SQL — thay ' bằng ''"""
    if s is None:
        return "NULL"
    return "'" + str(s).replace("\\", "\\\\").replace("'", "''") + "'"

def hash_password(pw):
    """Mô phỏng bcrypt — trong thực tế dùng Hash::make()"""
    return "$2y$12$" + hashlib.sha256(pw.encode("utf-8")).hexdigest()[:53]

# ============ SINH SQL ============

rows = []
now = dt.datetime.now()

# ---------- 1. USERS ----------
print("[1/13] users...")
users = [
    (1, "admin@baotangso.test", "Admin@123", "admin"),
    (2, "curator@baotangso.test", "Curator@123", "curator"),
    (3, "visitor1@baotangso.test", "Visitor@123", "visitor"),
    (4, "visitor2@baotangso.test", "Visitor@123", "visitor"),
    (5, "visitor3@baotangso.test", "Visitor@123", "visitor"),
]
for uid, email, pw, role in users:
    rows.append(
        f"INSERT INTO users (id,email,password_hash,role,status) VALUES "
        f"({uid},{sql_escape(email)},{sql_escape(hash_password(pw))},{sql_escape(role)},'active');"
    )

# ---------- 2. MUSEUMS ----------
print("[2/13] museums...")
for mid, (name, slug, address, lat, lng, desc) in enumerate(MUSEUMS, start=1):
    opening = '{"mon":"08:00-17:00","tue":"08:00-17:00","wed":"08:00-17:00","thu":"08:00-17:00","fri":"08:00-17:00","sat":"08:00-20:00","sun":"08:00-20:00"}'
    rows.append(
        f"INSERT INTO museums (id,name,slug,address,lat,lng,description,opening_hours,status) "
        f"VALUES ({mid},{sql_escape(name)},{sql_escape(slug)},{sql_escape(address)},"
        f"{lat},{lng},{sql_escape(desc)},{sql_escape(opening)},'published');"
    )

# ---------- 3. SCENES ----------
print("[3/13] scenes...")
scene_id = 0
scenes_by_museum = {}
for mid in range(1, 6):
    scenes_by_museum[mid] = []
    num_scenes = random.randint(6, 8)
    for idx in range(num_scenes):
        scene_id += 1
        title = SCENE_TITLES[idx % len(SCENE_TITLES)]
        slug = f"{MUSEUMS[mid-1][1]}-scene-{idx+1}"
        yaw = round(random.uniform(0, 360), 3)
        pitch = round(random.uniform(-30, 30), 3)
        rows.append(
            f"INSERT INTO scenes (id,museum_id,title,slug,panorama_url,thumbnail_url,"
            f"initial_yaw,initial_pitch,order_index,status) VALUES "
            f"({scene_id},{mid},{sql_escape(title)},{sql_escape(slug)},"
            f"'/storage/panoramas/scene-{scene_id}/tiles',"
            f"'/storage/panoramas/scene-{scene_id}/thumb.jpg',"
            f"{yaw},{pitch},{idx},'published');"
        )
        scenes_by_museum[mid].append(scene_id)

# ---------- 4. ARTIFACTS ----------
print("[4/13] artifacts...")
artifact_id = 0
artifacts_by_museum = {}
for mid in range(1, 6):
    artifacts_by_museum[mid] = []
    num_artifacts = random.randint(12, 20)
    for _ in range(num_artifacts):
        artifact_id += 1
        name, era, material, dims = random.choice(ARTIFACT_TEMPLATES)
        images = f'["/storage/artifacts/{artifact_id}-1.jpg","/storage/artifacts/{artifact_id}-2.jpg"]'
        desc = f"Mô tả hiện vật {name} thuộc {era}"
        source = f"Nguồn: {MUSEUMS[mid-1][0]}"
        rows.append(
            f"INSERT INTO artifacts (id,museum_id,name,era,material,dimensions,"
            f"description_vi,image_urls,source_note) VALUES "
            f"({artifact_id},{mid},{sql_escape(name)},{sql_escape(era)},"
            f"{sql_escape(material)},{sql_escape(dims)},{sql_escape(desc)},"
            f"{sql_escape(images)},{sql_escape(source)});"
        )
        artifacts_by_museum[mid].append(artifact_id)

# ---------- 5. HOTSPOTS ----------
print("[5/13] hotspots...")
hotspot_id = 0
for mid, scenes in scenes_by_museum.items():
    for s_id in scenes:
        # 2-4 navigation hotspots
        for _ in range(random.randint(2, 4)):
            hotspot_id += 1
            target = random.choice(scenes)
            if target == s_id and len(scenes) > 1:
                target = random.choice([s for s in scenes if s != s_id])
            label = f"Đi tới scene {target}"
            yaw = round(random.uniform(0, 360), 3)
            pitch = round(random.uniform(-30, 30), 3)
            rows.append(
                f"INSERT INTO hotspots (id,scene_id,type,yaw,pitch,label,target_scene_id,order_index) "
                f"VALUES ({hotspot_id},{s_id},'navigation',{yaw},{pitch},"
                f"{sql_escape(label)},{target},{hotspot_id});"
            )
        # 3-5 info hotspots
        for _ in range(random.randint(3, 5)):
            hotspot_id += 1
            art = random.choice(artifacts_by_museum[mid])
            yaw = round(random.uniform(0, 360), 3)
            pitch = round(random.uniform(-30, 30), 3)
            rows.append(
                f"INSERT INTO hotspots (id,scene_id,type,yaw,pitch,label,artifact_id,"
                f"content_vi,content_en,order_index) VALUES "
                f"({hotspot_id},{s_id},'info',{yaw},{pitch},"
                f"'Xem hiện vật',{art},"
                f"'Thông tin chi tiết về hiện vật',"
                f"'Detailed artifact information',{hotspot_id});"
            )

# ---------- 6. TOURS ----------
print("[6/13] tours...")
tour_id = 0
tours_by_museum = {}
for mid, scenes in scenes_by_museum.items():
    tours_by_museum[mid] = []
    themes = ["Khám phá tổng quát", "Chuyên sâu lịch sử", "Trải nghiệm văn hóa"]
    num_tours = random.randint(2, 3)
    for idx in range(num_tours):
        tour_id += 1
        theme = themes[idx % len(themes)]
        title = f"Tour {theme} - {MUSEUMS[mid-1][0]}"
        slug = f"tour-{mid}-{idx+1}"
        desc = f"Tour tham quan {theme}"
        duration = random.randint(30, 90)
        rows.append(
            f"INSERT INTO tours (id,museum_id,title,slug,theme,description,duration_minutes,status) "
            f"VALUES ({tour_id},{mid},{sql_escape(title)},{sql_escape(slug)},"
            f"{sql_escape(theme)},{sql_escape(desc)},{duration},'published');"
        )
        tours_by_museum[mid].append((tour_id, scenes))

# ---------- 7. TOUR STEPS ----------
print("[7/13] tour_steps...")
step_id = 0
for mid, tours in tours_by_museum.items():
    for tid, scenes in tours:
        selected = random.sample(scenes, min(len(scenes), random.randint(4, 6)))
        for step_no, s_id in enumerate(selected, start=1):
            step_id += 1
            narration_vi = f"Hướng dẫn bước {step_no}"
            narration_en = f"Guidance for step {step_no}"
            rows.append(
                f"INSERT INTO tour_steps (id,tour_id,scene_id,step_no,narration_vi,narration_en) "
                f"VALUES ({step_id},{tid},{s_id},{step_no},"
                f"{sql_escape(narration_vi)},{sql_escape(narration_en)});"
            )

# ---------- 8. VISIT SESSIONS ----------
print("[8/13] visit_sessions...")
session_id = 0
for _ in range(60):
    session_id += 1
    mid = random.randint(1, 5)
    tid = random.choice(tours_by_museum[mid])[0] if random.random() < 0.6 else None
    mode = "guided" if tid else "free"
    user_id = random.choice([3, 4, 5, None])
    guest_token = "NULL" if user_id else sql_escape(
        f"{random.randint(10000000, 99999999)}-aaaa-bbbb-cccc-{random.randint(100000000000, 999999999999)}"
    )
    start = now - dt.timedelta(days=random.randint(0, 30), minutes=random.randint(0, 1440))
    duration = random.randint(120, 3600)
    end = start + dt.timedelta(seconds=duration)
    tid_val = tid if tid else "NULL"
    uid_val = user_id if user_id else "NULL"
    rows.append(
        f"INSERT INTO visit_sessions (id,user_id,guest_token,museum_id,tour_id,mode,"
        f"started_at,ended_at,duration_sec) VALUES "
        f"({session_id},{uid_val},{guest_token},{mid},{tid_val},{sql_escape(mode)},"
        f"'{start.strftime('%Y-%m-%d %H:%M:%S')}',"
        f"'{end.strftime('%Y-%m-%d %H:%M:%S')}',{duration});"
    )

# ---------- 9. VISIT EVENTS ----------
print("[9/13] visit_events...")
event_id = 0
for s_id in range(1, 61):
    mid = random.randint(1, 5)
    scenes = scenes_by_museum[mid]
    num_events = random.randint(5, 15)
    for _ in range(num_events):
        event_id += 1
        scene = random.choice(scenes)
        event_type = random.choice(["enter_scene", "leave_scene", "click_hotspot", "play_audio"])
        rows.append(
            f"INSERT INTO visit_events (id,session_id,scene_id,event_type) "
            f"VALUES ({event_id},{s_id},{scene},{sql_escape(event_type)});"
        )

# ---------- 10. GUESTBOOK ENTRIES ----------
print("[10/13] guestbook_entries...")
gb_id = 0
comments = [
    "Trải nghiệm tuyệt vời, rất bổ ích!",
    "Bảo tàng ảo giúp tôi hiểu thêm về lịch sử.",
    "Hình ảnh 360 độ rất sống động.",
    "Thuyết minh âm thanh dễ nghe, hay.",
    "Tour dẫn dắt hợp lý, dễ theo dõi.",
    "Rất tiếc không có phiên bản tiếng Anh đầy đủ.",
    "Tôi muốn xem thêm hiện vật.",
    "Giao diện thân thiện, dễ dùng.",
]
for _ in range(40):
    gb_id += 1
    mid = random.randint(1, 5)
    user_id = random.choice([3, 4, 5, None])
    name = f"Khách {random.randint(1000, 9999)}"
    content = random.choice(comments)
    sentiment = random.choices(["positive", "neutral", "negative"], weights=[7, 2, 1])[0]
    is_approved = "TRUE" if random.random() < 0.8 else "FALSE"
    uid_val = user_id if user_id else "NULL"
    rows.append(
        f"INSERT INTO guestbook_entries (id,museum_id,user_id,display_name,content,"
        f"sentiment,is_approved) VALUES "
        f"({gb_id},{mid},{uid_val},{sql_escape(name)},{sql_escape(content)},"
        f"{sql_escape(sentiment)},{is_approved});"
    )

# ---------- 11. COLLECTIONS ----------
print("[11/13] collections...")
col_id = 0
collection_names = ["Hiện vật yêu thích", "Bộ sưu tập gốm sứ", "Lịch sử Việt Nam", "Di sản văn hóa"]
for user_id in [3, 4, 5]:
    for name in random.sample(collection_names, random.randint(1, 3)):
        col_id += 1
        rows.append(
            f"INSERT INTO collections (id,user_id,name,description,is_public) "
            f"VALUES ({col_id},{user_id},{sql_escape(name)},"
            f"'Bộ sưu tập cá nhân',FALSE);"
        )

# ---------- 12. COLLECTION ITEMS ----------
print("[12/13] collection_items...")
for c_id in range(1, col_id + 1):
    museum = random.randint(1, 5)
    arts = artifacts_by_museum[museum]
    for art in random.sample(arts, min(len(arts), random.randint(2, 4))):
        rows.append(
            f"INSERT INTO collection_items (collection_id,artifact_id,note) "
            f"VALUES ({c_id},{art},'Lưu vào bộ sưu tập');"
        )

# ---------- 13. AUDIT LOGS ----------
print("[13/13] audit_logs...")
for _ in range(50):
    rows.append(
        f"INSERT INTO audit_logs (actor_id,action,entity,entity_id,ip_address) "
        f"VALUES ({random.choice([1,2])},'admin.view','museums',{random.randint(1,5)},'127.0.0.1');"
    )

# ============ GHI FILE UTF-8 ============
print()
print("-" * 60)
print(f"Ghi {len(rows)} câu lệnh INSERT vào: {OUTPUT_FILE}")

with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
    f.write("-- ============================================\n")
    f.write("-- SEED DATA — Hệ thống Bảo tàng ảo (DT-16)\n")
    f.write(f"-- Sinh ngày: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"-- Tổng số câu lệnh INSERT: {len(rows)}\n")
    f.write("-- ============================================\n\n")
    f.write("SET NAMES utf8mb4;\n")
    f.write("SET FOREIGN_KEY_CHECKS = 0;\n")
    f.write("USE baotangso;\n\n")
    for r in rows:
        f.write(r + "\n")
    f.write("\nSET FOREIGN_KEY_CHECKS = 1;\n")
    f.write(f"\n-- Tổng số câu lệnh INSERT: {len(rows)}\n")

# Verify lại encoding bằng cách đọc file
with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
    first_lines = f.read(500)

# Kiểm tra có chứa tiếng Việt đúng không
has_vietnamese = "Bảo tàng" in first_lines or "Đông Sơn" in first_lines

print("-" * 60)
print()
print("[KẾT QUẢ]")
print(f"  ✓ File: {OUTPUT_FILE}")
print(f"  ✓ Số dòng INSERT: {len(rows)}")
print(f"  ✓ Encoding: UTF-8")
print(f"  ✓ Có tiếng Việt đúng: {'CÓ' if has_vietnamese else 'KHÔNG — KIỂM TRA LẠI!'}")
print()
print("BƯỚC TIẾP THEO — nạp vào MySQL:")
print(f'  mysql -u root -pRoot@123 --default-character-set=utf8mb4 baotangso -e "source seed.sql"')
print()
print("=" * 60)
