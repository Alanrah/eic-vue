<template>
    <div>
        <div class="album-img-list">
            <ul>
                <li v-for="img in imgList"><div class="album-bg-img"><img  :src='img.src'> </div></li>

            </ul>
        </div>
        <div class="album">
            <label for="img-upload">上传照片</label>
                <imagehtml5upload :img-arr.sync="imgList"></imagehtml5upload>
        </div>
    </div>
</template>
<script>
import imagehtml5upload from './collects.vue'
    export default {
        components:{
            imagehtml5upload,
        },
        data(){
            return {imgList:[]}
        }
    }
</script>