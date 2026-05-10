import { defineStore } from 'pinia'
import type { Notice } from '@/types/notice'

export const useNoticeStore = defineStore('notice', {
  state: () => ({
    notices: [] as Notice[]
  }),
  actions: {
    setNotices(notices: Notice[]) {
      this.notices = notices
    }
  }
})
