<template>
  <div>
    <h1>공지사항 상세</h1>
    <div v-if="notice">
      <h2>{{ notice.title }}</h2>
      <p>{{ notice.content }}</p>
      <small>작성일: {{ notice.created_at }}</small>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const notice = ref(null)

onMounted(async () => {
  const res = await axios.get(`http://localhost:8000/notices/${route.params.id}`)
  notice.value = res.data
})
</script>
