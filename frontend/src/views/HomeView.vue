<template>
  <section class="home">
    <h1>Chào mừng đến với Bảo tàng ảo</h1>
    <p>Khám phá di sản văn hóa Việt Nam qua trải nghiệm tham quan 360°.</p>
    <router-link to="/bao-tang" class="nut-chinh">Xem danh sách bảo tàng →</router-link>
  </section>
</template>

<style scoped>
.home { text-align: center; padding: var(--kc-5) var(--kc-3); }
.home h1 { font-size: 2.5rem; margin-bottom: var(--kc-3); }
.home p { color: var(--mau-chu-nhat); margin-bottom: var(--kc-4); }
.nut-chinh { display: inline-block; background: var(--mau-chinh); color: #fff;
  padding: var(--kc-3) var(--kc-5); border-radius: var(--bo-goc);
  text-decoration: none; font-weight: 600; }
</style>
