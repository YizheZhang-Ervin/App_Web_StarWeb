var app = new Vue({
    el: '#app',
    data() {
        return {
            title:"Astar | Monitor System",
            textarea:"",
            displayComponent: "homepage"
        }
    },
    mounted() {
        document.title = this.title;
    },
    methods: {
        // 更改显示内容
        changePage(key) {
            switch (key) {
                case "homepage":
                    this.displayComponent = "homepage";
                    break;
                case "contactus":
                    this.displayComponent = "contactus";
                    break;
                case key.match(/C.+/).input:
                    this.displayComponent = key;
                    break;
            }
        },
        post(url) {
            axios.post(`/api/${url}/`, { key: JSON.stringify(this.textarea) })
                .then((response) => {
                    if (response.data.error == "error") {
                        console.log("bakend error");
                    } else {
                        this.textarea = response.data.result;
                    }
                },
                    function (err) {
                        console.log(err.data);
                    }
                );
        },
    }
});