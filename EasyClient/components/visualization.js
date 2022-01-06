Vue.component('visualization', {
    props: {
        msg: String,
        outerheight: String
    },
    // 动态props
    watch: {
        msg: function (newVal, oldVal) {
            this.visualData = newVal
        },
    },
    data() {
        return {
            visualData: "",
            width: parseInt((window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth) / 2) + "px",
            leftChartStyle: {
                width: this.width,
                height: this.outerheight.slice(0, -2) - 70 + "px"
            },
            rightChartStyle: {
                width: this.width,
                height: parseInt(this.outerheight.slice(0, -2) / 2 - 70) + "px"
            },
            allData: {
                dataLine1: [],
                dataLine2: [],
                dataLine3: [],
                dataGauge: 0
            },
            allCharts: {
                chart1: "",
                chart2: ""
            },
            apiURL: {
                getUrl: `/api/data?status=open`,
                postUrl: `/api/data`
            }
        }
    },
    mounted() {
        this.getInitData()
    },
    methods: {
        getInitData() {
            this.visualData = this.msg
            this.allCharts.chart1 = this.plot("chart1", "line")
            this.allCharts.chart2 = this.plot("chart2", "gauge")
            window.onresize = () => {
                Object.keys(this.allCharts).forEach(idx => {
                    this.allCharts[idx].resize()
                })
            };
            setInterval(() => {
                this.get()
            }, 1000)
        },
        get() {
            let params = {}
            axios.request({ method: "get", url: this.apiURL.getUrl, params: params })
                .then((res) => {
                    if (res.data.code === 200 || res.data.code === "200") {
                        this.allData.dataGauge = res.data.result
                        this.processLineData(this.allData.dataLine1, this.allData.dataGauge)
                        this.setPlotOptions(this.allCharts.chart1, "line")
                        this.setPlotOptions(this.allCharts.chart2, "gauge")
                    } else {
                        console.log("[非200]调取接口异常")
                    }
                }, (err) => {
                    console.log("[异常]调取接口异常")
                });
        },
        post() {
            let data = {}
            axios.request({ method: "post", url: this.apiURL.postUrl, data: data })
                .then((response) => {
                    if (res.data.code === 200 || res.data.code === "200") {
                    } else {
                        console.log("调取接口异常")
                    }
                }, (err) => {
                    console.log("调取接口失败")
                });
        },
        // 数据队列处理
        processLineData(dataLine, newData) {
            // 队头增加数据
            dataLine.unshift(newData)
            // 小于7个数据只增不减
            if (dataLine.length > 7) {
                // 队尾移除数据
                dataLine.pop()
            }
        },
        // 初始化画图
        plot(elementName, chartName) {
            let myChart = echarts.init(document.getElementById(elementName));
            this.setPlotOptions(myChart, chartName)
            return myChart
        },
        // 设置配置并绘制图表
        setPlotOptions(myChart, chartName) {
            let option = {}
            switch (chartName.toLowerCase()) {
                case "line":
                    option = this.setLineChartOptions()
                    break;
                case "gauge":
                    option = this.setGaugeOptions()
                    break;
            }
            myChart.setOption(option);
        },
        // 折线图配置
        setLineChartOptions() {
            let option = {
                title: {
                    text: '电位图'
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['输入1', '输入2', '输入3']
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    data: ['1s', '2s', '3s', '4s', '5s', '6s', '7s']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        name: '输入1',
                        type: 'line',
                        step: 'start',
                        data: this.allData.dataLine1
                    },
                    {
                        name: '输入2',
                        type: 'line',
                        step: 'middle',
                        data: this.allData.dataLine2
                    },
                    {
                        name: '输入3',
                        type: 'line',
                        step: 'end',
                        data: this.allData.dataLine3
                    }
                ]
            };
            return option
        },
        // 仪表盘的配置
        setGaugeOptions() {
            let option = {
                tooltip: {
                    formatter: '{a} <br/>{b} : {c}%'
                },
                series: [
                    {
                        name: 'Pressure',
                        type: 'gauge',
                        progress: {
                            show: true
                        },
                        detail: {
                            valueAnimation: true,
                            formatter: '{value}'
                        },
                        data: [
                            {
                                value: this.allData.dataGauge,
                                name: '电位'
                            }
                        ]
                    }
                ]
            };
            return option
        },
    },
    template:
        `
<section>
    <el-row class="flex header">
        <el-tag type="info" effect="dark" class="large-font">{{visualData}}</el-tag>
    </el-row>
    <el-row class="flex">
        <el-col :span="12">
            <div id="chart1" :style="leftChartStyle"></div>
        </el-col>
        <el-col :span="12">
            <el-row>
                <div id="chart2" :style="rightChartStyle"></div>
            </el-row>
            <el-row class="flex">
                <el-col :span="22">
                    <el-descriptions title="参数列表" :column="2" size="medium" border>
                        <template slot="extra">
                            <el-button type="primary" size="medium" @click="get">刷新</el-button>
                        </template>
                        <el-descriptions-item label="键A" label-class-name="desc-label" content-class-name="desc-content">
                            <el-tag effect="light">{{visualData}}</el-tag>
                        </el-descriptions-item>
                        <el-descriptions-item label="键B" label-class-name="desc-label" content-class-name="desc-content">
                            <el-tag effect="light">{{visualData}}</el-tag>
                        </el-descriptions-item>
                        <el-descriptions-item label="键C" label-class-name="desc-label" content-class-name="desc-content">
                            <el-tag effect="light">{{visualData}}</el-tag>
                        </el-descriptions-item>
                        <el-descriptions-item label="键D" label-class-name="desc-label" content-class-name="desc-content">
                            <el-tag effect="light">{{visualData}}</el-tag>
                        </el-descriptions-item>
                        <el-descriptions-item label="键E" label-class-name="desc-label" content-class-name="desc-content">
                            <el-tag effect="light">{{visualData}}</el-tag>
                        </el-descriptions-item>
                        <el-descriptions-item label="键F" label-class-name="desc-label" content-class-name="desc-content">
                            <el-tag effect="light">{{visualData}}</el-tag>
                        </el-descriptions-item>
                    </el-descriptions>
                </el-col>
            </el-row>
        </el-col>
    </el-row>
</section>
`
})