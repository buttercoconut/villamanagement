<template>
  <el-container style="height: 100vh;">
    <el-header>
      <el-menu mode="horizontal" router>
        <el-menu-item index="/">Home</el-menu-item>
        <el-menu-item index="/notices">Notices</el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script setup lang="ts">
// No script needed for now
</script>

<style scoped>
</style>
