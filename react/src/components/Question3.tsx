import { useEffect} from 'react';
import * as echarts from 'echarts';
import { DataType } from '../types';
import ContextMenu , {ContextMenuItem} from './ContextMenu';

// initalizing check, length, and value for context menu handler
var check: boolean = false;
var Length: string | undefined = undefined;
var value: string | number | Date | { [key: string]: string | number | Date | null | undefined; } | (string | number | Date | null | undefined)[] | { id?: (string | number) | undefined; name?: (string | number) | undefined; groupId?: (string | number) | undefined; childGroupId?: (string | number) | undefined; value?: (string | number | Date | null | undefined) | (string | number | Date | null | undefined)[]; selected?: boolean | undefined; } | null | undefined = undefined;

const ItemClickContextMenuHandler = (item: ContextMenuItem) =>{
        if(item.caption == "Copy" && check == true){
            navigator.clipboard.writeText(`Length for ${Length}: ${value} M`)
            Length = undefined;
            value = undefined;
            check = false;
        }else{
            alert("Select the data you would like to copy")
        }
}

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
                },
            },
            xAxis: {
                type: 'category',
                data: data.map((item: DataType) => item.name),
                name: 'Vintage Year',
                nameLocation: 'middle',
                nameGap: 35,
                axisLabel: {
                    interval: 0, // Show all labels
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
            }],
            selection: {
                enabled: true
            }
        };

        myChart.setOption(option);

        // checks if the user is right clicking on the data or not
        myChart.on("contextmenu", function(params){
            //if user is on the data, take the length and value, set the check to true.
            if(!params.target){
                Length = params.name;
                value = params.value;
                check = true;
            }else{
                alert("right click on data");
            }
        });
        return () => {
            myChart.dispose();
        };
    }, [data]);

    return (
        //contextMenu addon covers entire graph area
        <ContextMenu
            id="link-context-menu" 
            onItemClicked={ItemClickContextMenuHandler}
            items={[
                {
                    id: "entry1",
                    caption: "Copy"
                },
            ]}>
                <div className='Question3'>
                        <div
                            id="chart" style={{ width: '500px', height: '400px', padding: '20px' }} 
                        />
                </div>
        </ContextMenu>
    );
};

export default Question3;