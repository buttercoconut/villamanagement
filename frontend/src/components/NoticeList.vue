<template>
  <div>
    <h2>공지사항 목록</h2>
    <ul>
      <li v-for="notice in notices" :key="notice.id">
        <router-link :to="{ name: 'NoticeDetail', params: { id: notice.id } }">
          {{ notice.title }} - {{ notice.created_at }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const notices = ref([])

onMounted(async () => {
  const res = await axios.get('http://localhost:8000/notices/')
  notices.value = res.data.notices
})
</script>
