<template>
  <el-table :data="notices" style="width: 100%">
    <el-table-column prop="title" label="Title" width="180" />
    <el-table-column prop="date" label="Date" width="120" />
    <el-table-column label="Actions" width="120">
      <template #default="{ row }">
        <el-button size="small" @click="viewNotice(row)">View</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useNoticeStore } from '@/store'
import { useRouter } from 'vue-router'

const store = useNoticeStore()
const router = useRouter()
const notices = ref([])

const fetchNotices = async () => {
  // Placeholder: replace with real API call
  const data = [
    { id: 1, title: 'Notice 1', date: '2024-05-01' },
    { id: 2, title: 'Notice 2', date: '2024-05-02' }
  ]
  store.setNotices(data)
  notices.value = data
}

const viewNotice = (notice: any) => {
  router.push({ name: 'NoticeView', params: { id: notice.id } })
}

onMounted(fetchNotices)
</script>
