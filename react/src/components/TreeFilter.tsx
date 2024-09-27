import { Tree } from 'antd';
import { TreeDataType, TreeFilterProps } from '../types';
import { Key } from 'antd/es/table/interface';
import data from '../data/data.json';

const TreeFilter = ({ selectedKey, setSelectedKey }: TreeFilterProps) => {
    const onSelect = (selectedKeys: Key[]) => {
        setSelectedKey(selectedKeys[0] as string);
    };

    const treeData: TreeDataType[] = Object.keys(data).map((key) => ({
        title: key.charAt(0).toUpperCase() + key.slice(1),
        key: key
    }));

    return (
        <Tree
            onSelect={onSelect}
            selectedKeys={[selectedKey]}
            treeData={treeData}
            style={{ width: 200, marginRight: 20 }}
        />
    );
};

export default TreeFilter;