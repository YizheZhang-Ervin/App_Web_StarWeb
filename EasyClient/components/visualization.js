Vue.component('visualization', {
    props: {
        msg: String
    },
    // 动态props
    watch: {
        msg: function (newVal, oldVal) {
            this.visualData = newVal
        },
    },
    mounted() {
        this.getInitData()
    },
    data() {
        return {
            visualData: ""
        }
    },
    methods: {
        getInitData() {
            this.visualData = this.msg;
        },
        get() {
            axios.request({ method: "get", url: url, params: params })
                .then((response) => {

                }, (err) => { }

                );

        },
        post(url) {
            axios.request({ method: "post", url: url, data: data })
                .then((response) => {

                }, (err) => { }

                );
        },
    },
    template:
        `
<section>
    {{visualData}}
</section>
`
})