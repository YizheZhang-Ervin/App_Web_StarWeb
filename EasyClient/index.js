var app = new Vue({
    el: '#app',
    data() {
        return {
            visualData: "home",
            mainPartStyle: {
                height: parseInt(window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight) - 140 + "px",
                overflow: "auto"
            }
        }
    },
    mounted() {
    },
    methods: {
        doClick(btn) {
            switch (btn) {
                case "A":
                    this.visualData = "home"
                    break;
                case "B":
                    this.visualData = "line"
                    break;
                case "C":
                    this.visualData = "hist"
                    break;
                case "D":
                    this.visualData = "table"
                    break;
                case "E":
                    this.visualData = "other"
                    break;
            }
        }
    }
});