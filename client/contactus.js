Vue.component('contactus', {
    props: {
        msg: String
    },
    // 动态props
    watch: {
        msg: function (newVal) {
            if (newVal == "contactus") {
                this.display = true; //newVal即是msg
            }else{
                this.display = false;
            }
        },
    },
    mounted() {
        if (this.msg == "contactus") {
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
        contact us
    </div>
</section>
`
})