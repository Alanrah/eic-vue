<template>

  <div>

    <button @click='aaaaa'>sasa</button>

  </div>

</template>

 

<script>

import axios from 'axios';

 

export default {

  data () {

    return {

    }

  },

  methods: {

    aaaaa () {

      axios.post("http://127.0.0.1:5000").then(function(r) {

        alert(r.data)

      });

    },

  }

}
</script>