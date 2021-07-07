Vue.component('homepage', {
    props: {
        msg: String
    },
    // 动态props
    watch: {
        msg: function (newVal) {
            if (newVal == "homepage") {
                this.display = true; //newVal即是msg
            }else{
                this.display = false;
            }
        },
    },
    mounted() {
        if (this.msg == "homepage") {
            this.display = true;
        }else{
            this.display = false;
        }
    },
    data() {
        return {
            display: false
        }
    },
    methods: {

    },
    template:
        `
<section v-show="display" class="center">
    <div>
        home page
    </div>
</section>
`
})