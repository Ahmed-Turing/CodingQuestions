import { useEffect } from 'react';
import * as echarts from 'echarts';
import { DataType } from '../types';

const Question3 = ({ data }: { data: DataType[] }) => {
    useEffect(() => {
        const chartDom = document.getElementById('chart');
        const myChart = echarts.init(chartDom);

        const option = {
            title: {
                text: 'Horizontal Length (M) by Vintage Year'
            },
            tooltip: {},
            xAxis: {
                type: 'category',
                data: data.map((item: DataType) => item.name)
            },
            yAxis: {
                type: 'value'
            },
            grid: {
                top: 50,
                left: 50,
                right: 50,
                bottom: 50
            },
            series: [{
                name: 'Vintage Year',
                type: 'bar',
                data: data.map((item: DataType) => item.value)
            }]
        };

        myChart.setOption(option);

        return () => {
            myChart.dispose();
        };
    }, [data]);

    return <div id="chart" style={{ width: '500px', height: '400px', padding: '20px' }} />;
};

export default Question3;