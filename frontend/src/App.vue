<template>
  <div id="app">
    <header>
      <h1>Bảo tàng ảo — CSE703073</h1>
      <button @click="toggleTheme">Đổi chủ đề</button>
    </header>
    <main>
      <p>Chào mừng đến với bảo tàng ảo!</p>
    </main>
    <footer class="site-footer">
      <p>Học phần CSE703073 — Nhóm 16</p>
      <p>Sản phẩm học thuật — phục vụ mục đích đào tạo.</p>
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
})

function toggleTheme() {
  theme.value = theme.value === 'sang' ? 'toi' : 'sang'
}
</script>

<style>
@import './assets/themes/tokens.css';

.site-footer {
  margin-top: var(--kc-5);
  padding: var(--kc-3);
  border-top: 1px solid var(--mau-vien);
  font-size: var(--co-chu-nho);
  color: var(--mau-chu-nhat);
  text-align: center;
}
</style>
