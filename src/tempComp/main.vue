
<template>
    <div>
        <h1>主页面</h1>
        欢迎!<b @click="login">点这里登录</b>
    </div>
</template>

<script>
    export default {
        methods: {
            login () {
                this.$router.replace('/login')
            }
        }
    }
</script>