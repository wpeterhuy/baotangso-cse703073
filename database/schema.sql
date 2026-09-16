-- database/schema.sql — MySQL 8.0 — Hệ thống Bảo tàng ảo (ĐT-16)
-- Charset: utf8mb4 để hỗ trợ tiếng Việt và emoji

CREATE DATABASE IF NOT EXISTS baotangso
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE baotangso;

-- Bật kiểm tra khóa ngoại
SET FOREIGN_KEY_CHECKS = 1;

-- 1. NGƯỜI DÙNG VÀ VAI TRÒ
CREATE TABLE users (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(180) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin','curator','visitor') NOT NULL DEFAULT 'visitor',
  status ENUM('active','locked') NOT NULL DEFAULT 'active',
  last_login_at TIMESTAMP NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_users_role_status (role, status)
) ENGINE=InnoDB;

-- 2. BẢO TÀNG
CREATE TABLE museums (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  slug VARCHAR(220) NOT NULL UNIQUE,
  address VARCHAR(300) NULL,
  lat DECIMAL(10,7) NULL,
  lng DECIMAL(10,7) NULL,
  description TEXT NULL,
  cover_image VARCHAR(500) NULL,
  opening_hours JSON NULL,
  status ENUM('draft','published') NOT NULL DEFAULT 'draft',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_museums_status (status)
) ENGINE=InnoDB;

-- 3. KHÔNG GIAN THAM QUAN (SCENE)
CREATE TABLE scenes (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  museum_id BIGINT UNSIGNED NOT NULL,
  title VARCHAR(200) NOT NULL,
  slug VARCHAR(220) NOT NULL,
  panorama_url VARCHAR(500) NOT NULL,
  thumbnail_url VARCHAR(500) NULL,
  initial_yaw DECIMAL(6,3) DEFAULT 0.000,
  initial_pitch DECIMAL(6,3) DEFAULT 0.000,
  initial_fov DECIMAL(5,2) DEFAULT 75.00,
  audio_url VARCHAR(500) NULL,
  order_index INT NOT NULL DEFAULT 0,
  status ENUM('draft','published') NOT NULL DEFAULT 'draft',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_scene_museum FOREIGN KEY (museum_id)
    REFERENCES museums(id) ON DELETE CASCADE,
  UNIQUE KEY uq_scene_slug (museum_id, slug),
  INDEX idx_scene_status (status, order_index)
) ENGINE=InnoDB;

-- 4. ĐIỂM NHÌN TRONG SCENE
CREATE TABLE viewpoints (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  scene_id BIGINT UNSIGNED NOT NULL,
  yaw DECIMAL(6,3) NOT NULL,
  pitch DECIMAL(6,3) NOT NULL,
  fov DECIMAL(5,2) DEFAULT 75.00,
  CONSTRAINT fk_vp_scene FOREIGN KEY (scene_id)
    REFERENCES scenes(id) ON DELETE CASCADE,
  INDEX idx_vp_scene (scene_id)
) ENGINE=InnoDB;

-- 5. HIỆN VẬT
CREATE TABLE artifacts (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  museum_id BIGINT UNSIGNED NOT NULL,
  name VARCHAR(200) NOT NULL,
  era VARCHAR(120) NULL,
  material VARCHAR(120) NULL,
  dimensions VARCHAR(120) NULL,
  description_vi TEXT NULL,
  description_en TEXT NULL,
  image_urls JSON NULL,
  source_note VARCHAR(300) NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_art_museum FOREIGN KEY (museum_id)
    REFERENCES museums(id) ON DELETE CASCADE,
  FULLTEXT KEY ft_artifact (name, description_vi)
) ENGINE=InnoDB;

-- 6. ĐIỂM NÓNG (HOTSPOT)
CREATE TABLE hotspots (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  scene_id BIGINT UNSIGNED NOT NULL,
  type ENUM('navigation','info','audio','video') NOT NULL,
  yaw DECIMAL(6,3) NOT NULL,
  pitch DECIMAL(6,3) NOT NULL,
  label VARCHAR(200) NULL,
  icon VARCHAR(80) DEFAULT 'default',
  target_scene_id BIGINT UNSIGNED NULL,
  artifact_id BIGINT UNSIGNED NULL,
  audio_url VARCHAR(500) NULL,
  content_vi TEXT NULL,
  content_en TEXT NULL,
  order_index INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_hs_scene FOREIGN KEY (scene_id)
    REFERENCES scenes(id) ON DELETE CASCADE,
  CONSTRAINT fk_hs_target FOREIGN KEY (target_scene_id)
    REFERENCES scenes(id) ON DELETE SET NULL,
  CONSTRAINT fk_hs_artifact FOREIGN KEY (artifact_id)
    REFERENCES artifacts(id) ON DELETE SET NULL,
  INDEX idx_hs_scene (scene_id, order_index)
) ENGINE=InnoDB;

-- 7. TOUR THEO CHỦ ĐỀ
CREATE TABLE tours (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  museum_id BIGINT UNSIGNED NOT NULL,
  title VARCHAR(200) NOT NULL,
  slug VARCHAR(220) NOT NULL UNIQUE,
  theme VARCHAR(120) NULL,
  description TEXT NULL,
  duration_minutes SMALLINT UNSIGNED NULL,
  cover_image VARCHAR(500) NULL,
  status ENUM('draft','published') NOT NULL DEFAULT 'draft',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_tour_museum FOREIGN KEY (museum_id)
    REFERENCES museums(id) ON DELETE CASCADE,
  INDEX idx_tour_status (status)
) ENGINE=InnoDB;

-- 8. BƯỚC TRONG TOUR
CREATE TABLE tour_steps (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  tour_id BIGINT UNSIGNED NOT NULL,
  scene_id BIGINT UNSIGNED NOT NULL,
  viewpoint_id BIGINT UNSIGNED NULL,
  step_no SMALLINT UNSIGNED NOT NULL,
  narration_vi TEXT NULL,
  narration_en TEXT NULL,
  audio_url VARCHAR(500) NULL,
  CONSTRAINT fk_ts_tour FOREIGN KEY (tour_id)
    REFERENCES tours(id) ON DELETE CASCADE,
  CONSTRAINT fk_ts_scene FOREIGN KEY (scene_id)
    REFERENCES scenes(id) ON DELETE CASCADE,
  CONSTRAINT fk_ts_vp FOREIGN KEY (viewpoint_id)
    REFERENCES viewpoints(id) ON DELETE SET NULL,
  UNIQUE KEY uq_tour_step (tour_id, step_no),
  INDEX idx_ts_tour (tour_id)
) ENGINE=InnoDB;

-- 9. PHIÊN THAM QUAN
CREATE TABLE visit_sessions (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id BIGINT UNSIGNED NULL,
  guest_token CHAR(36) NULL,
  museum_id BIGINT UNSIGNED NOT NULL,
  tour_id BIGINT UNSIGNED NULL,
  mode ENUM('free','guided') NOT NULL DEFAULT 'free',
  started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  ended_at TIMESTAMP NULL,
  duration_sec INT UNSIGNED DEFAULT 0,
  CONSTRAINT fk_vs_user FOREIGN KEY (user_id)
    REFERENCES users(id) ON DELETE SET NULL,
  CONSTRAINT fk_vs_museum FOREIGN KEY (museum_id)
    REFERENCES museums(id) ON DELETE CASCADE,
  CONSTRAINT fk_vs_tour FOREIGN KEY (tour_id)
    REFERENCES tours(id) ON DELETE SET NULL,
  INDEX idx_vs_user (user_id, started_at),
  INDEX idx_vs_museum (museum_id, started_at)
) ENGINE=InnoDB;

-- 10. SỰ KIỆN THAM QUAN
CREATE TABLE visit_events (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  session_id BIGINT UNSIGNED NOT NULL,
  scene_id BIGINT UNSIGNED NOT NULL,
  hotspot_id BIGINT UNSIGNED NULL,
  event_type ENUM('enter_scene','leave_scene','click_hotspot','play_audio','view_artifact') NOT NULL,
  at_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_ve_session FOREIGN KEY (session_id)
    REFERENCES visit_sessions(id) ON DELETE CASCADE,
  CONSTRAINT fk_ve_scene FOREIGN KEY (scene_id)
    REFERENCES scenes(id) ON DELETE CASCADE,
  CONSTRAINT fk_ve_hotspot FOREIGN KEY (hotspot_id)
    REFERENCES hotspots(id) ON DELETE SET NULL,
  INDEX idx_ve_session (session_id, at_time),
  INDEX idx_ve_scene (scene_id, event_type)
) ENGINE=InnoDB;

-- 11. SỔ LƯU BÚT
CREATE TABLE guestbook_entries (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  museum_id BIGINT UNSIGNED NOT NULL,
  user_id BIGINT UNSIGNED NULL,
  display_name VARCHAR(120) NOT NULL,
  content TEXT NOT NULL,
  sentiment ENUM('positive','neutral','negative') NULL,
  is_approved BOOLEAN DEFAULT FALSE,
  moderated_at DATETIME NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_gb_museum FOREIGN KEY (museum_id)
    REFERENCES museums(id) ON DELETE CASCADE,
  CONSTRAINT fk_gb_user FOREIGN KEY (user_id)
    REFERENCES users(id) ON DELETE SET NULL,
  INDEX idx_gb_museum (museum_id, is_approved, created_at)
) ENGINE=InnoDB;

-- 12. BỘ SƯU TẬP CÁ NHÂN
CREATE TABLE collections (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_id BIGINT UNSIGNED NOT NULL,
  name VARCHAR(160) NOT NULL,
  description VARCHAR(300) NULL,
  is_public BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_col_user FOREIGN KEY (user_id)
    REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 13. MỤC TRONG BỘ SƯU TẬP
CREATE TABLE collection_items (
  collection_id BIGINT UNSIGNED NOT NULL,
  artifact_id BIGINT UNSIGNED NOT NULL,
  note VARCHAR(300) NULL,
  added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (collection_id, artifact_id),
  CONSTRAINT fk_ci_col FOREIGN KEY (collection_id)
    REFERENCES collections(id) ON DELETE CASCADE,
  CONSTRAINT fk_ci_art FOREIGN KEY (artifact_id)
    REFERENCES artifacts(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 14. NHẬT KÝ KIỂM TOÁN
CREATE TABLE audit_logs (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  actor_id BIGINT UNSIGNED NULL,
  action VARCHAR(60) NOT NULL,
  entity VARCHAR(60) NOT NULL,
  entity_id BIGINT UNSIGNED NULL,
  before_json JSON NULL,
  after_json JSON NULL,
  ip_address VARCHAR(45) NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_audit_user FOREIGN KEY (actor_id)
    REFERENCES users(id) ON DELETE SET NULL,
  INDEX idx_audit_entity (entity, entity_id, created_at)
) ENGINE=InnoDB;

-- ===== TÀI KHOẢN ỨNG DỤNG RIÊNG (KHÔNG DÙNG ROOT) =====
-- Lưu ý: chạy lệnh này bằng root
-- CREATE USER IF NOT EXISTS 'baotangso_app'@'localhost' IDENTIFIED BY 'HUY@123';
-- GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, DROP, REFERENCES
--   ON baotangso.* TO 'baotangso_app'@'localhost';
-- FLUSH PRIVILEGES;
