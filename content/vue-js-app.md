<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

<div id="app">
    <h1>{{ message }}</h1>
    <p>This is a simple Vue.js application.</p>
    <button @click="updateMessage">Click Me</button>
</div>

<script>
    const { createApp, ref } = Vue;

    createApp({
        setup() {
            const message = ref('Hello, Vue!');

            const updateMessage = () => {
                message.value = 'Button Clicked!';
            };

            return {
                message,
                updateMessage
            };
        }
    }).mount('#app');
    
</script>
