<template>
  <div class="notice-list">
    <h2>공지사항 목록</h2>
    <ul>
      <li v-for="notice in notices" :key="notice.id" @click="selectNotice(notice)" class="notice-item">
        <h3>{{ notice.title }}</h3>
        <p class="date">{{ formatDate(notice.created_at) }}</p>
      </li>
    </ul>
    <div v-if="selectedNotice" class="notice-detail">
      <h3>{{ selectedNotice.title }}</h3>
      <p class="date">{{ formatDate(selectedNotice.created_at) }}</p>
      <p>{{ selectedNotice.content }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const notices = ref([]);
const selectedNotice = ref(null);

const fetchNotices = async () => {
  try {
    const res = await axios.get('/api/notices');
    notices.value = res.data;
  } catch (e) {
    console.error('공지사항 가져오기 실패', e);
  }
};

const selectNotice = (notice) => {
  selectedNotice.value = notice;
};

const formatDate = (iso) => {
  const d = new Date(iso);
  return d.toLocaleDateString('ko-KR');
};

onMounted(fetchNotices);
</script>

<style scoped>
.notice-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
}
.notice-item {
  cursor: pointer;
  padding: 0.5rem;
  border-bottom: 1px solid #ddd;
}
.notice-item:hover {
  background: #f9f9f9;
}
.notice-detail {
  margin-top: 1rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.date {
  color: #888;
  font-size: 0.9rem;
}
</style>
