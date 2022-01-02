Vue.component('displaypage', {
    props: {
        msg: String
    },
    // 动态props
    watch: {
        msg: function (newVal) {
            if (/C.+/.test(newVal)) {
                this.display = true; //newVal即是msg
            }else{
                this.display = false;
            }
        },
    },
    mounted() {
        if (/C.+/.test(this.msg)) {
            this.display = true;
        }else{
            this.display = false;
        }
    },
    data() {
        return {
            display: false,
            allData:"",
            rowLis:[0,1,2],
            colLis:[0,1,2,3]
        }
    },
    methods: {
        get() {
            axios.get(`/api/stock/`).then(
                (response) => {
                    if (response.data.error == "error") {
                        console.log("bakend error");
                    } else {
                        this.allData = JSON.parse(response.data.result);
                    }
                },
                (err) => {
                    console.log("frontend error", err);
                }
            );
        },

    },
    template:
        `
<section v-show="display" class="center vertical">
    <h1>{{msg}}</h1>
    <el-row type="flex" justify="space-around" class="margintb" v-for="(i) in rowLis" :key="i">
        <el-col :xs="5" :sm="4" :md="5" :lg="5" :xl="5" v-for="(i) in colLis" :key="i">
            <el-image fit="fit"
            src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg">
            </el-image>
        </el-col>
    </el-row>
</section>
`
})