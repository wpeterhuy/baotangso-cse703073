<template>
  <section>
    <h1>Chi tiết bảo tàng</h1>
    <p>Slug: {{ slug }}</p>
  </section>
</template>

<script setup>
defineProps({ slug: String })
</script>
