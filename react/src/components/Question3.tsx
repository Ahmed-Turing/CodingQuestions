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
            tooltip: {
                trigger: 'item',
                formatter: (params: { name: any; value: any; }) => {
                    return `${params.name}: ${params.value} M`;
                }
            },
            xAxis: {
                type: 'category',
                data: data.map((item: DataType) => item.name),
                name: 'Vintage Year',
                nameLocation: 'middle',
                nameGap: 35,
                axisLabel: {
                    interval: 0, // Show all labels
                    rotate: 45, // Rotate labels to prevent overlap
                    margin: 10, // Space between labels and axis
                },
                axisTick: {
                    alignWithLabel: true, // Align ticks with labels
                }
            },
            yAxis: {
                type: 'value',
                name: "Length (M)",
                nameLocation: 'middle',
                nameGap: 30
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
        
        myChart.on('click', (params) =>{
            if (params.componentType === 'series') {
                const value = params.value;
                const name = params.name;
                navigator.clipboard.writeText(`Length for ${name}: ${value} M`)
                    .then(() => {
                        alert(`Copied to clipboard: Length for ${name}: ${value} M`);
                    })
                    .catch(err => {
                        console.error('Could not copy text: ', err)
                    })
            }
        }); 
        return () => {
            myChart.dispose();
        };
    }, [data]);

    return <div id="chart" style={{ width: '500px', height: '400px', padding: '20px' }} />;
};

export default Question3;