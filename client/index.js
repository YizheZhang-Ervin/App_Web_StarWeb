var app = new Vue({
    el: '#app',
    data() {
        return {
            textarea:"",
            displayComponent: "1-1"
        }
    },
    mounted() {
        // title时钟
        setInterval(() => {
            this.checkVisibility();
        }, 1000);
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
        // title时钟，当页面在前台可见时
        checkVisibility: function () {
            let vs = document.visibilityState;
            let date = new Date(Date.now());
            if (vs == "visible") {
                document.title =
                    "XXX - " +
                    date.getHours() +
                    ":" +
                    date.getMinutes() +
                    ":" +
                    date.getSeconds();
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