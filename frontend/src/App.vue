<template>
  <div id="app">
    <header class="site-header">
      <div class="container header-inner">
        <router-link to="/" class="logo">🏛️ Bảo tàng ảo</router-link>
        <nav class="main-nav">
          <router-link to="/bao-tang">Bảo tàng</router-link>
          <router-link to="/luu-but">Sổ lưu bút</router-link>
          <router-link to="/bo-suu-tap">Bộ sưu tập</router-link>
        </nav>
        <button @click="toggleTheme" class="theme-toggle" aria-label="Đổi chủ đề">
          {{ theme === 'sang' ? '🌙' : '☀️' }}
        </button>
      </div>
    </header>

    <main class="container" id="noi-dung">
      <router-view />
    </main>

    <footer class="site-footer">
      <div class="container">
        <p>
          Học phần <strong>CSE703073 — Lập trình ứng dụng web trong du lịch 2</strong>
          &middot; Nhóm <strong>16</strong>
          &middot; Trường Công nghệ thông tin, Đại học Phenikaa
        </p>
        <p class="ghi-chu">
          Sản phẩm học thuật — phục vụ mục đích đào tạo.
          Dữ liệu trong hệ thống là dữ liệu mô phỏng.
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'

const KEY = 'cse703073-theme'
const theme = ref(localStorage.getItem(KEY) || 'sang')

watchEffect(() => {
  document.documentElement.dataset.theme = theme.value
  localStorage.setItem(KEY, theme.value)
  document.cookie = `theme=${theme.value}; path=/; max-age=31536000; sameSite=lax`
})

function toggleTheme() {
  theme.value = theme.value === 'sang' ? 'toi' : 'sang'
}
</script>

<style scoped>
.site-header {
  background: var(--mau-nen-phu);
  border-bottom: 1px solid var(--mau-vien);
  padding: var(--kc-3) 0;
  position: sticky;
  top: 0;
  z-index: 100;
}
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--kc-3);
}
.logo {
  font-size: var(--co-chu-lon);
  font-weight: 700;
  text-decoration: none;
  color: var(--mau-chinh);
}
.main-nav {
  display: flex;
  gap: var(--kc-3);
  flex: 1;
  justify-content: center;
}
.main-nav a {
  color: var(--mau-chu);
  text-decoration: none;
  padding: var(--kc-2) var(--kc-3);
  border-radius: var(--bo-goc);
}
.main-nav a:hover,
.main-nav a.router-link-active {
  background: var(--mau-chinh);
  color: #fff;
}
.theme-toggle {
  background: none;
  border: 1px solid var(--mau-vien);
  border-radius: var(--bo-goc);
  padding: var(--kc-2);
  cursor: pointer;
  font-size: var(--co-chu-lon);
}
.site-footer {
  margin-top: var(--kc-5);
  padding: var(--kc-4) 0;
  border-top: 1px solid var(--mau-vien);
  text-align: center;
  color: var(--mau-chu-nhat);
  font-size: var(--co-chu-nho);
}
</style>
