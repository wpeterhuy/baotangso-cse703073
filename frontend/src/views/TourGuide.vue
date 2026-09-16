<template>
  <section>
    <h1>Tour có dẫn dắt</h1>
    <p>Slug: {{ slug }}</p>
  </section>
</template>

<script setup>
defineProps({ slug: String })
</script>
